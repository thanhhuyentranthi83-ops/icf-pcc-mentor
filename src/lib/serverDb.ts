import fs from "fs";
import path from "path";
import crypto from "crypto";
import {
  CourseRecord,
  PackageRecord,
  EnrollmentRecord,
  EnrollmentHistoryRecord,
  EnrollmentRequestRecord,
  FeatureKey
} from "@/types";

export interface UserRecord {
  id: string;
  email: string;
  fullName: string;
  role: "super_admin" | "editor" | "billing" | "student";
  tier: "free" | "1_month" | "6_months" | "12_months";
  tierExpiresAt: string | null;
  streakCount: number;
  lastActiveDate: string;
  createdAt: string;
}

export interface LessonProgressRecord {
  status: "unread" | "read" | "quiz_passed";
  score?: number;
  quizPassedAt?: string;
  updatedAt: string;
  note?: string;
  needsReview?: boolean;
}

export interface DatabaseSchema {
  users: UserRecord[];
  progress: Record<string, Record<string, LessonProgressRecord>>; // userId -> lessonId -> progress
  bookmarks: Record<string, string[]>; // userId -> questionId[]
  exams: Record<string, any[]>; // userId -> examSessions[]
  sessions: Record<string, { userId: string; expiresAt: string }>; // token -> session
  courses: CourseRecord[];
  packages: PackageRecord[];
  enrollments: Record<string, EnrollmentRecord[]>; // userId -> EnrollmentRecord[]
  enrollmentHistory: EnrollmentHistoryRecord[];
  enrollmentRequests: EnrollmentRequestRecord[];
}

export const SEED_COURSES_INIT: CourseRecord[] = [
  {
    id: "crs-foundation",
    titleVi: "Nền Tảng Khai Vấn Chuẩn Quốc Tế ICF",
    titleEn: "ICF Professional Coaching Foundations",
    descriptionVi: "Làm chủ 8 Năng lực cốt lõi, Quy tắc đạo đức 2025 và tiêu chuẩn chuyển gửi khách hàng.",
    descriptionEn: "Master the 8 ICF Core Competencies, 2025 Code of Ethics, and client referral guidelines.",
    moduleIds: ["mod-1", "mod-2", "mod-4", "mod-7"],
    previewLessonIds: ["mod1-les1"], // Cho phép học thử Bài 1 Năng lực 1
    isPublished: true,
    orderIndex: 1,
    badgeText: "Nền tảng vững chắc"
  },
  {
    id: "crs-exam-prep",
    titleVi: "Luyện Thi ICF Credentialing (ACC/PCC Exam Prep)",
    titleEn: "ICF Credentialing Exam Preparation",
    descriptionVi: "Rèn luyện phản xạ tình huống phán đoán (SJT), tiêu chí thực hành PCC Markers và đề thi mô phỏng 78/80 câu.",
    descriptionEn: "Master Situational Judgment Tests (SJT), PCC Markers, and comprehensive 78/80 scenario mock exams.",
    moduleIds: ["mod-3", "mod-5", "mod-6"],
    previewLessonIds: ["mod6-les1"], // Cho phép xem thử Đề mẫu 8 câu ICF
    isPublished: true,
    orderIndex: 2,
    badgeText: "Luyện thi thực chiến"
  },
  {
    id: "crs-all-in-one",
    titleVi: "Học Coaching Toàn Diện: Nền Tảng & Luyện Thi ICF PCC",
    titleEn: "Comprehensive Coaching Mastery & ICF PCC Exam",
    descriptionVi: "Trọn bộ 7 học phần chính thức, luyện tập 10 câu mỗi ngày, thư viện thuật ngữ và phòng thi mô phỏng không giới hạn.",
    descriptionEn: "Complete access to all 7 modules, daily 10 SJT drills, terminology library, and unlimited mock exams.",
    moduleIds: ["mod-1", "mod-2", "mod-3", "mod-4", "mod-5", "mod-6", "mod-7"],
    previewLessonIds: ["mod1-les1", "mod6-les1"],
    isPublished: true,
    orderIndex: 3,
    badgeText: "Khuyên Dùng (All-in-One)"
  }
];

