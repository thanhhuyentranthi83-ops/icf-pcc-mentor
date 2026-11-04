"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import { LotusGardenState } from "@/lib/db";
import { Sparkles, Sprout, Sun } from "lucide-react";

interface Props {
  garden: LotusGardenState;
  streakCount: number;
}

export default function LotusGarden({ garden, streakCount }: Props) {
  const { t } = useLanguage();

  return (
    <div className="relative overflow-hidden rounded-3xl border border-zen-border bg-gradient-to-b from-[#EBF2EB] via-[#F7F3EA] to-[#E3EFE3] p-6 shadow-zen-card transition-all">
      {/* Gentle Morning Sun Ray Glow */}
      <div className="absolute -top-12 -right-12 w-48 h-48 rounded-full bg-zen-ochre/15 blur-2xl pointer-events-none" />

      {/* Header */}
      <div className="relative z-10 flex flex-wrap items-center justify-between gap-4 pb-4 border-b border-zen-border/50">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-zen-moss-dark text-white flex items-center justify-center shadow-zen-subtle">
            <Sun className="w-5 h-5 text-zen-ochre animate-spin-slow" />
          </div>
          <div>
            <h3 className="font-serif text-lg font-bold text-zen-ink">
              {t("Vườn Sen Chánh Niệm Của Tôi", "My Mindful Lotus Garden")}
            </h3>
            <p className="text-xs text-zen-muted">
              {t(
                "Mỗi bài học bạn hoàn thành là một đóa sen ngát hương nảy mầm",
                "Every lesson completed blossoms a fragrant lotus in your garden"
              )}
            </p>
          </div>
        </div>

        {/* Streak Counter */}
        <div className="flex items-center gap-2 bg-white/80 backdrop-blur-sm px-3.5 py-1.5 rounded-2xl border border-zen-border/80 shadow-zen-subtle">
          <Sparkles className="w-4 h-4 text-zen-ochre animate-pulse" />
          <span className="text-xs font-semibold text-zen-ink">
            {streakCount} {t("ngày liên tục", "day streak")}
          </span>
        </div>
      </div>

      {/* Visual Zen Pond */}
      <div className="relative h-44 my-4 rounded-2xl bg-gradient-to-b from-[#DFECE0] to-[#CFE0D1] border border-zen-moss/30 overflow-hidden flex items-end justify-around px-4 pb-3">
        {/* Subtle Water Waves */}
        <div className="absolute inset-0 opacity-20 pointer-events-none bg-[radial-gradient(circle_at_50%_120%,rgba(79,111,82,0.5),transparent_70%)]" />

        {/* Dragonflies & Butterflies (Animated) */}
        {garden.butterfliesUnlocked > 0 && (
          <div className="absolute top-4 left-1/4 animate-float text-base pointer-events-none">
            🦋
          </div>
        )}
        {garden.dragonfliesUnlocked > 0 && (
          <div
            className="absolute top-8 right-1/4 animate-float text-base pointer-events-none"
            style={{ animationDelay: "2s" }}
          >
            🌾
          </div>
        )}
        <div
          className="absolute top-6 right-1/3 animate-float text-sm pointer-events-none"
          style={{ animationDelay: "3s" }}
        >
          ✨
        </div>

        {/* Lily Pads & Lotus Flowers */}
        <div className="flex items-end justify-center gap-6 sm:gap-10 w-full z-10">
          {/* Seed Phase */}
          <div className="flex flex-col items-center group">
            <div className="w-10 h-10 rounded-full bg-zen-surface border border-zen-moss flex items-center justify-center text-zen-wood text-sm font-serif shadow-sm group-hover:scale-110 transition-transform">
              🌰
            </div>
            <div className="w-12 h-2.5 rounded-full bg-zen-moss-dark/20 mt-1" />
            <span className="text-[11px] font-medium text-zen-ink/80 mt-1">
              {garden.seedsPlanted} {t("Hạt giống", "Seeds")}
            </span>
          </div>

          {/* Sprout Phase */}
          <div className="flex flex-col items-center group">
            <div className="w-12 h-12 rounded-full bg-zen-paper border border-zen-moss-dark/40 flex items-center justify-center text-zen-moss-dark text-base shadow-sm group-hover:scale-110 transition-transform">
              🌱
            </div>
            <div className="w-14 h-3 rounded-full bg-zen-moss-dark/25 mt-1" />
            <span className="text-[11px] font-medium text-zen-ink/80 mt-1">
              {garden.sproutsGrown} {t("Chồi non", "Sprouts")}
            </span>
          </div>

          {/* Lotus Bloom Phase */}
          <div className="flex flex-col items-center group">
            <div className="relative">
              <div className="w-14 h-14 rounded-full bg-zen-lotus-light/80 border-2 border-zen-lotus flex items-center justify-center text-2xl shadow-zen-subtle animate-bounce-slow group-hover:scale-110 transition-transform">
                🪷
              </div>
              <div className="absolute -top-1 -right-1 w-3 h-3 rounded-full bg-zen-ochre animate-ping" />
            </div>
            <div className="w-16 h-3 rounded-full bg-zen-lotus/30 mt-1" />
            <span className="text-[11px] font-bold text-zen-moss-dark mt-1">
              {garden.lotusesBloomed} {t("Đóa sen nở", "Blooms")}
            </span>
          </div>
        </div>
      </div>

      {/* Gentle Insight Footer */}
      <div className="flex items-center justify-between text-xs text-zen-muted pt-1">
        <div className="flex items-center gap-1.5">
          <Sprout className="w-3.5 h-3.5 text-zen-moss-dark" />
          <span>
            {t(
              "Mỗi ngày học 10-15 phút để tưới tẩm sự hiểu biết",
              "10-15 mindful minutes daily to water your seeds of understanding"
            )}
          </span>
        </div>
        <span className="font-serif italic text-zen-wood text-[11px]">
          {t("Vạn sự tùy duyên, kiên trì đơm quả", "Patience blossoms into mastery")}
        </span>
      </div>
    </div>
  );
}
