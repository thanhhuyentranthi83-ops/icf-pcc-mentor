import {
  Section,
  Theory,
  Keyword,
  Flashcard,
  CaseStudy,
  QuizQuestion,
  MindfulnessMessage,
  Sticker,
  SystemSettings,
  UserProfile,
  Order,
  AuditLog
} from "@/types";
import {
  SEED_SECTIONS,
  SEED_THEORIES,
  SEED_KEYWORDS,
  SEED_FLASHCARDS,
  SEED_CASE_STUDIES,
  SEED_QUIZZES,
  SEED_FULL_MOCK_EXAM,
  SEED_MINDFULNESS_MESSAGES,
  SEED_STICKERS,
  SEED_SYSTEM_SETTINGS,
  SEED_USERS,
  SEED_ORDERS
} from "./seedData";
import { removeVietnameseAccents } from "./unaccent";

const STORAGE_KEYS = {
  SECTIONS: "icf_pcc_sections_v1",
  THEORIES: "icf_pcc_theories_v1",
  KEYWORDS: "icf_pcc_keywords_v1",
  FLASHCARDS: "icf_pcc_flashcards_v1",
  FLASHCARD_PROGRESS: "icf_pcc_fc_progress_v1",
  CASE_STUDIES: "icf_pcc_cases_v1",
  QUIZZES: "icf_pcc_quizzes_v1",
  MESSAGES: "icf_pcc_messages_v1",
  STICKERS: "icf_pcc_stickers_v1",
  SETTINGS: "icf_pcc_settings_v1",
  USERS: "icf_pcc_users_v1",
  ORDERS: "icf_pcc_orders_v1",
  EXAMS: "icf_pcc_exams_v1",
  GARDENS: "icf_pcc_gardens_v1",
  NOTES: "icf_pcc_notes_v1",
  AUDIT: "icf_pcc_audit_v1"
};

function isClient(): boolean {
  return typeof window !== "undefined";
}

function getItem<T>(key: string, fallback: T): T {
  if (!isClient()) return fallback;
  try {
    const val = localStorage.getItem(key);
    if (!val) {
      localStorage.setItem(key, JSON.stringify(fallback));
      return fallback;
    }
    return JSON.parse(val) as T;
  } catch {
    return fallback;
  }
}

function setItem<T>(key: string, value: T): void {
  if (!isClient()) return;
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (err) {
    console.warn("Storage write error", err);
  }
}

// 1. Sections
export function getSections(): Section[] {
  return getItem<Section[]>(STORAGE_KEYS.SECTIONS, SEED_SECTIONS);
}

export function saveSections(sections: Section[]): void {
  setItem(STORAGE_KEYS.SECTIONS, sections);
}

export function getSectionById(id: string): Section | undefined {
  const list = getSections();
  return list.find((s) => s.id === id);
}

// 2. Theories
export function getTheories(): Theory[] {
  return getItem<Theory[]>(STORAGE_KEYS.THEORIES, SEED_THEORIES);
}

export function getTheoryBySectionId(secId: string): Theory | undefined {
  const list = getTheories();
  return list.find((t) => t.sectionId === secId);
}

export function saveTheory(theory: Theory): void {
  const list = getTheories();
  const idx = list.findIndex((t) => t.id === theory.id || t.sectionId === theory.sectionId);
  if (idx >= 0) {
    list[idx] = theory;
  } else {
    list.push(theory);
  }
  setItem(STORAGE_KEYS.THEORIES, list);
}

// 3. Keywords
export function getKeywords(): Keyword[] {
  return getItem<Keyword[]>(STORAGE_KEYS.KEYWORDS, SEED_KEYWORDS);
}

export function getKeywordsBySectionId(secId: string): Keyword[] {
  const list = getKeywords();
  return list.filter((k) => k.sectionId === secId).sort((a, b) => a.orderIndex - b.orderIndex);
}

// 4. Flashcards
export function getFlashcards(): Flashcard[] {
  return getItem<Flashcard[]>(STORAGE_KEYS.FLASHCARDS, SEED_FLASHCARDS);
}

export function getFlashcardsBySectionId(secId: string): Flashcard[] {
  const list = getFlashcards();
  return list.filter((f) => f.sectionId === secId).sort((a, b) => a.orderIndex - b.orderIndex);
}

