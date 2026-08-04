# Right Code ImageGen Skill for Codex

A standalone Codex Skill for generating and editing images through Right Code's asynchronous image API.

It supports text-to-image, reference-image editing, sequential multi-image requests, resumable polling, local task checkpoints, and original-file downloads. This is an independent community project and is not affiliated with Right Code or OpenAI.

## Install

Ask Codex to install the Skill from this repository:

```text
Install the right-code-imagegen Skill from yfpgle-glitch/right-code-imagegen,
using the path skills/right-code-imagegen.
```

Or install it manually:

```bash
git clone https://github.com/yfpgle-glitch/right-code-imagegen.git
mkdir -p ~/.codex/skills
cp -R right-code-imagegen/skills/right-code-imagegen ~/.codex/skills/right-code-imagegen
```

Start a new Codex task after installation so the Skill is discovered.

## Configure the API key

Set the key for the current process:

```bash
export RIGHT_CODES_API_KEY="your-api-key"
```

Or store it locally:

```bash
mkdir -p ~/.config/right-code
chmod 700 ~/.config/right-code
printf '%s' "your-api-key" > ~/.config/right-code/api_key
chmod 600 ~/.config/right-code/api_key
```

Never commit the API key or paste it into a Codex conversation.

## Use

Examples:

- `Use Right Code to generate a cinematic 16:9 image.`
- `Use Right Code to edit this reference image.`
- `Use Right Code to generate three independent variations.`
- `Resume Right Code task task_example.`

The default model is `gpt-image-2`, the default aspect ratio is `16:9`, and the default resolution is `1K`. Multiple outputs are submitted as independent single-image tasks because the provider returns one image per task.

## Development

Run the offline unit tests:

```bash
python3 -m unittest discover skills/right-code-imagegen/tests
```

Validate the Skill with Codex's `skill-creator` validator before publishing a release.

## License

MIT
