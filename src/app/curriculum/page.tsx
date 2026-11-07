"use client";

import React, { useState, useEffect, useMemo } from "react";
import Link from "next/link";
import { useSearchParams, useRouter } from "next/navigation";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import {
  ICF_7_MODULES,
  GLOSSARY_TERMS,
  GLOSSARY_EXERCISES,
  TEA_MICRO_LESSONS,
  CurriculumModule,
  Lesson,
  GlossaryTerm,
  GlossaryExercise,
  getCurriculumProgress,
  saveLessonProgress,
  computeModuleProgress,
  computeOverallProgress,
  UserLessonProgress,
  fetchServerProgress,
  getGuestProgressSummary,
  mergeGuestProgressToServer
} from "@/lib/curriculumData";
import { removeVietnameseAccents } from "@/lib/unaccent";
import {
  GraduationCap,
  BookOpen,
  CheckCircle2,
  Bookmark,
  ChevronRight,
  ChevronLeft,
  Sparkles,
  ArrowRight,
  Search,
  RotateCcw,
  Eye,
  EyeOff,
  HelpCircle,
  FileText,
  Clock,
  ExternalLink,
  ShieldCheck,
  Award,
  Lock,
  ListOrdered
} from "lucide-react";

export default function CurriculumPage() {
  return (
    <React.Suspense fallback={<div className="max-w-6xl mx-auto px-4 py-16 text-center text-xs text-zen-muted">Đang tải lộ trình học...</div>}>
      <CurriculumContent />
    </React.Suspense>
  );
}

function formatLessonStructured(text: string): string {
  if (!text) return "";
  const lines = text.trim().split("\n");
  const formattedLines: string[] = [];
  for (const line of lines) {
    let l = line.trim();
    if (!l) continue;
    l = l.replace(/^(Định nghĩa:|Definition:)\s*/i, "<b>$1</b> ");
    l = l.replace(/^(Tiêu chuẩn \d+:|Standard \d+:)\s*/i, "• <b>$1</b> ");
    l = l.replace(/^(Marker \d+\.\d+:?)\s*/i, "• <b>$1</b> ");
    l = l.replace(/^(Trụ cột \d+:|Pillar \d+:)\s*/i, "• <b>$1</b> ");
    l = l.replace(/^(Giá trị \d+:|Core Value \d+:)\s*/i, "• <b>$1</b> ");
    l = l.replace(/^([1-8]\.\d{1,2}\.?)\s*/i, "• <b>$1</b> ");

    l = l.replace(/\s+(Marker \d+\.\d+:?)\s*/gi, "<br/><br/>• <b>$1</b> ");
    l = l.replace(/\s+(Tiêu chuẩn \d+:|Standard \d+:)\s*/gi, "<br/><br/>• <b>$1</b> ");
    l = l.replace(/(?:\s+|^)([1-8]\.\d{1,2}\.?)\s+/g, "<br/><br/>• <b>$1</b> ");
    l = l.replace(/\s+(Trụ cột \d+:|Pillar \d+:)\s*/gi, "<br/><br/>• <b>$1</b> ");
    l = l.replace(/\s+(Giá trị \d+:|Core Value \d+:)\s*/gi, "<br/><br/>• <b>$1</b> ");
    l = l.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
    formattedLines.push(l);
  }
  return formattedLines.join("<br/><br/>");
}

function CurriculumContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const initialModId = searchParams.get("module") || "mod-1";
  const initialLesId = searchParams.get("lesson") || "";

  const { lang, t } = useLanguage();
  const { ringBell } = useSound();
  const { user, isAuthenticated, loading: authLoading } = useAuth();

  // Active state
  const [activeModuleId, setActiveModuleId] = useState<string>(initialModId);
  const [activeLessonId, setActiveLessonId] = useState<string>(initialLesId);
  const [displayMode, setDisplayMode] = useState<"vi" | "en" | "bilingual">("bilingual");
  const [progress, setProgress] = useState<Record<string, UserLessonProgress>>({});
  const [loadingProgress, setLoadingProgress] = useState(true);
  const [loadError, setLoadError] = useState(false);
  const [guestMergePrompt, setGuestMergePrompt] = useState<{ count: number; lotuses: number } | null>(null);
  const [merging, setMerging] = useState(false);

  // Quiz state for active lesson
  const [selectedQuizOption, setSelectedQuizOption] = useState<string | null>(null);
  const [quizSubmitted, setQuizSubmitted] = useState<boolean>(false);
  const [quizFeedback, setQuizFeedback] = useState<{ isCorrect: boolean; text: string } | null>(null);

  // Case Study Step 4 reveal state
  const [revealedCaseStudies, setRevealedCaseStudies] = useState<Record<string, boolean>>({});

  // Glossary search & flashcard state
  const [glossaryQuery, setGlossaryQuery] = useState("");
  const [glossaryCategory, setGlossaryCategory] = useState<string>("all");
  const [fcIndex, setFcIndex] = useState(0);
  const [fcFlipped, setFcFlipped] = useState(false);

  // Glossary drill state
  const [drillAnswers, setDrillAnswers] = useState<Record<string, { selected: string; submitted: boolean }>>({});

  // Personal note
  const [personalNote, setPersonalNote] = useState("");
  const [noteSaved, setNoteSaved] = useState(false);

  const loadData = async () => {
    setLoadingProgress(true);
    setLoadError(false);
    try {
      const res = await fetchServerProgress();
      if (res.success) {
        setProgress(res.progress);
        // Check for guest data
        const guestSummary = getGuestProgressSummary();
        const unmerged = Object.keys(guestSummary.progress).some(
          id => !res.progress[id] || (guestSummary.progress[id].status === "quiz_passed" && res.progress[id].status !== "quiz_passed")
        );
        if (guestSummary.count > 0 && unmerged) {
          setGuestMergePrompt({ count: guestSummary.count, lotuses: guestSummary.lotuses });
        }
      } else {
        setLoadError(true);
      }
    } catch {
      setLoadError(true);
    } finally {
      setLoadingProgress(false);
    }
  };

  const handleMergeGuest = async () => {
    setMerging(true);
    try {
      const res = await mergeGuestProgressToServer();
      if (res.success) {
        setGuestMergePrompt(null);
        const updated = await fetchServerProgress();
        if (updated.success) setProgress(updated.progress);
      }
    } finally {
      setMerging(false);
    }
  };

  // Auth gate & load progress on mount
  useEffect(() => {
    if (authLoading) return;
    if (!isAuthenticated) {
      const curQuery = searchParams.toString();
      const target = `/curriculum${curQuery ? `?${curQuery}` : ""}`;
      router.push(`/login?returnUrl=${encodeURIComponent(target)}`);
      return;
    }

    loadData();
  }, [isAuthenticated, authLoading]);

  // Sync with search params if changed
  useEffect(() => {
    const modParam = searchParams.get("module");
    const lesParam = searchParams.get("lesson");
    if (modParam && ICF_7_MODULES.some(m => m.id === modParam)) {
      setActiveModuleId(modParam);
    }
    if (lesParam) {
      setActiveLessonId(lesParam);
    }
  }, [searchParams]);

  // Active module object
  const activeModule = useMemo(() => {
    return ICF_7_MODULES.find(m => m.id === activeModuleId) || ICF_7_MODULES[0];
  }, [activeModuleId]);

  // Active lesson object
  const activeLesson = useMemo(() => {
    if (!activeModule.lessons || activeModule.lessons.length === 0) return null;
    if (activeLessonId) {
      const found = activeModule.lessons.find(l => l.id === activeLessonId);
      if (found) return found;
    }
    return activeModule.lessons[0];
  }, [activeModule, activeLessonId]);

  // Ensure activeLessonId is synchronized
  useEffect(() => {
    if (activeLesson && activeLesson.id !== activeLessonId) {
      setActiveLessonId(activeLesson.id);
    }
  }, [activeLesson, activeLessonId]);

  // Reset quiz state when active lesson changes
  useEffect(() => {
    if (activeLesson) {
      const lesProg = progress[activeLesson.id];
      setSelectedQuizOption(null);
      setQuizSubmitted(lesProg?.status === "quiz_passed");
      setQuizFeedback(null);
      setPersonalNote(lesProg?.note || "");
      setNoteSaved(false);
    }
  }, [activeLesson?.id]);

  // Handle quiz submission
  const handleQuizSubmit = () => {
    if (!activeLesson?.quiz || !selectedQuizOption) return;
    const isCorrect = selectedQuizOption === activeLesson.quiz.correctAnswer;
    setQuizSubmitted(true);
    setQuizFeedback({
      isCorrect,
      text: isCorrect
        ? t("Chính xác! ", "Correct! ") + activeLesson.quiz.explanationVi
        : t("Chưa chuẩn xác. ", "Not quite right. ") + activeLesson.quiz.explanationVi
    });

    if (isCorrect) {
      ringBell();
      const updated = saveLessonProgress(activeLesson.id, {
        status: "quiz_passed",
        score: 100
      });
      setProgress(updated);
    } else {
      const updated = saveLessonProgress(activeLesson.id, {
        status: "read",
        score: 50
      });
      setProgress(updated);
    }
  };

  // Mark lesson as read
  const handleMarkAsRead = () => {
    if (!activeLesson) return;
    ringBell();
    const updated = saveLessonProgress(activeLesson.id, { status: "read" });
    setProgress(updated);
  };

  // Save note & flag
  const handleSaveNote = () => {
    if (!activeLesson) return;
    const curProg = progress[activeLesson.id] || { status: "unread" };
    const updated = saveLessonProgress(activeLesson.id, {
      ...curProg,
      note: personalNote
    });
    setProgress(updated);
    setNoteSaved(true);
    setTimeout(() => setNoteSaved(false), 2000);
  };

  const handleToggleReviewFlag = () => {
    if (!activeLesson) return;
    const curProg = progress[activeLesson.id] || { status: "unread" };
    const updated = saveLessonProgress(activeLesson.id, {
      ...curProg,
      needsReview: !curProg.needsReview
    });
    setProgress(updated);
  };

  // Navigation: Next & Prev lesson
  const currentLessonIndex = activeModule.lessons.findIndex(l => l.id === activeLesson?.id);
  const prevLesson = currentLessonIndex > 0 ? activeModule.lessons[currentLessonIndex - 1] : null;
  const nextLesson = currentLessonIndex >= 0 && currentLessonIndex < activeModule.lessons.length - 1
    ? activeModule.lessons[currentLessonIndex + 1]
    : null;

  // Next module jump
  const currentModuleIndex = ICF_7_MODULES.findIndex(m => m.id === activeModule.id);
  const nextModule = currentModuleIndex < ICF_7_MODULES.length - 1 ? ICF_7_MODULES[currentModuleIndex + 1] : null;

  // Filtered glossary terms with accent-folding search
  const filteredGlossary = useMemo(() => {
    let list = GLOSSARY_TERMS;
    if (glossaryCategory !== "all") {
      list = list.filter(t => t.category === glossaryCategory);
    }
    if (glossaryQuery.trim()) {
      const q = removeVietnameseAccents(glossaryQuery.toLowerCase().trim());
      list = list.filter(t => {
        const viClean = removeVietnameseAccents(t.termVi.toLowerCase() + " " + t.definitionVi.toLowerCase());
        const enClean = (t.termEn + " " + t.definitionEn).toLowerCase();
        return viClean.includes(q) || enClean.includes(q);
      });
    }
    return list;
  }, [glossaryQuery, glossaryCategory]);

  // Overall stats
  const overallStats = useMemo(() => computeOverallProgress(progress), [progress]);
  const activeModuleStats = useMemo(() => computeModuleProgress(activeModule.id, progress), [activeModule.id, progress]);

  if (authLoading || (isAuthenticated && loadingProgress)) {
    return (
      <div className="min-h-[60vh] flex flex-col items-center justify-center space-y-4 px-4 text-center">
        <div className="w-10 h-10 rounded-full border-2 border-zen-moss/30 border-t-zen-moss animate-spin" />
        <h2 className="font-serif text-lg font-medium text-zen-ink">
          🌱 {t("Đang tải tiến độ học tập...", "Loading your learning progress...")}
        </h2>
        <p className="text-xs text-zen-muted max-w-sm">
          {t("Đồng bộ an toàn với máy chủ Học Coaching.", "Securely syncing with Học Coaching server.")}
        </p>
      </div>
    );
  }

  if (loadError) {
    return (
      <div className="min-h-[60vh] flex flex-col items-center justify-center space-y-4 px-4 text-center">
        <div className="text-3xl">⚠️</div>
        <h2 className="font-serif text-lg font-medium text-zen-ink">
          {t("Không thể tải tiến độ học tập", "Unable to load learning progress")}
        </h2>
        <p className="text-xs text-zen-muted max-w-sm">
          {t("Đã xảy ra sự cố kết nối máy chủ. Vui lòng bấm thử lại để tiếp tục học.", "A connection issue occurred. Please retry to continue.")}
        </p>
        <button
          onClick={loadData}
          className="px-5 py-2 rounded-2xl bg-zen-moss text-white text-xs font-semibold shadow hover:bg-zen-moss-dark transition-all"
        >
          {t("Thử lại", "Retry")}
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-6 sm:py-8 space-y-6">
      {/* Guest Merge Banner */}
      {guestMergePrompt && (
        <div className="rounded-2xl border border-amber-300 bg-amber-50/95 p-4 text-amber-900 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-zen-card">
          <div className="flex items-center gap-3">
            <span className="text-2xl">🌱</span>
            <div>
              <p className="font-semibold text-xs sm:text-sm">
                {t("Tìm thấy tiến độ học tập từ phiên duyệt khách!", "Found previous learning progress from guest session!")}
              </p>
              <p className="text-[11px] sm:text-xs text-amber-800">
                {t(
                  `Hệ thống nhận diện bạn có ${guestMergePrompt.count} bài học và ${guestMergePrompt.lotuses} đóa sen đã tích lũy trước đó. Bạn có muốn đồng bộ vào tài khoản này không?`,
                  `Found ${guestMergePrompt.count} lessons and ${guestMergePrompt.lotuses} lotuses from guest mode. Would you like to merge into your account?`
                )}
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2 shrink-0">
            <button
              onClick={handleMergeGuest}
              disabled={merging}
              className="px-3.5 py-1.5 rounded-xl bg-amber-700 hover:bg-amber-800 text-white font-medium text-xs shadow-sm transition-all disabled:opacity-50"
            >
              {merging ? t("Đang đồng bộ...", "Merging...") : t("Đồng bộ vào tài khoản", "Merge to Account")}
            </button>
            <button
              onClick={() => setGuestMergePrompt(null)}
              className="px-3 py-1.5 rounded-xl bg-white hover:bg-stone-50 text-xs text-stone-600 border border-amber-200 transition-all"
            >
              {t("Bỏ qua", "Dismiss")}
            </button>
          </div>
        </div>
      )}

      {/* 1. Header Banner & Mindful Context */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-zen-border/60 pb-6">
          <div className="space-y-1.5 max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold">
              <GraduationCap className="w-3.5 h-3.5 text-zen-moss-dark" />
              <span>{t("Lộ Trình Học Tập 7 Tài Liệu Chuẩn ICF", "7 ICF Official Curriculum Modules")}</span>
            </div>
            <h1 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink flex items-center gap-2">
              <span>{activeModule.icon}</span>
              <span>{t(activeModule.titleVi, activeModule.titleEn)}</span>
            </h1>
            <p className="text-xs sm:text-sm text-zen-wood font-medium">
              📜 <b>{t("Tài liệu nguồn:", "Source:")}</b>{" "}
              <a
                href={activeModule.sourceUrl}
                target="_blank"
                rel="noreferrer"
                className="underline hover:text-zen-moss-dark inline-flex items-center gap-1"
              >
                {activeModule.sourceDoc} <ExternalLink className="w-3 h-3" />
              </a>
            </p>
            <p className="text-xs text-zen-muted italic">
              * {t(
                "Bản dịch phục vụ học tập, không phải bản dịch chính thức của ICF. Phân định rõ ràng giữa quy chuẩn chính thức và phần diễn giải học tập.",
                "Educational study translation; not an official ICF translation. Clear distinction between official standards and pedagogical commentary."
              )}
            </p>
          </div>

          {/* Module Progress Pill */}
          <div className="bg-white/90 border border-zen-border rounded-2xl p-4 shrink-0 min-w-[200px] text-center shadow-zen-subtle">
            <span className="text-xs text-zen-muted font-medium block">
              {t("Tiến độ học phần", "Module Progress")}
            </span>
            <div className="flex items-center justify-center gap-2 my-1">
              <span className="font-serif text-2xl font-bold text-zen-moss-dark">
                {activeModuleStats.percent}%
              </span>
              <span className="text-xs text-zen-ink/70">
                ({activeModuleStats.completed}/{activeModuleStats.total} {t("bài", "lessons")})
              </span>
            </div>
            <div className="w-full h-2 rounded-full bg-zen-surface overflow-hidden">
              <div
                className="h-full bg-zen-moss-dark transition-all duration-300"
                style={{ width: `${activeModuleStats.percent}%` }}
              />
            </div>
          </div>
        </div>

        {/* 7 Modules Horizontal Scroll Tabs */}
        <div className="flex items-center gap-2 overflow-x-auto pt-4 pb-2 no-scrollbar">
          {ICF_7_MODULES.map((mod) => {
            const isActive = mod.id === activeModuleId;
            const stats = computeModuleProgress(mod.id, progress);
            return (
              <button
                key={mod.id}
                onClick={() => {
                  setActiveModuleId(mod.id);
                  if (mod.lessons.length > 0) {
                    setActiveLessonId(mod.lessons[0].id);
                  }
                }}
                className={`flex items-center gap-2 px-3.5 py-2.5 rounded-2xl text-xs font-semibold whitespace-nowrap transition-all border shrink-0 ${
                  isActive
                    ? "bg-zen-moss-dark text-white border-zen-moss-dark shadow-zen-subtle"
                    : "bg-white/80 hover:bg-zen-surface text-zen-ink border-zen-border"
                }`}
              >
                <span>{mod.icon}</span>
                <span>{t(mod.titleVi.split(":")[1]?.trim() || mod.titleVi, mod.titleEn.split(":")[1]?.trim() || mod.titleEn)}</span>
                <span
                  className={`text-[10px] px-1.5 py-0.5 rounded-full ${
                    isActive ? "bg-white/20 text-white" : "bg-zen-surface text-zen-muted"
                  }`}
                >
                  {stats.percent}%
                </span>
              </button>
            );
          })}
        </div>
      </div>

      {/* 2. Main Curriculum Body (2-Column Grid on Desktop) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: Lesson Directory (4 Cols) */}
        <div className="lg:col-span-4 space-y-4">
          <div className="bg-zen-paper rounded-3xl border border-zen-border p-4 shadow-zen-card">
            <div className="flex items-center justify-between px-2 pb-3 border-b border-zen-border/60">
              <span className="text-xs font-bold text-zen-ink uppercase tracking-wider flex items-center gap-1.5">
                <ListOrdered className="w-4 h-4 text-zen-moss-dark" />
                {t("Mục Lục Bài Học", "Lesson Directory")}
              </span>
              <span className="text-[11px] text-zen-muted">
                {activeModule.lessons.length} {t("bài học", "lessons")}
              </span>
            </div>

            {/* List of lessons */}
            <div className="space-y-1.5 mt-3 max-h-[600px] overflow-y-auto pr-1">
              {activeModule.lessons.map((les) => {
                const isSelected = activeLesson?.id === les.id;
                const lesProg = progress[les.id];
                const isQuizPassed = lesProg?.status === "quiz_passed";
                const isRead = lesProg?.status === "read" || isQuizPassed;
                const hasFlag = lesProg?.needsReview;

                return (
                  <button
                    key={les.id}
                    onClick={() => setActiveLessonId(les.id)}
                    className={`w-full text-left p-3 rounded-2xl text-xs transition-all flex items-start gap-2.5 border ${
                      isSelected
                        ? "bg-zen-moss/15 border-zen-moss-dark font-semibold text-zen-moss-dark shadow-zen-subtle"
                        : "bg-white/70 hover:bg-white text-zen-ink/90 border-transparent hover:border-zen-border"
                    }`}
                  >
                    <div className="mt-0.5 shrink-0">
                      {isQuizPassed ? (
                        <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                      ) : isRead ? (
                        <BookOpen className="w-4 h-4 text-zen-wood" />
                      ) : (
                        <div className="w-4 h-4 rounded-full border-2 border-zen-border" />
                      )}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-1">
                        <span className="text-[11px] text-zen-muted font-normal block truncate">
                          {t(`Bài ${les.lessonNumber}`, `Lesson ${les.lessonNumber}`)} • {les.estimatedMinutes}p
                        </span>
                        {hasFlag && <span className="text-[10px] text-amber-600">🚩</span>}
                      </div>
                      <p className="text-xs leading-snug truncate mt-0.5">
                        {t(les.titleVi, les.titleEn)}
                      </p>
                    </div>
                  </button>
                );
              })}

              {activeModule.id === "mod-7" && (
                <div className="p-3 text-center text-xs text-zen-muted italic">
                  {t("Học phần Thuật ngữ tích hợp Tra cứu, Flashcards & Bài tập bên dưới", "Glossary module integrates search, flashcards & drills below")}
                </div>
              )}
            </div>

            {/* Quick Micro-lesson Tea Cup Link */}
            <div className="mt-4 pt-4 border-t border-zen-border/60">
              {TEA_MICRO_LESSONS.filter(tl => tl.moduleId === activeModule.id).map(tea => (
                <div key={tea.id} className="p-3 rounded-2xl bg-zen-surface text-zen-ink space-y-1.5 text-xs">
                  <span className="font-bold text-zen-wood flex items-center gap-1">
                    🍵 {t(tea.titleVi, tea.titleEn)}
                  </span>
                  <p className="italic text-[11px] text-zen-ink/80">
                    "{tea.quoteVi}"
                  </p>
                  <p className="text-[10px] text-zen-muted">
                    {tea.promptVi}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right Column: Active Lesson Content (8 Cols) */}
        <div className="lg:col-span-8 space-y-6">
          {/* SPECIAL VIEW FOR MODULE 7: GLOSSARY EXPLORER */}
          {activeModule.id === "mod-7" ? (
            <div className="space-y-6">
              {/* Glossary Search & Filters */}
              <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
                <div className="flex items-center justify-between">
                  <h2 className="font-serif text-lg font-bold text-zen-ink flex items-center gap-2">
                    <Search className="w-5 h-5 text-zen-moss-dark" />
                    <span>{t("Tra Cứu Thuật Ngữ Thông Minh (Accent-Folding Search)", "Smart Terminology Lookup")}</span>
                  </h2>
                  <span className="text-xs text-zen-muted font-medium">
                    {filteredGlossary.length} {t("thuật ngữ", "terms")}
                  </span>
                </div>

                <div className="relative">
                  <input
                    type="text"
                    value={glossaryQuery}
                    onChange={(e) => setGlossaryQuery(e.target.value)}
                    placeholder={t(
                      "Gõ tiếng Việt không dấu (vd: khach hang, bao mat, ranh gioi, coaching)...",
                      "Type unaccented Vietnamese or English term (e.g. khach hang, confidentiality)..."
                    )}
                    className="w-full bg-white rounded-2xl border border-zen-border px-4 py-3 text-sm text-zen-ink placeholder:text-zen-muted/70 focus:outline-none focus:border-zen-moss-dark transition-all shadow-zen-subtle"
                  />
                  {glossaryQuery && (
                    <button
                      onClick={() => setGlossaryQuery("")}
                      className="absolute right-3 top-3 text-xs text-zen-muted hover:text-zen-ink"
                    >
                      ✕
                    </button>
                  )}
                </div>

                {/* Category Pills */}
                <div className="flex items-center gap-2 overflow-x-auto pb-1 text-xs">
                  {[
                    { id: "all", labelVi: "Tất cả", labelEn: "All" },
                    { id: "Official Ethics Definitions", labelVi: "Đạo đức ICF", labelEn: "Ethics" },
                    { id: "Official Competencies Definitions", labelVi: "Năng lực cốt lõi", labelEn: "Competencies" },
                    { id: "Official Referral Definitions", labelVi: "Chuyển gửi trị liệu", labelEn: "Referral" },
                    { id: "Supporting Coaching Definitions", labelVi: "Thuật ngữ hỗ trợ", labelEn: "Supporting" }
                  ].map((cat) => (
                    <button
                      key={cat.id}
                      onClick={() => setGlossaryCategory(cat.id)}
                      className={`px-3 py-1.5 rounded-xl transition-all shrink-0 ${
                        glossaryCategory === cat.id
                          ? "bg-zen-moss-dark text-white font-semibold shadow-zen-subtle"
                          : "bg-white border border-zen-border text-zen-ink hover:bg-zen-surface"
                      }`}
                    >
                      {t(cat.labelVi, cat.labelEn)}
                    </button>
                  ))}
                </div>
              </div>

              {/* Glossary Flashcards Interactive Deck */}
              {filteredGlossary.length > 0 && (
                <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-zen-wood uppercase tracking-wider flex items-center gap-1.5">
                      🗂️ {t("Thẻ Ghi Nhớ Thuật Ngữ (Flashcards)", "Terminology Flashcards")}
                    </span>
                    <span className="text-xs text-zen-muted">
                      {fcIndex + 1} / {filteredGlossary.length}
                    </span>
                  </div>

                  {/* Flashcard 2-sided */}
                  {(() => {
                    const curTerm = filteredGlossary[fcIndex % filteredGlossary.length];
                    return (
                      <div
                        onClick={() => setFcFlipped(!fcFlipped)}
                        className="cursor-pointer min-h-[220px] rounded-3xl border-2 border-dashed border-zen-moss/40 bg-white p-6 flex flex-col justify-between hover:border-zen-moss-dark transition-all shadow-zen-subtle text-center select-none"
                      >
                        <div className="text-[11px] text-zen-muted font-medium">
                          {curTerm.isOfficial ? (
                            <span className="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-bold">
                              ✓ {t("Thuật ngữ ICF chính thức", "Official ICF Term")}
                            </span>
                          ) : (
                            <span className="px-2 py-0.5 rounded-full bg-amber-100 text-amber-800">
                              ℹ {t("Thuật ngữ học tập bổ trợ", "Supporting Term")}
                            </span>
                          )}
                        </div>

                        {!fcFlipped ? (
                          <div className="my-auto space-y-2">
                            <h3 className="font-serif text-2xl font-bold text-zen-ink">
                              {curTerm.termEn}
                            </h3>
                            <p className="text-sm text-zen-wood font-medium">
                              {curTerm.termVi}
                            </p>
                            <span className="text-[11px] text-zen-muted block mt-2">
                              👉 {t("Nhấn để xem định nghĩa chi tiết", "Click to reveal definition")}
                            </span>
                          </div>
                        ) : (
                          <div className="my-auto space-y-3 text-left">
                            <div className="p-3 rounded-2xl bg-zen-surface text-xs text-zen-ink">
                              <b>{t("Định nghĩa tiếng Việt:", "Vietnamese Definition:")}</b>
                              <p className="mt-1 leading-relaxed">{curTerm.definitionVi}</p>
                            </div>
                            <div className="p-3 rounded-2xl bg-white border border-zen-border text-xs text-zen-muted">
                              <b>English Definition:</b>
                              <p className="mt-1 leading-relaxed italic">{curTerm.definitionEn}</p>
                            </div>
                            <p className="text-[10px] text-zen-wood">
                              📜 {curTerm.source} ({curTerm.version})
                            </p>
                          </div>
                        )}

                        <div className="text-[10px] text-zen-muted pt-2 border-t border-zen-border/50">
                          {t("Lật thẻ 2 mặt • Ôn luyện phản xạ tiếng Anh & Việt", "2-sided flip • Practice English & Vietnamese definitions")}
                        </div>
                      </div>
                    );
                  })()}

                  <div className="flex items-center justify-between pt-2">
                    <button
                      onClick={() => {
                        setFcFlipped(false);
                        setFcIndex(prev => (prev > 0 ? prev - 1 : filteredGlossary.length - 1));
                      }}
                      className="px-4 py-2 rounded-xl border border-zen-border bg-white text-xs font-semibold text-zen-ink hover:bg-zen-surface flex items-center gap-1"
                    >
                      <ChevronLeft className="w-4 h-4" /> {t("Thẻ trước", "Previous")}
                    </button>
                    <button
                      onClick={() => setFcFlipped(!fcFlipped)}
                      className="px-4 py-2 rounded-xl bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold hover:bg-zen-moss/25"
                    >
                      {fcFlipped ? t("Xem mặt trước", "Show Front") : t("Lật xem định nghĩa", "Flip Card")}
                    </button>
                    <button
                      onClick={() => {
                        setFcFlipped(false);
                        setFcIndex(prev => (prev + 1) % filteredGlossary.length);
                      }}
                      className="px-4 py-2 rounded-xl border border-zen-border bg-white text-xs font-semibold text-zen-ink hover:bg-zen-surface flex items-center gap-1"
                    >
                      {t("Thẻ sau", "Next")} <ChevronRight className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              )}

              {/* Glossary List */}
              <div className="space-y-3">
                <h3 className="font-serif text-base font-bold text-zen-ink">
                  {t("Danh Mục Thuật Ngữ Chi Tiết", "Detailed Terminology Directory")}
                </h3>
                {filteredGlossary.map((term) => (
                  <div
                    key={term.id}
                    className="p-5 rounded-3xl border border-zen-border bg-zen-paper shadow-zen-subtle space-y-2.5"
                  >
                    <div className="flex items-center justify-between flex-wrap gap-2">
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-sm text-zen-ink">{term.termEn}</span>
                        <span className="text-xs text-zen-wood">({term.termVi})</span>
                      </div>
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-zen-surface text-zen-muted font-medium">
                        {term.categoryVi}
                      </span>
                    </div>
                    <p className="text-xs text-zen-ink leading-relaxed">
                      <b>{t("Tiếng Việt:", "Vietnamese:")}</b> {term.definitionVi}
                    </p>
                    <p className="text-xs text-zen-muted leading-relaxed italic">
                      <b>English:</b> {term.definitionEn}
                    </p>
                    {term.nearSynonyms && (
                      <div className="text-[11px] text-zen-wood pt-1 flex items-center gap-1.5 flex-wrap">
                        <span className="font-medium">{t("Cặp khái niệm cần phân biệt:", "Confusable pairs:")}</span>
                        {term.nearSynonyms.map((syn, idx) => (
                          <span key={idx} className="px-2 py-0.5 rounded-md bg-white border border-zen-border text-[10px]">
                            {syn}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>

              {/* Glossary Exercises: Near-Synonym Drills */}
              <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
                <h3 className="font-serif text-base font-bold text-zen-ink flex items-center gap-2">
                  <Award className="w-5 h-5 text-zen-ochre" />
                  <span>{t("Bài Tập Phân Biệt Các Cặp Dễ Nhầm Lẫn", "Near-Synonym Disambiguation Drills")}</span>
                </h3>

                {GLOSSARY_EXERCISES.map((ex) => {
                  const state = drillAnswers[ex.id] || { selected: "", submitted: false };
                  const isCorrect = state.selected === ex.correctAnswer;

                  return (
                    <div key={ex.id} className="p-4 rounded-2xl bg-white border border-zen-border space-y-3">
                      <div className="flex items-center justify-between">
                        <span className="text-xs font-bold text-zen-moss-dark">
                          ⚖️ {ex.termPair}
                        </span>
                        {state.submitted && (
                          <span className={`text-xs font-bold ${isCorrect ? "text-emerald-600" : "text-rose-600"}`}>
                            {isCorrect ? t("✓ Chính xác", "✓ Correct") : t("✗ Chưa đúng", "✗ Incorrect")}
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-zen-ink font-medium leading-relaxed">
                        {t(ex.questionVi, ex.questionEn)}
                      </p>

                      <div className="space-y-1.5">
                        {ex.options.map((opt) => (
                          <label
                            key={opt.key}
                            className={`flex items-start gap-2.5 p-2.5 rounded-xl border text-xs cursor-pointer transition-all ${
                              state.selected === opt.key
                                ? "bg-zen-moss/10 border-zen-moss-dark font-medium"
                                : "bg-zen-surface/40 hover:bg-zen-surface border-transparent"
                            }`}
                          >
                            <input
                              type="radio"
                              name={`drill_${ex.id}`}
                              checked={state.selected === opt.key}
                              onChange={() => setDrillAnswers(prev => ({
                                ...prev,
                                [ex.id]: { selected: opt.key, submitted: false }
                              }))}
                              className="mt-0.5 accent-zen-moss-dark"
                            />
                            <span><b>{opt.key}.</b> {t(opt.textVi, opt.textEn)}</span>
                          </label>
                        ))}
                      </div>

                      <div className="flex items-center justify-between pt-2">
                        <button
                          onClick={() => {
                            if (!state.selected) return;
                            setDrillAnswers(prev => ({
                              ...prev,
                              [ex.id]: { ...state, submitted: true }
                            }));
                            if (state.selected === ex.correctAnswer) {
                              ringBell();
                              saveLessonProgress(`gl-drill-${ex.id}`, { status: "quiz_passed" });
                            }
                          }}
                          disabled={!state.selected}
                          className="px-4 py-1.5 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-dark/90 disabled:opacity-50"
                        >
                          {t("Kiểm tra đáp án", "Check Answer")}
                        </button>
                      </div>

                      {state.submitted && (
                        <div className={`p-3 rounded-xl text-xs leading-relaxed ${
                          isCorrect ? "bg-emerald-50 text-emerald-900 border border-emerald-200" : "bg-rose-50 text-rose-900 border border-rose-200"
                        }`}>
                          <b>{t("Giải thích sư phạm:", "Pedagogical Explanation:")}</b> {ex.explanationVi}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          ) : activeLesson ? (
            /* STANDARD 10-POINT LESSON VIEWER (MODULES 1–6) */
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card space-y-6">
              {/* Top Bar: Language Mode Switcher & Lesson Meta */}
              <div className="flex flex-wrap items-center justify-between gap-3 border-b border-zen-border/60 pb-4">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold text-zen-moss-dark px-2.5 py-1 rounded-xl bg-zen-moss/15">
                    {t(`Bài ${activeLesson.lessonNumber}`, `Lesson ${activeLesson.lessonNumber}`)}
                  </span>
                  <span className="text-xs text-zen-muted flex items-center gap-1">
                    <Clock className="w-3.5 h-3.5" /> {activeLesson.estimatedMinutes} {t("phút học", "min read")}
                  </span>
                </div>

                {/* Display mode buttons */}
                <div className="flex items-center gap-1 bg-white p-1 rounded-xl border border-zen-border text-xs">
                  <button
                    onClick={() => setDisplayMode("vi")}
                    className={`px-2.5 py-1 rounded-lg font-medium transition-all ${
                      displayMode === "vi" ? "bg-zen-moss-dark text-white shadow-zen-subtle" : "text-zen-muted hover:text-zen-ink"
                    }`}
                  >
                    🇻🇳 Tiếng Việt
                  </button>
                  <button
                    onClick={() => setDisplayMode("en")}
                    className={`px-2.5 py-1 rounded-lg font-medium transition-all ${
                      displayMode === "en" ? "bg-zen-moss-dark text-white shadow-zen-subtle" : "text-zen-muted hover:text-zen-ink"
                    }`}
                  >
                    🇬🇧 English
                  </button>
                  <button
                    onClick={() => setDisplayMode("bilingual")}
                    className={`px-2.5 py-1 rounded-lg font-medium transition-all ${
                      displayMode === "bilingual" ? "bg-zen-moss-dark text-white shadow-zen-subtle" : "text-zen-muted hover:text-zen-ink"
                    }`}
                  >
                    🌐 Song ngữ
                  </button>
                </div>
              </div>

              {/* Lesson Title */}
              <div>
                <h2 className="font-serif text-xl sm:text-2xl font-bold text-zen-ink leading-tight">
                  {displayMode === "en" ? activeLesson.titleEn : activeLesson.titleVi}
                </h2>
                {displayMode === "bilingual" && (
                  <p className="text-xs sm:text-sm text-zen-muted italic mt-1 font-serif">
                    {activeLesson.titleEn}
                  </p>
                )}
              </div>

              {/* 1. Objectives */}
              {activeLesson.objectivesVi && (
                <div className="p-4 rounded-2xl bg-zen-surface text-xs text-zen-ink space-y-1.5 border border-zen-border/50">
                  <span className="font-bold text-zen-moss-dark block">
                    🎯 {t("Mục Tiêu Bài Học:", "Learning Objectives:")}
                  </span>
                  <ul className="list-disc list-inside space-y-1 text-zen-ink/90">
                    {(displayMode === "en" ? activeLesson.objectivesEn : activeLesson.objectivesVi)?.map((obj, i) => (
                      <li key={i}>{obj}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* 2. Source & Version Reference */}
              {activeLesson.sourceDocument && (
                <div className="text-xs text-zen-wood p-3 rounded-xl bg-white border border-zen-border flex items-center justify-between flex-wrap gap-2">
                  <div>
                    <b>📜 {t("Văn bản nguồn:", "Source:")}</b> {activeLesson.sourceDocument}
                    {activeLesson.sourceVersion && <span className="text-zen-muted"> • {activeLesson.sourceVersion}</span>}
                  </div>
                  {activeLesson.sourceLink && (
                    <a
                      href={activeLesson.sourceLink}
                      target="_blank"
                      rel="noreferrer"
                      className="text-zen-moss-dark hover:underline flex items-center gap-1 font-medium"
                    >
                      {t("Xem tài liệu gốc ↗", "Original Doc ↗")}
                    </a>
                  )}
                </div>
              )}

              {/* 3 & 4. Excerpt & Faithful Translation */}
              {(activeLesson.originalExcerptEn || activeLesson.translationVi || activeLesson.definitionEn || activeLesson.definitionVi) && (
                <div className="space-y-4">
                  <h3 className="text-xs font-bold text-zen-moss-dark uppercase tracking-wider">
                    📖 {t("Văn Bản Chuẩn Mực & Bản Dịch Học Tập", "Official Excerpt & Faithful Translation")}
                  </h3>

                  {(displayMode === "en" || displayMode === "bilingual") && (activeLesson.originalExcerptEn || activeLesson.definitionEn) && (
                    <div className="p-5 rounded-2xl bg-white border border-zen-border text-xs text-zen-ink/90 font-serif leading-relaxed space-y-3">
                      <span className="text-[11px] uppercase font-sans font-bold text-blue-900 block not-italic tracking-wider">
                        🇬🇧 Original ICF Language (Authoritative Reference)
                      </span>
                      {activeLesson.definitionEn && activeLesson.subCompetencies && activeLesson.subCompetencies.length > 0 ? (
                        <div className="space-y-3 not-italic">
                          <div className="p-3.5 bg-blue-50/60 rounded-xl border border-blue-100 text-[13px] leading-relaxed">
                            <span className="font-sans font-bold text-blue-950 block mb-1">Definition:</span>
                            <p className="font-serif italic text-blue-950/90">{activeLesson.definitionEn}</p>
                          </div>
                          <div className="space-y-2 mt-3 pt-1">
                            <span className="text-[10px] font-sans font-bold uppercase tracking-wider text-zen-muted block">
                              Core Sub-Competencies ({activeLesson.subCompetencies.length} items):
                            </span>
                            {activeLesson.subCompetencies.map((sub) => (
                              <div key={sub.code} className="p-2.5 rounded-lg bg-slate-50/80 border border-slate-200/60 font-sans text-[12.5px] leading-relaxed flex items-start gap-2.5">
                                <span className="font-bold text-blue-900 bg-blue-100/80 px-2 py-0.5 rounded text-[11px] shrink-0 font-mono">
                                  {sub.code}
                                </span>
                                <span className="text-slate-800 font-serif">{sub.textEn}</span>
                              </div>
                            ))}
                          </div>
                        </div>
                      ) : (
                        <div
                          className="leading-relaxed whitespace-pre-line space-y-2 font-serif text-[13px]"
                          dangerouslySetInnerHTML={{ __html: formatLessonStructured(activeLesson.originalExcerptEn || "") }}
                        />
                      )}
                    </div>
                  )}

                  {(displayMode === "vi" || displayMode === "bilingual") && (activeLesson.translationVi || activeLesson.definitionVi) && (
                    <div className="p-5 rounded-2xl bg-zen-surface/60 border border-zen-border text-xs text-zen-ink leading-relaxed space-y-3">
                      <span className="text-[11px] uppercase font-sans font-bold text-zen-wood block tracking-wider">
                        🇻🇳 Bản Dịch Đầy Đủ Phục Vụ Học Tập (Faithful Vietnamese Translation)
                      </span>
                      {activeLesson.definitionVi && activeLesson.subCompetencies && activeLesson.subCompetencies.length > 0 ? (
                        <div className="space-y-3">
                          <div className="p-3.5 bg-emerald-50/60 rounded-xl border border-emerald-100 text-[13px] leading-relaxed">
                            <span className="font-bold text-emerald-950 block mb-1">Định nghĩa:</span>
                            <p className="text-emerald-950/90 leading-relaxed">{activeLesson.definitionVi}</p>
                          </div>
                          <div className="space-y-2 mt-3 pt-1">
                            <span className="text-[10px] font-bold uppercase tracking-wider text-zen-muted block">
                              Các Năng Lực Thành Phần ({activeLesson.subCompetencies.length} mục):
                            </span>
                            {activeLesson.subCompetencies.map((sub) => (
                              <div key={sub.code} className="p-2.5 rounded-lg bg-white/90 border border-emerald-200/60 text-[12.5px] leading-relaxed flex items-start gap-2.5">
                                <span className="font-bold text-emerald-900 bg-emerald-100/80 px-2 py-0.5 rounded text-[11px] shrink-0 font-mono">
                                  {sub.code}
                                </span>
                                <span className="text-emerald-950">{sub.textVi}</span>
                              </div>
                            ))}
                          </div>
                        </div>
                      ) : (
                        <div
                          className="leading-relaxed whitespace-pre-line space-y-2 text-[13px]"
                          dangerouslySetInnerHTML={{ __html: formatLessonStructured(activeLesson.translationVi || "") }}
                        />
                      )}
                    </div>
                  )}
                </div>
              )}

              {/* 5. Pedagogical Commentary */}
              {activeLesson.commentaryVi && (
                <div className="p-4 rounded-2xl bg-amber-50/60 border border-amber-200/70 text-xs text-amber-950 space-y-1.5">
                  <span className="font-bold text-amber-900 block flex items-center gap-1.5">
                    💡 {t("Giải Thích Sư Phạm (Pedagogical Commentary):", "Pedagogical Commentary:")}
                  </span>
                  <p className="leading-relaxed whitespace-pre-line">
                    {displayMode === "en" ? (activeLesson.commentaryEn || activeLesson.commentaryVi) : activeLesson.commentaryVi}
                  </p>
                </div>
              )}

              {/* 6. Practical Application Example */}
              {activeLesson.exampleContentVi && (
                <div className="p-4 rounded-2xl bg-emerald-50/60 border border-emerald-200/70 text-xs text-emerald-950 space-y-1.5">
                  <span className="font-bold text-emerald-900 block flex items-center gap-1.5">
                    🌿 {t("Ví Dụ Ứng Dụng Thực Tế (Application Example):", "Practical Application Example:")}
                  </span>
                  <p className="leading-relaxed whitespace-pre-line">
                    {displayMode === "en" ? (activeLesson.exampleContentEn || activeLesson.exampleContentVi) : activeLesson.exampleContentVi}
                  </p>
                  <span className="text-[10px] text-emerald-700 italic block pt-1">
                    * {activeLesson.exampleType || t("Ví dụ tự soạn phục vụ học tập", "Pedagogical illustrative example")}
                  </span>
                </div>
              )}

              {/* SPECIAL CASE STUDY 5-STEP WORKFLOW (MODULE 5) */}
              {activeLesson.caseWorkflow && (
                <div className="rounded-2xl border-2 border-zen-border bg-white p-5 space-y-5">
                  <div className="flex items-center justify-between border-b border-zen-border/60 pb-3">
                    <span className="text-xs font-bold text-zen-moss-dark uppercase tracking-wider flex items-center gap-1.5">
                      🎭 {t("Quy Trình 5 Bước Giải Quyết Tình Huống Đạo Đức", "5-Step Ethical Decision Process")}
                    </span>
                    <span className="text-[11px] text-zen-wood font-medium">ICF Ethics Framework</span>
                  </div>

                  {/* Step 1: Scenario */}
                  <div className="space-y-1.5">
                    <span className="text-xs font-bold text-zen-ink block">
                      {t("Bước 1: Đọc kịch bản tình huống thực tế", "Step 1: Read Real-world Scenario")}
                    </span>
                    <div className="p-3.5 rounded-xl bg-zen-surface text-xs leading-relaxed text-zen-ink">
                      {displayMode === "en" ? activeLesson.caseWorkflow.step1_scenarioEn : activeLesson.caseWorkflow.step1_scenarioVi}
                    </div>
                  </div>

                  {/* Step 2: Stakeholders */}
                  <div className="space-y-1.5">
                    <span className="text-xs font-bold text-zen-ink block">
                      {t("Bước 2: Nhận diện các bên liên quan & Ranh giới hợp đồng", "Step 2: Identify Stakeholders & Boundaries")}
                    </span>
                    <div className="p-3.5 rounded-xl bg-white border border-zen-border text-xs leading-relaxed text-zen-ink/90">
                      {displayMode === "en" ? activeLesson.caseWorkflow.step2_stakeholdersEn : activeLesson.caseWorkflow.step2_stakeholdersVi}
                    </div>
                  </div>

                  {/* Step 3: Self-Reflection Prompt */}
                  <div className="space-y-1.5">
                    <span className="text-xs font-bold text-zen-ochre block">
                      {t("Bước 3: Tự suy ngẫm & Ghi chép cách bạn xử lý", "Step 3: Self-Reflect & Outline Your Approach")}
                    </span>
                    <p className="text-xs text-zen-muted italic">
                      "{displayMode === "en" ? activeLesson.caseWorkflow.step3_selfReflectionPromptEn : activeLesson.caseWorkflow.step3_selfReflectionPromptVi}"
                    </p>
                    <textarea
                      value={personalNote}
                      onChange={(e) => setPersonalNote(e.target.value)}
                      placeholder={t("Ghi lại cách bạn sẽ xử lý tình huống này trước khi mở phân tích của ICF...", "Record your initial response before revealing ICF analysis...")}
                      rows={3}
                      className="w-full bg-zen-surface/50 rounded-xl border border-zen-border p-3 text-xs text-zen-ink focus:outline-none focus:border-zen-moss-dark"
                    />
                  </div>

                  {/* Step 4: Collapsible Official ICF Analysis (HIDDEN BY DEFAULT) */}
                  <div className="space-y-2 pt-2 border-t border-zen-border/60">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-bold text-zen-moss-dark">
                        {t("Bước 4: Mở phần phân tích đạo đức chính thức từ ICF", "Step 4: Reveal Official ICF Ethical Analysis")}
                      </span>
                      <button
                        onClick={() => {
                          setRevealedCaseStudies(prev => ({
                            ...prev,
                            [activeLesson.id]: !prev[activeLesson.id]
                          }));
                        }}
                        className="px-3 py-1.5 rounded-xl bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold hover:bg-zen-moss/25 flex items-center gap-1.5 transition-colors"
                      >
                        {revealedCaseStudies[activeLesson.id] ? (
                          <>
                            <EyeOff className="w-3.5 h-3.5" /> {t("Ẩn phân tích", "Hide Analysis")}
                          </>
                        ) : (
                          <>
                            <Eye className="w-3.5 h-3.5" /> {t("Mở phân tích chính thức ↗", "Reveal Official Analysis ↗")}
                          </>
                        )}
                      </button>
                    </div>

                    {revealedCaseStudies[activeLesson.id] ? (
                      <div className="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 text-xs text-amber-950 space-y-2 animate-in fade-in duration-200">
                        <span className="font-bold text-amber-900 block">
                          📜 {t("Phân Tích Căn Cứ Chuẩn Mực ICF:", "Official ICF Analysis & Guidance:")}
                        </span>
                        <p className="leading-relaxed whitespace-pre-line">
                          {displayMode === "en" ? activeLesson.caseWorkflow.step4_sourceAnalysisEn : activeLesson.caseWorkflow.step4_sourceAnalysisVi}
                        </p>
                      </div>
                    ) : (
                      <div className="p-3 rounded-xl bg-zen-surface/40 border border-dashed border-zen-border text-center text-xs text-zen-muted italic">
                        {t("Phần phân tích nguồn được ẩn kín để bạn tự lập luận trước. Bấm 'Mở phân tích' khi sẵn sàng.", "Analysis hidden to protect critical thinking. Click 'Reveal' when ready.")}
                      </div>
                    )}
                  </div>

                  {/* Step 5: Key Takeaway */}
                  <div className="space-y-1.5 pt-2 border-t border-zen-border/60">
                    <span className="text-xs font-bold text-emerald-800 block">
                      {t("Bước 5: So sánh & Đúc kết bài học cốt lõi", "Step 5: Compare & Consolidate Takeaway")}
                    </span>
                    <div className="p-3.5 rounded-xl bg-emerald-50/60 border border-emerald-200 text-xs text-emerald-950 font-medium">
                      {activeLesson.caseWorkflow.step5_takeawaysVi}
                    </div>
                  </div>
                </div>
              )}

              {/* SPECIAL FAQS LIST (MODULE 6) */}
              {activeLesson.faqs && activeLesson.faqs.length > 0 && (
                <div className="space-y-3">
                  <h3 className="text-xs font-bold text-zen-moss-dark uppercase tracking-wider flex items-center gap-1.5">
                    ❓ {t("Tập Hợp Câu Hỏi Thường Gặp (ICF FAQs)", "Official Curated FAQs")}
                  </h3>

                  <div className="space-y-3">
                    {activeLesson.faqs.map((faq) => (
                      <div
                        key={faq.faqId}
                        className="p-4 rounded-2xl bg-white border border-zen-border space-y-2.5 shadow-zen-subtle"
                      >
                        <div className="flex items-center justify-between gap-2 flex-wrap">
                          <span className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${
                            faq.tag === "Official ICF FAQ"
                              ? "bg-emerald-100 text-emerald-800"
                              : "bg-blue-100 text-blue-800"
                          }`}>
                            {faq.tag}
                          </span>
                          <span className="text-[10px] text-zen-muted">
                            {t("Đã xác minh:", "Verified:")} {faq.verifiedDate}
                          </span>
                        </div>

                        <p className="font-bold text-xs text-zen-ink">
                          {displayMode === "en" ? faq.questionEn : faq.questionVi}
                        </p>

                        <div className="p-3 rounded-xl bg-zen-surface text-xs text-zen-ink/90 leading-relaxed">
                          <b>{t("Giải đáp chính thức:", "Official Answer:")}</b>{" "}
                          {displayMode === "en" ? faq.answerEn : faq.answerVi}
                        </div>

                        {faq.relatedStandard && (
                          <div className="text-[10px] text-zen-wood">
                            📜 {t("Chuẩn mực liên quan:", "Standard:")} {faq.relatedStandard}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* 7. Interactive Self-Check Quiz */}
              {activeLesson.quiz && (
                <div className="rounded-2xl border-2 border-zen-border bg-white p-5 space-y-4 shadow-zen-subtle">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-zen-moss-dark uppercase tracking-wider flex items-center gap-1.5">
                      📝 {t("Trắc Nghiệm Tự Kiểm Tra Hiểu Biết", "Self-Check Diagnostic Quiz")}
                    </span>
                    {quizSubmitted && (
                      <span className={`text-xs font-bold ${quizFeedback?.isCorrect ? "text-emerald-600" : "text-amber-600"}`}>
                        {quizFeedback?.isCorrect ? t("✓ Đã đạt", "✓ Passed") : t("Đã làm", "Completed")}
                      </span>
                    )}
                  </div>

                  <p className="text-xs font-semibold text-zen-ink leading-relaxed">
                    {displayMode === "en" ? activeLesson.quiz.questionEn : activeLesson.quiz.questionVi}
                  </p>

                  <div className="space-y-2">
                    {activeLesson.quiz.options.map((opt) => {
                      const isSelected = selectedQuizOption === opt.key;
                      const isCorrect = opt.key === activeLesson.quiz?.correctAnswer;
                      let optionStyle = "bg-zen-surface/40 hover:bg-zen-surface border-transparent text-zen-ink";

                      if (quizSubmitted) {
                        if (isCorrect) {
                          optionStyle = "bg-emerald-50 border-emerald-400 text-emerald-950 font-medium";
                        } else if (isSelected && !isCorrect) {
                          optionStyle = "bg-rose-50 border-rose-300 text-rose-950 line-through";
                        }
                      } else if (isSelected) {
                        optionStyle = "bg-zen-moss/10 border-zen-moss-dark text-zen-moss-dark font-medium shadow-zen-subtle";
                      }

                      return (
                        <label
                          key={opt.key}
                          className={`flex items-start gap-2.5 p-3 rounded-xl border text-xs cursor-pointer transition-all ${optionStyle}`}
                        >
                          <input
                            type="radio"
                            name={`quiz_${activeLesson.id}`}
                            checked={selectedQuizOption === opt.key}
                            onChange={() => {
                              if (!quizSubmitted) {
                                setSelectedQuizOption(opt.key);
                              }
                            }}
                            disabled={quizSubmitted}
                            className="mt-0.5 accent-zen-moss-dark"
                          />
                          <span className="leading-relaxed">
                            <b>{opt.key}.</b> {displayMode === "en" ? opt.textEn : opt.textVi}
                          </span>
                        </label>
                      );
                    })}
                  </div>

                  <div className="flex items-center justify-between pt-2">
                    {!quizSubmitted ? (
                      <button
                        onClick={handleQuizSubmit}
                        disabled={!selectedQuizOption}
                        className="px-5 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-dark/90 disabled:opacity-50 transition-all shadow-zen-subtle"
                      >
                        {t("Nộp bài tự kiểm tra", "Submit Quiz")}
                      </button>
                    ) : (
                      <button
                        onClick={() => {
                          setQuizSubmitted(false);
                          setSelectedQuizOption(null);
                          setQuizFeedback(null);
                        }}
                        className="px-4 py-1.5 rounded-xl border border-zen-border bg-white text-xs font-medium text-zen-muted hover:text-zen-ink"
                      >
                        {t("Làm lại câu hỏi", "Retake Quiz")}
                      </button>
                    )}
                  </div>

                  {quizFeedback && (
                    <div className={`p-3.5 rounded-xl text-xs leading-relaxed ${
                      quizFeedback.isCorrect
                        ? "bg-emerald-50 text-emerald-900 border border-emerald-200"
                        : "bg-amber-50 text-amber-900 border border-amber-200"
                    }`}>
                      {quizFeedback.text}
                    </div>
                  )}
                </div>
              )}

              {/* 8. Personal Note & Review Flag */}
              <div className="rounded-2xl border border-zen-border bg-white p-4 space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-zen-ink flex items-center gap-1.5">
                    📓 {t("Sổ Tay Ghi Chú Cá Nhân", "Personal Study Notes")}
                  </span>
                  <button
                    onClick={handleToggleReviewFlag}
                    className={`text-xs px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 ${
                      progress[activeLesson.id]?.needsReview
                        ? "bg-amber-100 text-amber-800 border-amber-300 font-bold"
                        : "bg-zen-surface text-zen-muted border-zen-border hover:text-zen-ink"
                    }`}
                  >
                    <span>🚩</span>
                    <span>{progress[activeLesson.id]?.needsReview ? t("Đã cắm cờ ôn lại", "Flagged") : t("Cắm cờ cần ôn lại", "Flag for review")}</span>
                  </button>
                </div>

                <textarea
                  value={personalNote}
                  onChange={(e) => setPersonalNote(e.target.value)}
                  placeholder={t("Ghi chú những chiêm nghiệm sâu sắc hoặc mẹo ghi nhớ cho bài học này...", "Record your reflections or mnemonics...")}
                  rows={3}
                  className="w-full bg-zen-surface/40 rounded-xl border border-zen-border p-3 text-xs text-zen-ink focus:outline-none focus:border-zen-moss-dark"
                />

                <div className="flex items-center justify-between">
                  <span className="text-[11px] text-emerald-600 font-medium">
                    {noteSaved && t("✓ Đã lưu ghi chú", "✓ Note saved")}
                  </span>
                  <button
                    onClick={handleSaveNote}
                    className="px-4 py-1.5 rounded-xl bg-zen-surface hover:bg-zen-surface/80 text-zen-ink text-xs font-semibold border border-zen-border transition-colors"
                  >
                    {t("Lưu ghi chú", "Save Note")}
                  </button>
                </div>
              </div>

              {/* 9. Sequential Bottom Navigation */}
              <div className="flex items-center justify-between pt-4 border-t border-zen-border/70">
                {prevLesson ? (
                  <button
                    onClick={() => setActiveLessonId(prevLesson.id)}
                    className="px-4 py-2 rounded-xl border border-zen-border bg-white text-xs font-semibold text-zen-ink hover:bg-zen-surface flex items-center gap-1.5"
                  >
                    <ChevronLeft className="w-4 h-4" />
                    <span>{t("Bài trước", "Previous")}</span>
                  </button>
                ) : (
                  <div />
                )}

                <button
                  onClick={handleMarkAsRead}
                  className="px-5 py-2 rounded-xl bg-white border border-zen-moss-dark text-zen-moss-dark text-xs font-semibold hover:bg-zen-moss/10 transition-colors shadow-zen-subtle"
                >
                  ✓ {t("Đánh dấu đã đọc", "Mark Complete")}
                </button>

                {nextLesson ? (
                  <button
                    onClick={() => setActiveLessonId(nextLesson.id)}
                    className="px-5 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-dark/90 flex items-center gap-1.5 shadow-zen-subtle"
                  >
                    <span>{t("Bài tiếp theo", "Next Lesson")}</span>
                    <ChevronRight className="w-4 h-4" />
                  </button>
                ) : nextModule ? (
                  <button
                    onClick={() => {
                      setActiveModuleId(nextModule.id);
                      if (nextModule.lessons.length > 0) {
                        setActiveLessonId(nextModule.lessons[0].id);
                      }
                    }}
                    className="px-5 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-dark/90 flex items-center gap-1.5 shadow-zen-subtle"
                  >
                    <span>{t("Sang Học Phần Tiếp Theo", "Next Module")}</span>
                    <ArrowRight className="w-4 h-4" />
                  </button>
                ) : (
                  <div />
                )}
              </div>
            </div>
          ) : (
            <div className="p-8 text-center text-zen-muted text-xs">
              {t("Vui lòng chọn một bài học từ mục lục bên trái.", "Please select a lesson from the directory on the left.")}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
