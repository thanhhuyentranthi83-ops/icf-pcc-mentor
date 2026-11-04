"use client";

import React, { useState, useEffect } from "react";
import { QuizQuestion } from "@/types";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import { saveExamSession, updateLotusGarden } from "@/lib/db";
import {
  Clock,
  Pause,
  Play,
  CheckCircle,
  XCircle,
  Award,
  AlertTriangle,
  RotateCcw,
  Sparkles,
  ChevronRight,
  ChevronLeft
} from "lucide-react";

interface Props {
  questions: QuizQuestion[];
  examTitleVi: string;
  examTitleEn: string;
  examType: "section_mock" | "full_pcc_mock";
  sectionId?: string | null;
  durationMinutes?: number;
}

interface UserChoice {
  best?: string;
  worst?: string;
}

export default function SjtExamRunner({
  questions,
  examTitleVi,
  examTitleEn,
  examType,
  sectionId,
  durationMinutes = 30
}: Props) {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user } = useAuth();

  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, UserChoice>>({});
  const [secondsRemaining, setSecondsRemaining] = useState(durationMinutes * 60);
  const [isPaused, setIsPaused] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  // Timer
  useEffect(() => {
    if (isSubmitted || isPaused) return;

    const timer = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [isSubmitted, isPaused]);

  if (!questions.length) {
    return (
      <div className="p-8 text-center text-zen-muted text-sm bg-zen-paper rounded-2xl border border-zen-border">
        {t("Chưa có câu hỏi thi thử", "No exam questions available")}
      </div>
    );
  }

  const current = questions[currentIndex];
  const curAnswer = answers[current.id] || {};

  const handleSelectBest = (key: string) => {
    if (isSubmitted) return;
    setAnswers((prev) => {
      const existing = prev[current.id] || {};
      // If was selected as worst, clear worst
      const updatedWorst = existing.worst === key ? undefined : existing.worst;
      const updatedBest = existing.best === key ? undefined : key;
      return { ...prev, [current.id]: { ...existing, best: updatedBest, worst: updatedWorst } };
    });
  };

  const handleSelectWorst = (key: string) => {
    if (isSubmitted) return;
    setAnswers((prev) => {
      const existing = prev[current.id] || {};
      // If was selected as best, clear best
      const updatedBest = existing.best === key ? undefined : existing.best;
      const updatedWorst = existing.worst === key ? undefined : key;
      return { ...prev, [current.id]: { ...existing, best: updatedBest, worst: updatedWorst } };
    });
  };

  const handleSubmit = () => {
    setIsSubmitted(true);
    ringBell();

    // Calculate score
    let bestCorrect = 0;
    let worstCorrect = 0;
    questions.forEach((q) => {
      const userAns = answers[q.id];
      if (userAns?.best && userAns.best === q.bestAnswer) bestCorrect++;
      if (userAns?.worst && userAns.worst === q.worstAnswer) worstCorrect++;
    });

    const totalPoints = bestCorrect + worstCorrect;
    const maxPoints = questions.length * 2;
    const finalScore = Number(((totalPoints / maxPoints) * 100).toFixed(1));

    // Save session
    saveExamSession({
      id: `exam-${Date.now()}`,
      userId: user.id,
      examType,
      sectionId,
      score: finalScore,
      totalQuestions: questions.length,
      correctBestCount: bestCorrect,
      correctWorstCount: worstCorrect,
      durationSeconds: durationMinutes * 60 - secondsRemaining,
      answers,
      completedAt: new Date().toISOString()
    });

    // Water the lotus garden!
    updateLotusGarden(user.id, (prev) => ({
      lotusesBloomed: prev.lotusesBloomed + 1,
      seedsPlanted: prev.seedsPlanted + 2
    }));
  };

  const handleRetake = () => {
    setAnswers({});
    setCurrentIndex(0);
    setSecondsRemaining(durationMinutes * 60);
    setIsPaused(false);
    setIsSubmitted(false);
  };

  // Format time
  const formatTime = (secs: number) => {
    const mins = Math.floor(secs / 60);
    const s = secs % 60;
    return `${mins.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
  };

  // Score Calculation for review
  let bestCorrectCount = 0;
  let worstCorrectCount = 0;
  if (isSubmitted) {
    questions.forEach((q) => {
      const userAns = answers[q.id];
      if (userAns?.best && userAns.best === q.bestAnswer) bestCorrectCount++;
      if (userAns?.worst && userAns.worst === q.worstAnswer) worstCorrectCount++;
    });
  }

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Exam Header Banner */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-5 sm:p-6 shadow-zen-card flex flex-wrap items-center justify-between gap-4">
        <div>
          <span className="text-[11px] font-bold uppercase tracking-wider text-zen-ochre-dark bg-zen-ochre/15 px-2.5 py-1 rounded-full">
            {t("Đề thi mô phỏng chuẩn ICF (Situational Judgment)", "Standard ICF Situational Judgment Test")}
          </span>
          <h2 className="font-serif text-xl sm:text-2xl font-bold text-zen-ink mt-1.5">
            {t(examTitleVi, examTitleEn)}
          </h2>
          <p className="text-xs text-zen-muted mt-0.5">
            {t(
              "Chọn 1 phương án TỐT NHẤT (BEST) và 1 phương án TỆ NHẤT (WORST) cho mỗi tình huống",
              "Choose one BEST response and one WORST response for each scenario"
            )}
          </p>
        </div>

        {/* Timer & Controls */}
        {!isSubmitted && (
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2 bg-zen-surface px-4 py-2 rounded-2xl border border-zen-border text-zen-ink font-mono text-sm font-bold shadow-zen-subtle">
              <Clock className="w-4 h-4 text-zen-moss-dark" />
              <span>{formatTime(secondsRemaining)}</span>
            </div>
            <button
              onClick={() => setIsPaused(!isPaused)}
              title={isPaused ? t("Tiếp tục làm bài", "Resume") : t("Tạm dừng chánh niệm", "Mindful Pause")}
              className="p-2 rounded-2xl border border-zen-border bg-zen-paper hover:bg-zen-surface text-zen-ink transition-colors shadow-zen-subtle"
            >
              {isPaused ? <Play className="w-4 h-4 text-emerald-600" /> : <Pause className="w-4 h-4 text-zen-muted" />}
            </button>
          </div>
        )}
      </div>

      {/* Paused Overlay */}
      {isPaused && (
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-8 text-center space-y-3">
          <Sparkles className="w-8 h-8 text-zen-ochre mx-auto animate-pulse" />
          <h3 className="font-serif text-xl font-bold text-zen-ink">
            {t("Khoảng Lặng Chánh Niệm", "Mindful Pause")}
          </h3>
          <p className="text-xs text-zen-muted max-w-sm mx-auto">
            {t(
              "Đồng hồ đã tạm dừng. Bạn có thể uống một ngụm trà, hít thở sâu để hồi phục năng lượng.",
              "Timer is paused. Take a sip of warm tea, breathe deeply to restore calm presence."
            )}
          </p>
          <button
            onClick={() => setIsPaused(false)}
            className="mt-4 px-6 py-2.5 rounded-2xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-colors shadow-zen-subtle"
          >
            {t("Tiếp tục làm bài", "Resume Exam")}
          </button>
        </div>
      )}

      {/* Main Exam Area */}
      {!isPaused && (
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          {/* Question View (Left 3 cols) */}
          <div className="lg:col-span-3 space-y-6">
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card">
              {/* Question Header */}
              <div className="flex items-center justify-between text-xs text-zen-muted pb-3 mb-4 border-b border-zen-border/50">
                <span className="font-semibold text-zen-ink">
                  {t("Tình huống", "Scenario")} {currentIndex + 1} / {questions.length} (
                  {current.id})
                </span>
                <span className="text-[11px] text-zen-moss-dark font-medium">
                  {current.primaryCompetency || t("Chuẩn đạo đức & Năng lực ICF", "ICF Ethics & Competencies")}
                </span>
              </div>

              {/* Scenario Narrative */}
              <div className="bg-zen-surface/60 rounded-2xl p-5 border border-zen-border/60 mb-6">
                <p className="font-serif text-sm sm:text-base text-zen-ink leading-relaxed">
                  {t(current.questionVi, current.questionEn)}
                </p>
              </div>

              {/* SJT Instruction Notice */}
              <div className="flex items-center justify-between px-2 py-1 text-xs text-zen-muted font-medium mb-3">
                <span>{t("Chọn phản hồi cho tình huống:", "Select your responses:")}</span>
                <div className="flex items-center gap-4 text-[11px]">
                  <span className="text-emerald-700 font-semibold flex items-center gap-1">
                    <span className="w-2.5 h-2.5 rounded-full bg-emerald-500" />
                    BEST: {t("Tốt nhất", "Best")}
                  </span>
                  <span className="text-rose-700 font-semibold flex items-center gap-1">
                    <span className="w-2.5 h-2.5 rounded-full bg-rose-500" />
                    WORST: {t("Tệ nhất", "Worst")}
                  </span>
                </div>
              </div>

              {/* Options List */}
              <div className="space-y-3">
                {current.options.map((opt) => {
                  const isBest = curAnswer.best === opt.key;
                  const isWorst = curAnswer.worst === opt.key;

                  let borderClass = "border-zen-border bg-white";
                  if (isBest) borderClass = "border-emerald-500 bg-emerald-50/70";
                  if (isWorst) borderClass = "border-rose-400 bg-rose-50/70";

                  return (
                    <div
                      key={opt.key}
                      className={`rounded-2xl border p-4 transition-all flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-zen-subtle ${borderClass}`}
                    >
                      <div className="flex items-start gap-3 flex-1">
                        <span className="w-6 h-6 rounded-full bg-zen-surface text-zen-ink text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">
                          {opt.key}
                        </span>
                        <p className="text-xs sm:text-sm text-zen-ink leading-relaxed">
                          {t(opt.textVi, opt.textEn)}
                        </p>
                      </div>

                      {/* Best & Worst Action Buttons */}
                      {!isSubmitted && (
                        <div className="flex items-center gap-2 shrink-0 self-end sm:self-center">
                          <button
                            type="button"
                            onClick={() => handleSelectBest(opt.key)}
                            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                              isBest
                                ? "bg-emerald-600 text-white shadow-sm"
                                : "bg-emerald-50 text-emerald-700 border border-emerald-200 hover:bg-emerald-100"
                            }`}
                          >
                            BEST
                          </button>
                          <button
                            type="button"
                            onClick={() => handleSelectWorst(opt.key)}
                            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                              isWorst
                                ? "bg-rose-600 text-white shadow-sm"
                                : "bg-rose-50 text-rose-700 border border-rose-200 hover:bg-rose-100"
                            }`}
                          >
                            WORST
                          </button>
                        </div>
                      )}

                      {/* Post-Submit Review Badges */}
                      {isSubmitted && (
                        <div className="flex flex-wrap items-center gap-2 shrink-0">
                          {opt.key === current.bestAnswer && (
                            <span className="px-2.5 py-1 rounded-xl bg-emerald-600 text-white text-[11px] font-bold">
                              ✓ {t("ĐÁP ÁN BEST CHUẨN", "CORRECT BEST")}
                            </span>
                          )}
                          {opt.key === current.worstAnswer && (
                            <span className="px-2.5 py-1 rounded-xl bg-rose-600 text-white text-[11px] font-bold">
                              ✗ {t("ĐÁP ÁN WORST CHUẨN", "CORRECT WORST")}
                            </span>
                          )}
                          {isBest && opt.key !== current.bestAnswer && (
                            <span className="px-2 py-0.5 rounded-lg bg-amber-100 text-amber-800 text-[10px] font-semibold">
                              {t("Bạn chọn Best (Sai)", "You picked Best (Incorrect)")}
                            </span>
                          )}
                          {isWorst && opt.key !== current.worstAnswer && (
                            <span className="px-2 py-0.5 rounded-lg bg-amber-100 text-amber-800 text-[10px] font-semibold">
                              {t("Bạn chọn Worst (Sai)", "You picked Worst (Incorrect)")}
                            </span>
                          )}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>

              {/* Rationale & Clues (Shown upon submission) */}
              {isSubmitted && (
                <div className="mt-6 p-5 rounded-2xl bg-zen-surface border border-zen-moss/40 text-xs sm:text-sm text-zen-ink space-y-3 animate-in fade-in duration-200">
                  <div className="flex items-center gap-1.5 font-bold text-zen-moss-dark text-xs uppercase tracking-wider">
                    <Award className="w-4 h-4 text-zen-moss-dark" />
                    <span>{t("Phân tích lý do (Official Rationale):", "Official Exam Rationale:")}</span>
                  </div>
                  <p className="leading-relaxed whitespace-pre-line text-zen-ink/90">
                    {t(current.explanationVi, current.explanationEn)}
                  </p>

                  {current.keyClueVi && (
                    <div className="pt-2 border-t border-zen-border/40 text-xs flex items-center gap-1.5 text-zen-wood font-medium">
                      <AlertTriangle className="w-3.5 h-3.5 text-zen-ochre" />
                      <span>
                        {t("Dấu hiệu then chốt (Key Clue):", "Key Clue:")}{" "}
                        {t(current.keyClueVi, current.keyClueEn || "")}
                      </span>
                    </div>
                  )}
                </div>
              )}

              {/* Pagination controls */}
              <div className="flex items-center justify-between mt-8 pt-4 border-t border-zen-border/50">
                <button
                  onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
                  disabled={currentIndex === 0}
                  className="flex items-center gap-1 px-4 py-2 rounded-xl border border-zen-border bg-white text-xs font-semibold text-zen-ink disabled:opacity-40 hover:bg-zen-surface transition-colors shadow-zen-subtle"
                >
                  <ChevronLeft className="w-4 h-4" />
                  <span>{t("Câu trước", "Previous")}</span>
                </button>

                <span className="text-xs text-zen-muted font-medium">
                  {currentIndex + 1} / {questions.length}
                </span>

                <button
                  onClick={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
                  disabled={currentIndex === questions.length - 1}
                  className="flex items-center gap-1 px-4 py-2 rounded-xl border border-zen-border bg-white text-xs font-semibold text-zen-ink disabled:opacity-40 hover:bg-zen-surface transition-colors shadow-zen-subtle"
                >
                  <span>{t("Câu sau", "Next")}</span>
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>

          {/* Navigation Grid & Action (Right 1 col) */}
          <div className="space-y-4">
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-5 shadow-zen-card">
              <h4 className="text-xs font-bold text-zen-ink uppercase tracking-wider mb-3">
                {t("Bảng câu hỏi", "Questions Grid")}
              </h4>

              <div className="grid grid-cols-4 sm:grid-cols-8 lg:grid-cols-4 gap-2">
                {questions.map((q, idx) => {
                  const ans = answers[q.id];
                  const hasAnswered = ans?.best && ans?.worst;
                  const isCurrent = idx === currentIndex;

                  let badgeColor = "border-zen-border bg-white text-zen-ink";
                  if (hasAnswered) {
                    badgeColor = "border-zen-moss bg-zen-moss/20 text-zen-moss-dark font-bold";
                  }
                  if (isCurrent) {
                    badgeColor = "border-zen-moss-dark bg-zen-moss-dark text-white font-bold";
                  }

                  return (
                    <button
                      key={q.id}
                      onClick={() => setCurrentIndex(idx)}
                      className={`h-9 rounded-xl border text-xs flex items-center justify-center transition-all ${badgeColor}`}
                    >
                      {idx + 1}
                    </button>
                  );
                })}
              </div>

              {/* Progress Summary */}
              <div className="mt-4 pt-3 border-t border-zen-border/50 text-xs text-zen-muted space-y-1">
                <div className="flex justify-between">
                  <span>{t("Đã trả lời đủ Best & Worst:", "Completed:")}</span>
                  <span className="font-semibold text-zen-ink">
                    {Object.values(answers).filter((a) => a.best && a.worst).length} / {questions.length}
                  </span>
                </div>
              </div>

              {/* Submit Button */}
              {!isSubmitted ? (
                <button
                  onClick={handleSubmit}
                  className="w-full mt-5 py-3 rounded-2xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-all shadow-zen-subtle flex items-center justify-center gap-2"
                >
                  <CheckCircle className="w-4 h-4" />
                  <span>{t("Nộp bài & Chấm điểm", "Submit Exam")}</span>
                </button>
              ) : (
                <button
                  onClick={handleRetake}
                  className="w-full mt-5 py-3 rounded-2xl border border-zen-border bg-white text-zen-ink text-xs font-semibold hover:bg-zen-surface transition-all shadow-zen-subtle flex items-center justify-center gap-2"
                >
                  <RotateCcw className="w-4 h-4" />
                  <span>{t("Làm lại bài thi", "Retake Exam")}</span>
                </button>
              )}
            </div>

            {/* Post-Exam Report Card */}
            {isSubmitted && (
              <div className="rounded-3xl border border-zen-border bg-zen-paper p-5 shadow-zen-card text-center space-y-3">
                <div className="w-12 h-12 rounded-full bg-zen-moss/20 text-zen-moss-dark mx-auto flex items-center justify-center">
                  <Award className="w-6 h-6" />
                </div>
                <h4 className="font-serif text-lg font-bold text-zen-ink">
                  {t("Kết quả bài thi", "Exam Results")}
                </h4>
                <div className="text-3xl font-serif font-bold text-zen-moss-dark">
                  {Math.round(((bestCorrectCount + worstCorrectCount) / (questions.length * 2)) * 100)}%
                </div>
                <div className="text-xs text-zen-muted space-y-1">
                  <div>
                    {t("Đáp án BEST chính xác:", "Correct BEST:")}{" "}
                    <span className="font-bold text-emerald-700">{bestCorrectCount} / {questions.length}</span>
                  </div>
                  <div>
                    {t("Đáp án WORST chính xác:", "Correct WORST:")}{" "}
                    <span className="font-bold text-rose-700">{worstCorrectCount} / {questions.length}</span>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
