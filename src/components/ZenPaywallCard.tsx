"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth, EntitlementCheckStatus } from "@/context/AuthContext";
import {
  Lock,
  Sparkles,
  ArrowRight,
  Clock,
  ShieldCheck,
  Send,
  CheckCircle2,
  BookOpen
} from "lucide-react";

interface ZenPaywallCardProps {
  status: EntitlementCheckStatus;
  targetTitle?: string;
  className?: string;
}

export default function ZenPaywallCard({ status, targetTitle, className = "" }: ZenPaywallCardProps) {
  const { t } = useLanguage();
  const pathname = usePathname();
  const { isAuthenticated, requestEnrollment, user } = useAuth();
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [userNote, setUserNote] = useState("");
  const [errMsg, setErrMsg] = useState("");

  const requiredPkgId = status.requiredPackageId || "pkg-foundation";
  const requiredPkgName = status.requiredPackageName || "Gói Nền Tảng Khai Vấn";
  const isExpired = status.reason === "expired";

  const handleRequest = async (type: "register" | "renew") => {
    try {
      setSubmitting(true);
      setErrMsg("");
      const res = await requestEnrollment(requiredPkgId, type, userNote);
      if (res.success) {
        setSubmitted(true);
      } else {
        setErrMsg(res.error || "Không thể gửi yêu cầu.");
      }
    } catch {
      setErrMsg("Lỗi kết nối máy chủ.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div
      className={`rounded-3xl border border-amber-200/80 bg-gradient-to-b from-amber-50/50 via-zen-paper to-zen-paper p-8 text-center max-w-xl mx-auto shadow-zen-card ${className}`}
    >
      <div className="w-12 h-12 rounded-2xl bg-amber-100 border border-amber-200 text-amber-900 flex items-center justify-center mx-auto mb-4 shadow-2xs">
        {isExpired ? <Clock className="w-6 h-6 text-amber-800" /> : <Lock className="w-6 h-6 text-amber-800" />}
      </div>

      <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-100/70 border border-amber-200 text-amber-900 text-[11px] font-semibold mb-3">
        <Sparkles className="w-3.5 h-3.5 text-amber-700" />
        <span>
          {isExpired
            ? t("Gói Học Đã Hết Hạn", "Package Expired")
            : t(`Nội Dung Thuộc ${requiredPkgName}`, `Included in ${requiredPkgName}`)}
        </span>
      </div>

      <h3 className="font-serif text-xl font-bold text-zen-ink mb-2">
        {isExpired
          ? t("Thời Gian Học Của Gói Đã Kết Thúc", "Your Package Has Expired")
          : targetTitle
          ? t(`Mở Khóa Toàn Bộ Nội Dung: ${targetTitle}`, `Unlock Full Content: ${targetTitle}`)
          : t("Nội Dung Dành Cho Học Viên Theo Gói", "Content Reserved for Enrolled Students")}
      </h3>

      <p className="text-xs text-zen-muted leading-relaxed max-w-md mx-auto mb-6">
        {isExpired
          ? t(
              `Gói học "${requiredPkgName}" của bạn đã hết hạn vào ${
                status.expiresAt ? new Date(status.expiresAt).toLocaleDateString("vi-VN") : "gần đây"
              }. Mọi tiến độ học, ghi chú chiêm nghiệm và hoa sen của bạn đều được bảo toàn 100%. Bạn có thể gửi yêu cầu gia hạn để tiếp tục bài học.`,
              `Your package has expired. All your progress, reflections, and blooming lotuses are 100% safely preserved. You can submit a renewal request to resume.`
            )
          : !isAuthenticated
          ? t(
              "Bài học này thuộc chương trình chuyên sâu. Vui lòng đăng nhập bằng tài khoản email học viên hoặc gửi yêu cầu kích hoạt gói học để truy cập.",
              "This lesson belongs to the in-depth program. Please sign in with your student email or request package activation to continue."
            )
          : t(
              `Tài khoản (${user.email}) hiện chưa được mở khóa gói "${requiredPkgName}". Bạn có thể gửi yêu cầu đăng ký ngay bên dưới để ban quản trị duyệt và kích hoạt quyền học.`,
              `Your account (${user.email}) is not enrolled in "${requiredPkgName}". Submit an activation request below for admin approval.`
            )}
      </p>

      {/* Action Area */}
      {!isAuthenticated ? (
        <div className="space-y-3">
          <Link
            href={`/login?returnUrl=${encodeURIComponent(pathname)}`}
            className="inline-flex items-center justify-center gap-2 w-full sm:w-auto px-6 py-3 rounded-2xl bg-amber-900 text-white font-semibold text-xs hover:bg-amber-950 transition-colors shadow-sm"
          >
            <span>{t("Đăng nhập để vào học", "Sign in to continue")}</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
          <div>
            <Link
              href="/curriculum?module=mod-1&lesson=mod1-les1"
              className="text-[11px] text-amber-800 hover:text-amber-950 font-medium underline inline-flex items-center gap-1"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>{t("Học thử bài miễn phí: Năng lực Đạo đức (Module 1)", "Try free lesson: Ethical Practice")}</span>
            </Link>
          </div>
        </div>
      ) : submitted ? (
        <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs font-medium space-y-1">
          <div className="flex items-center justify-center gap-1.5 font-bold text-sm">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            <span>{t("Đã gửi yêu cầu thành công!", "Request Submitted!")}</span>
          </div>
          <p className="text-[11px] text-emerald-800 leading-relaxed">
            {t(
              "Ban quản trị đã nhận được yêu cầu của bạn. Sau khi được duyệt, quyền truy cập sẽ tự động mở mà không mất bất kỳ tiến độ nào.",
              "The administrator has received your request. Once approved, access will be granted seamlessly."
            )}
          </p>
        </div>
      ) : (
        <div className="space-y-3 max-w-sm mx-auto">
          <input
            type="text"
            value={userNote}
            onChange={(e) => setUserNote(e.target.value)}
            placeholder={t("Ghi chú (ví dụ: đã chuyển khoản / mã ưu đãi)", "Optional note for admin...")}
            className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs focus:outline-hidden focus:border-amber-700"
          />

          {errMsg && <div className="text-[11px] text-rose-700 font-medium">{errMsg}</div>}

          <button
            onClick={() => handleRequest(isExpired ? "renew" : "register")}
            disabled={submitting}
            className="inline-flex items-center justify-center gap-2 w-full px-6 py-2.5 rounded-2xl bg-amber-900 text-white font-semibold text-xs hover:bg-amber-950 transition-colors shadow-sm disabled:opacity-50"
          >
            <Send className="w-3.5 h-3.5" />
            <span>
              {submitting
                ? t("Đang gửi yêu cầu...", "Submitting...")
                : isExpired
                ? t("Yêu Cầu Gia Hạn Gói Này", "Request Package Renewal")
                : t("Gửi Yêu Cầu Đăng Ký Gói Này", "Request Package Activation")}
            </span>
          </button>

          <div>
            <Link
              href="/curriculum?module=mod-1&lesson=mod1-les1"
              className="text-[11px] text-amber-800 hover:text-amber-950 font-medium underline inline-flex items-center gap-1"
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>{t("Xem bài học thử miễn phí (Module 1)", "View free preview lesson")}</span>
            </Link>
          </div>
        </div>
      )}

      {/* Preservation Assurance Footer */}
      <div className="pt-6 mt-6 border-t border-amber-200/50 flex items-center justify-center gap-1.5 text-[11px] text-zen-muted">
        <ShieldCheck className="w-3.5 h-3.5 text-zen-moss-dark" />
        <span>{t("Cam kết bảo toàn 100% dữ liệu mốc học tập và hoa sen của bạn", "100% progress and lotus data preserved")}</span>
      </div>
    </div>
  );
}
