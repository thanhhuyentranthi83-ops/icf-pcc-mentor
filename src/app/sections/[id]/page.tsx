"use client";

import React, { useState, useEffect } from "react";
import { useParams, useRouter } from "next/navigation";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import {
  getSectionById,
  getTheoryBySectionId,
  getKeywordsBySectionId,
  getFlashcardsBySectionId,
  getCaseStudiesBySectionId,
  getQuizzesBySectionId,
  getUserNotes,
  saveUserNote,
  updateLotusGarden
} from "@/lib/db";
import {
  Section,
  Theory,
  Keyword,
  Flashcard,
  CaseStudy,
  QuizQuestion
} from "@/types";
import NatureIcon from "@/components/NatureIcon";
import FlashcardDeck from "@/components/FlashcardDeck";
import CaseStudyViewer from "@/components/CaseStudyViewer";
import QuizRunner from "@/components/QuizRunner";
import SjtExamRunner from "@/components/SjtExamRunner";
import {
  BookOpen,
  KeyRound,
  Layers,
  HelpCircle,
  FileQuestion,
  Mountain,
  Volume2,
  Lock,
  ArrowLeft,
  Sparkles,
  Save,
  CheckCircle,
  Bookmark
} from "lucide-react";

type TabKey = "theory" | "keyword" | "flashcard" | "case_study" | "quiz" | "mock_exam";

