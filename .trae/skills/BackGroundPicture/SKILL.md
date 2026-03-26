---
name: "BackGroundPicture"
description: "Manages blog background images and their corresponding subtitles. Invoke when user wants to add, update, or remove background images with associated text for the blog homepage slider, or when user provides image files to save."
---

# BackGroundPicture Skill

## Purpose

管理博客首页背景图及其对应的小标题文字。支持用户直接提供图片文件，自动保存到指定位置并重命名。

## Background Image Configuration File

背景图配置存储在：`source/_data/backgrounds.yml`

## Configuration Format

```yaml
backgrounds:
  - image: /images/bg-1.jpg
    subtitle: "Miku"
  - image: /images/bg-2.jpg
    subtitle: "Ayase"
  - image: /images/bg-3.jpg
    subtitle: "Rin/Ren"
```

## When to Invoke

1. **添加新背景图**：用户提供图片路径和对应文字时
2. **更新背景图文字**：用户想要修改某张图片对应的文字时
3. **删除背景图**：用户想要移除某张背景图时
4. **查看所有背景图**：用户想要查看当前配置的所有背景图时
5. **用户提供图片文件**：用户直接发送/粘贴图片文件时，自动保存并重命名

## Operations

### 1. 添加背景图（配置方式）

当用户提供图片路径和文字时：

1. 检查 `source/_data/` 目录是否存在，不存在则创建
2. 检查 `source/_data/backgrounds.yml` 文件是否存在，不存在则创建
3. 将新配置追加到 backgrounds 列表中
4. 确保图片存放在 `source/images/` 目录

### 2. 自动保存图片文件（文件方式）

当用户直接提供图片文件时（如粘贴图片）：

1. **确定目标文件名**：
   - 按顺序查找 `source/images/` 目录中已有的背景图
   - 新图片命名为 `bg-{n}.jpg`，其中 n 为下一个可用序号
   - 例如：已有 bg-1.jpg, bg-2.jpg，则新图片命名为 bg-3.jpg

2. **保存图片文件**：
   - 将图片保存到 `source/images/bg-{n}.jpg`
   - 确保目录存在，不存在则创建

3. **询问用户对应文字**：
   - 保存成功后，询问用户这张图片对应的小标题文字
   - 例如："图片已保存为 bg-3.jpg，请输入对应的小标题文字："

4. **更新配置文件**：
   - 将新配置添加到 `source/_data/backgrounds.yml`
   - 格式：`{image: /images/bg-{n}.jpg, subtitle: "用户提供的文字"}`

5. **重新生成和部署**（可选）：
   - 询问用户是否需要立即重新生成和部署网站
   - 执行 `hexo generate` 和 `hexo deploy`

### 3. 图片命名规范

- 自动命名：`bg-1.jpg`, `bg-2.jpg`, `bg-3.jpg` 等顺序命名
- 支持格式：jpg, jpeg, png, webp
- 推荐尺寸：1920x1080 或更高，用于全屏背景
- 保存位置：`source/images/`

### 4. 批量处理多张图片

当用户一次提供多张图片时：

1. 按顺序为每张图片分配文件名（bg-1.jpg, bg-2.jpg, bg-3.jpg...）
2. 依次保存所有图片
3. 询问每张图片对应的小标题文字（或一次性询问所有文字）
4. 批量更新 `backgrounds.yml` 配置文件
5. 执行重新生成和部署

## Example Usage

### 场景1：用户提供图片路径和文字
用户说："添加一张背景图，路径是 /images/my-star.jpg，文字是'七姐妹在天空中永恒守望'"

操作：
1. 确认图片已放入 `source/images/my-star.jpg`
2. 更新 `source/_data/backgrounds.yml` 添加新条目
3. 告知用户添加成功

### 场景2：用户直接粘贴图片文件
用户直接粘贴一张图片

操作：
1. 保存图片到 `source/images/bg-3.jpg`（假设已有2张）
2. 询问用户："图片已保存为 bg-3.jpg，请输入对应的小标题文字："
3. 用户回复："Miku"
4. 更新 `source/_data/backgrounds.yml` 添加 `{image: /images/bg-3.jpg, subtitle: "Miku"}`
5. 询问是否重新生成部署，用户确认后执行

### 场景3：用户一次提供多张图片
用户一次粘贴3张图片

操作：
1. 保存为 `bg-1.jpg`, `bg-2.jpg`, `bg-3.jpg`
2. 询问："3张图片已保存，请分别输入对应的小标题文字（用逗号分隔）："
3. 用户回复："Miku, Ayase, Rin/Ren"
4. 更新配置文件，添加3条记录
5. 执行重新生成和部署