export const SEED_PACKAGES_INIT: PackageRecord[] = [
  {
    id: "pkg-trial",
    nameVi: "Gói Học Thử Trải Nghiệm (Free Trial)",
    nameEn: "Free Trial Experience",
    descriptionVi: "Trải nghiệm miễn phí các bài học mẫu, 8 câu hỏi tình huống ICF và Sổ học tập chánh niệm.",
    descriptionEn: "Free access to trial lessons, 8 official sample questions, and personal learning journal.",
    price: 0,
    durationDays: 0, // Vĩnh viễn cho nội dung xem thử
    isRegistrationOpen: true,
    allowedCourseIds: ["crs-foundation", "crs-exam-prep"],
    allowedFeatures: ["curriculum", "glossary_search", "tea_micro"],
    badge: "Miễn phí",
    isDefaultTrial: true
  },
  {
    id: "pkg-foundation",
    nameVi: "Gói Nền Tảng Khai Vấn (Foundation)",
    nameEn: "Coaching Foundations Tier",
    descriptionVi: "Mở khóa trọn bộ Lộ trình 7 học phần chuẩn hóa ICF, lý thuyết chuyên sâu và tra cứu thuật ngữ.",
    descriptionEn: "Full access to 7 official ICF modules, in-depth competencies, and glossary library.",
    price: 299000,
    durationDays: 30,
    isRegistrationOpen: true,
    allowedCourseIds: ["crs-foundation"],
    allowedFeatures: ["curriculum", "glossary_search", "tea_micro", "resource_download"],
    badge: "Khởi đầu"
  },
  {
    id: "pkg-exam-prep",
    nameVi: "Gói Luyện Thi ICF Credentialing (Exam Prep)",
    nameEn: "ICF Exam Prep Tier",
    descriptionVi: "Mở khóa chế độ Luyện 10 câu/ngày, Đề thi mô phỏng toàn diện 78/80 câu SJT và phân tích Best/Worst.",
    descriptionEn: "Unlock Daily 10 SJT drills, full 78/80 question mock exams, and Best/Worst rationale.",
    price: 1190000,
    durationDays: 180,
    isRegistrationOpen: true,
    allowedCourseIds: ["crs-exam-prep"],
    allowedFeatures: ["daily_sjt_10", "mock_exam_sjt", "glossary_search", "resource_download"],
    badge: "Mục tiêu đỗ PCC"
  },
  {
    id: "pkg-pcc-master",
    nameVi: "Gói Đồng Hành Toàn Diện (PCC Master Pass)",
    nameEn: "PCC Master Comprehensive Pass",
    descriptionVi: "Quyền truy cập cao nhất vào tất cả các khóa học, đề thi thử, tính năng hiện tại và các bản cập nhật mới trong 12 tháng.",
    descriptionEn: "Unrestricted access to all courses, modules, mock exams, and future updates for 12 months.",
    price: 1990000,
    durationDays: 365,
    isRegistrationOpen: true,
    allowedCourseIds: ["*"],
    allowedFeatures: ["curriculum", "daily_sjt_10", "mock_exam_sjt", "glossary_search", "tea_micro", "resource_download"],
    badge: "Toàn diện nhất"
  }
];

const DB_PATH = path.join(process.cwd(), "data", "app_database.json");
const WHITELIST_PATH = path.join(process.cwd(), "config", "admin_whitelist.json");

const SEED_USERS_INIT: UserRecord[] = [
  {
    id: "usr-admin",
    email: "admin@pcc.vn",
    fullName: "Super Admin Tâm An",
    role: "super_admin",
    tier: "12_months",
    tierExpiresAt: "2027-12-31T23:59:59Z",
    streakCount: 28,
    lastActiveDate: "2026-11-07",
    createdAt: "2026-11-01T00:00:00Z"
  },
  {
    id: "usr-editor",
    email: "editor@pcc.vn",
    fullName: "Biên Tập Viên Tuệ Minh",
    role: "editor",
    tier: "12_months",
    tierExpiresAt: "2027-12-31T23:59:59Z",
    streakCount: 14,
    lastActiveDate: "2026-11-07",
    createdAt: "2026-11-01T00:00:00Z"
  },
  {
    id: "usr-billing",
    email: "billing@pcc.vn",
    fullName: "Thu Ngân Diệu Thiện",
    role: "billing",
    tier: "12_months",
    tierExpiresAt: "2027-12-31T23:59:59Z",
    streakCount: 7,
    lastActiveDate: "2026-11-07",
    createdAt: "2026-11-01T00:00:00Z"
  },
  {
    id: "usr-free",
    email: "student.free@pcc.vn",
    fullName: "Học Viên Minh Đức (Gói Free)",
    role: "student",
    tier: "free",
    tierExpiresAt: null,
    streakCount: 3,
    lastActiveDate: "2026-11-07",
    createdAt: "2026-11-01T00:00:00Z"
  },
  {
    id: "usr-1m",
    email: "student.1m@pcc.vn",
    fullName: "Học Viên Thu Hương (Gói 1 Tháng)",
    role: "student",
    tier: "1_month",
    tierExpiresAt: "2026-11-30T23:59:59Z",
    streakCount: 9,
    lastActiveDate: "2026-11-07",
    createdAt: "2026-11-01T00:00:00Z"
  }
];

