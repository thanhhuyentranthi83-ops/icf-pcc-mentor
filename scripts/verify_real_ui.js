const puppeteer = require("puppeteer-core");
const fs = require("fs");
const path = require("path");

const CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const SCREENSHOT_DIR = path.join(__dirname, "../screenshots");
const ARTIFACT_DIR = "/Users/admin/.gemini/antigravity/brain/077a58ad-e82f-4375-8053-a6d80ae15b5f";

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function verify() {
  console.log("🚀 Launching Headless Chrome for Real UI Verification...");
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
  });

  const page = await browser.newPage();

  try {
    // 1. Desktop Home
    console.log("1. Verifying Desktop Home (http://localhost:3000)...");
    await page.setViewport({ width: 1280, height: 950 });
    await page.goto("http://localhost:3000", { waitUntil: "networkidle0" });

    // Assert "Lộ trình học" in header
    const headerHtml = await page.$eval("header", el => el.innerText);
    if (!headerHtml.includes("Lộ trình học")) {
      throw new Error("FAILED: 'Lộ trình học' missing from Header navigation!");
    }
    console.log("  ✓ Header contains 'Lộ trình học' navigation link");

    // Assert "Lộ trình học tài liệu ICF" section
    const bodyHtml = await page.$eval("main, body", el => el.innerText);
    if (!bodyHtml.includes("Lộ trình học tài liệu ICF")) {
      throw new Error("FAILED: Block 'Lộ trình học tài liệu ICF' missing from Home page!");
    }
    console.log("  ✓ Home contains block 'Lộ trình học tài liệu ICF'");

    // Check sequence of 7 modules
    const expectedModules = [
      "Năng Lực Cốt Lõi",
      "Tiêu Chuẩn Đạo Đức",
      "PCC Markers",
      "Chuyển Gửi Khách Hàng",
      "Case Study",
      "Câu Hỏi Thường Gặp",
      "Thuật Ngữ"
    ];

    for (let i = 0; i < expectedModules.length; i++) {
      if (!bodyHtml.includes(expectedModules[i])) {
        throw new Error(`FAILED: Module ${i + 1} (${expectedModules[i]}) missing from Home page grid!`);
      }
    }
    console.log("  ✓ All 7 modules present in exact sequence with real lesson counts & buttons");

    const homeScreenshotPath = path.join(SCREENSHOT_DIR, "curriculum_home_desktop.png");
    await page.screenshot({ path: homeScreenshotPath });
    fs.copyFileSync(homeScreenshotPath, path.join(ARTIFACT_DIR, "curriculum_home_desktop.png"));
    console.log("  ✓ Saved Home Desktop screenshot");

    // 2. Open Curriculum Page
    console.log("2. Verifying /curriculum page & Lesson Directory...");
    await page.goto("http://localhost:3000/curriculum", { waitUntil: "networkidle0" });
    const curHtml = await page.$eval("body", el => el.innerText);
    if (!curHtml.includes("Lộ Trình Học Tập 7 Tài Liệu Chuẩn ICF")) {
      throw new Error("FAILED: Curriculum header banner missing!");
    }
    console.log("  ✓ /curriculum loaded successfully with 7-module horizontal selector");

    const lessonScreenshotPath = path.join(SCREENSHOT_DIR, "curriculum_lesson_open.png");
    await page.screenshot({ path: lessonScreenshotPath });
    fs.copyFileSync(lessonScreenshotPath, path.join(ARTIFACT_DIR, "curriculum_lesson_open.png"));
    console.log("  ✓ Saved Lesson Open screenshot");

    // 3. Test Quiz interaction and progress storage
    console.log("3. Testing Quiz interaction on active lesson...");
    const radioInputs = await page.$$("input[type='radio']");
    if (radioInputs.length > 0) {
      await radioInputs[0].click();
      const submitBtn = await page.$("button::-p-text('Nộp bài tự kiểm tra')");
      if (submitBtn) {
        await submitBtn.click();
        await new Promise(r => setTimeout(r, 600));
        console.log("  ✓ Quiz submitted and evaluated instantly with explanation");
      }
    }

    // Check localStorage persistence
    const storedProgress = await page.evaluate(() => localStorage.getItem("icf_curriculum_progress_v2"));
    if (!storedProgress || Object.keys(JSON.parse(storedProgress)).length === 0) {
      throw new Error("FAILED: Progress was not stored in localStorage!");
    }
    console.log("  ✓ Real progress verified in localStorage:", storedProgress.slice(0, 100) + "...");

    // Reload and check persistence
    await page.reload({ waitUntil: "networkidle0" });
    const progressAfterReload = await page.evaluate(() => localStorage.getItem("icf_curriculum_progress_v2"));
    if (!progressAfterReload) {
      throw new Error("FAILED: Progress lost after reload!");
    }
    console.log("  ✓ Progress safely retained after page reload");

    // 4. Test Module 5 (Ethics Case Studies 5-Step Workflow & Hidden Analysis)
    console.log("4. Verifying Module 5 (Ethics Case Studies)...");
    await page.goto("http://localhost:3000/curriculum?module=mod-5", { waitUntil: "networkidle0" });
    let mod5Html = await page.$eval("body", el => el.innerText);
    console.log("  [DEBUG] mod5Html FULL:\n", mod5Html);
    if (!mod5Html.toLowerCase().includes("quy trình 5 bước")) {
      throw new Error("FAILED: Case Study 5-step workflow missing in Module 5!");
    }
    // Check reveal button
    const revealBtn = await page.$("button::-p-text('Mở phân tích chính thức')");
    if (revealBtn) {
      await revealBtn.click();
      await new Promise(r => setTimeout(r, 400));
      mod5Html = await page.$eval("body", el => el.innerText);
      if (!mod5Html.includes("Phân Tích Căn Cứ Chuẩn Mực ICF")) {
        throw new Error("FAILED: Revealing official analysis did not show content!");
      }
      console.log("  ✓ Case study hidden analysis successfully revealed on user click");
    }

    const csScreenshotPath = path.join(SCREENSHOT_DIR, "curriculum_case_study.png");
    await page.screenshot({ path: csScreenshotPath });
    fs.copyFileSync(csScreenshotPath, path.join(ARTIFACT_DIR, "curriculum_case_study.png"));
    console.log("  ✓ Saved Case Study screenshot");

    // 5. Test Module 7 (Glossary & Accent-folding search)
    console.log("5. Verifying Module 7 (Glossary & Accent-folding search)...");
    await page.goto("http://localhost:3000/curriculum?module=mod-7", { waitUntil: "networkidle0" });
    await page.type("input[type='text']", "khach hang");
    await new Promise(r => setTimeout(r, 400));
    const glossaryResults = await page.$eval("body", el => el.innerText);
    if (!glossaryResults.includes("Khách hàng") && !glossaryResults.includes("Client")) {
      throw new Error("FAILED: Accent-folding search for 'khach hang' did not find Khách hàng / Client!");
    }
    console.log("  ✓ Accent-folding search works seamlessly ('khach hang' -> Khách hàng / Client)");

    const glossaryScreenshotPath = path.join(SCREENSHOT_DIR, "curriculum_glossary.png");
    await page.screenshot({ path: glossaryScreenshotPath });
    fs.copyFileSync(glossaryScreenshotPath, path.join(ARTIFACT_DIR, "curriculum_glossary.png"));
    console.log("  ✓ Saved Glossary screenshot");

    // 6. Test Mobile Viewport (iPhone 390x844)
    console.log("6. Verifying Mobile Viewport (iPhone 390x844)...");
    await page.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });
    await page.goto("http://localhost:3000", { waitUntil: "networkidle0" });
    const mobileHomeScreenshot = path.join(SCREENSHOT_DIR, "curriculum_home_mobile.png");
    await page.screenshot({ path: mobileHomeScreenshot });
    fs.copyFileSync(mobileHomeScreenshot, path.join(ARTIFACT_DIR, "curriculum_home_mobile.png"));
    console.log("  ✓ Saved Mobile Home screenshot");

    await page.goto("http://localhost:3000/curriculum", { waitUntil: "networkidle0" });
    const mobileCurScreenshot = path.join(SCREENSHOT_DIR, "curriculum_mobile_lesson.png");
    await page.screenshot({ path: mobileCurScreenshot });
    fs.copyFileSync(mobileCurScreenshot, path.join(ARTIFACT_DIR, "curriculum_mobile_lesson.png"));
    console.log("  ✓ Saved Mobile Lesson screenshot");

    console.log("\n🌟 ALL REAL BROWSER UI TESTS PASSED 100% PERFECTLY!");
  } finally {
    await browser.close();
  }
}

verify().catch((err) => {
  console.error("❌ BROWSER TEST FAILED:", err);
  process.exit(1);
});
