---
name: "StyleConsistency"
description: "Maintains consistent styling across all website elements. Invoke when user mentions style changes, design updates, or when modifying any styled component to ensure all related elements are updated consistently."
---

# Style Consistency Skill

## Purpose

Maintain visual consistency across the entire blog website. When any style element is modified, all related elements using the same style must be updated simultaneously.

## Style Registry

### Current Style Elements

| Element | Location | Style Properties | Usage Locations |
|---------|----------|------------------|-----------------|
| **Primary Button** | `.back-link` | Background: #39c5bb, Border-radius: 6px, Padding: 12px 24px, Color: white | resume/index.html (返回目录按钮) |
| **Sidebar Background** | `.sidebar` | Background: #39c5bb, Color: white | resume/index.html |
| **Section Title** | `.section-title` | Color: #39c5bb, Uppercase, Letter-spacing: 1px | resume/index.html |
| **Skill Tag** | `.skill-tag` | Background: rgba(255,255,255,0.15), Border: 1px solid rgba(255,255,255,0.3), Border-radius: 15px, Color: white | resume/index.html (侧边栏技能标签) |
| **Card Container** | `.resume-container` | Background: #fff, Box-shadow: 0 10px 40px rgba(0,0,0,0.1) | resume/index.html |
| **Wrapper Background** | `.resume-wrapper` | Background: #f5f5f5, Min-height: 100vh | resume/index.html |

### Recent Changes Log

**2025-03-27:**
- ✅ Changed "技能特长" to "技能标签" in sidebar
- ✅ Updated skill tag style: white text on transparent background with white border
- ✅ Changed "返回首页" button to "返回目录", target changed from "/" to "/archives/"
- ✅ Moved button position to below project experience section
- ✅ Fixed background split line issue by adding .resume-wrapper with full background

## When to Invoke

**MUST invoke this skill when:**
1. User requests to change any color, font, spacing, or visual element
2. User mentions "style", "design", "color", "theme" changes
3. Modifying buttons, links, cards, or any UI component
4. User says "keep consistent" or mentions consistency
5. User asks to modify an element that exists in the Style Registry

## Workflow

1. **Identify** the element being modified
2. **Check** the Style Registry for related elements
3. **Update** all locations using the same style
4. **Document** any new style elements in the registry
5. **Log** changes in the Recent Changes Log

## Example

User: "Change the button color to red"
→ Action: Update all `.back-link` buttons in resume/index.html, nav/index.html, and landing/index.html

User: "Make the sidebar darker"
→ Action: Update `.sidebar` background color and check for related elements

User: "Change skill tag style"
→ Action: Update `.skill-tag` in Style Registry and modify all skill tag elements