export function getAdminWhitelist(): string[] {
  const emails = new Set<string>();
  // From env
  if (process.env.ADMIN_EMAILS) {
    process.env.ADMIN_EMAILS.split(",").forEach(e => emails.add(e.trim().toLowerCase()));
  }
  // From config file
  try {
    if (fs.existsSync(WHITELIST_PATH)) {
      const content = fs.readFileSync(WHITELIST_PATH, "utf-8");
      const parsed = JSON.parse(content);
      if (Array.isArray(parsed.adminEmails)) {
        parsed.adminEmails.forEach((e: string) => emails.add(e.trim().toLowerCase()));
      }
    }
  } catch (err) {
    console.error("Error reading admin whitelist:", err);
  }
  // Default fallbacks
  emails.add("admin@pcc.vn");
  emails.add("admin@hoccoaching.vn");
  emails.add("admin.coach@pcc.edu.vn");
  return Array.from(emails);
}

export function isAdminEmail(email: string): boolean {
  const clean = email.trim().toLowerCase();
  const list = getAdminWhitelist();
  return list.includes(clean);
}

export function getDatabase(): DatabaseSchema {
  try {
    if (!fs.existsSync(DB_PATH)) {
      const initial: DatabaseSchema = {
        users: [...SEED_USERS_INIT],
        progress: {},
        bookmarks: {},
        exams: {},
        sessions: {},
        courses: [...SEED_COURSES_INIT],
        packages: [...SEED_PACKAGES_INIT],
        enrollments: {},
        enrollmentHistory: [],
        enrollmentRequests: []
      };
      saveDatabase(initial);
      return initial;
    }
    const raw = fs.readFileSync(DB_PATH, "utf-8");
    const parsed = JSON.parse(raw);
    if (!parsed.users) parsed.users = [...SEED_USERS_INIT];
    if (!parsed.progress) parsed.progress = {};
    if (!parsed.bookmarks) parsed.bookmarks = {};
    if (!parsed.exams) parsed.exams = {};
    if (!parsed.sessions) parsed.sessions = {};
    if (!parsed.courses || parsed.courses.length === 0) parsed.courses = [...SEED_COURSES_INIT];
    if (!parsed.packages || parsed.packages.length === 0) parsed.packages = [...SEED_PACKAGES_INIT];
    if (!parsed.enrollments) parsed.enrollments = {};
    if (!parsed.enrollmentHistory) parsed.enrollmentHistory = [];
    if (!parsed.enrollmentRequests) parsed.enrollmentRequests = [];
    return parsed;
  } catch (err) {
    console.error("Error reading database:", err);
    return {
      users: [...SEED_USERS_INIT],
      progress: {},
      bookmarks: {},
      exams: {},
      sessions: {},
      courses: [...SEED_COURSES_INIT],
      packages: [...SEED_PACKAGES_INIT],
      enrollments: {},
      enrollmentHistory: [],
      enrollmentRequests: []
    };
  }
}

export function saveDatabase(db: DatabaseSchema): void {
  try {
    const dir = path.dirname(DB_PATH);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    const tmpPath = `${DB_PATH}.tmp.${Date.now()}`;
    fs.writeFileSync(tmpPath, JSON.stringify(db, null, 2), "utf-8");
    fs.renameSync(tmpPath, DB_PATH);
  } catch (err) {
    console.error("Error saving database:", err);
  }
}

export function findUserByEmail(email: string): UserRecord | undefined {
  const db = getDatabase();
  const clean = email.trim().toLowerCase();
  return db.users.find(u => u.email.toLowerCase() === clean);
}

export function findUserById(id: string): UserRecord | undefined {
  const db = getDatabase();
  return db.users.find(u => u.id === id);
}

export function createOrUpdateUser(email: string, fullName?: string): UserRecord {
  const db = getDatabase();
  const clean = email.trim().toLowerCase();
  const isSuper = isAdminEmail(clean);

  let user = db.users.find(u => u.email.toLowerCase() === clean);
  const now = new Date().toISOString();

  if (user) {
    // If email is in admin whitelist, promote to super_admin
    if (isSuper && user.role !== "super_admin") {
      user.role = "super_admin";
      user.tier = "12_months";
    }
    if (fullName && fullName.trim() && user.fullName.startsWith("Học Viên ") && !fullName.startsWith("Học Viên ")) {
      user.fullName = fullName.trim();
    }
    user.lastActiveDate = now.split("T")[0];
  } else {
    // Generate clean id
    const hash = crypto.createHash("md5").update(clean).digest("hex").slice(0, 8);
    user = {
      id: isSuper ? `usr-admin-${hash}` : `usr-${hash}`,
      email: clean,
      fullName: fullName?.trim() || (isSuper ? "Quản Trị Viên" : `Học Viên ${clean.split("@")[0]}`),
      role: isSuper ? "super_admin" : "student",
      tier: isSuper ? "12_months" : "free",
      tierExpiresAt: isSuper ? "2027-12-31T23:59:59Z" : null,
      streakCount: 1,
      lastActiveDate: now.split("T")[0],
      createdAt: now
    };
    db.users.push(user);
  }

  saveDatabase(db);
  return user;
}

export function computeLotuses(userProgress: Record<string, LessonProgressRecord>): number {
  if (!userProgress) return 0;
  // 1 lotus per valid completed lesson (read or quiz_passed), counted strictly once
  const completed = Object.values(userProgress).filter(
    p => p.status === "read" || p.status === "quiz_passed"
  ).length;
  return completed;
}

