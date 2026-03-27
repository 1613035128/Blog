#!/usr/bin/env python3
"""
生成简历PDF
"""
import asyncio
from playwright.async_api import async_playwright

async def generate_pdf():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # 加载本地HTML文件
        await page.goto(f'file:///e:/MyBlog/Pleiadorum/public/resume/index.html')
        
        # 等待页面加载完成
        await page.wait_for_load_state('networkidle')
        
        # 生成PDF
        await page.pdf(
            path='宋浩然-游戏客户端开发工程师-简历.pdf',
            format='A4',
            print_background=True,
            margin={
                'top': '0',
                'right': '0',
                'bottom': '0',
                'left': '0'
            }
        )
        
        await browser.close()
        print("PDF生成成功：宋浩然-游戏客户端开发工程师-简历.pdf")

if __name__ == '__main__':
    asyncio.run(generate_pdf())
