"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { getStickers, getMindfulnessMessages } from "@/lib/db";
import { Sticker, MindfulnessMessage } from "@/types";
import { Smile, Sparkles, Check, Plus } from "lucide-react";

export default function AdminStickersPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();

  const [stickers, setStickers] = useState<Sticker[]>([]);
  const [messages, setMessages] = useState<MindfulnessMessage[]>([]);
  const [tab, setTab] = useState<"stickers" | "messages">("stickers");

  useEffect(() => {
    setStickers(getStickers());
    setMessages(getMindfulnessMessages());
  }, []);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card">
        <h1 className="font-serif text-2xl font-bold text-zen-ink">
          {t("Quản Lý Kho Sticker & Lời Nhắn Chánh Niệm", "Stickers & Mindfulness Quotes Library")}
        </h1>
        <p className="text-xs text-zen-muted mt-1">
          {t(
            "Kho sticker truyền cảm hứng và kho 30+ câu nhắn nhủ chánh niệm song ngữ được tuyển chọn kỹ lưỡng.",
            "Exclusive SVG mindfulness character stickers and 30+ bilingual quotes for presence and insight."
          )}
        </p>
      </div>

      {/* Tabs */}
      <div className="flex items-center gap-2 border-b border-zen-border pb-2 text-xs">
        <button
          onClick={() => setTab("stickers")}
          className={`px-4 py-2 rounded-2xl font-bold transition-all ${
            tab === "stickers"
              ? "bg-amber-900 text-white shadow-sm"
              : "bg-zen-paper text-zen-ink border border-zen-border"
          }`}
        >
          🎭 {t("Kho 12 Sticker Độc Quyền", "12 Exclusive Stickers")} ({stickers.length})
        </button>
        <button
          onClick={() => setTab("messages")}
          className={`px-4 py-2 rounded-2xl font-bold transition-all ${
            tab === "messages"
              ? "bg-amber-900 text-white shadow-sm"
              : "bg-zen-paper text-zen-ink border border-zen-border"
          }`}
        >
          🪷 {t("Kho 30 Câu Lời Nhắn Chánh Niệm", "30 Mindfulness Quotes")} ({messages.length})
        </button>
      </div>

      {/* Tab: Stickers */}
      {tab === "stickers" && (
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
          {stickers.map((stk) => (
            <div
              key={stk.id}
              className="rounded-3xl border border-zen-border bg-zen-paper p-5 shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col items-center text-center justify-between"
            >
              <div
                className="w-20 h-20 my-2"
                dangerouslySetInnerHTML={{ __html: stk.svgContent }}
              />

              <div className="space-y-1 w-full pt-2 border-t border-zen-border/50">
                <span className="font-bold text-xs text-zen-ink block truncate">
                  {t(stk.nameVi, stk.nameEn)}
                </span>
                <span className="text-[10px] font-mono font-medium text-zen-moss-dark bg-zen-moss/15 px-2 py-0.5 rounded-md inline-block truncate max-w-full">
                  Trigger: {stk.triggerEvent}
                </span>
                <span className="text-[10px] text-zen-muted block capitalize">
                  {stk.category}
                </span>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Tab: Mindfulness Messages */}
      {tab === "messages" && (
        <div className="space-y-3">
          {messages.map((m, idx) => (
            <div
              key={m.id}
              className="rounded-2xl border border-zen-border bg-zen-paper p-4 shadow-zen-subtle text-xs space-y-1.5"
            >
              <div className="flex items-center justify-between text-zen-muted">
                <span className="font-bold text-zen-moss-dark">
                  #{idx + 1} • {m.theme}
                </span>
                <span className="text-[10px] px-2 py-0.5 rounded bg-zen-surface text-zen-ink font-medium">
                  {m.author}
                </span>
              </div>
              <p className="font-serif italic text-zen-ink text-sm">“{m.textVi}”</p>
              <p className="font-serif italic text-zen-muted text-xs">“{m.textEn}”</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