export function getUserProgress(userId: string) {
  const db = getDatabase();
  const progress = db.progress[userId] || {};
  const bookmarks = db.bookmarks[userId] || [];
  const exams = db.exams[userId] || [];

  const lotusBloomed = computeLotuses(progress);

  // Extract personal notes
  const notes: Record<string, string> = {};
  const flaggedLessons: string[] = [];

  for (const [lesId, p] of Object.entries(progress)) {
    if (p.note) notes[lesId] = p.note;
    if (p.needsReview) flaggedLessons.push(lesId);
  }

  return {
    userId,
    progress,
    lotusBloomed,
    notes,
    flaggedLessons,
    bookmarks,
    exams
  };
}

export function saveUserLessonProgress(
  userId: string,
  lessonId: string,
  update: Partial<LessonProgressRecord>
) {
  const db = getDatabase();
  if (!db.progress[userId]) {
    db.progress[userId] = {};
  }

  const existing = db.progress[userId][lessonId] || {
    status: "unread",
    updatedAt: new Date().toISOString()
  };

  // Do not downgrade quiz_passed to read
  let nextStatus = update.status || existing.status;
  if (existing.status === "quiz_passed" && update.status === "read") {
    nextStatus = "quiz_passed";
  }

  const now = new Date().toISOString();
  db.progress[userId][lessonId] = {
    ...existing,
    ...update,
    status: nextStatus,
    updatedAt: now
  };

  // Update user last active
  const user = db.users.find(u => u.id === userId);
  if (user) {
    user.lastActiveDate = now.split("T")[0];
  }

  saveDatabase(db);
  return getUserProgress(userId);
}

export function saveUserBookmark(userId: string, questionId: string, action: "toggle" | "add" | "remove") {
  const db = getDatabase();
  if (!db.bookmarks[userId]) {
    db.bookmarks[userId] = [];
  }
  const set = new Set(db.bookmarks[userId]);
  if (action === "add") {
    set.add(questionId);
  } else if (action === "remove") {
    set.delete(questionId);
  } else {
    if (set.has(questionId)) set.delete(questionId);
    else set.add(questionId);
  }
  db.bookmarks[userId] = Array.from(set);
  saveDatabase(db);
  return db.bookmarks[userId];
}

export function mergeGuestProgress(userId: string, guestProgress: Record<string, LessonProgressRecord>) {
  const db = getDatabase();
  if (!db.progress[userId]) {
    db.progress[userId] = {};
  }

  const userProg = db.progress[userId];
  let mergedCount = 0;

  for (const [lesId, gItem] of Object.entries(guestProgress)) {
    const existing = userProg[lesId];
    if (!existing) {
      userProg[lesId] = { ...gItem, updatedAt: new Date().toISOString() };
      mergedCount++;
    } else {
      // Merge smartly: keep higher status
      let nextStatus = existing.status;
      if (gItem.status === "quiz_passed") nextStatus = "quiz_passed";
      else if (existing.status !== "quiz_passed" && gItem.status === "read") nextStatus = "read";

      // Keep user's note if exists, otherwise take guest note
      const note = existing.note || gItem.note;
      const needsReview = existing.needsReview || gItem.needsReview;
      const score = Math.max(existing.score || 0, gItem.score || 0);

      userProg[lesId] = {
        ...existing,
        status: nextStatus,
        score,
        note,
        needsReview,
        updatedAt: new Date().toISOString()
      };
      mergedCount++;
    }
  }

  saveDatabase(db);
  return {
    ...getUserProgress(userId),
    mergedCount
  };
}

export function createSession(userId: string): string {
  const db = getDatabase();
  const token = crypto.randomBytes(32).toString("hex");
  // 30 days session
  const exp = new Date();
  exp.setDate(exp.getDate() + 30);

  db.sessions[token] = {
    userId,
    expiresAt: exp.toISOString()
  };
  saveDatabase(db);
  return token;
}

export function getUserBySession(token: string): UserRecord | null {
  if (!token) return null;
  const db = getDatabase();
  const sess = db.sessions[token];
  if (!sess) return null;

  if (new Date(sess.expiresAt) < new Date()) {
    delete db.sessions[token];
    saveDatabase(db);
    return null;
  }

  const user = db.users.find(u => u.id === sess.userId);
  return user || null;
}

export function deleteSession(token: string): void {
  if (!token) return;
  const db = getDatabase();
  if (db.sessions[token]) {
    delete db.sessions[token];
    saveDatabase(db);
  }
}

/**
 * Returns all student profiles for admin inspection.
 * IMPORTANT: To protect student privacy, personal note texts are STRICTLY excluded!
 */
