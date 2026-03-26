---
name: "WebsiteVerification"
description: "Verifies website deployment by fetching and analyzing the live site. Invoke after deploying changes to validate visual effects, layout, and functionality."
---

# WebsiteVerification Skill

## Purpose

在部署网站修改后，自动验证网站是否正确部署，检查视觉效果、布局和功能是否符合预期。

## When to Invoke

**必须在以下场景调用：**
1. 完成网站修改并部署后
2. 用户要求验证网站效果时
3. 视觉类效果改动后需要确认准确性
4. 功能修改后需要验证是否正常工作

## Verification Process

### 1. 获取网站内容

使用 WebFetch 工具获取网站 HTML 内容：
```javascript
WebFetch({ url: "https://1613035128.github.io/nav/" })
```

### 2. 验证检查项

#### 视觉类效果检查：
- [ ] 页面是否正确加载
- [ ] 标题是否正确显示
- [ ] 副标题/文字是否正确
- [ ] 按钮颜色和文字是否正确
- [ ] 背景图是否正确显示
- [ ] 布局是否符合预期

#### 功能类检查：
- [ ] 跳转链接是否正确
- [ ] 交互元素是否存在
- [ ] 响应式布局是否生效

### 3. 截图验证（如需要）

对于视觉类改动，应该：
1. 获取页面 HTML 内容
2. 分析关键元素是否存在
3. 检查 CSS 样式是否正确应用
4. 报告验证结果

## Example Usage

### 场景1：验证导航页部署
用户完成了导航页的修改并部署。

操作：
1. 使用 WebFetch 获取 `https://1613035128.github.io/nav/`
2. 检查 HTML 内容中是否包含：
   - `<h1 class="nav-title">昴星团</h1>`
   - `<p class="nav-subtitle">Miku</p>`
   - `<a href="/archives" class="enter-button">Button</a>`
   - 按钮样式 `background-color: #39c5bb`
3. 检查背景图配置
4. 报告验证结果

### 场景2：验证跳转功能
用户设置了首页跳转到导航页。

操作：
1. 使用 WebFetch 获取 `https://1613035128.github.io/`
2. 检查是否包含跳转代码：
   - `<meta http-equiv="refresh" content="0; url=/nav/">`
   - `window.location.replace('/nav/')`
3. 报告验证结果

## Report Format

验证完成后，输出报告：

```
## 网站验证报告

### 验证项目
- 验证URL: [URL]
- 验证时间: [时间]

### 检查结果
| 检查项 | 状态 | 说明 |
|--------|------|------|
| 页面加载 | ✅/❌ | [说明] |
| 标题显示 | ✅/❌ | [说明] |
| 按钮样式 | ✅/❌ | [说明] |
| 背景图 | ✅/❌ | [说明] |
| 跳转功能 | ✅/❌ | [说明] |

### 结论
[总体结论]
```

## Important Notes

1. **必须在部署后立即验证**
2. **视觉类改动需要详细检查 CSS 样式**
3. **功能类改动需要检查交互元素**
4. **如发现问题，立即报告用户**
