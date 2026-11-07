"use client";

import React, { useState, useEffect, useMemo } from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import {
  getSections,
  getDailyMindfulnessMessage,
  LotusGardenState
} from "@/lib/db";
import {
  ICF_7_MODULES,
  getCurriculumProgress,
  computeModuleProgress,
  computeOverallProgress,
  UserLessonProgress,
  fetchServerProgress
} from "@/lib/curriculumData";
import { Section, MindfulnessMessage } from "@/types";
import LotusGarden from "@/components/LotusGarden";
import NatureIcon from "@/components/NatureIcon";
import {
  Search,
  Sparkles,
  CupSoda,
  ChevronRight,
  Lock,
  CheckCircle2,
  Mountain,
  Compass,
  GraduationCap,
  BookOpen,
  ArrowRight
} from "lucide-react";

export default function HomePage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user, isAuthenticated, loading, canAccessSection } = useAuth();

  const [sections, setSections] = useState<Section[]>([]);
  const [dailyMsg, setDailyMsg] = useState<MindfulnessMessage | null>(null);
  const [curriculumProg, setCurriculumProg] = useState<Record<string, UserLessonProgress>>({});
  const [garden, setGarden] = useState<LotusGardenState>({
    seedsPlanted: 0,
    sproutsGrown: 0,
    lotusesBloomed: 0,
    butterfliesUnlocked: 0,
    dragonfliesUnlocked: 0
  });
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    setSections(getSections());
    setDailyMsg(getDailyMindfulnessMessage());
    
    if (isAuthenticated && user?.id && user.id !== "guest") {
      fetchServerProgress().then((res) => {
        if (res.success) {
          setCurriculumProg(res.progress);
          const readLessons = Object.values(res.progress).filter((p) => p.status === "read" || p.status === "quiz_passed").length;
          const realBloomed = res.lotusBloomed;

          setGarden({
            seedsPlanted: Math.max(0, 26 - readLessons),
            sproutsGrown: readLessons,
            lotusesBloomed: realBloomed,
            butterfliesUnlocked: Math.floor(realBloomed / 2),
            dragonfliesUnlocked: Math.floor(realBloomed / 4)
          });
        }
      });
    } else {
      // Guest state: Clean 0 lotus, clean progress
      setCurriculumProg({});
      setGarden({
        seedsPlanted: 26,
        sproutsGrown: 0,
        lotusesBloomed: 0,
        butterfliesUnlocked: 0,
        dragonfliesUnlocked: 0
      });
    }
  }, [user.id, isAuthenticated]);

  // Overall stats for 7 ICF modules
  const overallStats = useMemo(() => computeOverallProgress(curriculumProg), [curriculumProg]);

  // Root sections
  const rootSections = sections.filter((s) => !s.parentId).sort((a, b) => a.orderIndex - b.orderIndex);

  // Subsections map
  const getSubsections = (parentId: string) => {
    return sections.filter((s) => s.parentId === parentId).sort((a, b) => a.orderIndex - b.orderIndex);
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-6 sm:py-8 space-y-8">
      {/* 1. Zen Welcome & Hero Section */}
      <section className="relative overflow-hidden rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-10 shadow-zen-card transition-all">
        <div className="relative z-10 max-w-3xl space-y-4">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs sm:text-sm font-semibold">
            <Sparkles className="w-4 h-4 text-zen-ochre" />
            <span>{t("Học Coaching", "Học Coaching")}</span>
          </div>

          <h1 className="font-serif text-3xl sm:text-4xl lg:text-[2.65rem] font-bold text-zen-ink leading-tight">
            {t(
              "Đưa coaching trở thành lối sống",
              "Making coaching a way of life"
            )}
          </h1>

          <p className="text-base sm:text-lg text-zen-wood leading-relaxed font-sans">
            {t(
              "Cùng Coach Thanh Huyền học cách lắng nghe sâu hơn, đặt câu hỏi với sự tò mò và mang tinh thần khai vấn vào công việc, gia đình và những cuộc trò chuyện mỗi ngày.",
              "With Coach Thanh Huyen, learn to listen deeper, ask questions with curiosity, and bring the coaching spirit into work, family, and daily conversations."
            )}
          </p>

          {/* Action Buttons */}
          <div className="pt-2 flex flex-wrap items-center gap-3">
            <a
              href="#curriculum-pathway"
              className="px-6 py-3 rounded-xl bg-zen-moss-dark hover:bg-zen-moss-dark/90 text-white text-sm sm:text-base font-semibold shadow-zen-subtle transition-all flex items-center gap-2"
            >
              <span>
                {overallStats.completedLessons > 0
                  ? t("Tiếp tục học →", "Continue Learning →")
                  : t("Khám phá lộ trình học →", "Explore Curriculum Pathway →")}
              </span>
            </a>
            <a
              href="#exam-section"
              className="px-6 py-3 rounded-xl border border-zen-border bg-zen-surface hover:bg-zen-border/40 text-zen-ink text-sm sm:text-base font-semibold transition-all flex items-center gap-2"
            >
              <span>{t("Luyện thi ICF Credentialing", "ICF Credentialing Prep")}</span>
            </a>
          </div>

          {dailyMsg && (
            <div className="pt-3 border-t border-zen-border/50 mt-4">
              <blockquote className="font-serif italic text-sm sm:text-base text-zen-ink/85 pl-4 border-l-2 border-zen-moss leading-relaxed">
                “{t(dailyMsg.textVi, dailyMsg.textEn)}”
              </blockquote>
              <div className="flex items-center gap-3 mt-2 text-xs text-zen-muted pl-4">
                <span className="font-medium text-zen-wood">• {dailyMsg.theme}</span>
                <span>— {dailyMsg.author || "ICF Presence"}</span>
                <button
                  onClick={ringBell}
                  className="text-zen-moss-dark hover:underline flex items-center gap-1 font-medium"
                >
                  🔔 {t("Thỉnh chuông lắng tâm", "Sound bell")}
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Subtle Background Lotus Pattern */}
        <div className="absolute right-4 bottom-2 text-7xl select-none opacity-10 pointer-events-none">
          🪷
        </div>
      </section>

      {/* 2. KHỐI LỘ TRÌNH HỌC TÀI LIỆU ICF (7 HỌC PHẦN THEO ĐÚNG THỨ TỰ) */}
      <section id="curriculum-pathway" className="space-y-4">
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card space-y-6">
          {/* Header & Overall Progress */}
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 border-b border-zen-border/60 pb-6">
            <div className="space-y-2 max-w-2xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold">
                <GraduationCap className="w-3.5 h-3.5 text-zen-moss-dark" />
                <span>{t("Lộ Trình Học Tập Tỉnh Thức Chuẩn ICF", "Official ICF Document Pathway")}</span>
              </div>
              <h2 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink">
                {t("Lộ trình học tài liệu ICF", "ICF Document Curriculum Pathway")}
              </h2>
              <p className="text-xs sm:text-sm text-zen-muted leading-relaxed">
                {t(
                  "Học tuần tự 7 nhóm tài liệu chuẩn hóa từ ICF. Hiểu sâu chuẩn mực — Vững vàng phán đoán — Phát triển năng lực coaching.",
                  "Master all 7 official ICF document sets in strict sequence. Master standards — Hone judgment — Elevate coaching."
                )}
              </p>
              <p className="text-[11px] text-zen-wood italic">
                * {t(
                  "Bản dịch phục vụ học tập, không phải bản dịch chính thức của ICF. Phân định rõ ràng giữa quy chuẩn chính thức và phần diễn giải học tập.",
                  "Educational study translation; not an official ICF translation. Clear distinction between official standards and pedagogical commentary."
                )}
              </p>
            </div>

            {/* Overall Progress Box */}
            <div className="bg-white/90 border border-zen-border rounded-2xl p-5 shrink-0 min-w-[240px] text-center shadow-zen-subtle space-y-2.5">
              <span className="text-xs text-zen-muted font-medium block">
                {t("Tiến độ tổng thể 7 học phần", "Overall 7-Module Progress")}
              </span>
              <div className="flex items-center justify-center gap-2">
                <span className="font-serif text-3xl font-bold text-zen-moss-dark">
                  {overallStats.overallPercent}%
                </span>
                <span className="text-xs text-zen-ink/70">
                  ({overallStats.completedLessons}/{overallStats.totalLessons} {t("bài xong", "done")})
                </span>
              </div>
              <div className="w-full h-2 rounded-full bg-zen-surface overflow-hidden">
                <div
                  className="h-full bg-zen-moss-dark transition-all duration-300"
                  style={{ width: `${overallStats.overallPercent}%` }}
                />
              </div>
              <Link
                href="/curriculum"
                className="inline-flex items-center justify-center w-full px-4 py-2.5 rounded-xl bg-zen-moss-dark hover:bg-zen-moss-dark/90 text-white text-xs font-semibold shadow-zen-subtle transition-all mt-1"
              >
                {overallStats.completedLessons > 0
                  ? t("Tiếp tục học lộ trình →", "Continue Pathway →")
                  : t("Bắt đầu học từ Bài 1 →", "Start from Lesson 1 →")}
              </Link>
            </div>
          </div>

          {/* 7 Modules Grid in Exact Strict Order */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {ICF_7_MODULES.map((mod, index) => {
              const stats = computeModuleProgress(mod.id, curriculumProg);
              const hasStarted = stats.completed > 0;
              const isCompleted = stats.percent === 100;

              return (
                <div
                  key={mod.id}
                  className="rounded-2xl border border-zen-border/80 bg-white p-5 flex flex-col justify-between hover:shadow-zen-floating transition-all group"
                >
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span className="w-7 h-7 rounded-lg bg-zen-moss/10 text-zen-moss-dark font-mono font-bold text-xs flex items-center justify-center">
                          0{index + 1}
                        </span>
                        <span className="text-xl">{mod.icon}</span>
                      </div>
                      <span
                        className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${
                          isCompleted
                            ? "bg-emerald-100 text-emerald-800"
                            : hasStarted
                            ? "bg-amber-100 text-amber-800"
                            : "bg-zen-surface text-zen-muted"
                        }`}
                      >
                        {isCompleted
                          ? t("Đã xong", "Completed")
                          : hasStarted
                          ? t("Đang học", "In Progress")
                          : t("Chưa học", "Not Started")}
                      </span>
                    </div>

                    <div>
                      <h3 className="font-serif text-base font-bold text-zen-ink group-hover:text-zen-moss-dark transition-colors line-clamp-1">
                        {t(
                          mod.titleVi.split(":")[1]?.trim() || mod.titleVi,
                          mod.titleEn.split(":")[1]?.trim() || mod.titleEn
                        )}
                      </h3>
                      <p className="text-xs text-zen-muted line-clamp-2 mt-1 leading-relaxed">
                        {t(mod.summaryVi, mod.summaryEn)}
                      </p>
                    </div>

                    <div className="space-y-1.5 pt-2 border-t border-zen-border/50 text-[11px]">
                      <div className="flex items-center justify-between text-zen-wood">
                        <span className="font-medium">
                          {mod.id === "mod-7"
                            ? t("12 Thuật ngữ + Flashcard + Bài tập", "12 Terms + Flashcards + Drills")
                            : t(`${mod.lessons.length} bài học có nội dung`, `${mod.lessons.length} lessons with content`)}
                        </span>
                        <span className="font-bold text-zen-moss-dark">{stats.percent}%</span>
                      </div>
                      <div className="w-full h-1.5 rounded-full bg-zen-surface overflow-hidden">
                        <div
                          className="h-full bg-zen-moss transition-all duration-300"
                          style={{ width: `${stats.percent}%` }}
                        />
                      </div>
                    </div>
                  </div>

                  <div className="pt-4 mt-2">
                    <Link
                      href={isAuthenticated ? `/curriculum?module=${mod.id}` : `/login?returnUrl=${encodeURIComponent(`/curriculum?module=${mod.id}`)}`}
                      className="w-full py-2 px-3 rounded-xl border border-zen-border bg-zen-surface/60 hover:bg-zen-moss-dark hover:text-white hover:border-zen-moss-dark text-zen-ink text-xs font-semibold flex items-center justify-center gap-1.5 transition-all shadow-zen-subtle"
                    >
                      <span>{hasStarted ? t("Tiếp tục học", "Continue") : t("Bắt đầu học", "Start Learning")}</span>
                      <ChevronRight className="w-3.5 h-3.5" />
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Về Coach Thanh Huyền */}
      <section className="rounded-3xl border border-zen-border bg-gradient-to-br from-zen-paper via-white to-zen-paper p-6 sm:p-8 shadow-zen-card overflow-hidden relative">
        <div className="flex flex-col md:flex-row items-center md:items-start gap-6 sm:gap-8">
          <div className="relative shrink-0 w-full md:w-auto flex justify-center md:justify-start">
            <div className="w-full max-w-[320px] sm:max-w-[360px] md:w-[320px] lg:w-[350px] aspect-[1024/814] rounded-2xl overflow-hidden border-2 border-zen-moss/40 shadow-zen-card bg-zen-surface">
              <img
                src="/images/coach_thanh_huyen.jpg"
                alt="Coach Thanh Huyền - ICF PCC Coach | EQ Trainer"
                className="w-full h-full object-cover object-center"
              />
            </div>
          </div>
          
          <div className="space-y-3.5 text-center md:text-left flex-1">
            <div className="space-y-1">
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold">
                <span>🌱 {t("Người Sáng Lập & Đồng Hành", "Founder & Companion")}</span>
              </div>
              <h3 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink">
                Coach Thanh Huyền
              </h3>
              <p className="text-xs sm:text-sm font-semibold text-zen-wood">
                ICF PCC Coach | EQ Trainer
              </p>
            </div>

            <blockquote className="font-serif italic text-sm sm:text-base text-zen-ink/90 border-l-0 md:border-l-2 md:border-zen-moss md:pl-4 leading-relaxed">
              “{t(
                "Tôi tạo Học Coaching vì muốn đưa coaching vào những cuộc trò chuyện hằng ngày. Khi biết dừng lại để lắng nghe, hỏi thêm trước khi vội kết luận và dành cho người đối diện khoảng trống để tự suy nghĩ, chúng ta có thể hiểu mình và hiểu nhau hơn. Tôi mong những gì bạn học ở đây sẽ theo bạn ra ngoài phiên khai vấn, vào công việc và những mối quan hệ quan trọng với bạn.",
                "I created Học Coaching to bring coaching into everyday conversations. When we pause to listen, ask with curiosity before jumping to conclusions, and give others the space to think for themselves, we understand ourselves and one another more deeply. I hope what you learn here stays with you beyond coaching sessions, into your work and meaningful relationships."
              )}”
            </blockquote>

            <div className="pt-2 flex flex-wrap items-center justify-center md:justify-start gap-3">
              <Link
                href={isAuthenticated ? "/curriculum" : "/login?returnUrl=/curriculum"}
                className="px-5 py-2.5 rounded-xl bg-zen-moss-dark hover:bg-zen-moss-dark/90 text-white text-xs sm:text-sm font-semibold shadow-zen-subtle transition-all"
              >
                {overallStats.completedLessons > 0
                  ? t("Tiếp tục học lộ trình →", "Continue Pathway →")
                  : t("Bắt đầu học ngay →", "Start Learning Now →")}
              </Link>
              <Link
                href="/mock-exam"
                className="px-5 py-2.5 rounded-xl border border-zen-border bg-zen-surface hover:bg-zen-border/40 text-zen-ink text-xs sm:text-sm font-semibold transition-all"
              >
                {t("Luyện thi ICF Credentialing", "ICF Credentialing Prep")}
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* 3. Quick Search & Micro-Learning Bar */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Quick Search */}
        <div className="md:col-span-2 relative">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              if (searchQuery.trim()) {
                window.location.href = `/search?q=${encodeURIComponent(searchQuery)}`;
              }
            }}
            className="flex items-center w-full bg-zen-paper rounded-2xl border border-zen-border px-4 py-3 shadow-zen-subtle focus-within:border-zen-moss-dark transition-all"
          >
            <Search className="w-4 h-4 text-zen-muted mr-3 shrink-0" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder={t(
                "Tra cứu nhanh thuật ngữ, mẹo ghi nhớ, đạo đức (gõ tiếng Việt không dấu)...",
                "Quick search terms, mnemonics, ethics, competencies..."
              )}
              className="w-full bg-transparent text-sm text-zen-ink placeholder:text-zen-muted/70 focus:outline-none"
            />
            <button
              type="submit"
              className="ml-2 px-3 py-1 rounded-xl bg-zen-moss/20 text-zen-moss-dark text-xs font-semibold hover:bg-zen-moss/30 transition-colors shrink-0"
            >
              {t("Tìm", "Search")}
            </button>
          </form>
        </div>

        {/* Micro-learning: "Một tách trà học" */}
        <Link
          href="/curriculum?module=mod-1"
          className="flex items-center justify-between p-3.5 rounded-2xl border border-zen-border bg-zen-surface hover:bg-zen-surface/80 text-zen-ink transition-all shadow-zen-subtle group"
        >
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-zen-wood/15 text-zen-wood flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
              <CupSoda className="w-5 h-5" />
            </div>
            <div>
              <span className="text-xs font-bold text-zen-ink block">
                {t("Một Tách Trà Học", "One Cup of Tea")}
              </span>
              <span className="text-[11px] text-zen-muted">
                {t("12 phút học chánh niệm", "12 min micro session")}
              </span>
            </div>
          </div>
          <ChevronRight className="w-4 h-4 text-zen-muted group-hover:translate-x-0.5 transition-transform" />
        </Link>
      </section>

      {/* 4. Lotus Garden Progress (Connected to Genuine Accomplishments) */}
      <section>
        <LotusGarden garden={garden} streakCount={user.streakCount} />
      </section>

      {/* 5. KHU VỰC: LUYỆN THI ICF CREDENTIALING */}
      <section id="exam-section" className="space-y-4">
        <div className="rounded-3xl border-2 border-zen-ochre/40 bg-gradient-to-r from-amber-50/70 via-zen-paper to-amber-50/50 p-6 sm:p-8 shadow-zen-card space-y-6">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-zen-border/60 pb-5">
            <div className="space-y-1.5 max-w-2xl">
              <div className="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-zen-ochre/20 text-zen-ochre-dark text-xs font-bold uppercase tracking-wider">
                <Mountain className="w-3.5 h-3.5" />
                <span>{t("Kỳ Thi ICF Credentialing Exam", "ICF Credentialing Exam")}</span>
              </div>
              <h3 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink">
                {t("Luyện thi ICF Credentialing", "ICF Credentialing Exam Prep")}
              </h3>
              <p className="text-xs sm:text-sm text-zen-muted leading-relaxed">
                {t(
                  "Dành cho cả ứng viên ACC và PCC. Nội dung phản ánh cấu trúc kỳ thi ICF Credentialing Exam hiện hành: Situational Judgment Test (SJT) chọn 1 BEST và 1 WORST, thang điểm 200–600 (ngưỡng đỗ 460).",
                  "For both ACC and PCC candidates. Fully aligns with current ICF Credentialing Exam standards: SJT 1 BEST & 1 WORST, scaled 200–600 (passing score 460)."
                )}
              </p>
            </div>
            <Link
              href="/mock-exam"
              className="shrink-0 px-5 py-3 rounded-2xl bg-zen-ochre hover:bg-zen-ochre-dark text-white font-semibold text-xs sm:text-sm shadow-zen-card hover:shadow-zen-floating transition-all flex items-center justify-center gap-2"
            >
              <Compass className="w-4 h-4" />
              <span>{t("Vào phòng thi thử ngay", "Enter Exam Room")}</span>
            </Link>
          </div>

          {/* 3 Entry points */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Link
              href="/daily"
              className="p-5 rounded-2xl bg-white border border-zen-border/80 hover:border-zen-ochre hover:shadow-zen-subtle transition-all flex flex-col justify-between group"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xl">⚡</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800">
                    {t("Hàng ngày", "Daily")}
                  </span>
                </div>
                <h4 className="font-serif text-base font-bold text-zen-ink group-hover:text-zen-ochre-dark transition-colors">
                  {t("Luyện 10 câu / ngày", "Daily 10 Drill")}
                </h4>
                <p className="text-xs text-zen-muted leading-relaxed">
                  {t(
                    "Rèn luyện phán đoán không lặp câu: 10 tình huống Best/Worst hoặc câu hỏi kiến thức có phản hồi tức thì.",
                    "Non-repeating drill: 10 Best/Worst SJT items or knowledge questions with instant feedback."
                  )}
                </p>
              </div>
              <div className="pt-3 mt-2 border-t border-zen-border/40 text-xs font-semibold text-zen-ochre-dark flex items-center gap-1">
                <span>{t("Vào luyện ngay", "Start Drill")}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </div>
            </Link>

            <Link
              href="/official-samples"
              className="p-5 rounded-2xl bg-white border border-zen-border/80 hover:border-zen-moss hover:shadow-zen-subtle transition-all flex flex-col justify-between group"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xl">📑</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800">
                    {t("Đề gốc", "Official")}
                  </span>
                </div>
                <h4 className="font-serif text-base font-bold text-zen-ink group-hover:text-zen-moss-dark transition-colors">
                  {t("8 câu mẫu ICF", "8 Official Samples")}
                </h4>
                <p className="text-xs text-zen-muted leading-relaxed">
                  {t(
                    "8 tình huống nguyên bản tiếng Anh có đáp án công bố trên website ICF, song ngữ và phân tích đa chiều.",
                    "8 authentic English scenarios with official answer key published on the ICF website."
                  )}
                </p>
              </div>
              <div className="pt-3 mt-2 border-t border-zen-border/40 text-xs font-semibold text-zen-moss-dark flex items-center gap-1">
                <span>{t("Khảo sát đề gốc", "View Samples")}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </div>
            </Link>

            <Link
              href="/mock-exam"
              className="p-5 rounded-2xl bg-white border border-zen-border/80 hover:border-zen-ochre hover:shadow-zen-subtle transition-all flex flex-col justify-between group"
            >
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-xl">⚖️</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-purple-100 text-purple-800">
                    {t("Mô phỏng", "Simulator")}
                  </span>
                </div>
                <h4 className="font-serif text-base font-bold text-zen-ink group-hover:text-zen-ochre-dark transition-colors">
                  {t("Thi thử mô phỏng", "Mock Simulator")}
                </h4>
                <p className="text-xs text-zen-muted leading-relaxed">
                  {t(
                    "Mô phỏng sát thực tế: Cấu hình 78 SJT (180p) hoặc 80 câu 4 phần (150p). Chấm 4 mức điểm quy đổi 200–600.",
                    "Authentic simulation: 78 SJT (180m) or 80 items (150m). Timed, 4-tier grading scaled 200–600."
                  )}
                </p>
              </div>
              <div className="pt-3 mt-2 border-t border-zen-border/40 text-xs font-semibold text-zen-ochre-dark flex items-center gap-1">
                <span>{t("Vào thi thử", "Enter Simulator")}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </div>
            </Link>
          </div>
        </div>
      </section>

      {/* 6. Nature-Themed Sections Tree */}
      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="font-serif text-xl sm:text-2xl font-bold text-zen-ink">
              {t("Lộ Trình Học Tập 8 Năng Lực", "8 Core Competencies Path")}
            </h2>
            <p className="text-xs text-zen-muted mt-0.5">
              {t(
                "Chọn từng mục để khám phá 6 tab chuyên sâu: Lý thuyết, Keyword, Flashcard, Case study, Quiz và Thi thử",
                "Explore in-depth 6 tabs per section: Theory, Keywords, Flashcards, Case studies, Quizzes, and Mock exams"
              )}
            </p>
          </div>

          <Link
            href="/mock-exam"
            className="text-xs font-semibold text-zen-moss-dark hover:underline flex items-center gap-1"
          >
            <span>{t("Xem tất cả", "View all")}</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </Link>
        </div>

        {/* Tree Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {rootSections.map((sec) => {
            const children = getSubsections(sec.id);
            const hasAccess = canAccessSection(sec);

            return (
              <div
                key={sec.id}
                className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col justify-between"
              >
                <div>
                  {/* Section Header */}
                  <div className="flex items-center justify-between mb-3">
                    <div className="flex items-center gap-2.5">
                      <div className="w-9 h-9 rounded-2xl bg-zen-moss/15 text-zen-moss-dark flex items-center justify-center">
                        <NatureIcon icon={sec.natureIcon} size={18} />
                      </div>
                      <span className="text-xs font-bold uppercase tracking-wider text-zen-moss-dark">
                        {sec.code}
                      </span>
                    </div>

                    {sec.isFree ? (
                      <span className="px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-700 text-[11px] font-semibold border border-emerald-200">
                        {t("Miễn phí", "Free")}
                      </span>
                    ) : !hasAccess ? (
                      <span className="flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-700 text-[11px] font-semibold border border-amber-200">
                        <Lock className="w-3 h-3" />
                        {t("Khóa (Gói trả phí)", "Locked")}
                      </span>
                    ) : (
                      <span className="flex items-center gap-1 text-[11px] text-zen-moss-dark font-medium">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                        {t("Đã mở khóa", "Unlocked")}
                      </span>
                    )}
                  </div>

                  <h3 className="font-serif text-lg font-bold text-zen-ink mb-1.5">
                    {t(sec.titleVi, sec.titleEn)}
                  </h3>
                  <p className="text-xs text-zen-muted leading-relaxed line-clamp-2 mb-4">
                    {t(sec.descriptionVi, sec.descriptionEn)}
                  </p>

                  {/* Subsections List */}
                  {children.length > 0 && (
                    <div className="space-y-2 pt-3 border-t border-zen-border/50">
                      <span className="text-[10px] font-bold uppercase text-zen-muted tracking-wider block">
                        {t("Các bài học chuyên đề:", "Topics & Sub-competencies:")}
                      </span>
                      {children.map((sub) => {
                        const leafChildren = getSubsections(sub.id);
                        const targetId = leafChildren.length > 0 ? leafChildren[0].id : sub.id;

                        return (
                          <Link
                            key={sub.id}
                            href={`/sections/${targetId}`}
                            className="flex items-center justify-between p-2.5 rounded-xl bg-zen-surface/60 hover:bg-zen-surface text-xs font-medium text-zen-ink transition-colors group/item"
                          >
                            <div className="flex items-center gap-2">
                              <span className="text-zen-moss-dark font-bold font-mono text-[11px]">
                                {sub.code}
                              </span>
                              <span className="line-clamp-1">{t(sub.titleVi, sub.titleEn)}</span>
                            </div>
                            <ChevronRight className="w-3.5 h-3.5 text-zen-muted group-hover/item:translate-x-0.5 transition-transform" />
                          </Link>
                        );
                      })}
                    </div>
                  )}
                </div>

                {/* Footer action */}
                <div className="mt-5 pt-3 border-t border-zen-border/40 flex items-center justify-between text-xs">
                  <span className="text-zen-muted">
                    {children.length} {t("chủ đề nhánh", "sub-topics")}
                  </span>
                  <Link
                    href={`/sections/${children[0]?.id || sec.id}`}
                    className="text-zen-moss-dark font-semibold hover:underline flex items-center gap-1"
                  >
                    <span>{t("Vào học ngay", "Start Lesson")}</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}
