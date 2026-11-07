"use client";

import React, { useState, useEffect, useMemo } from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import {
  ICF_7_MODULES,
  getCurriculumProgress,
  saveLessonProgress,
  UserLessonProgress
} from "@/lib/curriculumData";
import {
  BookOpen,
  Sparkles,
  Search,
  Flag,
  Bookmark,
  ChevronRight,
  ExternalLink,
  Award,
  Lock,
  CheckCircle2,
  Save,
  Trash2
} from "lucide-react";

export default function JournalPage() {
  const { t } = useLanguage();
  const { user } = useAuth();

  const [curriculumProg, setCurriculumProg] = useState<Record<string, UserLessonProgress>>({});
  const [activeTab, setActiveTab] = useState<"garden" | "notes" | "flagged" | "bookmarks">("garden");
  const [searchQuery, setSearchQuery] = useState("");
  const [editedNotes, setEditedNotes] = useState<Record<string, string>>({});
  const [saveSuccessId, setSaveSuccessId] = useState<string | null>(null);

  // Load progress on mount
  useEffect(() => {
    const prog = getCurriculumProgress();
    setCurriculumProg(prog);
    
    // Initialize edited notes
    const initialNotes: Record<string, string> = {};
    Object.entries(prog).forEach(([k, v]) => {
      if (v.note) initialNotes[k] = v.note;
    });
    setEditedNotes(initialNotes);
  }, [user.id]);

  // Compute lotus count: 1 completed lesson = 1 lotus (awarded once per lesson)
  const lotusCount = useMemo(() => {
    return Object.values(curriculumProg).filter(
      (p) => p.status === "read" || p.status === "quiz_passed"
    ).length;
  }, [curriculumProg]);

  // Build lesson lookup map across all 7 modules
  const lessonLookup = useMemo(() => {
    const map = new Map<string, { moduleId: string; moduleTitleVi: string; moduleTitleEn: string; titleVi: string; titleEn: string; lessonNumber: number }>();
    ICF_7_MODULES.forEach((mod) => {
      mod.lessons.forEach((les) => {
        map.set(les.id, {
          moduleId: mod.id,
          moduleTitleVi: mod.titleVi,
          moduleTitleEn: mod.titleEn,
          titleVi: les.titleVi,
          titleEn: les.titleEn,
          lessonNumber: les.lessonNumber
        });
      });
    });
    return map;
  }, []);

  // Filtered notes
  const notesList = useMemo(() => {
    const list: Array<{ lessonId: string; note: string; metadata?: any }> = [];
    Object.entries(curriculumProg).forEach(([lesId, p]) => {
      if (p.note && p.note.trim()) {
        const meta = lessonLookup.get(lesId);
        if (
          !searchQuery ||
          p.note.toLowerCase().includes(searchQuery.toLowerCase()) ||
          meta?.titleVi.toLowerCase().includes(searchQuery.toLowerCase()) ||
          meta?.titleEn.toLowerCase().includes(searchQuery.toLowerCase())
        ) {
          list.push({ lessonId: lesId, note: p.note, metadata: meta });
        }
      }
    });
    return list;
  }, [curriculumProg, searchQuery, lessonLookup]);

  // Flagged lessons list
  const flaggedList = useMemo(() => {
    const list: Array<{ lessonId: string; progress: UserLessonProgress; metadata?: any }> = [];
    Object.entries(curriculumProg).forEach(([lesId, p]) => {
      if (p.needsReview) {
        list.push({ lessonId: lesId, progress: p, metadata: lessonLookup.get(lesId) });
      }
    });
    return list;
  }, [curriculumProg, lessonLookup]);

  // Save updated note
  const handleSaveNote = (lessonId: string) => {
    const newNote = editedNotes[lessonId] || "";
    saveLessonProgress(lessonId, { note: newNote });
    const updated = getCurriculumProgress();
    setCurriculumProg(updated);
    setSaveSuccessId(lessonId);
    setTimeout(() => setSaveSuccessId(null), 2500);
  };

  // Toggle review flag
  const handleToggleFlag = (lessonId: string) => {
    const current = curriculumProg[lessonId];
    const nextFlag = !current?.needsReview;
    saveLessonProgress(lessonId, { needsReview: nextFlag });
    setCurriculumProg(getCurriculumProgress());
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-6 sm:py-8 space-y-8">
      {/* Header Banner */}
      <section className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card">
        <div className="max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold">
            <BookOpen className="w-3.5 h-3.5 text-zen-moss-dark" />
            <span>{t("Sổ Học Tập • Học Coaching", "Learning Journal • Học Coaching")}</span>
          </div>
          <h1 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink">
            {t("Sổ Học Tập & Vườn Sen Chánh Niệm", "Learning Journal & Mindful Garden")}
          </h1>
          <p className="text-xs sm:text-sm text-zen-muted leading-relaxed">
            {t(
              "Nơi lưu giữ hành trình chuyển hóa thực chất của bạn: Vườn Sen Chánh Niệm, toàn bộ ghi chú học tập có thể tìm kiếm và chỉnh sửa, danh sách bài cần ôn lại và các câu hỏi đã lưu.",
              "A serene sanctuary documenting your genuine progress: Mindful Lotus Garden, searchable personal notes, self-flagged review lessons, and bookmarked questions."
            )}
          </p>
        </div>
      </section>

      {/* Navigation Tabs */}
      <div className="flex flex-wrap items-center gap-2 border-b border-zen-border pb-3">
        <button
          onClick={() => setActiveTab("garden")}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
            activeTab === "garden"
              ? "bg-zen-moss-dark text-white shadow-zen-subtle"
              : "bg-zen-surface text-zen-ink hover:bg-zen-border/40"
          }`}
        >
          <span>🪷 {t("Vườn Sen Chánh Niệm", "Lotus Garden")}</span>
          <span className="px-1.5 py-0.2 rounded-full bg-white/20 text-[11px] font-bold">
            {lotusCount}
          </span>
        </button>

        <button
          onClick={() => setActiveTab("notes")}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
            activeTab === "notes"
              ? "bg-zen-moss-dark text-white shadow-zen-subtle"
              : "bg-zen-surface text-zen-ink hover:bg-zen-border/40"
          }`}
        >
          <span>📝 {t("Ghi Chú Của Tôi", "My Notes")}</span>
          <span className="px-1.5 py-0.2 rounded-full bg-white/20 text-[11px] font-bold">
            {notesList.length}
          </span>
        </button>

        <button
          onClick={() => setActiveTab("flagged")}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
            activeTab === "flagged"
              ? "bg-zen-moss-dark text-white shadow-zen-subtle"
              : "bg-zen-surface text-zen-ink hover:bg-zen-border/40"
          }`}
        >
          <span>🚩 {t("Bài Cần Ôn", "Needs Review")}</span>
          <span className="px-1.5 py-0.2 rounded-full bg-white/20 text-[11px] font-bold">
            {flaggedList.length}
          </span>
        </button>
      </div>

      {/* TAB 1: VƯỜN SEN CHÁNH NIỆM */}
      {activeTab === "garden" && (
        <div className="space-y-6">
          <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-zen-border/60 pb-5">
              <div className="space-y-1">
                <span className="text-xs font-semibold text-zen-wood uppercase tracking-wider block">
                  {t("Thành tựu học tập thực tế", "Verified Study Harvest")}
                </span>
                <h2 className="font-serif text-2xl font-bold text-zen-ink">
                  {t("Bạn đang sở hữu", "You have bloomed")}{" "}
                  <span className="text-zen-moss-dark font-extrabold">{lotusCount}</span>{" "}
                  {t("đóa sen chánh niệm", "mindful lotuses")}
                </h2>
              </div>
              <div className="text-3xl sm:text-4xl">
                {"🪷 ".repeat(Math.min(lotusCount, 10))}
              </div>
            </div>

            <div className="bg-white/90 border border-zen-border rounded-2xl p-4 sm:p-5 space-y-2 text-xs sm:text-sm text-zen-ink/90 leading-relaxed">
              <p>
                📌 <b>{t("Cách nhận sen:", "How to harvest lotuses:")}</b>{" "}
                {t(
                  "Hoàn thành hợp lệ mỗi bài học nhận 1 đóa sen chánh niệm. Mỗi bài chỉ được nhận 1 lần duy nhất, không cộng dồn khi xem lại.",
                  "Complete each study lesson to earn exactly 1 mindful lotus. Awarded only once per lesson; never duplicate."
                )}
              </p>
              <p>
                🌱 <b>{t("Số sen hiện có:", "Current lotuses:")}</b> <b>{lotusCount}</b> {t("đóa sen", "lotuses")}.
              </p>
              <p className="text-zen-wood font-medium">
                🎯 <b>{t("Mốc tiếp theo:", "Next milestone:")}</b>{" "}
                {lotusCount < 3
                  ? t(`Còn thiếu ${3 - lotusCount} sen để mở khóa Mốc 3 sen (Bộ Flashcard)`, `${3 - lotusCount} more lotuses to unlock 3-Lotus Flashcards`)
                  : lotusCount < 8
                  ? t(`Còn thiếu ${8 - lotusCount} sen để mở khóa Mốc 8 sen (Bài ôn theo chủ đề)`, `${8 - lotusCount} more lotuses to unlock 8-Lotus Themed Practice`)
                  : lotusCount < 15
                  ? t(`Còn thiếu ${15 - lotusCount} sen để mở khóa Mốc 15 sen (Thử thách nâng cao)`, `${15 - lotusCount} more lotuses to unlock 15-Lotus Advanced Challenge`)
                  : t("🎉 Bạn đã mở khóa trọn vẹn toàn bộ các mốc thành tựu cao nhất!", "🎉 You have unlocked all highest milestones!")}
              </p>
            </div>
          </div>

          {/* Milestones Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {/* Milestone 3 Sen */}
            <div className="rounded-2xl border border-zen-border bg-white p-5 shadow-zen-card flex flex-col justify-between space-y-4">
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-2xl">🃏</span>
                  <span
                    className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                      lotusCount >= 3 ? "bg-emerald-100 text-emerald-800" : "bg-amber-100 text-amber-800"
                    }`}
                  >
                    {lotusCount >= 3 ? t("Đã mở khóa", "Unlocked") : `${lotusCount}/3 Sen`}
                  </span>
                </div>
                <h3 className="font-serif text-base font-bold text-zen-ink">
                  {t("Mốc 3 Sen: Bộ Flashcard", "3 Lotuses: Core Flashcards")}
                </h3>
                <p className="text-xs text-zen-muted leading-relaxed">
                  {t(
                    "Mở khóa bộ Flashcard 8 Năng lực Cốt lõi và Thuật ngữ then chốt giúp ôn phản xạ nhanh.",
                    "Unlock 8 Core Competencies & Glossary Flashcards for quick recall drills."
                  )}
                </p>
              </div>
              <div className="pt-2">
                {lotusCount >= 3 ? (
                  <Link
                    href="/curriculum?module=mod-7"
                    className="w-full py-2 px-3 rounded-xl bg-zen-moss-dark hover:bg-zen-moss-dark/90 text-white text-xs font-semibold flex items-center justify-center gap-1 transition-all"
                  >
                    <span>{t("Mở Bộ Flashcard", "Open Flashcards")}</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </Link>
                ) : (
                  <button
                    disabled
                    className="w-full py-2 px-3 rounded-xl bg-zen-surface text-zen-muted text-xs font-semibold flex items-center justify-center gap-1 cursor-not-allowed"
                  >
                    <Lock className="w-3.5 h-3.5" />
                    <span>{t(`Cần thêm ${3 - lotusCount} sen`, `Need ${3 - lotusCount} more`)}</span>
                  </button>
                )}
              </div>
            </div>

            {/* Milestone 8 Sen */}
            <div className="rounded-2xl border border-zen-border bg-white p-5 shadow-zen-card flex flex-col justify-between space-y-4">
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-2xl">🎯</span>
                  <span
                    className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                      lotusCount >= 8 ? "bg-emerald-100 text-emerald-800" : "bg-amber-100 text-amber-800"
                    }`}
                  >
                    {lotusCount >= 8 ? t("Đã mở khóa", "Unlocked") : `${lotusCount}/8 Sen`}
                  </span>
                </div>
                <h3 className="font-serif text-base font-bold text-zen-ink">
                  {t("Mốc 8 Sen: Bài Ôn Chủ Đề", "8 Lotuses: Themed Practice")}
                </h3>
                <p className="text-xs text-zen-muted leading-relaxed">
                  {t(
                    "Mở khóa chế độ Luyện 10 câu chuyên sâu tập trung vào Đạo đức và Ranh giới chuyển gửi.",
                    "Unlock Daily 10 Drills focusing deeply on Ethics and Referral Boundaries."
                  )}
                </p>
              </div>
              <div className="pt-2">
                {lotusCount >= 8 ? (
                  <Link
                    href="/daily"
                    className="w-full py-2 px-3 rounded-xl bg-zen-moss-dark hover:bg-zen-moss-dark/90 text-white text-xs font-semibold flex items-center justify-center gap-1 transition-all"
                  >
                    <span>{t("Vào Luyện 10 Câu", "Start Daily Drill")}</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </Link>
                ) : (
                  <button
                    disabled
                    className="w-full py-2 px-3 rounded-xl bg-zen-surface text-zen-muted text-xs font-semibold flex items-center justify-center gap-1 cursor-not-allowed"
                  >
                    <Lock className="w-3.5 h-3.5" />
                    <span>{t(`Cần thêm ${Math.max(0, 8 - lotusCount)} sen`, `Need ${Math.max(0, 8 - lotusCount)} more`)}</span>
                  </button>
                )}
              </div>
            </div>

            {/* Milestone 15 Sen */}
            <div className="rounded-2xl border border-zen-border bg-white p-5 shadow-zen-card flex flex-col justify-between space-y-4">
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-2xl">⚡</span>
                  <span
                    className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                      lotusCount >= 15 ? "bg-emerald-100 text-emerald-800" : "bg-amber-100 text-amber-800"
                    }`}
                  >
                    {lotusCount >= 15 ? t("Đã mở khóa", "Unlocked") : `${lotusCount}/15 Sen`}
                  </span>
                </div>
                <h3 className="font-serif text-base font-bold text-zen-ink">
                  {t("Mốc 15 Sen: Thử Thách Nâng Cao", "15 Lotuses: Advanced Challenge")}
                </h3>
                <p className="text-xs text-zen-muted leading-relaxed">
                  {t(
                    "Mở khóa Phòng thi thử mô phỏng toàn diện 78–80 câu SJT chấm 4 mức điểm quy đổi 200–600.",
                    "Unlock full 78–80 SJT exam simulation with authentic 4-tier grading scaled 200–600."
                  )}
                </p>
              </div>
              <div className="pt-2">
                {lotusCount >= 15 ? (
                  <Link
                    href="/mock-exam"
                    className="w-full py-2 px-3 rounded-xl bg-zen-moss-dark hover:bg-zen-moss-dark/90 text-white text-xs font-semibold flex items-center justify-center gap-1 transition-all"
                  >
                    <span>{t("Vào Thi Thử Mô Phỏng", "Enter Simulator")}</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </Link>
                ) : (
                  <button
                    disabled
                    className="w-full py-2 px-3 rounded-xl bg-zen-surface text-zen-muted text-xs font-semibold flex items-center justify-center gap-1 cursor-not-allowed"
                  >
                    <Lock className="w-3.5 h-3.5" />
                    <span>{t(`Cần thêm ${Math.max(0, 15 - lotusCount)} sen`, `Need ${Math.max(0, 15 - lotusCount)} more`)}</span>
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: GHI CHÚ CỦA TÔI */}
      {activeTab === "notes" && (
        <div className="space-y-4">
          <div className="flex items-center w-full bg-zen-paper rounded-2xl border border-zen-border px-4 py-3 shadow-zen-subtle">
            <Search className="w-4 h-4 text-zen-muted mr-3 shrink-0" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder={t(
                "Tìm kiếm trong toàn bộ ghi chú học tập của bạn...",
                "Search across all your study reflections..."
              )}
              className="w-full bg-transparent text-xs sm:text-sm text-zen-ink placeholder:text-zen-muted/70 focus:outline-none"
            />
          </div>

          {notesList.length === 0 ? (
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-8 text-center space-y-3">
              <p className="text-xs sm:text-sm text-zen-muted">
                {t(
                  "Bạn chưa lưu ghi chú nào trong các bài học lý thuyết.",
                  "You have not saved any personal notes in your lessons yet."
                )}
              </p>
              <Link
                href="/curriculum"
                className="inline-flex items-center gap-1 px-4 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold"
              >
                <span>{t("Đến Lộ trình học ngay", "Explore Curriculum")}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          ) : (
            <div className="space-y-4">
              {notesList.map((item) => (
                <div
                  key={item.lessonId}
                  className="rounded-2xl border border-zen-border bg-white p-5 shadow-zen-card space-y-3"
                >
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-zen-border/40 pb-3">
                    <div>
                      <span className="text-[10px] font-bold uppercase text-zen-wood tracking-wider block">
                        {item.metadata?.moduleTitleVi || "Học phần"}
                      </span>
                      <h3 className="font-serif text-base font-bold text-zen-ink">
                        {item.metadata?.titleVi || item.lessonId}
                      </h3>
                    </div>
                    <Link
                      href={`/curriculum?module=${item.metadata?.moduleId || "mod-1"}&lesson=${item.lessonId}`}
                      className="inline-flex items-center gap-1 text-xs font-semibold text-zen-moss-dark hover:underline self-start sm:self-center"
                    >
                      <span>{t("Quay lại bài gốc", "Jump to Lesson")}</span>
                      <ExternalLink className="w-3 h-3" />
                    </Link>
                  </div>

                  <textarea
                    value={editedNotes[item.lessonId] ?? item.note}
                    onChange={(e) =>
                      setEditedNotes({ ...editedNotes, [item.lessonId]: e.target.value })
                    }
                    rows={3}
                    className="w-full text-xs sm:text-sm text-zen-ink border border-zen-border rounded-xl p-3 focus:outline-none focus:border-zen-moss-dark bg-zen-surface/30"
                  />

                  <div className="flex items-center justify-between pt-1">
                    <span className="text-[11px] text-emerald-700 font-medium">
                      {saveSuccessId === item.lessonId && `✓ ${t("Đã lưu thành công!", "Saved successfully!")}`}
                    </span>
                    <button
                      onClick={() => handleSaveNote(item.lessonId)}
                      className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-dark/90 shadow-zen-subtle transition-all"
                    >
                      <Save className="w-3.5 h-3.5" />
                      <span>{t("Lưu thay đổi", "Save Note")}</span>
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* TAB 3: BÀI CẦN ÔN 🚩 */}
      {activeTab === "flagged" && (
        <div className="space-y-4">
          <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-1">
            <h3 className="font-serif text-lg font-bold text-zen-ink">
              {t("Danh sách bài học tự gắn cờ cần ôn", "Self-Flagged Review Lessons")}
            </h3>
            <p className="text-xs text-zen-muted leading-relaxed">
              {t(
                "Các bài học bạn đã gắn cờ 🚩 'Cần ôn lại'. Trạng thái hoàn thành bài học vẫn được giữ nguyên đầy đủ.",
                "Lessons you marked with a 🚩 review flag. Your completion status remains fully intact."
              )}
            </p>
          </div>

          {flaggedList.length === 0 ? (
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-8 text-center space-y-3">
              <p className="text-xs sm:text-sm text-zen-muted">
                {t(
                  "Hiện chưa có bài học nào được gắn cờ cần ôn.",
                  "No lessons currently flagged for review."
                )}
              </p>
              <Link
                href="/curriculum"
                className="inline-flex items-center gap-1 px-4 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold"
              >
                <span>{t("Xem Lộ trình học", "View Curriculum")}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          ) : (
            <div className="space-y-3">
              {flaggedList.map((item) => (
                <div
                  key={item.lessonId}
                  className="rounded-2xl border border-zen-border bg-white p-5 shadow-zen-card flex flex-col sm:flex-row sm:items-center justify-between gap-4"
                >
                  <div className="space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-100 text-rose-800">
                        🚩 {t("Cần ôn lại", "Review")}
                      </span>
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800">
                        {item.progress.status === "quiz_passed"
                          ? t("Đã đạt kiểm tra", "Quiz Passed")
                          : t("Đã hoàn thành đọc", "Read")}
                      </span>
                    </div>
                    <h4 className="font-serif text-base font-bold text-zen-ink">
                      {item.metadata?.titleVi || item.lessonId}
                    </h4>
                    <p className="text-xs text-zen-muted">
                      {item.metadata?.moduleTitleVi || ""}
                    </p>
                  </div>

                  <div className="flex items-center gap-2 self-end sm:self-center">
                    <Link
                      href={`/curriculum?module=${item.metadata?.moduleId || "mod-1"}&lesson=${item.lessonId}`}
                      className="px-4 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-dark/90 transition-all"
                    >
                      {t("Vào ôn ngay", "Review Now")}
                    </Link>
                    <button
                      onClick={() => handleToggleFlag(item.lessonId)}
                      className="px-3 py-2 rounded-xl border border-zen-border bg-zen-surface hover:bg-zen-border/40 text-zen-ink text-xs font-semibold transition-all"
                    >
                      {t("Bỏ cờ", "Unflag")}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
