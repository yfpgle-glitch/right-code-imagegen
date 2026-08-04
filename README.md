# Right Code ImageGen Skill for Codex

通过 Right Code 在 Codex 中生成和编辑图片。支持文生图、参考图编辑、多图任务、断点恢复和原图下载。

[中文](#中文) | [English](#english)

## 中文

### 三分钟安装

#### 1. 让 Codex 安装 Skill

把下面这句话发给 Codex：

```text
请安装 yfpgle-glitch/right-code-imagegen 仓库中
skills/right-code-imagegen 这个 Skill。
```

安装完成后，新建一个 Codex 任务。

#### 2. 注册 Right Code 并创建 API Key

[注册 Right Code](https://www.rightapi.ai/register?aff=9ec111f0)

如果不知道如何创建 Key，请查看 [Right Code 官方 ApiKey 管理图文教程](https://docs.rightapi.ai/docs/rc_quick_start/apikey.html)。进入后台后，依次点击“令牌管理”和“创建密钥”。

#### 3. 让 Codex 安全配置 Key

不用手动创建配置文件。直接对 Codex 说：

```text
帮我配置 Right Code API Key。
```

Codex 会打开本地隐藏输入框。把 API Key 粘贴到输入框并确认即可。Key 会保存在：

```text
~/.config/right-code/api_key
```

API Key 不会显示在终端输出中。为了安全，不要把 Key 直接发送到聊天记录、GitHub 或其他公开位置。

#### 4. 免费检查配置

对 Codex 说：

```text
检查一下 Right Code 配置。
```

这个检查不会调用生图接口，也不会产生生图费用。第一次实际生成图片时才会提交 Right Code 任务。

### 开始使用

你可以直接对 Codex 说：

- `使用 Right Code 生成一张电影感的 16:9 图片。`
- `使用 Right Code 编辑这张参考图。`
- `使用 Right Code 生成三种不同方案。`
- `继续处理 Right Code 任务 task_example。`

默认模型为 `gpt-image-2`，默认比例为 `16:9`，默认分辨率为 `1K`。你也可以直接指定其他比例或分辨率。生成多张图片会创建多个独立任务，可能产生多次费用。

### 手动配置（可选）

如果你更喜欢使用终端：

```bash
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py --check
```

## English

Generate and edit images in Codex through Right Code. The Skill supports text-to-image generation, reference-image editing, multiple outputs, task recovery, and original-file downloads.

### Install in three minutes

#### 1. Ask Codex to install the Skill

Send this instruction to Codex:

```text
Install the Skill at skills/right-code-imagegen from the
yfpgle-glitch/right-code-imagegen repository.
```

Start a new Codex task after installation.

#### 2. Register with Right Code and create an API key

[Register with Right Code](https://www.rightapi.ai/register?aff=9ec111f0)

If you need help creating a key, follow the [official Right Code API key guide](https://docs.rightapi.ai/docs/rc_quick_start/apikey.html). In the dashboard, open **Token Management** and select **Create Key**.

#### 3. Ask Codex to configure the key securely

You do not need to create the configuration file yourself. Tell Codex:

```text
Configure my Right Code API key.
```

Codex will open a local hidden-input dialog. Paste the API key there and confirm. The key is saved at:

```text
~/.config/right-code/api_key
```

The API key is not printed in terminal output. Do not paste it into a chat, GitHub, or any other public location.

#### 4. Check the configuration for free

Tell Codex:

```text
Check my Right Code configuration.
```

This check does not call the image-generation API and does not incur image-generation charges. The first real image request submits a Right Code task.

### Usage

You can ask Codex:

- `Use Right Code to generate a cinematic 16:9 image.`
- `Use Right Code to edit this reference image.`
- `Use Right Code to generate three different concepts.`
- `Resume the Right Code task task_example.`

The defaults are `gpt-image-2`, a `16:9` aspect ratio, and `1K` resolution. You can request another aspect ratio or resolution directly. Multiple images are generated as independent tasks and may incur multiple charges.

### Manual configuration (optional)

If you prefer the terminal:

```bash
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py --check
```

## Development

```bash
python3 -m unittest discover skills/right-code-imagegen/tests
```

## License

MIT
