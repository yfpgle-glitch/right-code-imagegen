# Right Code ImageGen for Codex

使用 Right Code 在 Codex 里生成或修改图片。

[中文](#中文) | [English](#english)

## 中文

### 安装

#### 1. 安装 Skill

把这句话发给 Codex：

```text
请安装 GitHub 仓库 yfpgle-glitch/right-code-imagegen 中的
skills/right-code-imagegen Skill。
```

安装后，新建一个 Codex 任务。

#### 2. 创建 API Key

1. [注册 Right Code](https://www.rightapi.ai/register?aff=9ec111f0) 并登录。
2. 打开“令牌管理”。
3. 点击“创建密钥”。

不知道怎么操作，可以查看 [Right Code 官方 API Key 教程](https://docs.rightapi.ai/docs/rc_quick_start/apikey.html)。

#### 3. 保存 API Key

对 Codex 说：

```text
帮我配置 Right Code API Key。
```

Codex 会打开一个隐藏输入框。粘贴 API Key，然后确认。

Key 会保存在：

```text
~/.config/right-code/api_key
```

输入时不会显示 Key。不要把 Key 直接发到聊天里，也不要上传到 GitHub。

#### 4. 检查配置

对 Codex 说：

```text
检查一下 Right Code 配置。
```

这一步只检查 Key 是否已经保存，不会生成图片，也不会产生生图费用。

### 使用

直接告诉 Codex 你想要什么：

- `使用 Right Code 生成一张电影感的 16:9 图片。`
- `使用 Right Code 修改这张图片。`
- `使用 Right Code 生成三种不同方案。`
- `继续处理 Right Code 任务 task_example。`

默认使用 `gpt-image-2`、`16:9` 和 `1K`。你也可以指定其他比例或分辨率。

每张图片会单独提交。一次生成多张图片，可能产生多次费用。

### 手动配置（可选）

也可以在终端运行：

```bash
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py --check
```

## English

Use Right Code to generate or edit images in Codex.

### Install

#### 1. Install the Skill

Send this message to Codex:

```text
Install the skills/right-code-imagegen Skill from the GitHub repository
yfpgle-glitch/right-code-imagegen.
```

After installation, start a new Codex task.

#### 2. Create an API key

1. [Register with Right Code](https://www.rightapi.ai/register?aff=9ec111f0) and sign in.
2. Open **Token Management**.
3. Select **Create Key**.

For more help, read the [official Right Code API key guide](https://docs.rightapi.ai/docs/rc_quick_start/apikey.html).

#### 3. Save the API key

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

#### 4. Check the setup

Tell Codex:

```text
Check my Right Code configuration.
```

This only checks whether the key is saved. It does not generate an image or incur an image-generation charge.

### Use the Skill

Tell Codex what you want:

- `Use Right Code to generate a cinematic 16:9 image.`
- `Use Right Code to edit this image.`
- `Use Right Code to generate three different versions.`
- `Resume the Right Code task task_example.`

The defaults are `gpt-image-2`, `16:9`, and `1K`. You can ask for another aspect ratio or resolution.

Each image is submitted separately. Generating several images may result in several charges.

### Manual setup (optional)

You can also run:

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