export function getAllStudentsForAdmin() {
  const db = getDatabase();

  return db.users.map(u => {
    const prog = db.progress[u.id] || {};
    const completedLessons = Object.values(prog).filter(p => p.status === "read" || p.status === "quiz_passed").length;
    const passedQuizzes = Object.values(prog).filter(p => p.status === "quiz_passed").length;
    const lotuses = computeLotuses(prog);
    const flaggedCount = Object.values(prog).filter(p => p.needsReview).length;
    const notesCount = Object.values(prog).filter(p => !!p.note).length;
    const bookmarksCount = (db.bookmarks[u.id] || []).length;
    const examSessionsCount = (db.exams[u.id] || []).length;

    // Detailed milestone events (without personal note texts)
    const milestones = Object.entries(prog)
      .filter(([_, p]) => p.status === "read" || p.status === "quiz_passed")
      .map(([lesId, p]) => ({
        lessonId: lesId,
        status: p.status,
        score: p.score || null,
        updatedAt: p.updatedAt
      }));

    return {
      id: u.id,
      email: u.email,
      fullName: u.fullName,
      role: u.role,
      tier: u.tier,
      tierExpiresAt: u.tierExpiresAt,
      streakCount: u.streakCount,
      lastActiveDate: u.lastActiveDate,
      createdAt: u.createdAt,
      enrollments: db.enrollments[u.id] || [],
      enrollmentStatus: (() => {
        const uEnrs = db.enrollments[u.id] || [];
        const now = new Date().toISOString();
        const hasPendingReq = (db.enrollmentRequests || []).some(r => r.userId === u.id && r.status === "pending");
        if (hasPendingReq) return "pending";
        const activeEnr = uEnrs.find(e => e.status === "active" && (!e.expiresAt || e.expiresAt > now));
        if (activeEnr) return activeEnr.packageId === "pkg-trial" ? "trial" : "active";
        if (uEnrs.some(e => e.status === "expired" || (e.expiresAt && e.expiresAt < now))) return "expired";
        if (uEnrs.some(e => e.status === "revoked")) return "revoked";
        return "none";
      })(),
      stats: {
        completedLessons,
        passedQuizzes,
        lotusesBloomed: lotuses,
        flaggedLessonsCount: flaggedCount,
        notesCount, // Count only, NOT note content
        bookmarksCount,
        examSessionsCount
      },
      milestones
    };
  });
}

// -------------------------------------------------------------
// COURSE MANAGEMENT METHODS
// -------------------------------------------------------------

export function getCourses(publishedOnly: boolean = false): CourseRecord[] {
  const db = getDatabase();
  const list = db.courses || [...SEED_COURSES_INIT];
  if (publishedOnly) {
    return list.filter(c => c.isPublished).sort((a, b) => a.orderIndex - b.orderIndex);
  }
  return [...list].sort((a, b) => a.orderIndex - b.orderIndex);
}

export function getCourseById(id: string): CourseRecord | undefined {
  const db = getDatabase();
  return (db.courses || []).find(c => c.id === id);
}

export function saveCourse(course: CourseRecord): CourseRecord {
  const db = getDatabase();
  if (!db.courses) db.courses = [...SEED_COURSES_INIT];
  const idx = db.courses.findIndex(c => c.id === course.id);
  if (idx >= 0) {
    db.courses[idx] = { ...course };
  } else {
    db.courses.push({ ...course });
  }
  saveDatabase(db);
  return course;
}

export function deleteCourse(id: string): boolean {
  const db = getDatabase();
  if (!db.courses) return false;
  const initialLen = db.courses.length;
  db.courses = db.courses.filter(c => c.id !== id);
  if (db.courses.length !== initialLen) {
    saveDatabase(db);
    return true;
  }
  return false;
}

// -------------------------------------------------------------
// PACKAGE (GÓI HỌC VIÊN) MANAGEMENT METHODS
// -------------------------------------------------------------

export function getPackages(openOnly: boolean = false): PackageRecord[] {
  const db = getDatabase();
  const list = db.packages || [...SEED_PACKAGES_INIT];
  if (openOnly) {
    return list.filter(p => p.isRegistrationOpen);
  }
  return list;
}

export function getPackageById(id: string): PackageRecord | undefined {
  const db = getDatabase();
  return (db.packages || []).find(p => p.id === id);
}

export function savePackage(pkg: PackageRecord): PackageRecord {
  const db = getDatabase();
  if (!db.packages) db.packages = [...SEED_PACKAGES_INIT];
  const idx = db.packages.findIndex(p => p.id === pkg.id);
  if (idx >= 0) {
    db.packages[idx] = { ...pkg };
  } else {
    db.packages.push({ ...pkg });
  }
  saveDatabase(db);
  return pkg;
}

export function deletePackage(id: string): boolean {
  const db = getDatabase();
  if (!db.packages) return false;
  const initialLen = db.packages.length;
  db.packages = db.packages.filter(p => p.id !== id);
  if (db.packages.length !== initialLen) {
    saveDatabase(db);
    return true;
  }
  return false;
}

