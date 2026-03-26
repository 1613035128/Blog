import asyncio
from playwright.async_api import async_playwright
import os

async def generate_pdf():
    async with async_playwright() as p:
        # 使用系统自带的Edge浏览器
        browser = await p.chromium.launch(
            executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
            headless=True
        )
        page = await browser.new_page()
        
        # 加载本地简历HTML文件
        resume_path = os.path.abspath('source/resume/index.html')
        await page.goto(f'file:///{resume_path}', wait_until='networkidle')
        
        # 生成PDF
        await page.pdf(
            path='宋浩然-游戏客户端开发工程师-简历.pdf',
            format='A4',
            print_background=True,
            margin={
                'top': '20px',
                'right': '20px',
                'bottom': '20px',
                'left': '20px'
            }
        )
        
        await browser.close()
        print('PDF生成成功: 宋浩然-游戏客户端开发工程师-简历.pdf')

if __name__ == '__main__':
    asyncio.run(generate_pdf())