export default function SectionDetailPage() {
  const params = useParams();
  const router = useRouter();
  const secId = String(params.id || "");

  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user, canAccessSection } = useAuth();

  const [section, setSection] = useState<Section | null>(null);
  const [activeTab, setActiveTab] = useState<TabKey>("theory");
  const [theory, setTheory] = useState<Theory | null>(null);
  const [keywords, setKeywords] = useState<Keyword[]>([]);
  const [flashcards, setFlashcards] = useState<Flashcard[]>([]);
  const [caseStudies, setCaseStudies] = useState<CaseStudy[]>([]);
  const [quizzes, setQuizzes] = useState<QuizQuestion[]>([]);
  const [keywordSubTab, setKeywordSubTab] = useState<"mnemonic" | "overview">("mnemonic");

  // Notes
  const [noteContent, setNoteContent] = useState("");
  const [isNoteSaved, setIsNoteSaved] = useState(false);
  const [isCompleted, setIsCompleted] = useState(false);

  useEffect(() => {
    if (!secId) return;
    const s = getSectionById(secId);
    if (s) {
      setSection(s);
      setTheory(getTheoryBySectionId(secId) || null);
      setKeywords(getKeywordsBySectionId(secId));
      setFlashcards(getFlashcardsBySectionId(secId));
      setCaseStudies(getCaseStudiesBySectionId(secId));
      setQuizzes(getQuizzesBySectionId(secId));
      setNoteContent(getUserNotes(user.id, secId));
    }
  }, [secId, user.id]);

  if (!section) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-16 text-center space-y-4">
        <p className="text-sm text-zen-muted">{t("Đang tải dữ liệu bài học...", "Loading lesson data...")}</p>
        <Link href="/" className="text-xs text-zen-moss-dark font-semibold hover:underline">
          ← {t("Trở về Trang chủ", "Back to Home")}
        </Link>
      </div>
    );
  }

  const hasAccess = canAccessSection(section);

  const handleSaveNote = () => {
    saveUserNote(user.id, secId, noteContent);
    setIsNoteSaved(true);
    ringBell();
    setTimeout(() => setIsNoteSaved(false), 2000);
  };

  const handleMarkCompleted = () => {
    setIsCompleted(true);
    ringBell();
    updateLotusGarden(user.id, (prev) => ({
      lotusesBloomed: prev.lotusesBloomed + 1
    }));
  };

  // Speech pronunciation for English terms
  const speakTerm = (text: string) => {
    if (typeof window !== "undefined" && "speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = "en-US";
      utterance.rate = 0.9;
      window.speechSynthesis.speak(utterance);
    }
  };

  const tabs: { key: TabKey; labelVi: string; labelEn: string; icon: React.ElementType }[] = [
    { key: "theory", labelVi: "1. Lý Thuyết", labelEn: "1. Theory", icon: BookOpen },
    { key: "keyword", labelVi: "2. Keyword", labelEn: "2. Keywords", icon: KeyRound },
    { key: "flashcard", labelVi: "3. Flashcard", labelEn: "3. Flashcards", icon: Layers },
    { key: "case_study", labelVi: "4. Case Study", labelEn: "4. Case Studies", icon: HelpCircle },
    { key: "quiz", labelVi: "5. Quiz", labelEn: "5. Quiz", icon: FileQuestion },
    { key: "mock_exam", labelVi: "6. Thi Thử Theo Phần", labelEn: "6. Section Mock", icon: Mountain }
  ];

  return (
    <div className="max-w-6xl mx-auto px-4 py-6 sm:py-8 space-y-6">
      {/* Top Breadcrumb & Actions */}
      <div className="flex flex-wrap items-center justify-between gap-3 text-xs text-zen-muted">
        <Link
          href="/"
          className="flex items-center gap-1.5 font-medium hover:text-zen-ink transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>{t("Quay lại danh mục", "Back to Curriculum")}</span>
        </Link>

        <div className="flex items-center gap-2">
          <button
            onClick={handleMarkCompleted}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-semibold transition-all shadow-zen-subtle ${
              isCompleted
                ? "bg-emerald-50 border-emerald-300 text-emerald-800"
                : "bg-zen-paper border-zen-border text-zen-ink hover:bg-zen-surface"
            }`}
          >
            <CheckCircle className={`w-3.5 h-3.5 ${isCompleted ? "text-emerald-600" : "text-zen-muted"}`} />
            <span>{isCompleted ? t("Đã hoàn thành", "Completed") : t("Đánh dấu hoàn thành", "Mark as Done")}</span>
          </button>
        </div>
      </div>

      {/* Section Header Card */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card">
        <div className="flex items-center gap-3 mb-3">
          <div className="w-10 h-10 rounded-2xl bg-zen-moss/20 text-zen-moss-dark flex items-center justify-center shadow-zen-subtle">
            <NatureIcon icon={section.natureIcon} size={20} />
          </div>
          <div>
            <span className="text-xs font-mono font-bold text-zen-moss-dark uppercase tracking-wider">
              {section.code}
            </span>
            <span className="mx-2 text-zen-border">•</span>
            <span className="text-xs text-zen-muted">
              {section.isFree ? t("Bài học miễn phí", "Free Lesson") : t("Bài học nâng cao", "Premium Lesson")}
            </span>
          </div>
        </div>

        <h1 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink mb-2">
          {t(section.titleVi, section.titleEn)}
        </h1>
        <p className="text-xs sm:text-sm text-zen-muted leading-relaxed max-w-3xl">
          {t(section.descriptionVi, section.descriptionEn)}
        </p>
      </div>

      {/* Access Gate Warning for Locked Content */}
      {!hasAccess ? (
        <div className="rounded-3xl border border-amber-200 bg-amber-50/70 p-8 text-center space-y-4 shadow-zen-card">
          <div className="w-12 h-12 rounded-full bg-amber-100 text-amber-800 mx-auto flex items-center justify-center">
            <Lock className="w-6 h-6" />
          </div>
          <h3 className="font-serif text-xl font-bold text-amber-900">
            {t("Bài học thuộc gói trả phí", "Premium Section Locked")}
          </h3>
          <p className="text-xs text-amber-800/90 max-w-md mx-auto leading-relaxed">
            {t(
              "Nội dung chuyên sâu của bài học này đang được bảo lưu cho các học viên gói 1 Tháng, 6 Tháng hoặc 12 Tháng. Bạn có thể nâng cấp gói bất kỳ lúc nào để mở khóa toàn bộ 8 năng lực và đề thi thử.",
              "This in-depth lesson is reserved for paid tiers. Upgrade to unlock all 8 competencies, situational judgment cases, and mock exams."
            )}
          </p>
          <div className="pt-2">
            <Link
              href="/pricing"
              className="inline-flex items-center gap-2 px-6 py-3 rounded-2xl bg-zen-ochre hover:bg-zen-ochre-dark text-white text-xs font-semibold shadow-zen-card transition-all"
            >
              <Sparkles className="w-4 h-4" />
              <span>{t("Xem bảng giá & Nâng cấp gói", "View Pricing & Upgrade")}</span>
            </Link>
          </div>
        </div>
      ) : (
        <>
          {/* 6 Tabs Navigation Bar */}
          <div className="flex items-center gap-1.5 overflow-x-auto pb-2 border-b border-zen-border/70 scrollbar-none">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              const isActive = activeTab === tab.key;
              return (
                <button
                  key={tab.key}
                  onClick={() => setActiveTab(tab.key)}
                  className={`flex items-center gap-2 px-4 py-2.5 rounded-2xl text-xs font-semibold whitespace-nowrap transition-all ${
                    isActive
                      ? "bg-zen-moss-dark text-white shadow-zen-subtle"
                      : "bg-zen-paper hover:bg-zen-surface text-zen-ink/80 border border-zen-border/60"
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  <span>{t(tab.labelVi, tab.labelEn)}</span>
                </button>
              );
            })}
          </div>

          {/* Tab 1: Lý thuyết (Theory) */}
          {activeTab === "theory" && theory && (
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card space-y-6">
              <div className="prose prose-stone max-w-none text-zen-ink leading-relaxed whitespace-pre-line font-sans">
                {t(theory.contentVi, theory.contentEn)}
              </div>

              {/* Attachments */}
              {theory.attachments && theory.attachments.length > 0 && (
                <div className="pt-6 border-t border-zen-border/50">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-zen-ink mb-3 flex items-center gap-1.5">
                    <Bookmark className="w-4 h-4 text-zen-moss-dark" />
                    <span>{t("Tài liệu đính kèm & Sơ đồ tư duy:", "Attachments & Mindmaps:")}</span>
                  </h4>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {theory.attachments.map((att, i) => (
                      <div
                        key={i}
                        className="flex items-center justify-between p-3.5 rounded-2xl bg-zen-surface/60 border border-zen-border/60 text-xs font-medium text-zen-ink"
                      >
                        <span>{t(att.nameVi, att.nameEn)}</span>
                        <span className="text-[10px] uppercase font-bold text-zen-moss-dark px-2 py-0.5 rounded-md bg-zen-moss/20">
                          {att.type}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Tab 2: Keyword (Mẹo ghi nhớ & Tổng quát) */}
          {activeTab === "keyword" && (
            <div className="space-y-6">
              {/* Sub-branch selector */}
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setKeywordSubTab("mnemonic")}
                  className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all ${
                    keywordSubTab === "mnemonic"
                      ? "bg-zen-wood text-white shadow-zen-subtle"
                      : "bg-zen-paper text-zen-ink border border-zen-border"
                  }`}
                >
                  ⚡ {t("Mẹo Ghi Nhớ Nhanh (Mnemonics)", "Fast Mnemonics & Cues")}
                </button>
                <button
                  onClick={() => setKeywordSubTab("overview")}
                  className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all ${
                    keywordSubTab === "overview"
                      ? "bg-zen-moss-dark text-white shadow-zen-subtle"
                      : "bg-zen-paper text-zen-ink border border-zen-border"
                  }`}
                >
                  📖 {t("Tổng Quát Thuật Ngữ (Glossary)", "General Terms & Glossary")}
                </button>
              </div>

              {/* Keywords List */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {keywords
                  .filter((k) => k.category === keywordSubTab)
                  .map((kw) => (
                    <div
                      key={kw.id}
                      className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col justify-between"
                    >
                      <div>
                        <div className="flex items-start justify-between gap-2 mb-2">
                          <h4 className="font-serif text-lg font-bold text-zen-ink">
                            {t(kw.termVi, kw.termEn)}
                          </h4>
                          <button
                            onClick={() => speakTerm(kw.termEn)}
                            title={t("Phát âm thuật ngữ tiếng Anh", "Pronounce English Term")}
                            className="p-1.5 rounded-lg border border-zen-border text-zen-muted hover:text-zen-moss-dark hover:bg-zen-surface transition-colors shrink-0"
                          >
                            <Volume2 className="w-4 h-4" />
                          </button>
                        </div>

                        <p className="text-xs sm:text-sm text-zen-ink/80 leading-relaxed mb-4">
                          {t(kw.definitionVi, kw.definitionEn)}
                        </p>
                      </div>

                      {/* Memory cue / trap notice */}
                      {(kw.memoryCueVi || kw.memoryCueEn) && (
                        <div className="p-3 rounded-2xl bg-amber-50/70 border border-amber-200/80 text-[11px] text-amber-900 leading-relaxed">
                          <span className="font-bold">{t("Lưu ý khi làm bài:", "Exam Cue:")}</span>{" "}
                          {t(kw.memoryCueVi, kw.memoryCueEn)}
                        </div>
                      )}
                    </div>
                  ))}
              </div>
            </div>
          )}

          {/* Tab 3: Flashcard */}
          {activeTab === "flashcard" && <FlashcardDeck flashcards={flashcards} />}

          {/* Tab 4: Case Study */}
          {activeTab === "case_study" && (
            <div className="space-y-6">
              {caseStudies.map((cs) => (
                <CaseStudyViewer key={cs.id} caseStudy={cs} />
              ))}
            </div>
          )}

          {/* Tab 5: Quiz */}
          {activeTab === "quiz" && <QuizRunner quizzes={quizzes} />}

          {/* Tab 6: Thi Thử Theo Phần (Chuẩn ICF) */}
          {activeTab === "mock_exam" && (
            <SjtExamRunner
              questions={quizzes}
              examTitleVi={`Thi Thử Theo Phần: ${section.titleVi}`}
              examTitleEn={`Section Mock Exam: ${section.titleEn}`}
              examType="section_mock"
              sectionId={secId}
              durationMinutes={15}
            />
          )}

          {/* Personal Notes Box */}
          <div className="mt-8 rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card">
            <div className="flex items-center justify-between mb-3">
              <h4 className="font-serif text-base font-bold text-zen-ink flex items-center gap-2">
                <span>📝</span>
                <span>{t("Ghi chú cá nhân trên bài học", "Personal Study Notes")}</span>
              </h4>
              <button
                onClick={handleSaveNote}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-colors shadow-zen-subtle"
              >
                <Save className="w-3.5 h-3.5" />
                <span>{isNoteSaved ? t("Đã lưu!", "Saved!") : t("Lưu ghi chú", "Save Note")}</span>
              </button>
            </div>
            <textarea
              value={noteContent}
              onChange={(e) => setNoteContent(e.target.value)}
              placeholder={t(
                "Ghi lại những nhận thức sâu sắc, từ khóa hoặc câu hỏi của riêng bạn cho bài học này...",
                "Write down personal insights, keywords, or reflections for this section..."
              )}
              rows={3}
              className="w-full rounded-2xl border border-zen-border bg-white p-3.5 text-xs text-zen-ink placeholder:text-zen-muted/60 focus:outline-none focus:border-zen-moss-dark transition-colors"
            />
          </div>
        </>
      )}
    </div>
  );
}
