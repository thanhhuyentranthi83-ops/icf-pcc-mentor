"use client";

import React, { useState, useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import { Sparkles, ArrowRight, ShieldCheck, Mail, User, CheckCircle2, AlertCircle } from "lucide-react";

export default function LoginPage() {
  return (
    <React.Suspense fallback={<div className="min-h-[60vh] flex items-center justify-center text-xs text-zen-muted">Đang tải trang đăng nhập...</div>}>
      <LoginFormContent />
    </React.Suspense>
  );
}

function LoginFormContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const returnUrl = searchParams.get("returnUrl") || "/curriculum";
  const { t } = useLanguage();
  const { user, login, logout, isAuthenticated, loading } = useAuth();

  const [email, setEmail] = useState("");
  const [fullName, setFullName] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");
  const [successMsg, setSuccessMsg] = useState("");

  const handleLoginSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg("");
    setSuccessMsg("");

    if (!email.trim() || !email.includes("@")) {
      setErrorMsg(t("Vui lòng nhập địa chỉ email hợp lệ", "Please enter a valid email address"));
      return;
    }

    setSubmitting(true);
    try {
      const res = await login(email.trim(), fullName.trim() || undefined);
      if (res.success) {
        setSuccessMsg(t("Đăng nhập thành công! Đang chuyển hướng...", "Login successful! Redirecting..."));
        setTimeout(() => {
          router.push(returnUrl);
        }, 600);
      } else {
        setErrorMsg(res.error || t("Không thể đăng nhập, vui lòng thử lại.", "Login failed, please try again."));
      }
    } catch (err: any) {
      setErrorMsg(err.message || t("Đã xảy ra lỗi, vui lòng thử lại.", "An error occurred."));
    } finally {
      setSubmitting(false);
    }
  };

  const handleQuickDemo = async (demoEmail: string, demoName: string) => {
    setEmail(demoEmail);
    setFullName(demoName);
    setSubmitting(true);
    try {
      const res = await login(demoEmail, demoName);
      if (res.success) {
        router.push(returnUrl);
      }
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="min-h-[82vh] flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-md rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card space-y-6">
        {/* Brand Eyebrow */}
        <div className="text-center space-y-2">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs font-semibold">
            <Sparkles className="w-3.5 h-3.5 text-zen-ochre" />
            <span>Học Coaching • Zen Edition</span>
          </div>
          <h1 className="font-serif text-2xl sm:text-3xl font-bold text-zen-ink">
            {t("Đăng nhập hoặc tạo tài khoản", "Sign in or Create Account")}
          </h1>
          <p className="text-xs sm:text-sm text-zen-wood leading-relaxed">
            {t(
              "Nhập email để lưu tiến độ từng bài học, đếm đóa sen và đồng bộ trên mọi thiết bị.",
              "Enter your email to permanently save lesson progress, count lotuses, and sync across devices."
            )}
          </p>
        </div>

        {/* If already authenticated */}
        {isAuthenticated && user && (
          <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-xs text-emerald-900 space-y-3">
            <div className="flex items-center gap-2 font-semibold">
              <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
              <span>{t("Bạn đang đăng nhập với tài khoản:", "Currently signed in as:")}</span>
            </div>
            <div className="pl-6 space-y-0.5">
              <div className="font-bold text-zen-ink">{user.fullName}</div>
              <div className="text-zen-muted">{user.email}</div>
              <div className="text-[10px] uppercase font-semibold text-zen-ochre-dark mt-1">
                {user.role === "super_admin" ? "🛡️ Quản trị viên" : `Học viên • ${user.tier}`}
              </div>
            </div>
            <div className="pt-2 flex items-center gap-2">
              <Link
                href={returnUrl}
                className="flex-1 py-2 rounded-xl bg-zen-moss-dark text-white text-xs font-semibold text-center hover:bg-zen-moss-dark/90 transition-all shadow-zen-subtle"
              >
                {t("Tiếp tục vào học →", "Continue to Lesson →")}
              </Link>
              <button
                onClick={logout}
                className="py-2 px-3 rounded-xl border border-emerald-300 bg-white text-emerald-800 text-xs font-semibold hover:bg-emerald-100/50 transition-all"
              >
                {t("Đổi tài khoản", "Switch")}
              </button>
            </div>
          </div>
        )}

        {/* Error or Success notification */}
        {errorMsg && (
          <div className="p-3 rounded-xl bg-rose-50 border border-rose-200 text-xs text-rose-800 flex items-center gap-2">
            <AlertCircle className="w-4 h-4 text-rose-600 shrink-0" />
            <span>{errorMsg}</span>
          </div>
        )}

        {successMsg && (
          <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-xs text-emerald-800 flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
            <span>{successMsg}</span>
          </div>
        )}

        {/* Login Form */}
        {(!isAuthenticated || !user) && (
          <form onSubmit={handleLoginSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-zen-ink mb-1.5 flex items-center gap-1.5">
                <Mail className="w-3.5 h-3.5 text-zen-wood" />
                <span>{t("Email học viên", "Student Email")} *</span>
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="name@example.com"
                required
                className="w-full px-3.5 py-2.5 rounded-xl border border-zen-border bg-white text-xs sm:text-sm text-zen-ink focus:outline-none focus:border-zen-moss-dark shadow-zen-subtle transition-all"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-zen-ink mb-1.5 flex items-center gap-1.5">
                <User className="w-3.5 h-3.5 text-zen-wood" />
                <span>{t("Họ và tên (dành cho học viên mới)", "Full Name (Optional for new students)")}</span>
              </label>
              <input
                type="text"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                placeholder="Nguyễn Văn A"
                className="w-full px-3.5 py-2.5 rounded-xl border border-zen-border bg-white text-xs sm:text-sm text-zen-ink focus:outline-none focus:border-zen-moss-dark shadow-zen-subtle transition-all"
              />
            </div>

            <button
              type="submit"
              disabled={submitting}
              className="w-full py-3 rounded-xl bg-zen-moss-dark hover:bg-zen-moss-dark/90 text-white text-xs sm:text-sm font-semibold transition-all shadow-zen-subtle flex items-center justify-center gap-2 disabled:opacity-60"
            >
              <span>{submitting ? t("Đang xử lý...", "Processing...") : t("Tiếp Tục Với Email Này →", "Continue with Email →")}</span>
            </button>
          </form>
        )}

        {/* Demo Quick Selectors for Convenience */}
        <div className="pt-4 border-t border-zen-border/50 text-center space-y-2">
          <p className="text-[11px] font-semibold text-zen-muted uppercase tracking-wider">
            {t("Lối vào nhanh thử nghiệm (1-Click):", "Quick Demo Logins:")}
          </p>
          <div className="grid grid-cols-2 gap-2 text-xs">
            <button
              type="button"
              onClick={() => handleQuickDemo("admin@pcc.vn", "Super Admin Tâm An")}
              className="p-2 rounded-xl border border-amber-300 bg-amber-50 hover:bg-amber-100/70 text-amber-900 font-medium transition-colors text-left flex items-center gap-1.5"
            >
              <ShieldCheck className="w-3.5 h-3.5 text-amber-700 shrink-0" />
              <div className="truncate">
                <div className="font-bold truncate">Quản Trị Viên</div>
                <div className="text-[10px] text-amber-700 truncate">admin@pcc.vn</div>
              </div>
            </button>

            <button
              type="button"
              onClick={() => handleQuickDemo("student.1m@pcc.vn", "Học Viên Thu Hương")}
              className="p-2 rounded-xl border border-zen-border bg-white hover:bg-zen-surface text-zen-ink font-medium transition-colors text-left flex items-center gap-1.5"
            >
              <User className="w-3.5 h-3.5 text-zen-moss-dark shrink-0" />
              <div className="truncate">
                <div className="font-bold truncate">Học Viên Thu Hương</div>
                <div className="text-[10px] text-zen-muted truncate">student.1m@pcc.vn</div>
              </div>
            </button>
          </div>
        </div>

        {/* Return home link */}
        <div className="text-center pt-2">
          <Link
            href="/"
            className="text-xs text-zen-muted hover:text-zen-moss-dark font-medium transition-colors"
          >
            ← {t("Quay về Trang chủ", "Back to Home")}
          </Link>
        </div>
      </div>
    </div>
  );
}
