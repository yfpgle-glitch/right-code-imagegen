import base64
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest


DEFAULT_TARGET = Path(__file__).resolve().parents[1] / "scripts" / "generate_image.py"
TARGET = Path(os.environ.get("RIGHT_CODE_CLIENT_UNDER_TEST", DEFAULT_TARGET))
SPEC = importlib.util.spec_from_file_location("right_code_generate_image", TARGET)
CLIENT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(CLIENT)


class RecoveringTransport:
    def __init__(self):
        self.calls = []

    def request_json(self, method, url, api_key, payload=None, stage="request"):
        self.calls.append((method, stage))
        if len(self.calls) == 1:
            raise CLIENT.RightCodeError("temporary TLS EOF")
        encoded = base64.b64encode(b"\x89PNG\r\n\x1a\nmock").decode("ascii")
        return {"status": "completed", "data": [{"b64_json": encoded}]}


class FailingPollTransport:
    def __init__(self):
        self.calls = 0

    def request_json(self, method, url, api_key, payload=None, stage="request"):
        self.calls += 1
        raise CLIENT.RightCodeError("temporary TLS EOF")


class FailingSubmitTransport:
    def __init__(self):
        self.calls = []

    def request_json(self, method, url, api_key, payload=None, stage="request"):
        self.calls.append((method, stage))
        raise CLIENT.RightCodeError("submit failed")


class RightCodeEndpointTests(unittest.TestCase):
    def test_uses_rightapi_submit_and_poll_endpoints(self):
        self.assertEqual(
            CLIENT.SUBMIT_URL,
            "https://www.rightapi.ai/draw/v1/images/generations",
        )
        self.assertEqual(
            CLIENT.TASK_URL,
            "https://www.rightapi.ai/v1/tasks/{task_id}",
        )
        self.assertIn("rightapi.ai", CLIENT.AUTHENTICATED_DOWNLOAD_HOSTS)


class RightCodeRecoveryTests(unittest.TestCase):
    def test_resume_retries_poll_without_posting_and_downloads_result(self):
        transport = RecoveringTransport()
        sleeps = []
        with tempfile.TemporaryDirectory() as temporary:
            result = CLIENT.resume_task(
                api_key="test-key",
                task_id="task-existing",
                output_dir=Path(temporary),
                poll_interval=0,
                timeout=30,
                poll_retries=2,
                transport=transport,
                sleep=sleeps.append,
                monotonic=lambda: 0,
            )

            self.assertEqual(result["status"], "completed")
            self.assertEqual(transport.calls, [("GET", "poll"), ("GET", "poll")])
            self.assertEqual(sleeps, [0, 1.0])
            self.assertEqual(len(result["files"]), 1)
            self.assertTrue(Path(result["files"][0]).is_file())
            checkpoint = json.loads(Path(result["checkpoint"]).read_text())
            self.assertEqual(checkpoint["status"], "completed")

    def test_poll_exhaustion_writes_traceable_checkpoint(self):
        transport = FailingPollTransport()
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(CLIENT.RightCodeError, "checkpoint"):
                CLIENT.resume_task(
                    api_key="test-key",
                    task_id="task-existing",
                    output_dir=Path(temporary),
                    poll_interval=0,
                    timeout=30,
                    poll_retries=2,
                    transport=transport,
                    sleep=lambda _: None,
                    monotonic=lambda: 0,
                )

            self.assertEqual(transport.calls, 3)
            checkpoint_path = Path(temporary) / "right-code-task-task-existing.json"
            checkpoint = json.loads(checkpoint_path.read_text())
            self.assertEqual(checkpoint["status"], "poll_error")
            self.assertEqual(checkpoint["attempts"], 3)

    def test_submit_failure_is_never_retried(self):
        transport = FailingSubmitTransport()
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(CLIENT.RightCodeError, "submit failed"):
                CLIENT.generate(
                    api_key="test-key",
                    payload={"model": "gpt-image-2", "n": 1, "async": True},
                    output_dir=Path(temporary),
                    poll_interval=0,
                    timeout=30,
                    poll_retries=5,
                    transport=transport,
                    sleep=lambda _: None,
                    monotonic=lambda: 0,
                )

            self.assertEqual(transport.calls, [("POST", "submit")])

    def test_resume_cli_does_not_require_prompt(self):
        args = CLIENT.parse_args(["--resume-task-id", "task-existing"])
        self.assertEqual(args.resume_task_id, "task-existing")
        self.assertIsNone(args.prompt)


if __name__ == "__main__":
    unittest.main()
