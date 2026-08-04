# Right Code ImageGen for Codex

[English](README_EN.md)

使用 Right Code 在 Codex 里生成或修改图片。

GitHub 仓库：[yfpgle-glitch/right-code-imagegen](https://github.com/yfpgle-glitch/right-code-imagegen)

## 安装

### 1. 安装 Skill

把这句话发给 Codex：

```text
请安装这个 Codex Skill：
https://github.com/yfpgle-glitch/right-code-imagegen/tree/main/skills/right-code-imagegen
```

安装后，新建一个 Codex 任务。

### 2. 创建 API Key

1. [注册 Right Code](https://www.rightapi.ai/register?aff=9ec111f0) 并登录。
2. 打开“令牌管理”。
3. 点击“创建密钥”。

**使用此链接注册，每次充值均可赠送 5% 额外额度。**

不知道怎么操作，可以查看 [Right Code 官方 API Key 教程](https://docs.rightapi.ai/docs/rc_quick_start/apikey.html)。

### 3. 保存 API Key

对 Codex 说：

```text
帮我配置 Right Code API Key。
```

Codex 会打开一个隐藏输入框。粘贴 API Key，然后确认。

Key 会保存在：

```text
~/.config/right-code/api_key
```

输入时不会显示 Key。不要把 Key 发到聊天里，也不要上传到 GitHub。

### 4. 检查配置

对 Codex 说：

```text
检查一下 Right Code 配置。
```

这一步只检查 Key 是否已经保存，不会生成图片，也不会产生生图费用。

## 使用

直接告诉 Codex 你想要什么：

- `使用 Right Code 生成一张电影感的 16:9 图片。`
- `使用 Right Code 修改这张图片。`
- `使用 Right Code 生成三种不同方案。`
- `继续处理 Right Code 任务 task_example。`

默认使用 `gpt-image-2`、`16:9` 和 `1K`。你也可以指定其他比例或分辨率。

每张图片会单独提交。一次生成多张图片，可能产生多次费用。
