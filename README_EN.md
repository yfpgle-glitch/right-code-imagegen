# Right Code ImageGen for Codex

[中文](README.md)

Use Right Code to generate or edit images in Codex.

GitHub repository: [yfpgle-glitch/right-code-imagegen](https://github.com/yfpgle-glitch/right-code-imagegen)

## Install

### 1. Install the Skill

Send this message to Codex:

```text
Install this Codex Skill:
https://github.com/yfpgle-glitch/right-code-imagegen/tree/main/skills/right-code-imagegen
```

After installation, start a new Codex task.

### 2. Create an API key

1. [Register with Right Code](https://www.rightapi.ai/register?aff=9ec111f0) and sign in.
2. Open **Token Management**.
3. Select **Create Key**.

**Register through this link to receive 5% extra credit on every top-up.**

For more help, read the [official Right Code API key guide](https://docs.rightapi.ai/docs/rc_quick_start/apikey.html).

### 3. Save the API key

Tell Codex:

```text
Configure my Right Code API key.
```

Codex will open a hidden input box. Paste the API key and confirm.

The key is saved at:

```text
~/.config/right-code/api_key
```

The key is hidden while you type. Do not send it in a chat or upload it to GitHub.

### 4. Check the setup

Tell Codex:

```text
Check my Right Code configuration.
```

This only checks whether the key is saved. It does not generate an image or incur an image-generation charge.

## Use the Skill

Tell Codex what you want:

- `Use Right Code to generate a cinematic 16:9 image.`
- `Use Right Code to edit this image.`
- `Use Right Code to generate three different versions.`
- `Resume the Right Code task task_example.`

The defaults are `gpt-image-2`, `16:9`, and `1K`. You can ask for another aspect ratio or resolution.

Each image is submitted separately. Generating several images may result in several charges.
