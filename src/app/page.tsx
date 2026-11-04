"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import {
  getSections,
  getDailyMindfulnessMessage,
  getLotusGarden,
  LotusGardenState
} from "@/lib/db";
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
  Compass
} from "lucide-react";

export default function HomePage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user, canAccessSection, canAccessPaidContent } = useAuth();

  const [sections, setSections] = useState<Section[]>([]);
  const [dailyMsg, setDailyMsg] = useState<MindfulnessMessage | null>(null);
  const [garden, setGarden] = useState<LotusGardenState>({
    seedsPlanted: 12,
    sproutsGrown: 8,
    lotusesBloomed: 4,
    butterfliesUnlocked: 2,
    dragonfliesUnlocked: 1
  });
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    setSections(getSections());
    setDailyMsg(getDailyMindfulnessMessage());
    setGarden(getLotusGarden(user.id));
  }, [user.id]);

  // Root sections
  const rootSections = sections.filter((s) => !s.parentId).sort((a, b) => a.orderIndex - b.orderIndex);

  // Subsections map
  const getSubsections = (parentId: string) => {
    return sections.filter((s) => s.parentId === parentId).sort((a, b) => a.orderIndex - b.orderIndex);
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-6 sm:py-8 space-y-8">
      {/* 1. Zen Welcome & Daily Mindfulness Card */}
      <section className="relative overflow-hidden rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card transition-all">
        <div className="relative z-10 max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold">
            <Sparkles className="w-3.5 h-3.5 text-zen-ochre" />
            <span>{t("Lời Nhắn Chánh Niệm Trong Ngày", "Daily Mindfulness Reflection")}</span>
          </div>

          <h1 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink leading-tight">
            {t(
              `Chào mừng bạn, ${user.fullName}. Chúc bạn một ngày học tĩnh tại.`,
              `Welcome, ${user.fullName}. May your study today be peaceful.`
            )}
          </h1>

          {dailyMsg && (
            <div className="pt-2">
              <blockquote className="font-serif italic text-base sm:text-lg text-zen-ink/90 pl-4 border-l-2 border-zen-moss leading-relaxed">
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

      {/* 2. Quick Search & Micro-Learning Bar */}
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
          href="/sections/sec-a1-1"
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

      {/* 3. Lotus Garden Progress */}
      <section>
        <LotusGarden garden={garden} streakCount={user.streakCount} />
      </section>

      {/* 4. Full PCC Mock Exam Highlight Card */}
      <section className="relative overflow-hidden rounded-3xl border-2 border-zen-ochre/40 bg-gradient-to-r from-amber-50/70 via-zen-paper to-amber-50/50 p-6 sm:p-8 shadow-zen-card">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
          <div className="space-y-2 max-w-xl">
            <div className="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-zen-ochre/20 text-zen-ochre-dark text-xs font-bold uppercase tracking-wider">
              <Mountain className="w-3.5 h-3.5" />
              <span>{t("Kỳ Thi Mô Phỏng", "Simulation Exam")}</span>
            </div>
            <h3 className="font-serif text-2xl font-bold text-zen-ink">
              {t("Thi Thử Tổng PCC Chuẩn ICF", "Full Standard ICF PCC Mock Exam")}
            </h3>
            <p className="text-xs sm:text-sm text-zen-muted leading-relaxed">
              {t(
                "Đề thi chuẩn Situational Judgment Test (SJT): Mỗi câu chọn 1 phản hồi TỐT NHẤT (BEST) và 1 phản hồi TỆ NHẤT (WORST). Có đồng hồ đếm ngược, chấm điểm và đối chiếu chi tiết.",
                "Authentic SJT exam format: Pick 1 BEST and 1 WORST response per scenario. Features countdown timer, detailed scoring, and rationale breakdown."
              )}
            </p>
          </div>

          <Link
            href="/mock-exam"
            className="shrink-0 px-6 py-3.5 rounded-2xl bg-zen-ochre hover:bg-zen-ochre-dark text-white font-semibold text-xs sm:text-sm shadow-zen-card hover:shadow-zen-floating transition-all flex items-center gap-2"
          >
            <Compass className="w-4 h-4" />
            <span>{t("Bắt đầu thi thử ngay", "Start Mock Exam Now")}</span>
          </Link>
        </div>
      </section>

      {/* 5. Nature-Themed Sections Tree */}
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