// -------------------------------------------------------------
// ENROLLMENT, GRANT, RENEW, REVOKE & HISTORY METHODS
// -------------------------------------------------------------

export function getUserEnrollments(userId: string): EnrollmentRecord[] {
  const db = getDatabase();
  return db.enrollments[userId] || [];
}

export function grantPackage(
  userId: string,
  packageId: string,
  durationDays: number,
  adminEmail: string,
  note: string = ""
): EnrollmentRecord {
  const db = getDatabase();
  const user = db.users.find(u => u.id === userId);
  const pkg = (db.packages || []).find(p => p.id === packageId) || SEED_PACKAGES_INIT.find(p => p.id === packageId);

  const now = new Date();
  const startsAt = now.toISOString();
  let expiresAt: string | null = null;
  if (durationDays > 0) {
    const exp = new Date(now.getTime() + durationDays * 24 * 60 * 60 * 1000);
    expiresAt = exp.toISOString();
  }

  if (!db.enrollments[userId]) {
    db.enrollments[userId] = [];
  }

  // Check if existing enrollment for this package
  const existingIdx = db.enrollments[userId].findIndex(e => e.packageId === packageId);
  const prevExpiresAt = existingIdx >= 0 ? db.enrollments[userId][existingIdx].expiresAt : null;

  const enrollment: EnrollmentRecord = {
    id: `enr-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    userId,
    userEmail: user?.email || "unknown",
    packageId,
    packageName: pkg?.nameVi || packageId,
    status: "active",
    startsAt,
    expiresAt,
    grantedBy: adminEmail,
    grantedAt: startsAt,
    note
  };

  if (existingIdx >= 0) {
    db.enrollments[userId][existingIdx] = enrollment;
  } else {
    db.enrollments[userId].push(enrollment);
  }

  // Append history log
  if (!db.enrollmentHistory) db.enrollmentHistory = [];
  db.enrollmentHistory.push({
    id: `hist-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    userId,
    userEmail: user?.email || "unknown",
    packageId,
    packageName: pkg?.nameVi || packageId,
    action: "grant",
    actorEmail: adminEmail,
    previousExpiresAt: prevExpiresAt,
    newExpiresAt: expiresAt,
    timestamp: startsAt,
    note: note || `Cấp quyền gói ${pkg?.nameVi || packageId} (${durationDays > 0 ? durationDays + " ngày" : "Vô thời hạn"})`
  });

  // If user had pending request for this package, approve it
  if (db.enrollmentRequests) {
    const req = db.enrollmentRequests.find(r => r.userId === userId && r.packageId === packageId && r.status === "pending");
    if (req) {
      req.status = "approved";
      req.processedBy = adminEmail;
      req.processedAt = startsAt;
    }
  }

  saveDatabase(db);
  return enrollment;
}

export function renewPackage(
  userId: string,
  packageId: string,
  extensionDays: number,
  adminEmail: string,
  note: string = ""
): EnrollmentRecord | null {
  const db = getDatabase();
  const user = db.users.find(u => u.id === userId);
  const pkg = (db.packages || []).find(p => p.id === packageId);
  const enrs = db.enrollments[userId] || [];
  const enr = enrs.find(e => e.packageId === packageId);
  if (!enr) return null;

  const now = new Date();
  const prevExp = enr.expiresAt ? new Date(enr.expiresAt) : now;
  const baseTime = prevExp > now ? prevExp : now;
  const newExp = new Date(baseTime.getTime() + extensionDays * 24 * 60 * 60 * 1000);

  const prevExpiresAtStr = enr.expiresAt;
  enr.expiresAt = newExp.toISOString();
  enr.status = "active";
  enr.note = note ? `${enr.note || ""}; ${note}` : enr.note;

  if (!db.enrollmentHistory) db.enrollmentHistory = [];
  db.enrollmentHistory.push({
    id: `hist-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    userId,
    userEmail: user?.email || enr.userEmail,
    packageId,
    packageName: enr.packageName,
    action: "renew",
    actorEmail: adminEmail,
    previousExpiresAt: prevExpiresAtStr,
    newExpiresAt: enr.expiresAt,
    timestamp: now.toISOString(),
    note: note || `Gia hạn thêm ${extensionDays} ngày cho gói ${enr.packageName}`
  });

  // If there's a pending renewal request, approve it
  if (db.enrollmentRequests) {
    const req = db.enrollmentRequests.find(r => r.userId === userId && r.packageId === packageId && r.status === "pending");
    if (req) {
      req.status = "approved";
      req.processedBy = adminEmail;
      req.processedAt = now.toISOString();
    }
  }

  saveDatabase(db);
  return enr;
}

export function revokePackage(
  userId: string,
  packageId: string,
  adminEmail: string,
  reason: string = ""
): boolean {
  const db = getDatabase();
  const user = db.users.find(u => u.id === userId);
  const enrs = db.enrollments[userId] || [];
  const enr = enrs.find(e => e.packageId === packageId);
  if (!enr) return false;

  const prevExpiresAtStr = enr.expiresAt;
  enr.status = "revoked";
  enr.note = reason ? `Thu hồi: ${reason}` : "Thu hồi quyền";

  if (!db.enrollmentHistory) db.enrollmentHistory = [];
  db.enrollmentHistory.push({
    id: `hist-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    userId,
    userEmail: user?.email || enr.userEmail,
    packageId,
    packageName: enr.packageName,
    action: "revoke",
    actorEmail: adminEmail,
    previousExpiresAt: prevExpiresAtStr,
    newExpiresAt: null,
    timestamp: new Date().toISOString(),
    note: reason || "Thu hồi quyền truy cập"
  });

  saveDatabase(db);
  return true;
}

