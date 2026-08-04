# Right Code ImageGen Skill for Codex

通过 Right Code 在 Codex 中生成和编辑图片。支持文生图、参考图编辑、多图任务、断点恢复和原图下载。

## 三分钟安装

### 1. 让 Codex 安装 Skill

把下面这句话发给 Codex：

```text
请安装 yfpgle-glitch/right-code-imagegen 仓库中
skills/right-code-imagegen 这个 Skill。
```

安装完成后，新建一个 Codex 任务。

### 2. 注册 Right Code 并创建 API Key

[注册 Right Code 并创建 API Key](https://www.rightapi.ai/register?aff=9ec111f0)

不会创建 Key？查看 [Right Code 官方 ApiKey 管理图文教程](https://docs.rightapi.ai/docs/rc_quick_start/apikey.html)。进入后台后，依次点击左侧的“令牌管理”和“创建密钥”。

> 说明：上面的注册链接包含推广参数。创建 Key 时通常保持“可用模型限制”的默认设置；如果不希望套餐用完后继续扣除余额，可以关闭“允许使用余额”。

### 3. 让 Codex 帮你配置 Key

不用手动创建配置文件。直接对 Codex 说：

```text
帮我配置 Right Code API Key。
```

Codex 会打开本地隐藏输入框。把 API Key 粘贴到输入框并确认即可。Key 会保存在：

```text
~/.config/right-code/api_key
```

API Key 不会显示在终端输出中。为了安全，不要把 Key 直接发送到聊天记录、GitHub 或其他公开位置。

### 4. 检查配置

对 Codex 说：

```text
检查一下 Right Code 配置。
```

这个检查不会调用生图接口，也不会产生生图费用。第一次实际生成图片时才会提交 Right Code 任务。

## 开始使用

你可以直接对 Codex 说：

- `使用 Right Code 生成一张电影感的 16:9 图片。`
- `使用 Right Code 编辑这张参考图。`
- `使用 Right Code 生成三种不同方案。`
- `继续处理 Right Code 任务 task_example。`

默认模型为 `gpt-image-2`，默认比例为 `16:9`，默认分辨率为 `1K`。生成多张图片会创建多个独立任务，可能产生多次费用。

## 手动配置（可选）

如果你更喜欢使用终端：

```bash
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py
python3 ~/.codex/skills/right-code-imagegen/scripts/configure_api_key.py --check
```

## 开发与测试

```bash
python3 -m unittest discover skills/right-code-imagegen/tests
```

## License

MIT
