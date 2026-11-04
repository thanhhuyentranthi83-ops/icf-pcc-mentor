"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import { getSystemSettings } from "@/lib/db";
import { formatVnd } from "@/lib/vietqr";
import { Tier } from "@/types";
import { Sparkles, Check, ArrowRight, ShieldCheck, HeartHandshake } from "lucide-react";

export default function PricingPage() {
  const router = useRouter();
  const { t } = useLanguage();
  const { user } = useAuth();
  const settings = getSystemSettings();

  const [promoCode, setPromoCode] = useState("");
  const [discountPercent, setDiscountPercent] = useState(0);
  const [promoError, setPromoError] = useState("");
  const [promoSuccess, setPromoSuccess] = useState("");

  const handleApplyPromo = (e: React.FormEvent) => {
    e.preventDefault();
    setPromoError("");
    setPromoSuccess("");

    const code = promoCode.trim().toUpperCase();
    if (!code) return;

    if (code === "PCC2026") {
      setDiscountPercent(20);
      setPromoSuccess(t("Áp dụng mã giảm 20% thành công!", "Applied 20% discount code!"));
    } else if (code === "ZENCOACH") {
      setDiscountPercent(15);
      setPromoSuccess(t("Áp dụng mã giảm 15% thành công!", "Applied 15% discount code!"));
    } else if (code === "LANGMAI") {
      setDiscountPercent(10);
      setPromoSuccess(t("Áp dụng mã giảm 10% thành công!", "Applied 10% discount code!"));
    } else {
      setPromoError(t("Mã giảm giá không hợp lệ hoặc đã hết hạn", "Invalid or expired promo code"));
    }
  };

  const handleSelectTier = (tier: Tier) => {
    if (tier === "free") {
      router.push("/");
    } else {
      const codeQuery = discountPercent > 0 ? `&code=${encodeURIComponent(promoCode.trim().toUpperCase())}` : "";
      router.push(`/checkout?tier=${tier}${codeQuery}`);
    }
  };

  const tiers: Tier[] = ["free", "1_month", "6_months", "12_months"];

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 sm:py-12 space-y-10">
      {/* Header */}
      <div className="text-center max-w-2xl mx-auto space-y-3">
        <span className="text-xs font-bold uppercase tracking-wider text-zen-moss-dark bg-zen-moss/15 px-3 py-1 rounded-full">
          {t("Gói Học Phí & Đồng Hành", "Study Tiers & Companionship")}
        </span>
        <h1 className="font-serif text-3xl sm:text-4xl font-bold text-zen-ink">
          {t("Đầu Tư Cho Sự Nghiệp Khai Vấn Chuyên Nghiệp", "Invest in Your Professional Coaching Journey")}
        </h1>
        <p className="text-xs sm:text-sm text-zen-muted leading-relaxed">
          {t(
            "Mở khóa toàn bộ 8 năng lực cốt lõi, ngân hàng tình huống SJT và đề thi thử chuẩn quốc tế với giọng văn dịu dàng, không áp lực.",
            "Unlock all 8 core competencies, SJT question banks, and standard mock exams in a serene, supportive atmosphere."
          )}
        </p>
      </div>

      {/* Expiration gentle reminder if on paid tier */}
      {user.tier !== "free" && user.tierExpiresAt && (
        <div className="max-w-xl mx-auto p-4 rounded-2xl bg-zen-surface border border-zen-moss/30 flex items-center justify-between text-xs text-zen-ink">
          <div className="flex items-center gap-2.5">
            <HeartHandshake className="w-5 h-5 text-zen-moss-dark shrink-0" />
            <div>
              <p className="font-semibold">
                {t("Gói hiện tại của bạn:", "Your current tier:")}{" "}
                <span className="capitalize text-zen-moss-dark">{user.tier.replace("_", " ")}</span>
              </p>
              <p className="text-[11px] text-zen-muted">
                {t("Thời hạn đến ngày:", "Valid until:")}{" "}
                {new Date(user.tierExpiresAt).toLocaleDateString("vi-VN")}
              </p>
            </div>
          </div>
          <span className="text-[11px] font-medium text-zen-wood">
            {t("Chúc bạn học vui", "Enjoy your practice")}
          </span>
        </div>
      )}

      {/* Promo Code Box */}
      <div className="max-w-md mx-auto">
        <form
          onSubmit={handleApplyPromo}
          className="flex items-center gap-2 p-2 rounded-2xl bg-zen-paper border border-zen-border shadow-zen-subtle"
        >
          <input
            type="text"
            value={promoCode}
            onChange={(e) => setPromoCode(e.target.value)}
            placeholder={t("Nhập mã giảm giá (VD: PCC2026, ZENCOACH)", "Enter coupon code (e.g. PCC2026)")}
            className="flex-1 px-3 py-1.5 bg-transparent text-xs text-zen-ink uppercase placeholder:normal-case placeholder:text-zen-muted focus:outline-none font-semibold"
          />
          <button
            type="submit"
            className="px-4 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-colors shrink-0"
          >
            {t("Áp dụng", "Apply")}
          </button>
        </form>
        {promoSuccess && (
          <p className="text-[11px] font-medium text-emerald-700 mt-2 text-center">
            {promoSuccess}
          </p>
        )}
        {promoError && (
          <p className="text-[11px] font-medium text-rose-600 mt-2 text-center">
            {promoError}
          </p>
        )}
      </div>

      {/* 4 Tier Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {tiers.map((tierKey) => {
          const info = settings.pricing[tierKey];
          const isBestValue = tierKey === "12_months";
          const isPopular = tierKey === "6_months";

          const originalPrice = info.price;
          const discountedPrice =
            discountPercent > 0 && originalPrice > 0
              ? originalPrice * (1 - discountPercent / 100)
              : originalPrice;

          return (
            <div
              key={tierKey}
              className={`rounded-3xl border bg-zen-paper p-6 shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col justify-between relative ${
                isBestValue
                  ? "border-zen-ochre ring-2 ring-zen-ochre/30 bg-gradient-to-b from-amber-50/40 to-zen-paper"
                  : isPopular
                  ? "border-zen-moss-dark ring-1 ring-zen-moss-dark/20"
                  : "border-zen-border"
              }`}
            >
              {/* Badge */}
              {isBestValue && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-0.5 rounded-full bg-zen-ochre text-white text-[10px] font-bold uppercase tracking-wider shadow-sm">
                  {t("Giá Trị Tốt Nhất", "Best Value")}
                </div>
              )}
              {isPopular && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-0.5 rounded-full bg-zen-moss-dark text-white text-[10px] font-bold uppercase tracking-wider shadow-sm">
                  {t("Được Chọn Nhiều Nhất", "Most Popular")}
                </div>
              )}

              <div>
                <h3 className="font-serif text-lg font-bold text-zen-ink">
                  {t(info.nameVi, info.nameEn)}
                </h3>

                {/* Price Display */}
                <div className="my-4">
                  {info.price === 0 ? (
                    <div className="text-3xl font-serif font-bold text-zen-moss-dark">
                      {t("Miễn Phí", "Free")}
                    </div>
                  ) : (
                    <div>
                      {discountPercent > 0 && (
                        <span className="text-xs text-zen-muted line-through block">
                          {formatVnd(originalPrice)}
                        </span>
                      )}
                      <div className="text-2xl sm:text-3xl font-serif font-bold text-zen-ink">
                        {formatVnd(discountedPrice)}
                      </div>
                      <span className="text-[11px] text-zen-muted">
                        {tierKey === "1_month"
                          ? t("/ tháng", "/ month")
                          : tierKey === "6_months"
                          ? t("/ 6 tháng", "/ 6 months")
                          : t("/ 12 tháng", "/ 12 months")}
                      </span>
                    </div>
                  )}
                </div>

                {/* Features List */}
                <div className="space-y-2.5 pt-4 border-t border-zen-border/50 text-xs">
                  {info.featuresVi.map((feat, i) => (
                    <div key={i} className="flex items-start gap-2 text-zen-ink/90 leading-relaxed">
                      <Check className="w-4 h-4 text-zen-moss-dark shrink-0 mt-0.5" />
                      <span>{t(feat, info.featuresEn[i] || feat)}</span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Action Button */}
              <div className="pt-6 mt-6 border-t border-zen-border/40">
                <button
                  onClick={() => handleSelectTier(tierKey)}
                  className={`w-full py-3 rounded-2xl font-semibold text-xs transition-all shadow-zen-subtle flex items-center justify-center gap-1.5 ${
                    isBestValue
                      ? "bg-zen-ochre hover:bg-zen-ochre-dark text-white"
                      : isPopular
                      ? "bg-zen-moss-dark hover:bg-zen-moss-deep text-white"
                      : "bg-zen-surface hover:bg-zen-border text-zen-ink"
                  }`}
                >
                  <span>
                    {tierKey === "free"
                      ? t("Bắt đầu học thử", "Start Learning")
                      : t("Chọn gói & Thanh toán", "Select & Pay")}
                  </span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          );
        })}
      </div>

      {/* Guarantee Notice */}
      <div className="max-w-2xl mx-auto rounded-3xl bg-zen-surface/60 border border-zen-border/70 p-6 text-center space-y-2">
        <div className="flex items-center justify-center gap-2 text-zen-moss-dark font-semibold text-xs">
          <ShieldCheck className="w-4 h-4" />
          <span>{t("Cam Kết Chất Lượng & Hỗ Trợ Tận Tâm", "Quality Assurance & Dedicated Support")}</span>
        </div>
        <p className="text-xs text-zen-muted leading-relaxed">
          {t(
            "Thanh toán chuyển khoản ngân hàng an toàn qua mã VietQR tự động. Sau khi duyệt đơn, gói học được kích hoạt tức thì kèm thông báo.",
            "Secure manual bank transfer via dynamic VietQR codes. Upon approval, your tier is activated immediately."
          )}
        </p>
      </div>
    </div>
  );
}
