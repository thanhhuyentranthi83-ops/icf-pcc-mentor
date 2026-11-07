const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const ARTIFACT_DIR = '/Users/admin/.gemini/antigravity/brain/077a58ad-e82f-4375-8053-a6d80ae15b5f';
const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const SCREENSHOT_DIR = path.join(__dirname, '..', 'screenshots');

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  console.log('Launching Chrome for Module 1 verification...');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 1800 });

    // ==========================================
    // 1. STREAMLIT APP VERIFICATION (PORT 8502)
    // ==========================================
    console.log('Navigating to Streamlit at http://localhost:8502...');
    await page.goto('http://localhost:8502', { waitUntil: 'networkidle2', timeout: 30000 });
    await page.waitForSelector('[data-testid="stAppViewContainer"]', { timeout: 20000 });
    await sleep(2500);

    // Click "Lộ Trình Học" button
    console.log('Finding Lộ Trình Học button...');
    const buttons = await page.$$('button');
    let currBtn = null;
    for (const btn of buttons) {
      const text = await page.evaluate(el => el.innerText, btn);
      if (text && text.includes('Lộ Trình Học')) {
        currBtn = btn;
        break;
      }
    }
    if (currBtn) {
      console.log('Clicking Lộ Trình Học button...');
      await currBtn.click();
      await sleep(3000);
    }

    // 1.1 Capture Header of Module 1
    console.log('Capturing Module 1 Header in Streamlit...');
    const headerStPath = path.join(SCREENSHOT_DIR, 'streamlit_module1_header_2025.png');
    await page.screenshot({ path: headerStPath, clip: { x: 260, y: 70, width: 1150, height: 350 } });
    console.log('Saved header to', headerStPath);

    // 1.2 Navigate to Lesson 2 (Competency 2)
    console.log('Finding Lesson 2 button...');
    const lesButtons = await page.$$('button');
    for (const btn of lesButtons) {
      const text = await page.evaluate(el => el.innerText, btn);
      if (text && text.includes('2. Năng Lực 2')) {
        console.log('Clicking Lesson 2 button...');
        await btn.click();
        await sleep(2500);
        break;
      }
    }
    const comp2StPath = path.join(SCREENSHOT_DIR, 'streamlit_competency2_separated.png');
    await page.screenshot({ path: comp2StPath, clip: { x: 420, y: 550, width: 980, height: 950 } });
    console.log('Saved Competency 2 to', comp2StPath);

    // 1.3 Navigate to Lesson 3 (Competency 3)
    console.log('Finding Lesson 3 button...');
    const lesButtons3 = await page.$$('button');
    for (const btn of lesButtons3) {
      const text = await page.evaluate(el => el.innerText, btn);
      if (text && text.includes('3. Năng Lực 3')) {
        console.log('Clicking Lesson 3 button...');
        await btn.click();
        await sleep(2500);
        break;
      }
    }
    const comp3StPath = path.join(SCREENSHOT_DIR, 'streamlit_competency3_sub_items.png');
    await page.screenshot({ path: comp3StPath, clip: { x: 420, y: 550, width: 980, height: 950 } });
    console.log('Saved Competency 3 to', comp3StPath);

    // 1.4 Navigate to Lesson 8 (Competency 8)
    console.log('Finding Lesson 8 button...');
    const lesButtons8 = await page.$$('button');
    for (const btn of lesButtons8) {
      const text = await page.evaluate(el => el.innerText, btn);
      if (text && text.includes('8. Năng Lực 8')) {
        console.log('Clicking Lesson 8 button...');
        await btn.click();
        await sleep(2500);
        break;
      }
    }
    const comp8StPath = path.join(SCREENSHOT_DIR, 'streamlit_competency8_sub_items.png');
    await page.screenshot({ path: comp8StPath, clip: { x: 420, y: 550, width: 980, height: 950 } });
    console.log('Saved Competency 8 to', comp8StPath);

    // ==========================================
    // 2. NEXT.JS APP VERIFICATION (PORT 3000)
    // ==========================================
    console.log('Navigating to Next.js Curriculum at http://localhost:3000/curriculum...');
    await page.goto('http://localhost:3000/curriculum?module=mod-1&lesson=mod1-les2', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2000);
    await page.evaluate(() => window.scrollTo(0, 650));
    await sleep(1000);
    const nextjsComp2Path = path.join(SCREENSHOT_DIR, 'nextjs_competency2_separated.png');
    await page.screenshot({ path: nextjsComp2Path, fullPage: false });
    console.log('Saved Next.js Competency 2 to', nextjsComp2Path);

    // Navigate to Lesson 3 in Next.js
    await page.goto('http://localhost:3000/curriculum?module=mod-1&lesson=mod1-les3', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2000);
    await page.evaluate(() => window.scrollTo(0, 650));
    await sleep(1000);
    const nextjsComp3Path = path.join(SCREENSHOT_DIR, 'nextjs_competency3_sub_items.png');
    await page.screenshot({ path: nextjsComp3Path, fullPage: false });
    console.log('Saved Next.js Competency 3 to', nextjsComp3Path);

    // Navigate to Lesson 8 in Next.js
    await page.goto('http://localhost:3000/curriculum?module=mod-1&lesson=mod1-les8', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2000);
    await page.evaluate(() => window.scrollTo(0, 650));
    await sleep(1000);
    const nextjsComp8Path = path.join(SCREENSHOT_DIR, 'nextjs_competency8_sub_items.png');
    await page.screenshot({ path: nextjsComp8Path, fullPage: false });
    console.log('Saved Next.js Competency 8 to', nextjsComp8Path);

    // Copy all to artifact dir
    const copyList = [
      headerStPath,
      comp2StPath,
      comp3StPath,
      comp8StPath,
      nextjsComp2Path,
      nextjsComp3Path,
      nextjsComp8Path
    ];

    for (const f of copyList) {
      if (fs.existsSync(f)) {
        fs.copyFileSync(f, path.join(ARTIFACT_DIR, path.basename(f)));
      }
    }
    console.log('All verification screenshots copied to artifact dir successfully!');

  } catch (err) {
    console.error('Error during capture:', err);
  } finally {
    await browser.close();
    console.log('Browser closed.');
  }
}

main();
