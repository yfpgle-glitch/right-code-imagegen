#!/usr/bin/env python3
"""Securely configure the local Right Code API key without printing it."""

from __future__ import annotations

import argparse
import getpass
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
from typing import Optional, Sequence


DEFAULT_KEY_PATH = Path.home() / ".config/right-code/api_key"


class ConfigurationError(RuntimeError):
    pass


def _clean_key(value: str) -> str:
    key = value.strip()
    if not key:
        raise ConfigurationError("The API key cannot be empty.")
    if "\n" in key or "\r" in key:
        raise ConfigurationError("The API key must be a single line.")
    return key


def save_api_key(value: str, key_path: Path = DEFAULT_KEY_PATH) -> Path:
    key = _clean_key(value)
    key_path = key_path.expanduser()
    key_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if os.name == "posix":
        os.chmod(key_path.parent, 0o700)

    temporary = key_path.with_name(f".{key_path.name}.tmp")
    try:
        descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(key)
        os.replace(temporary, key_path)
        if os.name == "posix":
            os.chmod(key_path, 0o600)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
    return key_path


def check_configuration(key_path: Path = DEFAULT_KEY_PATH) -> dict:
    key_path = key_path.expanduser()
    if not key_path.is_file():
        raise ConfigurationError(f"No API key was found at {key_path}.")
    _clean_key(key_path.read_text(encoding="utf-8"))

    result = {"status": "ready", "key_path": str(key_path)}
    if os.name == "posix":
        permissions = stat.S_IMODE(key_path.stat().st_mode)
        result["permissions"] = format(permissions, "03o")
        if permissions & 0o077:
            raise ConfigurationError(
                f"The API key file permissions are too broad ({permissions:03o}); expected 600."
            )
    return result


def _prompt_with_macos_dialog() -> str:
    script = """
set dialogResult to display dialog "Paste your Right Code API key. It will be saved locally and will not be printed." default answer "" with hidden answer buttons {"Cancel", "Save"} default button "Save" cancel button "Cancel" with title "Configure Right Code"
return text returned of dialogResult
"""
    completed = subprocess.run(
        ["osascript", "-e", script],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ConfigurationError("API key configuration was cancelled.")
    return completed.stdout


def prompt_for_api_key() -> str:
    if sys.platform == "darwin":
        return _prompt_with_macos_dialog()
    if sys.stdin.isatty():
        return getpass.getpass("Paste your Right Code API key: ")
    raise ConfigurationError(
        "Run this script in an interactive terminal so the API key can be entered securely."
    )


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Securely save or check the local Right Code API key."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check that the API key exists and has safe local permissions.",
    )
    parser.add_argument(
        "--key-path",
        type=Path,
        default=DEFAULT_KEY_PATH,
        help=argparse.SUPPRESS,
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    try:
        if args.check:
            result = check_configuration(args.key_path)
        else:
            saved_path = save_api_key(prompt_for_api_key(), args.key_path)
            result = {"status": "configured", "key_path": str(saved_path)}
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except ConfigurationError as error:
        print(json.dumps({"status": "error", "message": str(error)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
