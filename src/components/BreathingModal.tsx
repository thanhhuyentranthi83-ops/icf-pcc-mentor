"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { Sparkles, X } from "lucide-react";

interface Props {
  isOpen: boolean;
  onComplete: () => void;
  onClose: () => void;
}

export default function BreathingModal({ isOpen, onComplete, onClose }: Props) {
  const { t } = useLanguage();
  const { ringBell } = useSound();

  const [breathCount, setBreathCount] = useState(1);
  const [phase, setPhase] = useState<"inhale" | "hold" | "exhale">("inhale");
  const [timerSeconds, setTimerSeconds] = useState(4);

  useEffect(() => {
    if (!isOpen) return;

    // Ring gentle bell at start
    ringBell();
    setBreathCount(1);
    setPhase("inhale");
    setTimerSeconds(4);

    const interval = setInterval(() => {
      setTimerSeconds((prev) => {
        if (prev > 1) return prev - 1;

        // Transition phase
        setPhase((curPhase) => {
          if (curPhase === "inhale") {
            return "hold";
          }
          if (curPhase === "hold") {
            return "exhale";
          }
          // exhale ended -> increment breath
          setBreathCount((curBreath) => {
            if (curBreath >= 3) {
              clearInterval(interval);
              setTimeout(() => {
                ringBell();
                onComplete();
              }, 800);
              return 3;
            }
            return curBreath + 1;
          });
          return "inhale";
        });

        return 4; // reset 4 seconds
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [isOpen]);

  if (!isOpen) return null;

  const phaseInstruction = {
    inhale: t("Hít vào thật sâu... Đón nhận sự bình an", "Breathe in deeply... Welcoming calm presence"),
    hold: t("Giữ lại một nhịp... Cảm nhận sự tĩnh tại", "Hold gently... Resting in stillness"),
    exhale: t("Thở ra chầm chậm... Buông bỏ mọi âu lo", "Breathe out slowly... Releasing all tension")
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-md animate-in fade-in duration-300">
      <div className="relative w-full max-w-md bg-zen-bg rounded-3xl p-8 border border-zen-border shadow-zen-floating flex flex-col items-center text-center">
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-zen-muted hover:text-zen-ink rounded-full hover:bg-zen-surface transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Title */}
        <div className="flex items-center gap-2 text-zen-moss-dark text-xs font-semibold uppercase tracking-wider mb-2">
          <Sparkles className="w-4 h-4 text-zen-ochre" />
          <span>{t("Ba Hơi Thở Trước Khi Thi", "Three Mindful Breaths")}</span>
        </div>
        <h3 className="font-serif text-2xl font-bold text-zen-ink mb-1">
          {t("Lắng Đọng Thân Tâm", "Centering Body & Mind")}
        </h3>
        <p className="text-xs text-zen-muted mb-8 max-w-xs">
          {t(
            "Dành ít phút trở về với hơi thở để tâm trí sáng tỏ trước khi làm bài",
            "Take a quiet pause to ground your presence before beginning"
          )}
        </p>

        {/* Pulsing Enso Circle */}
        <div className="relative w-52 h-52 flex items-center justify-center my-2">
          {/* Animated Halo */}
          <div
            className={`absolute inset-0 rounded-full bg-zen-moss/10 transition-all duration-[4000ms] ease-in-out ${
              phase === "inhale"
                ? "scale-110 opacity-80"
                : phase === "hold"
                ? "scale-110 opacity-100"
                : "scale-75 opacity-30"
            }`}
          />

          {/* Enso Brush Ring */}
          <div
            className={`w-40 h-40 rounded-full border-4 border-zen-moss-dark/70 flex flex-col items-center justify-center bg-white/70 shadow-zen-card transition-all duration-[4000ms] ease-in-out ${
              phase === "inhale"
                ? "scale-125 border-zen-ochre"
                : phase === "hold"
                ? "scale-125 border-zen-moss-dark"
                : "scale-90 border-zen-moss/50"
            }`}
          >
            <span className="font-serif text-3xl font-bold text-zen-ink">
              {timerSeconds}
            </span>
            <span className="text-[11px] font-medium text-zen-moss-dark capitalize mt-0.5">
              {phase === "inhale"
                ? t("Hít vào", "Inhale")
                : phase === "hold"
                ? t("Giữ nhịp", "Hold")
                : t("Thở ra", "Exhale")}
            </span>
          </div>
        </div>

        {/* Step dots */}
        <div className="flex items-center gap-2 mt-6 mb-3">
          {[1, 2, 3].map((b) => (
            <div
              key={b}
              className={`w-2.5 h-2.5 rounded-full transition-all ${
                b === breathCount
                  ? "bg-zen-moss-dark w-6"
                  : b < breathCount
                  ? "bg-zen-moss"
                  : "bg-zen-border"
              }`}
            />
          ))}
        </div>
        <p className="text-xs text-zen-muted mb-2 font-medium">
          {t("Nhịp thở", "Breath")} {breathCount} / 3
        </p>

        {/* Phase instruction */}
        <p className="text-sm font-serif italic text-zen-ink/90 min-h-[40px] px-4">
          {phaseInstruction[phase]}
        </p>

        {/* Skip button */}
        <button
          onClick={onComplete}
          className="mt-6 text-xs text-zen-muted hover:text-zen-ink underline underline-offset-4 transition-colors"
        >
          {t("Bỏ qua và vào bài thi ngay", "Skip and enter exam now")}
        </button>
      </div>
    </div>
  );
}
