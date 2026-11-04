"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import { ShieldCheck, ArrowLeft, KeyRound } from "lucide-react";

export default function AdminLoginPage() {
  const router = useRouter();
  const { t } = useLanguage();
  const { switchUser } = useAuth();

  const [email, setEmail] = useState("admin@pcc.vn");
  const [password, setPassword] = useState("••••••••");

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (email.includes("editor")) {
      switchUser("usr-editor");
    } else if (email.includes("billing")) {
      switchUser("usr-billing");
    } else {
      switchUser("usr-admin");
    }
    router.push("/admin");
  };

  const handleQuickLogin = (role: "admin" | "editor" | "billing") => {
    if (role === "admin") {
      switchUser("usr-admin");
    } else if (role === "editor") {
      switchUser("usr-editor");
    } else {
      switchUser("usr-billing");
    }
    router.push("/admin");
  };

  return (
    <div className="min-h-[80vh] flex items-center justify-center px-4 py-12">
      <div className="w-full max-w-md rounded-3xl border border-zen-border bg-zen-paper p-8 shadow-zen-card space-y-6">
        <Link
          href="/"
          className="inline-flex items-center gap-1.5 text-xs text-zen-muted hover:text-zen-ink transition-colors"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>{t("Về Trang Chủ Học Viên", "Back to Student Portal")}</span>
        </Link>

        <div className="text-center space-y-2">
          <div className="w-12 h-12 rounded-2xl bg-amber-100 text-amber-900 mx-auto flex items-center justify-center shadow-zen-subtle">
            <ShieldCheck className="w-6 h-6" />
          </div>
          <h1 className="font-serif text-2xl font-bold text-zen-ink">
            {t("Cổng Quản Trị Hệ Thống", "Admin Management Portal")}
          </h1>
          <p className="text-xs text-zen-muted">
            {t("Dành riêng cho Super Admin, Biên tập viên và Kế toán", "Dedicated to Super Admin, Editor and Billing roles")}
          </p>
        </div>

        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-zen-ink mb-1.5">
              {t("Email quản trị viên", "Admin Email")}
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink focus:outline-none focus:border-zen-moss-dark"
              required
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-zen-ink mb-1.5">
              {t("Mật khẩu", "Password")}
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink focus:outline-none focus:border-zen-moss-dark"
              required
            />
          </div>

          <button
            type="submit"
            className="w-full py-3 rounded-2xl bg-amber-900 hover:bg-amber-950 text-white text-xs font-semibold transition-all shadow-zen-subtle"
          >
            {t("Đăng Nhập Quản Trị", "Login to Admin Portal")}
          </button>
        </form>

        {/* 1-Click Demo Logins */}
        <div className="pt-4 border-t border-zen-border/50 text-center space-y-2">
          <span className="text-[10px] font-bold uppercase tracking-wider text-zen-muted block">
            {t("Đăng nhập nhanh thử nghiệm theo vai trò:", "Quick Demo Login by Role:")}
          </span>
          <div className="grid grid-cols-3 gap-2">
            <button
              onClick={() => handleQuickLogin("admin")}
              className="p-2 rounded-xl border border-amber-300 bg-amber-50/70 hover:bg-amber-100 text-[11px] font-semibold text-amber-900 transition-colors"
            >
              Super Admin
            </button>
            <button
              onClick={() => handleQuickLogin("editor")}
              className="p-2 rounded-xl border border-blue-300 bg-blue-50/70 hover:bg-blue-100 text-[11px] font-semibold text-blue-900 transition-colors"
            >
              Editor
            </button>
            <button
              onClick={() => handleQuickLogin("billing")}
              className="p-2 rounded-xl border border-emerald-300 bg-emerald-50/70 hover:bg-emerald-100 text-[11px] font-semibold text-emerald-900 transition-colors"
            >
              Billing
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
