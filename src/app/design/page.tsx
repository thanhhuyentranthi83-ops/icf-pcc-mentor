"use client";

import React, { useState } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import NatureIcon from "@/components/NatureIcon";
import { getStickers } from "@/lib/db";
import { Sticker } from "@/types";
import { Sparkles, Bell, Volume2, Check } from "lucide-react";
import BreathingModal from "@/components/BreathingModal";

export default function DesignSystemPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const [stickers, setStickers] = useState<Sticker[]>([]);
  const [showBreathingDemo, setShowBreathingDemo] = useState(false);

  React.useEffect(() => {
    setStickers(getStickers());
  }, []);

  const colorSwatches = [
    { name: "Nền chính (Giấy dó kem)", hex: "#F7F3EA", role: "Background Canvas", text: "text-[#2F3A32]" },
    { name: "Nền thẻ ấm (Trắng giấy)", hex: "#FAF7F2", role: "Card Surface", text: "text-[#2F3A32]" },
    { name: "Xanh lá trà / Rêu nhạt", hex: "#8BA888", role: "Primary Zen Moss", text: "text-white" },
    { name: "Xanh rêu trầm", hex: "#4F6F52", role: "Primary Deep", text: "text-white" },
    { name: "Hồng sen thanh thoát", hex: "#E8A0B4", role: "Accent Lotus Pink", text: "text-white" },
    { name: "Hồng cánh sen non", hex: "#F6D6DF", role: "Soft Lotus Pink", text: "text-[#2F3A32]" },
    { name: "Vàng nghệ (CTA)", hex: "#D9A441", role: "Action Call-to-action", text: "text-white" },
    { name: "Nâu gỗ mộc", hex: "#6B4F3A", role: "Earth Wood", text: "text-white" },
    { name: "Chữ chính (Mực than dịu)", hex: "#2F3A32", role: "Text Ink", text: "text-white" },
    { name: "Đêm thiền (Nền tối)", hex: "#1E2621", role: "Night Mode Canvas", text: "text-[#EDE8DC]" }
  ];

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 sm:py-12 space-y-12">
      {/* Title */}
      <div className="text-center max-w-2xl mx-auto space-y-2">
        <span className="text-xs font-bold uppercase tracking-wider text-zen-moss-dark bg-zen-moss/15 px-3 py-1 rounded-full">
          Zen Làng Mai Design System
        </span>
        <h1 className="font-serif text-3xl sm:text-4xl font-bold text-zen-ink">
          {t("Hệ Thống Thiết Kế & Nhận Diện Thẩm Mỹ", "Design System & Aesthetics Showroom")}
        </h1>
        <p className="text-xs sm:text-sm text-zen-muted leading-relaxed">
          {t(
            "Triết lý ít mà sâu, tĩnh tại và ấm áp. Chuẩn tương phản WCAG AA, bo góc 16-24px, âm thanh chuông chánh niệm và 12 sticker độc quyền.",
            "Minimalist, calm and warm. WCAG AA contrast compliance, organic 16-24px curves, Web Audio mindfulness bell and 12 exclusive stickers."
          )}
        </p>
      </div>

      {/* 1. Color Palette */}
      <section className="space-y-4">
        <h2 className="font-serif text-xl font-bold text-zen-ink flex items-center gap-2">
          <span>🎨</span>
          <span>{t("1. Bảng Màu Chánh Niệm (Zen Color Palette)", "1. Zen Color Palette")}</span>
        </h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
          {colorSwatches.map((c) => (
            <div
              key={c.hex}
              className="rounded-3xl border border-zen-border p-3.5 shadow-zen-subtle space-y-2"
              style={{ backgroundColor: c.hex }}
            >
              <div className="h-12" />
              <div className={`p-2 rounded-xl bg-white/70 backdrop-blur-sm text-xs`}>
                <span className="font-bold block text-zen-ink text-[11px] truncate">{c.name}</span>
                <span className="font-mono text-[10px] text-zen-muted uppercase">{c.hex}</span>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 2. Nature Icons */}
      <section className="space-y-4">
        <h2 className="font-serif text-xl font-bold text-zen-ink flex items-center gap-2">
          <span>🌿</span>
          <span>{t("2. Bộ Biểu Tượng Thiên Nhiên Từng Phần", "2. Nature Domain Icons")}</span>
        </h2>
        <div className="grid grid-cols-2 sm:grid-cols-5 gap-4">
          {[
            { id: "seed", nameVi: "Hạt Giống (Phần A)", nameEn: "Seed (Domain A)", sub: "Khởi nguồn đạo đức" },
            { id: "sprout", nameVi: "Chồi Non (Phần B)", nameEn: "Sprout (Domain B)", sub: "Nuôi dưỡng gắn kết" },
            { id: "bamboo", nameVi: "Lá Tre (Phần C)", nameEn: "Bamboo (Domain C)", sub: "Lắng nghe sâu sắc" },
            { id: "lotus", nameVi: "Hoa Sen (Phần D)", nameEn: "Lotus (Domain D)", sub: "Đơm hoa trí tuệ" },
            { id: "mountain", nameVi: "Ngọn Núi (Thi Thử)", nameEn: "Mountain (Mock Exam)", sub: "Vững chãi tự tin" }
          ].map((item) => (
            <div
              key={item.id}
              className="rounded-3xl border border-zen-border bg-zen-paper p-5 text-center shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col items-center justify-center space-y-2"
            >
              <div className="w-12 h-12 rounded-2xl bg-zen-moss/20 text-zen-moss-dark flex items-center justify-center">
                <NatureIcon icon={item.id} size={24} />
              </div>
              <span className="font-serif font-bold text-xs text-zen-ink block">
                {t(item.nameVi, item.nameEn)}
              </span>
              <span className="text-[10px] text-zen-muted block">{item.sub}</span>
            </div>
          ))}
        </div>
      </section>

      {/* 3. Mindfulness Audio Bell Test */}
      <section className="space-y-4">
        <h2 className="font-serif text-xl font-bold text-zen-ink flex items-center gap-2">
          <span>🔔</span>
          <span>{t("3. Chuông Chánh Niệm (Mindfulness Bell Sound)", "3. Mindfulness Audio Bell")}</span>
        </h2>
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card flex flex-col sm:flex-row items-center justify-between gap-6">
          <div className="space-y-1 max-w-md text-center sm:text-left">
            <h3 className="font-serif text-lg font-bold text-zen-ink">
              {t("Âm sắc chuông Tây Tạng qua Web Audio API", "Resonant Tibetan Bowl Synthesis")}
            </h3>
            <p className="text-xs text-zen-muted leading-relaxed">
              {t(
                "Được tổng hợp từ các hài âm tự nhiên với độ suy hao 6 giây, mang lại cảm giác lắng dịu ngay tức thì khi hoàn thành bài học.",
                "Synthesized from organic acoustic harmonics with 6-second exponential decay for instant presence."
              )}
            </p>
          </div>

          <button
            onClick={() => ringBell()}
            className="px-6 py-3.5 rounded-2xl bg-zen-moss-dark hover:bg-zen-moss-deep text-white font-semibold text-xs shadow-zen-subtle transition-all flex items-center gap-2 shrink-0"
          >
            <Bell className="w-4 h-4 text-zen-ochre" />
            <span>{t("Thỉnh thử một tiếng chuông", "Sound the Bell")}</span>
          </button>
        </div>
      </section>

      {/* 4. Three Breaths Modal Demo */}
      <section className="space-y-4">
        <h2 className="font-serif text-xl font-bold text-zen-ink flex items-center gap-2">
          <span>🌀</span>
          <span>{t("4. Ba Hơi Thở Trước Khi Thi (Enso Breathing)", "4. Three Mindful Breaths")}</span>
        </h2>
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card flex flex-col sm:flex-row items-center justify-between gap-6">
          <div className="space-y-1 max-w-md text-center sm:text-left">
            <h3 className="font-serif text-lg font-bold text-zen-ink">
              {t("Bài tập điều hòa thân tâm trước bài thi", "Pre-Exam Calming Exercise")}
            </h3>
            <p className="text-xs text-zen-muted leading-relaxed">
              {t(
                "3 nhịp thở co giãn theo vòng tròn Enso để buông bỏ căng thẳng và sẵn sàng tập trung tối đa.",
                "Three breaths guided by an expanding/contracting Enso circle to release pre-exam anxiety."
              )}
            </p>
          </div>

          <button
            onClick={() => setShowBreathingDemo(true)}
            className="px-6 py-3.5 rounded-2xl bg-zen-wood hover:bg-[#573F2E] text-white font-semibold text-xs shadow-zen-subtle transition-all flex items-center gap-2 shrink-0"
          >
            <Sparkles className="w-4 h-4 text-zen-lotus" />
            <span>{t("Trải nghiệm 3 hơi thở", "Experience 3 Breaths")}</span>
          </button>
        </div>

        <BreathingModal
          isOpen={showBreathingDemo}
          onComplete={() => setShowBreathingDemo(false)}
          onClose={() => setShowBreathingDemo(false)}
        />
      </section>

      {/* 5. 12 Stickers Library Gallery */}
      <section className="space-y-4">
        <h2 className="font-serif text-xl font-bold text-zen-ink flex items-center gap-2">
          <span>✨</span>
          <span>{t("5. Kho 12 Sticker Độc Quyền (Original SVG)", "5. 12 Exclusive SVG Stickers")}</span>
        </h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
          {stickers.map((stk) => (
            <div
              key={stk.id}
              className="rounded-3xl border border-zen-border bg-zen-paper p-4 text-center shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col items-center justify-between"
            >
              <div
                className="w-16 h-16 my-2"
                dangerouslySetInnerHTML={{ __html: stk.svgContent }}
              />
              <span className="font-bold text-[11px] text-zen-ink block truncate w-full">
                {t(stk.nameVi, stk.nameEn)}
              </span>
              <span className="text-[10px] text-zen-moss-dark font-medium capitalize mt-0.5">
                {stk.triggerEvent.replace("_", " ")}
              </span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
