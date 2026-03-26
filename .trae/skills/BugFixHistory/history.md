# Bug 修复历史记录

---

## 2026-03-26 - landing 页面轮播图片不显示

### 问题描述
用户抓取网页元素发现：
1. 背景图（bg-default.png）显示正常
2. 标题"昴星团"显示正常
3. Button 按钮显示正常
4. 但轮播图片（Miku/Ayase/Rin/Ren）不显示
5. 副标题"subTitle"不显示

### 问题分析
`.bg-image` 的 `z-index` 设置为 1，与 `.background-slider::before`（z-index: 0）层级关系不正确，导致轮播图片被底层背景遮挡。

### 修复方案
修改 `.bg-image` 的 z-index 从 1 改为 2：
```css
.bg-image {
  position: absolute;
  /* ... */
  z-index: 2;  /* 改为 2，高于 ::before 的 0 */
}

.bg-image.active {
  opacity: 1;
  z-index: 2;
}
```

同时移除了 `.bg-image.fade-out` 类，因为使用纯 opacity 过渡不需要额外的 z-index 控制。

### 状态
✅ 已修复

### 经验教训
**z-index 层级关系很重要**：
- 底层背景图：z-index: 0
- 轮播图片：z-index: 2
- 内容（标题/按钮）：z-index: 10
- 导航区域：z-index: 5-6

---

## 2026-03-26 - landing 页面被 Hexo 模板包裹

### 问题描述
用户抓取网页元素发现：
1. landing 页面出现了 `#container`、`#wrap`、`#header` 等 Hexo 模板元素
2. 动态图片（背景图轮播）消失

### 问题分析
`_config.yml` 中的 `skip_render` 只配置了 `nav/**`，但 `landing` 目录也需要跳过渲染。

### 修复方案
在 `_config.yml` 中添加 `landing` 到 `skip_render`：
```yaml
skip_render:
  - nav/**
  - landing/**
```

### 状态
✅ 已修复

### 经验教训
**所有独立 HTML 页面都需要配置 skip_render**，包括：
- nav/**
- landing/**
- 任何其他独立页面

---

## 2026-03-25 - 图片切换时"突然放大然后消失"

### 问题描述
图片轮播切换时，当前图片会突然放大然后消失，视觉效果不流畅。

### 尝试方案 1：修改 z-index 切换逻辑
- **方案**：使用 `currentIndex % bgImages.length` 计算 DOM 索引
- **结果**：❌ 失败
- **原因**：索引计算错误，导致选到同一个 DOM 元素

### 尝试方案 2：使用 fade-out 类 + z-index 分层
- **方案**：
  - 添加 `.fade-out` 类，z-index: 0
  - 添加 `.active` 类，z-index: 1
  - 切换时先设置 z-index，再切换 opacity
- **结果**：❌ 失败
- **原因**：z-index 变化仍然是立即生效的，与 opacity 渐变不同步

### 尝试方案 3：使用 ::before 伪元素做背景
- **方案**：将背景图放在 `.background-slider::before` 中
- **结果**：❌ 失败
- **原因**：与背景图无关，问题出在切换逻辑

### 最终方案（待验证）：纯 opacity 过渡，移除 z-index 变化
- **方案**：
  - 所有图片固定 z-index: 2
  - 只使用 opacity 控制显示/隐藏
  - 不使用 z-index 切换
  - 使用交叉淡入淡出（cross-fade）

### 经验教训
1. **z-index 和 opacity 动画不同步** - z-index 是立即生效的，opacity 是渐变的
2. **不要混合使用 z-index 和 opacity 做切换动画**
3. **简单方案往往更有效** - 纯 opacity 过渡可能是最稳定的

---

## 2026-03-25 - 导航页图片轮播消失

### 问题描述
用户反馈"滚动图片消失了"，导航页的背景图轮播功能失效。

### 问题分析
在创建新的 `source/nav/index.html` 时，复制了旧的代码，其中包含已知的 bug。

### 修复方案
使用上述"纯 opacity 过渡"方案重写切换逻辑。

### 状态
✅ 已修复

---

## 2026-03-25 - 导航页被 Hexo 模板包裹

### 问题描述
`source/nav/index.html` 被 Hexo 当作 Markdown 处理，被 layout 模板包裹，导致页面显示不正确。

### 问题分析
Hexo 默认会处理所有 source 目录下的文件，HTML 文件也会被当作模板处理。

### 修复方案
在 `_config.yml` 中添加 `skip_render` 配置：
```yaml
skip_render:
  - nav/**
```

### 状态
✅ 已修复

### 经验教训
**独立 HTML 页面需要配置 skip_render**，否则会被 Hexo 模板系统处理。
