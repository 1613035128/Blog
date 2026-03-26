---
name: "BugFixHistory"
description: "Records all bug fixes and modifications with their context. Invoke when user reports a bug or requests a fix to avoid repeating failed solutions."
---

# BugFixHistory Skill

## Purpose

记录所有 bug 修复和修改的历史，包括：
1. Bug 的现象描述
2. 尝试过的解决方案
3. 方案的结果（成功/失败）
4. 最终解决方案

## When to Invoke

**必须在以下场景调用：**
1. 用户报告 bug 时
2. 用户要求修复问题时
3. 需要查询历史修改记录时
4. 需要避免重复失败的方案时

## History File

修改历史记录在：`.trae/skills/BugFixHistory/history.md`

## Record Format

```markdown
## [日期] - [Bug/修改标题]

### 问题描述
[详细描述问题现象]

### 尝试方案 1
- **方案**：[描述]
- **结果**：❌ 失败 / ✅ 成功
- **原因**：[失败原因分析]

### 尝试方案 2
- **方案**：[描述]
- **结果**：❌ 失败 / ✅ 成功
- **原因**：[失败原因分析]

### 最终方案
- **方案**：[描述]
- **代码修改**：[关键代码]
- **结果**：✅ 成功

### 经验教训
[总结，避免下次犯同样错误]
```

## Usage

### 记录新 Bug
1. 创建新的历史记录条目
2. 详细记录问题现象
3. 记录所有尝试的方案
4. 标记成功/失败

### 查询历史
1. 读取 history.md
2. 查找相关问题
3. 避免重复失败的方案
4. 基于历史给出新方案

## Example

用户说："图片切换时突然放大"

操作：
1. 查询 history.md 中是否有类似问题
2. 发现之前尝试过：
   - 方案1：修改 z-index ❌
   - 方案2：使用 fade-out 类 ❌
3. 给出新的方案3：使用 opacity-only 过渡
4. 记录新方案到 history.md