export interface FlashcardProgressItem {
  flashcardId: string;
  status: "known" | "unsure" | "unknown";
  isFavorite: boolean;
  reviewedAt: string;
}

export function getUserFlashcardProgress(userId: string): Record<string, FlashcardProgressItem> {
  const all = getItem<Record<string, Record<string, FlashcardProgressItem>>>(STORAGE_KEYS.FLASHCARD_PROGRESS, {});
  return all[userId] || {};
}

export function updateFlashcardProgress(
  userId: string,
  flashcardId: string,
  status: "known" | "unsure" | "unknown",
  isFavorite?: boolean
): void {
  const all = getItem<Record<string, Record<string, FlashcardProgressItem>>>(STORAGE_KEYS.FLASHCARD_PROGRESS, {});
  if (!all[userId]) all[userId] = {};
  const current = all[userId][flashcardId] || {
    flashcardId,
    status: "unknown",
    isFavorite: false,
    reviewedAt: new Date().toISOString()
  };
  all[userId][flashcardId] = {
    ...current,
    status,
    isFavorite: isFavorite !== undefined ? isFavorite : current.isFavorite,
    reviewedAt: new Date().toISOString()
  };
  setItem(STORAGE_KEYS.FLASHCARD_PROGRESS, all);
}

// 5. Case Studies
export function getCaseStudies(): CaseStudy[] {
  return getItem<CaseStudy[]>(STORAGE_KEYS.CASE_STUDIES, SEED_CASE_STUDIES);
}

export function getCaseStudiesBySectionId(secId: string): CaseStudy[] {
  const list = getCaseStudies();
  return list.filter((c) => c.sectionId === secId).sort((a, b) => a.orderIndex - b.orderIndex);
}

// 6. Quizzes
export function getQuizzes(): QuizQuestion[] {
  return getItem<QuizQuestion[]>(STORAGE_KEYS.QUIZZES, SEED_QUIZZES);
}

export function getQuizzesBySectionId(secId: string): QuizQuestion[] {
  const list = getQuizzes();
  return list.filter((q) => q.sectionId === secId).sort((a, b) => a.orderIndex - b.orderIndex);
}

export function getFullMockExam(): QuizQuestion[] {
  return SEED_FULL_MOCK_EXAM;
}

// 7. Exam Sessions
export interface ExamSessionRecord {
  id: string;
  userId: string;
  examType: "section_mock" | "full_pcc_mock" | "quick_tea";
  sectionId?: string | null;
  score: number;
  totalQuestions: number;
  correctBestCount: number;
  correctWorstCount: number;
  durationSeconds: number;
  answers: Record<string, { best?: string; worst?: string; selected?: string }>;
  completedAt: string;
}

export function getExamSessions(userId?: string): ExamSessionRecord[] {
  const list = getItem<ExamSessionRecord[]>(STORAGE_KEYS.EXAMS, []);
  if (!userId) return list;
  return list.filter((s) => s.userId === userId);
}

export function saveExamSession(session: ExamSessionRecord): void {
  const list = getItem<ExamSessionRecord[]>(STORAGE_KEYS.EXAMS, []);
  list.unshift(session);
  setItem(STORAGE_KEYS.EXAMS, list);
}

// 8. Lotus Garden
export interface LotusGardenState {
  seedsPlanted: number;
  sproutsGrown: number;
  lotusesBloomed: number;
  butterfliesUnlocked: number;
  dragonfliesUnlocked: number;
}

export function getLotusGarden(userId: string): LotusGardenState {
  const all = getItem<Record<string, LotusGardenState>>(STORAGE_KEYS.GARDENS, {});
  return (
    all[userId] || {
      seedsPlanted: 12,
      sproutsGrown: 8,
      lotusesBloomed: 4,
      butterfliesUnlocked: 2,
      dragonfliesUnlocked: 1
    }
  );
}

export function updateLotusGarden(
  userId: string,
  partialOrFn: Partial<LotusGardenState> | ((prev: LotusGardenState) => Partial<LotusGardenState>)
): void {
  const all = getItem<Record<string, LotusGardenState>>(STORAGE_KEYS.GARDENS, {});
  const current = getLotusGarden(userId);
  const partial = typeof partialOrFn === "function" ? partialOrFn(current) : partialOrFn;
  all[userId] = { ...current, ...partial };
  setItem(STORAGE_KEYS.GARDENS, all);
}

