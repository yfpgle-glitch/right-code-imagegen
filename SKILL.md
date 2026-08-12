---
name: rightcode-image
description: Configure a Right Code API key, generate or edit images through Right Code's asynchronous draw API, save original image files locally, and present them in the active AI agent. Use in Codex, Claude Code, or WorkBuddy when the user asks to set up or check Right Code authentication, or explicitly requests Right Code, rightapi.ai, right.codes, nano-banana, gpt-image through Right Code, or the Right Code draw endpoint; do not use when the user asks for the host agent's built-in image generator or another provider.
---

# Right Code Image

Use the bundled client for the complete submit, poll, decode, download, and checkpoint flow. Do not rebuild the API sequence with ad-hoc commands.

Choose an available Python 3 launcher for the bundled scripts. Prefer `python3`; use `python` when it points to Python 3. The examples below use `python3`.

Default to model `gpt-image-2`, aspect ratio `16:9`, and resolution `1K` unless the user explicitly requests different values.

## Configure the API key

When the user asks to configure or check Right Code authentication:

1. If they do not have an account or API key, direct them to `https://www.rightapi.ai/register?aff=9ec111f0`. If they need creation instructions, also provide `https://docs.rightapi.ai/docs/rc_quick_start/apikey.html`; the documented path is Right Code dashboard → Token Management → Create Key.
2. Do not ask the user to paste the API key into the conversation. Run `python3 scripts/configure_api_key.py`. On macOS and Windows this opens a local hidden-input dialog; in another interactive terminal it uses a hidden prompt.
3. After configuration, run `python3 scripts/configure_api_key.py --check`. Report only the status and saved path. Never print, repeat, log, or embed the key in a command.
4. Do not make a paid image request merely to verify configuration. Explain that the first real generation is the paid verification step.

## Workflow

1. Verify internally that the current request explicitly asks for paid image generation and selects Right Code either by name or through an active router whose documented default is Right Code. One request authorizes the requested output count and up to three total submit attempts per intended output when recovery is impossible; do not reuse that authorization for later requests or ask again between authorized recovery attempts.
2. Read the API key from `RIGHT_CODES_API_KEY` or `~/.config/right-code/api_key`. Never ask the user to paste the key into chat, print it, or embed it in this Skill.
3. Run `python3 scripts/generate_image.py --help` when options are unclear.
4. Invoke the script once. Pass each reference image with a separate `--reference` argument. Prefer an ASCII-only output directory inside the current workspace.
   - For multiple output images, pass `--count N`. The client must run `N` independent single-image tasks sequentially; never send provider field `n` greater than `1`.
   - Let the client derive a readable filename from the prompt. If the user gives a specific title, pass it with `--filename "title"`; omit the extension because the client detects the actual image format.
5. Read the final JSON from stdout. Present every absolute path in `files` using the host agent's supported artifact or Markdown features. Prefer an inline image plus a clickable local file link; if inline local images are unsupported, provide the saved file path and use the host's preview capability.
6. If the request fails, diagnose the exact `submit`, `poll`, or `download` stage. Prefer resuming a checkpointed task, reconnecting, polling again, or downloading again because those paths do not create another paid task. Automatically recover with bounded backoff and do not pause for progress confirmation. If no task can be recovered, use the authorization from step 1 for at most three total submit attempts. Only after three failed attempts, an unexpected cost increase, an authentication challenge, or a materially ambiguous request, report the evidence once and ask the user to intervene.

## Recover an existing task

When submission succeeded but polling stopped because of a transient network error, resume the saved task instead of running the generation command again:

```bash
python3 scripts/generate_image.py \
  --resume-task-id task_example \
  --output-dir ./outputs/right-code
```

Resume mode only sends authenticated `GET` requests to the existing task and never submits a new paid task. Polling retries transient network errors with bounded exponential backoff. Transport-level retries inside one task do not count as new paid attempts. Use `--poll-retries N` to change that limit. Never combine resume mode with `--prompt`, `--reference`, or a `--count` other than 1.

## Example

```bash
python3 scripts/generate_image.py \
  --prompt "一只戴着太空头盔的橘猫，电影级光影" \
  --output-dir ./outputs/right-code
```

For an edit, append `--reference /absolute/path/reference.png`.

For three independent output images, append `--count 3`. This creates three paid tasks. Later tasks continue even if one task fails, and the final JSON reports `completed`, `failed`, `files`, and per-task details. Recover failed tasks under the three-attempt policy above instead of stopping after each failure.

## Protocol Requirements

- Keep `"async": true` in every submission.
- Keep provider field `"n": 1`. Right Code accepted larger values in testing but returned only one image, so generate multiple outputs as separate sequential tasks.
- Submit to `https://www.rightapi.ai/draw/v1/images/generations`.
- Poll the site-level `https://www.rightapi.ai/v1/tasks/{task_id}` endpoint without a `/draw` prefix.
- Treat a response containing an image URL, `b64_json`, or Gemini inline image as completed even when `status` is absent.
- Preserve the checkpoint written immediately after submission so a task remains traceable after polling errors.
- Download the original bytes locally before displaying them. Do not rely on a temporary remote URL as the final result.
