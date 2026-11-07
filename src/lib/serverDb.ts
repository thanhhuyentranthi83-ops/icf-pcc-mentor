import fs from "fs";
import path from "path";
import crypto from "crypto";

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
}

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
        sessions: {}
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
    return parsed;
  } catch (err) {
    console.error("Error reading database:", err);
    return {
      users: [...SEED_USERS_INIT],
      progress: {},
      bookmarks: {},
      exams: {},
      sessions: {}
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