// -------------------------------------------------------------
// ENROLLMENT REQUESTS (HỌC VIÊN YÊU CẦU ĐĂNG KÝ / GIA HẠN)
// -------------------------------------------------------------

export function createEnrollmentRequest(
  userId: string,
  packageId: string,
  type: "register" | "renew",
  userNote: string = ""
): EnrollmentRequestRecord {
  const db = getDatabase();
  const user = db.users.find(u => u.id === userId);
  const pkg = (db.packages || []).find(p => p.id === packageId) || SEED_PACKAGES_INIT.find(p => p.id === packageId);

  if (!db.enrollmentRequests) db.enrollmentRequests = [];

  // Check if duplicate pending request
  const existing = db.enrollmentRequests.find(
    r => r.userId === userId && r.packageId === packageId && r.status === "pending"
  );
  if (existing) {
    existing.userNote = userNote || existing.userNote;
    saveDatabase(db);
    return existing;
  }

  const req: EnrollmentRequestRecord = {
    id: `req-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    userId,
    userEmail: user?.email || "unknown",
    userName: user?.fullName || "Học viên",
    packageId,
    packageName: pkg?.nameVi || packageId,
    type,
    status: "pending",
    requestedAt: new Date().toISOString(),
    userNote
  };

  db.enrollmentRequests.push(req);
  saveDatabase(db);
  return req;
}

export function getEnrollmentRequests(status?: string): EnrollmentRequestRecord[] {
  const db = getDatabase();
  const list = db.enrollmentRequests || [];
  if (status) {
    return list.filter(r => r.status === status);
  }
  return list;
}

export function processEnrollmentRequest(
  requestId: string,
  approve: boolean,
  adminEmail: string,
  durationDays: number = 30,
  note: string = ""
): EnrollmentRequestRecord | null {
  const db = getDatabase();
  if (!db.enrollmentRequests) return null;
  const req = db.enrollmentRequests.find(r => r.id === requestId);
  if (!req) return null;

  const now = new Date().toISOString();
  if (approve) {
    req.status = "approved";
    req.processedBy = adminEmail;
    req.processedAt = now;
    saveDatabase(db);
    // Automatically grant or renew package
    if (req.type === "renew") {
      renewPackage(req.userId, req.packageId, durationDays, adminEmail, note);
    } else {
      grantPackage(req.userId, req.packageId, durationDays, adminEmail, note);
    }
  } else {
    req.status = "rejected";
    req.processedBy = adminEmail;
    req.processedAt = now;
    saveDatabase(db);
  }

  return req;
}

export function getEnrollmentHistory(userId?: string): EnrollmentHistoryRecord[] {
  const db = getDatabase();
  const list = db.enrollmentHistory || [];
  if (userId) {
    return list.filter(h => h.userId === userId).sort((a, b) => b.timestamp.localeCompare(a.timestamp));
  }
  return [...list].sort((a, b) => b.timestamp.localeCompare(a.timestamp));
}

// -------------------------------------------------------------
// CENTRAL ENTITLEMENT CHECK (SERVER-SIDE GATEKEEPER)
// -------------------------------------------------------------

export interface EntitlementCheckResult {
  granted: boolean;
  reason?: "not_enrolled" | "expired" | "revoked" | "preview" | "admin" | "no_active_package";
  preview?: boolean;
  requiredPackageName?: string;
  requiredPackageId?: string;
  activeEnrollment?: EnrollmentRecord | null;
  expiresAt?: string | null;
}

export function checkUserEntitlement(
  userId: string | null | undefined,
  target: {
    courseId?: string;
    moduleId?: string;
    lessonId?: string;
    feature?: FeatureKey;
  }
): EntitlementCheckResult {
  const db = getDatabase();

  // 1. If guest / unauthenticated, allow preview lessons only
  if (!userId || userId === "guest") {
    if (target.lessonId) {
      const courses = db.courses || SEED_COURSES_INIT;
      const isPreview = courses.some(c => c.previewLessonIds?.includes(target.lessonId!));
      if (isPreview || target.lessonId === "mod1-les1" || target.lessonId === "mod6-les1") {
        return { granted: true, reason: "preview", preview: true };
      }
    }
    return {
      granted: false,
      reason: "not_enrolled",
      requiredPackageName: "Gói Học Thử hoặc Nền Tảng Khai Vấn",
      requiredPackageId: "pkg-trial"
    };
  }

  const user = db.users.find(u => u.id === userId);
  if (!user) {
    return { granted: false, reason: "not_enrolled", requiredPackageName: "Gói Học Viên" };
  }

  // 2. Super admin, editor, billing always have full access
  if (user.role === "super_admin" || user.role === "editor" || user.role === "billing") {
    return { granted: true, reason: "admin" };
  }

  // 3. Preview lesson check (preview is open to any authenticated student)
  if (target.lessonId) {
    const courses = db.courses || SEED_COURSES_INIT;
    const isPreview = courses.some(c => c.previewLessonIds?.includes(target.lessonId!));
    if (isPreview || target.lessonId === "mod1-les1" || target.lessonId === "mod6-les1") {
      return { granted: true, reason: "preview", preview: true };
    }
  }

  // 4. Enrollments check
  const userEnrollments = db.enrollments[userId] || [];
  const now = new Date().toISOString();

  // Active unexpired enrollments
  const activeEnrollments = userEnrollments.filter(e => {
    if (e.status !== "active") return false;
    if (e.expiresAt && e.expiresAt < now) return false;
    return true;
  });

  // Expired enrollments
  const expiredEnrollments = userEnrollments.filter(e => {
    return e.status === "expired" || (e.expiresAt && e.expiresAt < now);
  });

  // Support legacy user.tier mapping if tier is paid and not expired
  if (user.tier && user.tier !== "free") {
    if (!user.tierExpiresAt || user.tierExpiresAt > now) {
      return { granted: true };
    }
  }

  if (activeEnrollments.length === 0) {
    if (expiredEnrollments.length > 0) {
      const lastExp = expiredEnrollments[0];
      return {
        granted: false,
        reason: "expired",
        requiredPackageName: lastExp.packageName,
        requiredPackageId: lastExp.packageId,
        expiresAt: lastExp.expiresAt
      };
    }
    // Determine suggested package
    let reqPkgName = "Gói Nền Tảng Khai Vấn";
    let reqPkgId = "pkg-foundation";
    if (target.feature === "mock_exam_sjt" || target.feature === "daily_sjt_10" || target.moduleId === "mod-3" || target.moduleId === "mod-6") {
      reqPkgName = "Gói Luyện Thi ICF Credentialing";
      reqPkgId = "pkg-exam-prep";
    }
    return {
      granted: false,
      reason: "not_enrolled",
      requiredPackageName: reqPkgName,
      requiredPackageId: reqPkgId
    };
  }

  // Check if target is covered by any active enrollment
  for (const enr of activeEnrollments) {
    const pkg = (db.packages || []).find(p => p.id === enr.packageId) || SEED_PACKAGES_INIT.find(p => p.id === enr.packageId);
    if (!pkg) continue;

    // Allowed all
    if (pkg.allowedCourseIds.includes("*")) {
      return { granted: true, activeEnrollment: enr, expiresAt: enr.expiresAt };
    }

    // Check course permission
    if (target.courseId) {
      if (pkg.allowedCourseIds.includes(target.courseId)) {
        return { granted: true, activeEnrollment: enr, expiresAt: enr.expiresAt };
      }
    }

    // Check module permission
    if (target.moduleId) {
      const coursesForPkg = (db.courses || SEED_COURSES_INIT).filter(c => pkg.allowedCourseIds.includes(c.id));
      const hasMod = coursesForPkg.some(c => c.moduleIds.includes(target.moduleId!));
      if (hasMod) {
        return { granted: true, activeEnrollment: enr, expiresAt: enr.expiresAt };
      }
    }

    // Check lesson permission
    if (target.lessonId) {
      const modPrefix = target.lessonId.split("-")[0]; // e.g. "mod1"
      const mappedModId = modPrefix.replace("mod", "mod-"); // e.g. "mod-1"
      const coursesForPkg = (db.courses || SEED_COURSES_INIT).filter(c => pkg.allowedCourseIds.includes(c.id));
      const hasMod = coursesForPkg.some(c => c.moduleIds.includes(mappedModId));
      if (hasMod) {
        return { granted: true, activeEnrollment: enr, expiresAt: enr.expiresAt };
      }
    }

    // Check feature permission
    if (target.feature) {
      if (pkg.allowedFeatures.includes(target.feature)) {
        return { granted: true, activeEnrollment: enr, expiresAt: enr.expiresAt };
      }
    }
  }

  // Not covered by user's active packages
  return {
    granted: false,
    reason: "not_enrolled",
    requiredPackageName: target.feature === "mock_exam_sjt" ? "Gói Luyện Thi ICF Credentialing" : "Gói Nền Tảng Khai Vấn",
    requiredPackageId: target.feature === "mock_exam_sjt" ? "pkg-exam-prep" : "pkg-foundation"
  };
}