// 9. Mindfulness Messages
export function getMindfulnessMessages(): MindfulnessMessage[] {
  return getItem<MindfulnessMessage[]>(STORAGE_KEYS.MESSAGES, SEED_MINDFULNESS_MESSAGES);
}

export function getDailyMindfulnessMessage(): MindfulnessMessage {
  const list = getMindfulnessMessages().filter((m) => m.isActive);
  if (!list.length) return SEED_MINDFULNESS_MESSAGES[0];
  // Stable pick for the day
  const today = new Date();
  const dayIndex = (today.getFullYear() * 365 + today.getMonth() * 31 + today.getDate()) % list.length;
  return list[dayIndex];
}

// 10. Stickers
export function getStickers(): Sticker[] {
  return getItem<Sticker[]>(STORAGE_KEYS.STICKERS, SEED_STICKERS);
}

export function getStickerByTrigger(event: string): Sticker | undefined {
  const list = getStickers().filter((s) => s.isActive);
  return list.find((s) => s.triggerEvent === event) || list[0];
}

// 11. System Settings
export function getSystemSettings(): SystemSettings {
  return getItem<SystemSettings>(STORAGE_KEYS.SETTINGS, SEED_SYSTEM_SETTINGS);
}

export function saveSystemSettings(settings: SystemSettings): void {
  setItem(STORAGE_KEYS.SETTINGS, settings);
}

// 12. Users
export function getUsers(): UserProfile[] {
  return getItem<UserProfile[]>(STORAGE_KEYS.USERS, SEED_USERS);
}

export function getUserById(id: string): UserProfile | undefined {
  const list = getUsers();
  return list.find((u) => u.id === id);
}

export function saveUser(user: UserProfile): void {
  const list = getUsers();
  const idx = list.findIndex((u) => u.id === user.id);
  if (idx >= 0) {
    list[idx] = user;
  } else {
    list.push(user);
  }
  setItem(STORAGE_KEYS.USERS, list);
}

// 13. Orders
export function getOrders(): Order[] {
  return getItem<Order[]>(STORAGE_KEYS.ORDERS, SEED_ORDERS);
}

export function createOrder(order: Order): void {
  const list = getOrders();
  list.unshift(order);
  setItem(STORAGE_KEYS.ORDERS, list);
}

export function updateOrderStatus(orderId: string, status: Order["status"], approvedBy?: string): Order | undefined {
  const list = getOrders();
  const ord = list.find((o) => o.id === orderId);
  if (ord) {
    ord.status = status;
    ord.updatedAt = new Date().toISOString();
    if (status === "approved") {
      ord.approvedBy = approvedBy;
      ord.approvedAt = new Date().toISOString();
      // Automatically extend user tier!
      const user = getUserById(ord.userId);
      if (user) {
        user.tier = ord.tierId;
        const now = new Date();
        const months = ord.tierId === "1_month" ? 1 : ord.tierId === "6_months" ? 6 : 12;
        now.setMonth(now.getMonth() + months);
        user.tierExpiresAt = now.toISOString();
        saveUser(user);
      }
    }
    setItem(STORAGE_KEYS.ORDERS, list);
  }
  return ord;
}

// 14. Audit Logs
export function getAuditLogs(): AuditLog[] {
  return getItem<AuditLog[]>(STORAGE_KEYS.AUDIT, [
    {
      id: "aud-01",
      userId: "usr-admin",
      userName: "Super Admin Tâm An",
      action: "Cấu hình tài khoản VietQR",
      details: "Cập nhật số tài khoản Vietcombank 9988776655",
      createdAt: "2026-11-01T08:00:00Z"
    },
    {
      id: "aud-02",
      userId: "usr-billing",
      userName: "Thu Ngân Diệu Thiện",
      action: "Duyệt đơn hàng",
      details: "Duyệt đơn PCC-1001-A89 gói 1 Tháng cho học viên",
      createdAt: "2026-11-01T10:30:00Z"
    }
  ]);
}

export function addAuditLog(userId: string, userName: string, action: string, details: string): void {
  const list = getAuditLogs();
  list.unshift({
    id: `aud-${Date.now()}`,
    userId,
    userName,
    action,
    details,
    createdAt: new Date().toISOString()
  });
  setItem(STORAGE_KEYS.AUDIT, list);
}

// 15. Personal Notes
export function getUserNotes(userId: string, sectionId: string): string {
  const all = getItem<Record<string, Record<string, string>>>(STORAGE_KEYS.NOTES, {});
  return all[userId]?.[sectionId] || "";
}

