"use client";

import React from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";

export default function Footer() {
  const { t } = useLanguage();

  return (
    <footer className="mt-20 border-t border-zen-border/70 bg-zen-paper/60 text-zen-muted text-xs py-10 transition-colors">
      <div className="max-w-6xl mx-auto px-4 flex flex-col items-center text-center space-y-4">
        {/* Zen Lotus Emblem */}
        <div className="w-8 h-8 rounded-full bg-zen-moss/10 flex items-center justify-center text-zen-moss-dark">
          <span className="text-sm font-serif">蓮</span>
        </div>

        {/* Quiet Affirmation */}
        <p className="font-serif italic text-zen-ink/70 max-w-md text-sm">
          {t(
            "“Thở vào tâm tĩnh lặng, thở ra miệng mỉm cười. Ta an trú trong hiện tại, giây phút đẹp tuyệt vời.”",
            "“Breathing in, I calm my body and mind. Breathing out, I smile. Dwelling in the present moment.”"
          )}
        </p>

        {/* Mandatory Legal & Inspiration Disclaimers */}
        <div className="max-w-2xl text-[11px] leading-relaxed text-zen-muted/90 bg-zen-surface/60 rounded-2xl p-4 border border-zen-border/40">
          <p className="font-medium text-zen-ink/80 mb-1">
            {t("Lưu ý về nguồn cảm hứng & Bản quyền:", "Inspiration & Trademark Notice:")}
          </p>
          <p>
            {t(
              "Giao diện lấy cảm hứng từ tinh thần Zen, không liên kết chính thức với Làng Mai. Mọi lời nhắn nhủ trong ứng dụng là nội dung tự biên soạn theo tinh thần chánh niệm trong khai vấn.",
              "Interface inspired by Zen aesthetics, not officially affiliated with Plum Village. All mindfulness messages are original coaching reflections."
            )}
          </p>
          <p className="mt-1">
            {t(
              "Đây là ứng dụng ôn thi độc lập, không phải sản phẩm chính thức của ICF (International Coaching Federation). ICF® và PCC® là các nhãn hiệu đã đăng ký của International Coaching Federation.",
              "This is an independent exam preparation mentor and not an official product of the ICF. ICF® and PCC® are registered trademarks of the International Coaching Federation."
            )}
          </p>
        </div>

        {/* Quick Footer Links */}
        <div className="flex flex-wrap justify-center gap-6 text-zen-ink/70 font-medium pt-2">
          <Link href="/" className="hover:text-zen-moss-dark transition-colors">
            {t("Trang chủ", "Home")}
          </Link>
          <Link href="/mock-exam" className="hover:text-zen-moss-dark transition-colors">
            {t("Thi thử PCC", "PCC Mock")}
          </Link>
          <Link href="/pricing" className="hover:text-zen-moss-dark transition-colors">
            {t("Bảng giá & VietQR", "Pricing & VietQR")}
          </Link>
          <Link href="/admin/login" className="hover:text-zen-moss-dark transition-colors">
            {t("Cổng Quản Trị", "Admin Portal")}
          </Link>
          <Link href="/design" className="hover:text-zen-moss-dark transition-colors">
            {t("Hệ Thống Thiết Kế (Design System)", "Design System")}
          </Link>
        </div>

        <p className="text-[11px] text-zen-muted/80">
          © {new Date().getFullYear()} Mentor thi ICF PCC • {t("Vì ước mơ đưa Coaching thành lối sống.", "Making Coaching a Way of Life.")}
        </p>
      </div>
    </footer>
  );
}
