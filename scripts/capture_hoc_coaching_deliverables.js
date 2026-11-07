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

function copyToArtifact(srcPath, filename) {
  const destPath = path.join(ARTIFACT_DIR, filename);
  fs.copyFileSync(srcPath, destPath);
  console.log(`Copied ${filename} to artifact directory.`);
}

async function main() {
  console.log('Launching Chrome for Học Coaching verification...');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
  });

  try {
    const page = await browser.newPage();

    // ==========================================
    // 1. NEXT.JS HOME DESKTOP (PORT 3000)
    // ==========================================
    console.log('Capturing Next.js Home Desktop...');
    await page.setViewport({ width: 1440, height: 2400 });
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2000);
    const homeDeskPath = path.join(SCREENSHOT_DIR, 'hoc_coaching_home_desktop.png');
    await page.screenshot({ path: homeDeskPath, fullPage: false, clip: { x: 0, y: 0, width: 1440, height: 1600 } });
    copyToArtifact(homeDeskPath, 'hoc_coaching_home_desktop.png');

    // ==========================================
    // 2. NEXT.JS HOME MOBILE (PORT 3000)
    // ==========================================
    console.log('Capturing Next.js Home Mobile (iPhone 13 / 390px)...');
    await page.setViewport({ width: 390, height: 1800, isMobile: true });
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2000);
    const homeMobPath = path.join(SCREENSHOT_DIR, 'hoc_coaching_home_mobile.png');
    await page.screenshot({ path: homeMobPath, clip: { x: 0, y: 0, width: 390, height: 1400 } });
    copyToArtifact(homeMobPath, 'hoc_coaching_home_mobile.png');

    // ==========================================
    // 3. NEXT.JS LESSON WITH SEPARATED SUB-COMPETENCY ITEMS
    // ==========================================
    console.log('Capturing Next.js Lesson 1 (Separated Sub-competencies)...');
    await page.setViewport({ width: 1440, height: 1800 });
    await page.goto('http://localhost:3000/curriculum?module=mod-1&lesson=mod1-les1', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2000);
    const lessonDeskPath = path.join(SCREENSHOT_DIR, 'hoc_coaching_lesson_subitems.png');
    await page.screenshot({ path: lessonDeskPath, clip: { x: 280, y: 100, width: 1100, height: 1200 } });
    copyToArtifact(lessonDeskPath, 'hoc_coaching_lesson_subitems.png');

    // ==========================================
    // 4. NEXT.JS SỔ HỌC TẬP (JOURNAL)
    // ==========================================
    console.log('Capturing Next.js Journal Page (/journal)...');
    await page.goto('http://localhost:3000/journal', { waitUntil: 'networkidle2', timeout: 30000 });
    await sleep(2000);
    const journalDeskPath = path.join(SCREENSHOT_DIR, 'hoc_coaching_journal_desktop.png');
    await page.screenshot({ path: journalDeskPath, clip: { x: 0, y: 0, width: 1440, height: 1300 } });
    copyToArtifact(journalDeskPath, 'hoc_coaching_journal_desktop.png');

    // ==========================================
    // 5. STREAMLIT HOME PAGE (PORT 8502)
    // ==========================================
    console.log('Capturing Streamlit Home Page with Coach Thanh Huyen...');
    await page.setViewport({ width: 1440, height: 2600 });
    await page.goto('http://localhost:8502', { waitUntil: 'networkidle2', timeout: 30000 });
    await page.waitForSelector('[data-testid="stAppViewContainer"]', { timeout: 20000 });
    await sleep(3000);
    const stHomePath = path.join(SCREENSHOT_DIR, 'hoc_coaching_streamlit_home.png');
    await page.screenshot({ path: stHomePath, clip: { x: 260, y: 70, width: 1150, height: 1550 } });
    copyToArtifact(stHomePath, 'hoc_coaching_streamlit_home.png');

    // ==========================================
    // 6. STREAMLIT SỔ HỌC TẬP (PORT 8502)
    // ==========================================
    console.log('Navigating to Streamlit Sổ Học Tập...');
    const buttons = await page.$$('button');
    let journalBtn = null;
    for (const b of buttons) {
      const text = await page.evaluate(el => el.innerText, b);
      if (text && text.includes('Sổ Học Tập')) {
        journalBtn = b;
        break;
      }
    }
    if (journalBtn) {
      await journalBtn.click();
      await sleep(3000);
      const stJournalPath = path.join(SCREENSHOT_DIR, 'hoc_coaching_streamlit_journal.png');
      await page.screenshot({ path: stJournalPath, clip: { x: 260, y: 70, width: 1150, height: 1200 } });
      copyToArtifact(stJournalPath, 'hoc_coaching_streamlit_journal.png');
    }

    // ==========================================
    // 7. STREAMLIT DAILY PRACTICE (WRAPPED OPTIONS & STAR)
    // ==========================================
    console.log('Navigating to Streamlit Daily Practice...');
    const buttons2 = await page.$$('button');
    let dailyBtn = null;
    for (const b of buttons2) {
      const text = await page.evaluate(el => el.innerText, b);
      if (text && text.includes('Luyện 10 Câu')) {
        dailyBtn = b;
        break;
      }
    }
    if (dailyBtn) {
      await dailyBtn.click();
      await sleep(3000);
      const stDailyPath = path.join(SCREENSHOT_DIR, 'hoc_coaching_streamlit_options.png');
      await page.screenshot({ path: stDailyPath, clip: { x: 260, y: 70, width: 1150, height: 1400 } });
      copyToArtifact(stDailyPath, 'hoc_coaching_streamlit_options.png');
    }

    // ==========================================
    // 8. STREAMLIT AI ASSISTANT (2025 CITATIONS & URLS)
    // ==========================================
    console.log('Navigating to Streamlit Trợ Lý Học Tập...');
    const buttons3 = await page.$$('button');
    let assistBtn = null;
    for (const b of buttons3) {
      const text = await page.evaluate(el => el.innerText, b);
      if (text && text.includes('Trợ Lý Học Tập')) {
        assistBtn = b;
        break;
      }
    }
    if (assistBtn) {
      await assistBtn.click();
      await sleep(3000);
      // Click shortcut query on ethics
      const subBtns = await page.$$('button');
      for (const sb of subBtns) {
        const text = await page.evaluate(el => el.innerText, sb);
        if (text && (text.includes('Bộ Quy tắc') || text.includes('ranh giới'))) {
          await sb.click();
          await sleep(2500);
          break;
        }
      }
      const stAssistPath = path.join(SCREENSHOT_DIR, 'hoc_coaching_streamlit_assistant.png');
      await page.screenshot({ path: stAssistPath, clip: { x: 260, y: 70, width: 1150, height: 1400 } });
      copyToArtifact(stAssistPath, 'hoc_coaching_streamlit_assistant.png');
    }

    console.log('All verification screenshots captured and copied successfully!');
  } finally {
    await browser.close();
  }
}

main().catch(err => {
  console.error('Error during capture:', err);
  process.exit(1);
});
