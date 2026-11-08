export type Role = "super_admin" | "editor" | "billing" | "student";
export type Tier = "free" | "1_month" | "6_months" | "12_months";
export type NatureIcon = "seed" | "sprout" | "bamboo" | "lotus" | "mountain";

export interface UserProfile {
  id: string;
  email: string;
  fullName: string;
  role: Role;
  tier: Tier;
  tierExpiresAt?: string | null;
  streakCount: number;
  lastActiveDate?: string | null;
  selectedStickerPack: string;
  minimalMode: boolean;
  soundEnabled: boolean;
}

export interface Section {
  id: string;
  parentId: string | null;
  code: string;
  titleVi: string;
  titleEn: string;
  descriptionVi: string;
  descriptionEn: string;
  natureIcon: NatureIcon;
  orderIndex: number;
  isFree: boolean;
  isPublished: boolean;
  children?: Section[];
}

export interface Theory {
  id: string;
  sectionId: string;
  titleVi: string;
  titleEn: string;
  contentVi: string;
  contentEn: string;
  videoUrl?: string | null;
  attachments?: { nameVi: string; nameEn: string; url: string; type: string }[] | null;
  isFree: boolean;
}

export interface Keyword {
  id: string;
  sectionId: string;
  termVi: string;
  termEn: string;
  definitionVi: string;
  definitionEn: string;
  category: "mnemonic" | "overview";
  memoryCueVi: string;
  memoryCueEn: string;
  audioTermEnUrl?: string | null;
  orderIndex: number;
}

export interface Flashcard {
  id: string;
  sectionId: string;
  frontVi: string;
  frontEn: string;
  backVi: string;
  backEn: string;
  hintVi?: string | null;
  hintEn?: string | null;
  orderIndex: number;
}

export interface CaseStudy {
  id: string;
  sectionId: string;
  titleVi: string;
  titleEn: string;
  scenarioDialogueVi: string;
  scenarioDialogueEn: string;
  analysisQuestionsVi: string;
  analysisQuestionsEn: string;
  suggestedAnswersVi: string;
  suggestedAnswersEn: string;
  competencyMapping: string;
  pccMarkers: string[];
  orderIndex: number;
}

export interface QuizOption {
  key: string; // "A", "B", "C", "D"
  textVi: string;
  textEn: string;
}

export interface QuizQuestion {
  id: string;
  sectionId: string | null;
  type: "standard_mcq" | "icf_sjt";
  questionVi: string;
  questionEn: string;
  options: QuizOption[];
  correctAnswer?: string | null;
  bestAnswer?: string | null;
  worstAnswer?: string | null;
  explanationVi: string;
  explanationEn: string;
  primaryCompetency?: string | null;
  keyClueVi?: string | null;
  keyClueEn?: string | null;
  difficulty?: "easy" | "medium" | "hard" | null;
  orderIndex: number;
}

export interface Order {
  id: string;
  userId: string;
  orderCode: string;
  tierId: Tier;
  amount: number;
  discountCode?: string | null;
  discountAmount?: number | null;
  status: "pending_payment" | "pending_approval" | "approved" | "rejected" | "expired";
  receiptUrl?: string | null;
  approvedBy?: string | null;
  approvedAt?: string | null;
  createdAt: string;
  updatedAt: string;
}

export interface MindfulnessMessage {
  id: string;
  textVi: string;
  textEn: string;
  theme: string;
  author?: string | null;
  isActive: boolean;
}

export interface Sticker {
  id: string;
  code: string;
  nameVi: string;
  nameEn: string;
  category: "monk" | "lotus" | "cat" | "nature" | "badge";
  triggerEvent: "welcome" | "lesson_complete" | "streak_milestone" | "quiz_streak" | "comfort_mistake" | "exam_high_score" | "renewal_gentle";
  svgContent: string;
  isActive: boolean;
}

export interface SystemSettings {
  bankName: string;
  accountNumber: string;
  accountHolder: string;
  bankBin: string;
  pricing: Record<Tier, { price: number; nameVi: string; nameEn: string; featuresVi: string[]; featuresEn: string[] }>;
  bannerAnnouncement?: { vi: string; en: string; active: boolean };
}

export interface AuditLog {
  id: string;
  userId: string;
  userName: string;
  action: string;
  details: string;
  createdAt: string;
}

export type FeatureKey = "curriculum" | "daily_sjt_10" | "mock_exam_sjt" | "glossary_search" | "tea_micro" | "resource_download";

export interface CourseRecord {
  id: string; // ví dụ: "crs-foundation", "crs-exam-prep", "crs-all-in-one"
  titleVi: string;
  titleEn: string;
  descriptionVi: string;
  descriptionEn: string;
  moduleIds: string[]; // ví dụ: ["mod-1", "mod-2", "mod-4", "mod-7"]
  previewLessonIds: string[]; // Các bài cho phép xem thử, ví dụ: ["mod1-les1"]
  isPublished: boolean; // Bật/tắt hiển thị trong danh mục
  orderIndex: number;
  badgeText?: string; // ví dụ: "Nền tảng", "Trọng tâm", "Khuyên dùng"
  badge?: string;
}

export interface PackageRecord {
  id: string; // ví dụ: "pkg-trial", "pkg-foundation", "pkg-exam-prep", "pkg-pcc-master"
  nameVi: string;
  nameEn: string;
  descriptionVi: string;
  descriptionEn: string;
  price: number; // VNĐ (0 = Miễn phí)
  durationDays: number; // Số ngày (7, 30, 180, 365, hoặc 0 = vĩnh viễn)
  isRegistrationOpen: boolean; // Đang mở đăng ký hay đã ngừng
  allowedCourseIds: string[]; // Các khóa được mở (["*"] nếu mở tất cả)
  allowedFeatures: FeatureKey[]; // Các tính năng được mở
  badge?: string;
  isDefaultTrial?: boolean;
}

export interface EnrollmentRecord {
  id: string;
  userId: string;
  userEmail: string;
  packageId: string;
  packageName: string;
  status: "active" | "expired" | "revoked" | "pending";
  startsAt: string; // ISO string
  expiresAt: string | null; // ISO string, null = vĩnh viễn
  grantedBy: string; // Email admin
  grantedAt: string;
  note?: string;
}

export interface EnrollmentHistoryRecord {
  id: string;
  userId: string;
  userEmail: string;
  packageId: string;
  packageName: string;
  action: "grant" | "renew" | "revoke" | "expire";
  actorEmail: string;
  previousExpiresAt: string | null;
  newExpiresAt: string | null;
  timestamp: string;
  note: string;
}

export interface EnrollmentRequestRecord {
  id: string;
  userId: string;
  userEmail: string;
  userName: string;
  packageId: string;
  packageName: string;
  type: "register" | "renew";
  status: "pending" | "approved" | "rejected";
  requestedAt: string;
  userNote?: string;
  processedBy?: string;
  processedAt?: string;
}

