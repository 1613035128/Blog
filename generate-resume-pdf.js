const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // 加载本地简历HTML文件
  const resumePath = path.resolve(__dirname, 'source/resume/index.html');
  await page.goto('file://' + resumePath, {
    waitUntil: 'networkidle0'
  });
  
  // 生成PDF
  await page.pdf({
    path: '宋浩然-游戏客户端开发工程师-简历.pdf',
    format: 'A4',
    printBackground: true,
    margin: {
      top: '20px',
      right: '20px',
      bottom: '20px',
      left: '20px'
    }
  });
  
  await browser.close();
  console.log('PDF生成成功: 宋浩然-游戏客户端开发工程师-简历.pdf');
})();
