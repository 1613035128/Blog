#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量保存背景图脚本
使用方法：
1. 将图片 URL 填入下面的 image_urls 列表
2. 运行：python save_images.py
"""

import os
import urllib.request
import ssl

# 配置
images_dir = "source/images"
backgrounds_yml = "source/_data/backgrounds.yml"

# 图片配置 - 请在这里填入图片 URL 和对应文字
# 格式：(图片URL, 文件名, 小标题文字)
image_configs = [
    # 示例：("https://example.com/image1.jpg", "bg-1.jpg", "Miku"),
    # 示例：("https://example.com/image2.jpg", "bg-2.jpg", "Ayase"),
    # 示例：("https://example.com/image3.jpg", "bg-3.jpg", "Rin/Ren"),
]

# 创建目录
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"创建目录: {directory}")

# 下载图片
def download_image(url, filepath):
    try:
        # 忽略 SSL 验证
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        request = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(request, context=ssl_context, timeout=30) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print(f"✓ 已保存: {filepath}")
        return True
    except Exception as e:
        print(f"✗ 下载失败: {url}")
        print(f"  错误: {e}")
        return False

# 更新 backgrounds.yml
def update_backgrounds_yml(configs):
    ensure_dir(os.path.dirname(backgrounds_yml))
    
    content = "backgrounds:\n"
    for url, filename, subtitle in configs:
        content += f'  - image: /images/{filename}\n'
        content += f'    subtitle: "{subtitle}"\n'
    
    with open(backgrounds_yml, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n✓ 已更新: {backgrounds_yml}")

# 主函数
def main():
    print("=" * 50)
    print("博客背景图批量保存工具")
    print("=" * 50)
    
    if not image_configs:
        print("\n⚠ 请先编辑脚本，在 image_configs 列表中添加图片 URL")
        print("\n格式：")
        print('image_configs = [')
        print('    ("https://example.com/image1.jpg", "bg-1.jpg", "Miku"),')
        print('    ("https://example.com/image2.jpg", "bg-2.jpg", "Ayase"),')
        print('    ("https://example.com/image3.jpg", "bg-3.jpg", "Rin/Ren"),')
        print(']')
        return
    
    ensure_dir(images_dir)
    
    print(f"\n开始下载 {len(image_configs)} 张图片...\n")
    
    success_count = 0
    for url, filename, subtitle in image_configs:
        filepath = os.path.join(images_dir, filename)
        if download_image(url, filepath):
            success_count += 1
    
    print(f"\n下载完成: {success_count}/{len(image_configs)} 张图片")
    
    if success_count > 0:
        update_backgrounds_yml(image_configs)
        print("\n" + "=" * 50)
        print("下一步操作：")
        print("=" * 50)
        print("1. 运行: node node_modules\\hexo-cli\\bin\\hexo generate")
        print("2. 运行: node node_modules\\hexo-cli\\bin\\hexo deploy")
        print("=" * 50)

if __name__ == "__main__":
    main()
