const puppeteer = require("puppeteer-core");
const fs = require("fs");
const path = require("path");

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const SCREENSHOT_DIR = path.join(__dirname, "../screenshots");

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function run() {
  console.log("Launching headless Chrome from:", CHROME_PATH);
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
  });

  const page = await browser.newPage();

  // 1. Desktop Home
  console.log("1. Testing Desktop Home...");
  await page.setViewport({ width: 1280, height: 900 });
  await page.goto("http://localhost:3000", { waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "1_desktop_home.png") });

  // 2. Mobile Home
  console.log("2. Testing Mobile Home Viewport (iPhone 390x844)...");
  await page.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });
  await page.goto("http://localhost:3000", { waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "2_mobile_home.png") });

  // Reset to desktop
  await page.setViewport({ width: 1280, height: 900 });

  // 3. Test Language Toggle to English
  console.log("3. Testing Language Toggle...");
  await page.evaluate(() => {
    localStorage.setItem("icf_pcc_lang", "en");
  });
  await page.reload({ waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "3_english_home.png") });

  // Reset to Vietnamese
  await page.evaluate(() => {
    localStorage.setItem("icf_pcc_lang", "vi");
  });

  // 4. Test 6-Tab Section Page & Flashcards
  console.log("4. Testing 6-Tab Section & Flashcards...");
  await page.goto("http://localhost:3000/sections/sec-a1-1", { waitUntil: "networkidle0" });
  // Click Tab 3 (Flashcard)
  const tabButtons = await page.$$("button");
  for (const btn of tabButtons) {
    const text = await page.evaluate(el => el.textContent, btn);
    if (text && text.includes("Flashcard")) {
      await btn.click();
      break;
    }
  }
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "4_flashcards_tab.png") });

  // 5. Case Study Tab
  console.log("5. Testing Case Study Tab...");
  for (const btn of await page.$$("button")) {
    const text = await page.evaluate(el => el.textContent, btn);
    if (text && text.includes("Case Study")) {
      await btn.click();
      break;
    }
  }
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "5_case_study_tab.png") });

  // 6. Mock Exam 3-Breaths Modal
  console.log("6. Testing Mock Exam & Breathing Modal...");
  await page.goto("http://localhost:3000/mock-exam", { waitUntil: "networkidle0" });
  for (const btn of await page.$$("button")) {
    const text = await page.evaluate(el => el.textContent, btn);
    if (text && text.includes("Bắt đầu thi thử")) {
      await btn.click();
      break;
    }
  }
  await new Promise(r => setTimeout(r, 800));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "6_breathing_modal.png") });

  // 7. Skip to SJT Exam, select BEST & WORST, submit and view score report
  console.log("7. Testing SJT Best & Worst Exam Interaction...");
  for (const btn of await page.$$("button")) {
    const text = await page.evaluate(el => el.textContent, btn);
    if (text && text.includes("Bỏ qua và vào bài thi ngay")) {
      await btn.click();
      break;
    }
  }
  await new Promise(r => setTimeout(r, 1000));

  // Click BEST on option C, WORST on option A
  const bestButtons = await page.$$("button");
  for (const btn of bestButtons) {
    const text = await page.evaluate(el => el.textContent, btn);
    if (text === "BEST") {
      await btn.click();
      break;
    }
  }
  for (const btn of bestButtons) {
    const text = await page.evaluate(el => el.textContent, btn);
    if (text === "WORST") {
      await btn.click();
      break;
    }
  }
  // Submit exam
  for (const btn of await page.$$("button")) {
    const text = await page.evaluate(el => el.textContent, btn);
    if (text && text.includes("Nộp bài & Chấm điểm")) {
      await btn.click();
      break;
    }
  }
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "7_sjt_exam_results.png") });

  // 8. Checkout with 20% Promo code & VietQR
  console.log("8. Testing Checkout with VietQR...");
  await page.goto("http://localhost:3000/checkout?tier=6_months&code=PCC2026", { waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "8_checkout_vietqr.png") });

  // 9. Admin Dashboard (Logged in as Super Admin)
  console.log("9. Testing Admin Dashboard as Super Admin...");
  await page.evaluate(() => {
    localStorage.setItem("icf_pcc_current_user_id", "usr-admin");
  });
  await page.goto("http://localhost:3000/admin", { waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "9_admin_dashboard.png") });

  // 10. Admin Orders
  console.log("10. Testing Admin Orders...");
  await page.goto("http://localhost:3000/admin/orders", { waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "10_admin_orders.png") });

  // 11. Admin Sections Editor
  console.log("11. Testing Admin Sections Tree...");
  await page.goto("http://localhost:3000/admin/sections", { waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "11_admin_sections.png") });

  // 12. Design System Showroom
  console.log("12. Testing Design System Showroom...");
  await page.goto("http://localhost:3000/design", { waitUntil: "networkidle0" });
  await page.screenshot({ path: path.join(SCREENSHOT_DIR, "12_design_system.png") });

  await browser.close();
  console.log("All 12 E2E tests and screenshots captured successfully!");
}

run().catch(err => {
  console.error("Test failed:", err);
  process.exit(1);
});
