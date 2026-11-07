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
  console.log('Launching Chrome...');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 1000 });

    // 1. Visit Streamlit Library on port 8502
    console.log('Navigating to Streamlit at http://localhost:8502...');
    await page.goto('http://localhost:8502', { waitUntil: 'networkidle2', timeout: 30000 });
    await page.waitForSelector('[data-testid="stAppViewContainer"]', { timeout: 20000 });
    await sleep(3000);

    // Look for "Thư Viện Chuẩn" button
    console.log('Finding Library button...');
    const buttons = await page.$$('button');
    let libBtn = null;
    for (const btn of buttons) {
      const text = await page.evaluate(el => el.innerText, btn);
      if (text && text.includes('Thư Viện Chuẩn')) {
        libBtn = btn;
        break;
      }
    }

    if (libBtn) {
      console.log('Clicking Thư Viện Chuẩn button...');
      await libBtn.click();
      await sleep(3500);
    } else {
      console.log('Library button not found directly!');
    }

    // Now look for tab "8 Năng lực cốt lõi (2025)"
    console.log('Looking for Competencies 2025 tab...');
    const tabs = await page.$$('[role="tab"], button[data-baseweb="tab"]');
    for (const tab of tabs) {
      const text = await page.evaluate(el => el.innerText, tab);
      if (text && text.includes('8 Năng lực cốt lõi')) {
        console.log('Clicking tab:', text);
        await tab.click();
        await sleep(2500);
        break;
      }
    }

    // Expand the first competency expander if present
    const expanders = await page.$$('[data-testid="stExpander"]');
    if (expanders.length > 0) {
      console.log(`Found ${expanders.length} expanders, opening first one...`);
      await expanders[0].click();
      await sleep(1500);
    }

    // Scroll down slightly to show competencies header and content
    await page.evaluate(() => window.scrollBy(0, 180));
    await sleep(1000);

    const compScreenshotPath = path.join(SCREENSHOT_DIR, 'streamlit_competencies_2025.png');
    await page.screenshot({ path: compScreenshotPath, fullPage: false });
    console.log('Saved Competencies 2025 screenshot to', compScreenshotPath);

    // Now click on "Phân Định 3 Miền Chuẩn Mực" or "Bảng 11 Nguồn Kiểm Chứng"
    console.log('Looking for 3 Miền Chuẩn Mực tab...');
    const tabsAfter = await page.$$('[role="tab"], button[data-baseweb="tab"]');
    for (const tab of tabsAfter) {
      const text = await page.evaluate(el => el.innerText, tab);
      if (text && (text.includes('Phân Định 3 Miền') || text.includes('3 Miền Chuẩn Mực'))) {
        console.log('Clicking tab:', text);
        await tab.click();
        await sleep(2500);
        break;
      }
    }

    await page.evaluate(() => window.scrollBy(0, 80));
    await sleep(1000);

    const ethicsScreenshotPath = path.join(SCREENSHOT_DIR, 'streamlit_code_of_ethics_2025.png');
    await page.screenshot({ path: ethicsScreenshotPath, fullPage: false });
    console.log('Saved Code of Ethics 2025 screenshot to', ethicsScreenshotPath);

    // Also take screenshot of Tab 1: 11 Verified Sources
    for (const tab of tabsAfter) {
      const text = await page.evaluate(el => el.innerText, tab);
      if (text && text.includes('Nguồn Kiểm Chứng')) {
        console.log('Clicking tab:', text);
        await tab.click();
        await sleep(2500);
        break;
      }
    }
    await page.evaluate(() => window.scrollTo(0, 300));
    await sleep(1000);
    const sourcesScreenshotPath = path.join(SCREENSHOT_DIR, 'streamlit_verified_sources_2025.png');
    await page.screenshot({ path: sourcesScreenshotPath, fullPage: false });
    console.log('Saved Verified Sources screenshot to', sourcesScreenshotPath);

    // 2. Visit Next.js Curriculum
    console.log('Navigating to Next.js Curriculum at http://localhost:3000/curriculum...');
    await page.goto('http://localhost:3000/curriculum', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2500);

    const nextjsScreenshotPath = path.join(SCREENSHOT_DIR, 'nextjs_curriculum_2025.png');
    await page.screenshot({ path: nextjsScreenshotPath, fullPage: false });
    console.log('Saved Next.js Curriculum screenshot to', nextjsScreenshotPath);

    // Copy to artifact directory
    if (fs.existsSync(ARTIFACT_DIR)) {
      fs.copyFileSync(compScreenshotPath, path.join(ARTIFACT_DIR, 'streamlit_competencies_2025.png'));
      fs.copyFileSync(ethicsScreenshotPath, path.join(ARTIFACT_DIR, 'streamlit_code_of_ethics_2025.png'));
      fs.copyFileSync(sourcesScreenshotPath, path.join(ARTIFACT_DIR, 'streamlit_verified_sources_2025.png'));
      fs.copyFileSync(nextjsScreenshotPath, path.join(ARTIFACT_DIR, 'nextjs_curriculum_2025.png'));
      console.log('All screenshots copied to artifact directory successfully!');
    }

  } catch (err) {
    console.error('Error during capture:', err);
  } finally {
    await browser.close();
    console.log('Chrome closed.');
  }
}

main();