export function saveUserNote(userId: string, sectionId: string, content: string): void {
  const all = getItem<Record<string, Record<string, string>>>(STORAGE_KEYS.NOTES, {});
  if (!all[userId]) all[userId] = {};
  all[userId][sectionId] = content;
  setItem(STORAGE_KEYS.NOTES, all);
}

// 16. Global Search
export interface SearchResultItem {
  id: string;
  type: "theory" | "keyword" | "flashcard" | "case_study" | "quiz";
  sectionId: string;
  sectionTitleVi: string;
  sectionTitleEn: string;
  titleVi: string;
  titleEn: string;
  snippetVi: string;
  snippetEn: string;
  isLocked: boolean;
}

export function searchAllContent(
  query: string,
  filterSection?: string,
  userTier: string = "free"
): SearchResultItem[] {
  if (!query.trim()) return [];

  const cleanQ = removeVietnameseAccents(query);
  const sections = getSections();
  const secMap = new Map(sections.map((s) => [s.id, s]));

  const results: SearchResultItem[] = [];

  // Search Theories
  for (const th of getTheories()) {
    if (filterSection && th.sectionId !== filterSection) continue;
    const sec = secMap.get(th.sectionId);
    if (!sec) continue;

    const matchVi = removeVietnameseAccents(th.titleVi + " " + th.contentVi).includes(cleanQ);
    const matchEn = removeVietnameseAccents(th.titleEn + " " + th.contentEn).includes(cleanQ);

    if (matchVi || matchEn) {
      const isLocked = !sec.isFree && userTier === "free";
      results.push({
        id: th.id,
        type: "theory",
        sectionId: th.sectionId,
        sectionTitleVi: sec.titleVi,
        sectionTitleEn: sec.titleEn,
        titleVi: th.titleVi,
        titleEn: th.titleEn,
        snippetVi: th.contentVi.slice(0, 160).replace(/[#*`]/g, "") + "...",
        snippetEn: th.contentEn.slice(0, 160).replace(/[#*`]/g, "") + "...",
        isLocked
      });
    }
  }

  // Search Keywords
  for (const kw of getKeywords()) {
    if (filterSection && kw.sectionId !== filterSection) continue;
    const sec = secMap.get(kw.sectionId);
    if (!sec) continue;

    const matchVi = removeVietnameseAccents(kw.termVi + " " + kw.definitionVi + " " + kw.memoryCueVi).includes(cleanQ);
    const matchEn = removeVietnameseAccents(kw.termEn + " " + kw.definitionEn + " " + kw.memoryCueEn).includes(cleanQ);

    if (matchVi || matchEn) {
      const isLocked = !sec.isFree && userTier === "free";
      results.push({
        id: kw.id,
        type: "keyword",
        sectionId: kw.sectionId,
        sectionTitleVi: sec.titleVi,
        sectionTitleEn: sec.titleEn,
        titleVi: `Thuật ngữ: ${kw.termVi}`,
        titleEn: `Keyword: ${kw.termEn}`,
        snippetVi: kw.definitionVi,
        snippetEn: kw.definitionEn,
        isLocked
      });
    }
  }

  // Search Case Studies
  for (const cs of getCaseStudies()) {
    if (filterSection && cs.sectionId !== filterSection) continue;
    const sec = secMap.get(cs.sectionId);
    if (!sec) continue;

    const matchVi = removeVietnameseAccents(cs.titleVi + " " + cs.scenarioDialogueVi).includes(cleanQ);
    const matchEn = removeVietnameseAccents(cs.titleEn + " " + cs.scenarioDialogueEn).includes(cleanQ);

    if (matchVi || matchEn) {
      const isLocked = !sec.isFree && userTier === "free";
      results.push({
        id: cs.id,
        type: "case_study",
        sectionId: cs.sectionId,
        sectionTitleVi: sec.titleVi,
        sectionTitleEn: sec.titleEn,
        titleVi: cs.titleVi,
        titleEn: cs.titleEn,
        snippetVi: cs.scenarioDialogueVi.slice(0, 160).replace(/[#*`]/g, "") + "...",
        snippetEn: cs.scenarioDialogueEn.slice(0, 160).replace(/[#*`]/g, "") + "...",
        isLocked
      });
    }
  }

  return results;
}
