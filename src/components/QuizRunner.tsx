"use client";

import React, { useState } from "react";
import { QuizQuestion } from "@/types";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { CheckCircle2, XCircle, RefreshCw, Award, Lightbulb } from "lucide-react";
import { getStickerByTrigger } from "@/lib/db";
import StickerDisplay from "./StickerDisplay";

interface Props {
  quizzes: QuizQuestion[];
}

export default function QuizRunner({ quizzes }: Props) {
  const { t } = useLanguage();
  const { ringBell } = useSound();

  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [isFinished, setIsFinished] = useState(false);

  if (!quizzes.length) {
    return (
      <div className="p-8 text-center text-zen-muted text-sm bg-zen-paper rounded-2xl border border-zen-border">
        {t("Chưa có câu hỏi trắc nghiệm cho mục này", "No quiz questions in this section yet")}
      </div>
    );
  }

  const current = quizzes[currentIndex];
  const isCorrect = selectedOption === current.correctAnswer;

  const handleSelect = (key: string) => {
    if (isAnswered) return;
    setSelectedOption(key);
    setIsAnswered(true);

    if (key === current.correctAnswer) {
      setScore((prev) => prev + 1);
      ringBell();
    }
  };

  const handleNext = () => {
    if (currentIndex < quizzes.length - 1) {
      setCurrentIndex((prev) => prev + 1);
      setSelectedOption(null);
      setIsAnswered(false);
    } else {
      setIsFinished(true);
    }
  };

  const handleRestart = () => {
    setCurrentIndex(0);
    setSelectedOption(null);
    setIsAnswered(false);
    setScore(0);
    setIsFinished(false);
  };

  const comfortSticker = getStickerByTrigger("comfort_mistake");
  const winSticker = getStickerByTrigger("quiz_streak");

  if (isFinished) {
    const passed = score >= Math.ceil(quizzes.length * 0.7);
    return (
      <div className="max-w-md mx-auto text-center p-8 bg-zen-paper rounded-3xl border border-zen-border shadow-zen-card">
        {passed && winSticker ? (
          <StickerDisplay
            sticker={winSticker}
            size={100}
            message={t(
              "Tuyệt vời! Bạn đã hoàn thành tốt bài trắc nghiệm.",
              "Wonderful! You did great on this quiz."
            )}
          />
        ) : comfortSticker ? (
          <StickerDisplay
            sticker={comfortSticker}
            size={100}
            message={t(
              "Không sao, mỗi lần sai là một hạt giống của hiểu biết.",
              "It is okay, every mistake is a seed of understanding."
            )}
          />
        ) : null}

        <h3 className="font-serif text-2xl font-bold text-zen-ink mt-4">
          {t("Hoàn thành bài luyện tập", "Quiz Completed")}
        </h3>
        <p className="text-sm text-zen-muted mt-1">
          {t("Điểm số của bạn:", "Your score:")}{" "}
          <span className="font-bold text-zen-moss-dark text-lg">
            {score} / {quizzes.length}
          </span>
        </p>

        <button
          onClick={handleRestart}
          className="mt-6 inline-flex items-center gap-2 px-6 py-2.5 rounded-2xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-colors shadow-zen-subtle"
        >
          <RefreshCw className="w-4 h-4" />
          <span>{t("Làm lại bài này", "Retake Quiz")}</span>
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card">
      {/* Quiz Header */}
      <div className="flex items-center justify-between text-xs text-zen-muted mb-4 pb-3 border-b border-zen-border/50">
        <span className="font-semibold text-zen-ink">
          {t("Câu hỏi", "Question")} {currentIndex + 1} / {quizzes.length}
        </span>
        <span className="px-2.5 py-0.5 rounded-full bg-zen-moss/15 text-zen-moss-dark font-medium capitalize">
          {current.difficulty || "medium"}
        </span>
      </div>

      {/* Question Text */}
      <h3 className="font-serif text-lg sm:text-xl font-bold text-zen-ink leading-relaxed mb-6">
        {t(current.questionVi, current.questionEn)}
      </h3>

      {/* Options */}
      <div className="space-y-3">
        {current.options.map((opt) => {
          const isChosen = selectedOption === opt.key;
          const isRightChoice = opt.key === current.correctAnswer;

          let btnClass = "border-zen-border hover:bg-zen-surface text-zen-ink";
          if (isAnswered) {
            if (isRightChoice) {
              btnClass = "border-emerald-500 bg-emerald-50/80 text-emerald-900 font-medium";
            } else if (isChosen) {
              btnClass = "border-rose-400 bg-rose-50 text-rose-900";
            } else {
              btnClass = "border-zen-border/50 text-zen-muted opacity-60";
            }
          }

          return (
            <button
              key={opt.key}
              onClick={() => handleSelect(opt.key)}
              disabled={isAnswered}
              className={`w-full flex items-start gap-3 p-4 rounded-2xl border text-left text-xs sm:text-sm leading-relaxed transition-all ${btnClass}`}
            >
              <span
                className={`w-6 h-6 rounded-full flex items-center justify-center shrink-0 text-xs font-bold ${
                  isAnswered && isRightChoice
                    ? "bg-emerald-600 text-white"
                    : isAnswered && isChosen
                    ? "bg-rose-500 text-white"
                    : "bg-zen-surface text-zen-ink"
                }`}
              >
                {opt.key}
              </span>
              <span className="flex-1">{t(opt.textVi, opt.textEn)}</span>
              {isAnswered && isRightChoice && (
                <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
              )}
              {isAnswered && isChosen && !isRightChoice && (
                <XCircle className="w-5 h-5 text-rose-500 shrink-0" />
              )}
            </button>
          );
        })}
      </div>

      {/* Explanation Box */}
      {isAnswered && (
        <div
          className={`mt-6 p-5 rounded-2xl border text-xs sm:text-sm leading-relaxed animate-in fade-in duration-200 ${
            isCorrect
              ? "bg-emerald-50/70 border-emerald-200 text-emerald-900"
              : "bg-amber-50/80 border-amber-200 text-amber-900"
          }`}
        >
          <div className="flex items-center gap-2 font-bold mb-1.5">
            <Lightbulb className="w-4 h-4 text-zen-ochre" />
            <span>
              {isCorrect
                ? t("Chính xác! Lời giải thích:", "Correct! Explanation:")
                : t("Chưa đúng. Lời giải thích chi tiết:", "Not quite. Detailed Explanation:")}
            </span>
          </div>
          <p>{t(current.explanationVi, current.explanationEn)}</p>

          {current.primaryCompetency && (
            <div className="mt-3 pt-2 border-t border-zen-border/40 text-xs flex items-center gap-1.5 text-zen-muted">
              <Award className="w-3.5 h-3.5 text-zen-wood" />
              <span>
                {t("Năng lực liên quan:", "Competency:")} {current.primaryCompetency}
              </span>
            </div>
          )}
        </div>
      )}

      {/* Next Button */}
      {isAnswered && (
        <div className="mt-6 flex justify-end">
          <button
            onClick={handleNext}
            className="px-6 py-2.5 rounded-2xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-colors shadow-zen-subtle"
          >
            {currentIndex < quizzes.length - 1
              ? t("Câu tiếp theo →", "Next Question →")
              : t("Xem kết quả tổng kết", "Finish & View Results")}
          </button>
        </div>
      )}
    </div>
  );
}
