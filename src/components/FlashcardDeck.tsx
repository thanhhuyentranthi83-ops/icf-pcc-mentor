"use client";

import React, { useState } from "react";
import { Flashcard } from "@/types";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { RotateCw, Star, ChevronLeft, ChevronRight, HelpCircle, Check, AlertCircle, XCircle } from "lucide-react";
import { updateFlashcardProgress } from "@/lib/db";
import { useAuth } from "@/context/AuthContext";

interface Props {
  flashcards: Flashcard[];
}

export default function FlashcardDeck({ flashcards }: Props) {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user } = useAuth();

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [showHint, setShowHint] = useState(false);
  const [favorites, setFavorites] = useState<Record<string, boolean>>({});
  const [statusMap, setStatusMap] = useState<Record<string, "known" | "unsure" | "unknown">>({});

  if (!flashcards.length) {
    return (
      <div className="p-8 text-center text-zen-muted text-sm bg-zen-paper rounded-2xl border border-zen-border">
        {t("Chưa có flashcard cho mục này", "No flashcards in this section yet")}
      </div>
    );
  }

  const current = flashcards[currentIndex];
  const isFav = !!favorites[current.id];

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const handleNext = () => {
    setIsFlipped(false);
    setShowHint(false);
    setCurrentIndex((prev) => (prev + 1) % flashcards.length);
  };

  const handlePrev = () => {
    setIsFlipped(false);
    setShowHint(false);
    setCurrentIndex((prev) => (prev - 1 + flashcards.length) % flashcards.length);
  };

  const handleStatus = (status: "known" | "unsure" | "unknown") => {
    setStatusMap((prev) => ({ ...prev, [current.id]: status }));
    updateFlashcardProgress(user.id, current.id, status, isFav);
    if (status === "known") {
      ringBell();
    }
    // Auto advance
    setTimeout(handleNext, 300);
  };

  const toggleFavorite = (e: React.MouseEvent) => {
    e.stopPropagation();
    const next = !isFav;
    setFavorites((prev) => ({ ...prev, [current.id]: next }));
    updateFlashcardProgress(user.id, current.id, statusMap[current.id] || "unknown", next);
  };

  return (
    <div className="max-w-xl mx-auto flex flex-col items-center">
      {/* Top Controls & Counter */}
      <div className="w-full flex items-center justify-between text-xs text-zen-muted mb-4 px-2">
        <span className="font-semibold text-zen-ink">
          {t("Thẻ số", "Card")} {currentIndex + 1} / {flashcards.length}
        </span>
        <div className="flex items-center gap-2">
          {current.hintVi && (
            <button
              onClick={() => setShowHint(!showHint)}
              className="flex items-center gap-1 text-zen-moss-dark hover:underline"
            >
              <HelpCircle className="w-3.5 h-3.5" />
              <span>{showHint ? t("Ẩn gợi ý", "Hide hint") : t("Xem gợi ý", "Show hint")}</span>
            </button>
          )}
          <button
            onClick={toggleFavorite}
            className={`p-1.5 rounded-lg border transition-colors ${
              isFav ? "border-amber-400 bg-amber-50 text-amber-500" : "border-zen-border text-zen-muted hover:text-zen-ink"
            }`}
          >
            <Star className={`w-4 h-4 ${isFav ? "fill-amber-400" : ""}`} />
          </button>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full h-1.5 bg-zen-border/50 rounded-full overflow-hidden mb-6">
        <div
          className="h-full bg-zen-moss-dark transition-all duration-300"
          style={{ width: `${((currentIndex + 1) / flashcards.length) * 100}%` }}
        />
      </div>

      {/* 3D Flashcard Container */}
      <div
        onClick={handleFlip}
        className="w-full min-h-[260px] cursor-pointer rounded-3xl bg-zen-paper border border-zen-border p-8 shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col justify-between relative select-none"
      >
        <div className="flex items-center justify-between text-xs font-semibold text-zen-muted uppercase tracking-wider">
          <span className="text-zen-moss-dark">
            {isFlipped ? t("Mặt Sau (Giải nghĩa)", "Back (Definition)") : t("Mặt Trước (Thuật ngữ)", "Front (Term)")}
          </span>
          <div className="flex items-center gap-1 text-[11px] text-zen-muted font-normal">
            <RotateCw className="w-3 h-3" />
            <span>{t("Chạm để lật thẻ", "Tap to flip")}</span>
          </div>
        </div>

        {/* Content */}
        <div className="my-auto py-4 text-center">
          <h4 className="font-serif text-xl sm:text-2xl font-bold text-zen-ink leading-relaxed">
            {isFlipped ? t(current.backVi, current.backEn) : t(current.frontVi, current.frontEn)}
          </h4>

          {/* Hint */}
          {showHint && current.hintVi && (
            <div className="mt-4 p-3 rounded-2xl bg-amber-50/80 border border-amber-200 text-xs text-amber-800 text-left">
              <span className="font-bold">{t("Gợi ý:", "Hint:")}</span> {t(current.hintVi, current.hintEn || "")}
            </div>
          )}
        </div>

        {/* Status Tag */}
        <div className="flex items-center justify-between text-[11px] text-zen-muted pt-2 border-t border-zen-border/40">
          <span>{t("Ôn lặp lại ngắt quãng (Leitner)", "Spaced Repetition")}</span>
          {statusMap[current.id] && (
            <span className="capitalize font-semibold text-zen-moss-dark">
              {statusMap[current.id]}
            </span>
          )}
        </div>
      </div>

      {/* Leitner Evaluation Buttons */}
      <div className="w-full grid grid-cols-3 gap-3 mt-6">
        <button
          onClick={() => handleStatus("unknown")}
          className="flex items-center justify-center gap-1.5 py-3 rounded-2xl border border-rose-200 bg-rose-50 text-rose-700 hover:bg-rose-100 text-xs font-semibold transition-colors shadow-zen-subtle"
        >
          <XCircle className="w-4 h-4" />
          <span>{t("Chưa biết", "Don't Know")}</span>
        </button>

        <button
          onClick={() => handleStatus("unsure")}
          className="flex items-center justify-center gap-1.5 py-3 rounded-2xl border border-amber-200 bg-amber-50 text-amber-700 hover:bg-amber-100 text-xs font-semibold transition-colors shadow-zen-subtle"
        >
          <AlertCircle className="w-4 h-4" />
          <span>{t("Chưa chắc", "Unsure")}</span>
        </button>

        <button
          onClick={() => handleStatus("known")}
          className="flex items-center justify-center gap-1.5 py-3 rounded-2xl border border-emerald-200 bg-emerald-50 text-emerald-700 hover:bg-emerald-100 text-xs font-semibold transition-colors shadow-zen-subtle"
        >
          <Check className="w-4 h-4" />
          <span>{t("Đã biết", "Know")}</span>
        </button>
      </div>

      {/* Prev / Next Controls */}
      <div className="flex items-center justify-center gap-4 mt-6">
        <button
          onClick={handlePrev}
          className="p-2.5 rounded-full border border-zen-border bg-zen-paper hover:bg-zen-surface text-zen-ink transition-colors shadow-zen-subtle"
        >
          <ChevronLeft className="w-5 h-5" />
        </button>
        <button
          onClick={handleNext}
          className="p-2.5 rounded-full border border-zen-border bg-zen-paper hover:bg-zen-surface text-zen-ink transition-colors shadow-zen-subtle"
        >
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>
    </div>
  );
}
