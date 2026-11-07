"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import {
  LayoutDashboard,
  Layers,
  Users,
  CreditCard,
  Settings,
  Smile,
  FileText,
  ShieldAlert,
  ArrowLeft,
  ShieldCheck
} from "lucide-react";

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const { t } = useLanguage();
  const { user, isSuperAdmin, isEditor, isBilling, switchUser, isAuthenticated, isGuest, loading } = useAuth();

  // If on admin/login, do not wrap with sidebar
  if (pathname === "/admin/login") {
    return <>{children}</>;
  }

  if (loading) {
    return (
      <div className="min-h-[50vh] flex flex-col items-center justify-center space-y-3 py-16 text-center">
        <div className="w-8 h-8 rounded-full border-2 border-amber-800/30 border-t-amber-800 animate-spin" />
        <p className="text-xs text-zen-muted font-medium">
          {t("Đang kiểm tra quyền quản trị viên...", "Checking administrator privileges...")}
        </p>
      </div>
    );
  }

  // Guard: if guest or unauthenticated
  if (!isAuthenticated || isGuest) {
    return (
      <div className="max-w-md mx-auto my-16 p-8 rounded-3xl border border-amber-300 bg-amber-50 text-center space-y-4">
        <ShieldAlert className="w-12 h-12 text-amber-700 mx-auto" />
        <h2 className="font-serif text-xl font-bold text-amber-900">
          {t("Yêu Cầu Đăng Nhập Quản Trị", "Admin Login Required")}
        </h2>
        <p className="text-xs text-amber-800 leading-relaxed">
          {t(
            "Vui lòng đăng nhập bằng tài khoản email được cấp quyền quản trị để truy cập khu vực này.",
            "Please sign in with an authorized administrator email to access this area."
          )}
        </p>
        <div className="pt-2 flex flex-col gap-2">
          <Link
            href={`/login?returnUrl=${encodeURIComponent(pathname)}`}
            className="w-full py-2.5 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-colors shadow-sm"
          >
            {t("Đăng nhập tài khoản quản trị", "Sign In to Admin Account")}
          </Link>
          <Link
            href="/"
            className="w-full py-2 rounded-2xl border border-amber-300 bg-white text-amber-900 text-xs font-semibold hover:bg-amber-100/50 transition-colors"
          >
            {t("Về Trang Chủ Học Viên", "Back to Student Portal")}
          </Link>
        </div>
      </div>
    );
  }

  // Guard: if user is student
  if (user.role === "student") {
    return (
      <div className="max-w-md mx-auto my-16 p-8 rounded-3xl border border-amber-300 bg-amber-50 text-center space-y-4">
        <ShieldAlert className="w-12 h-12 text-amber-700 mx-auto" />
        <h2 className="font-serif text-xl font-bold text-amber-900">
          {t("Khu Vực Dành Cho Quản Trị Viên", "Admin Restricted Area")}
        </h2>
        <p className="text-xs text-amber-800 leading-relaxed">
          {t(
            "Tài khoản hiện tại của bạn là Học viên (Student) nên không có quyền truy cập trang quản trị. Để truy cập, vui lòng đăng nhập bằng email quản trị viên đã được phân quyền.",
            "You are currently logged in as a Student. Access to the admin portal is restricted. Please sign in with an authorized administrator account."
          )}
        </p>
        <div className="pt-2 flex flex-col gap-2">
          <Link
            href={`/login?returnUrl=${encodeURIComponent(pathname)}`}
            className="w-full py-2.5 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-colors shadow-sm"
          >
            {t("Đổi sang tài khoản Quản trị viên", "Switch to Administrator Account")}
          </Link>
          <Link
            href="/"
            className="w-full py-2 rounded-2xl border border-amber-300 bg-white text-amber-900 text-xs font-semibold hover:bg-amber-100/50 transition-colors"
          >
            {t("Về Trang Chủ Học Viên", "Back to Student Portal")}
          </Link>
        </div>
      </div>
    );
  }

  const navLinks = [
    {
      href: "/admin",
      labelVi: "Tổng Quan (Dashboard)",
      labelEn: "Dashboard",
      icon: LayoutDashboard,
      allowed: true
    },
    {
      href: "/admin/sections",
      labelVi: "Cây Nội Dung & 6 Tab",
      labelEn: "Curriculum & Tabs",
      icon: Layers,
      allowed: isEditor || isSuperAdmin
    },
    {
      href: "/admin/orders",
      labelVi: "Đơn Hàng & VietQR",
      labelEn: "Orders & Billing",
      icon: CreditCard,
      allowed: isBilling || isSuperAdmin
    },
    {
      href: "/admin/students",
      labelVi: "Quản Lý Học Viên",
      labelEn: "Students",
      icon: Users,
      allowed: true
    },
    {
      href: "/admin/stickers",
      labelVi: "Sticker & Lời Nhắn",
      labelEn: "Stickers & Quotes",
      icon: Smile,
      allowed: isEditor || isSuperAdmin
    },
    {
      href: "/admin/settings",
      labelVi: "Cấu Hình Ngân Hàng & Gói",
      labelEn: "Settings & Bank Info",
      icon: Settings,
      allowed: isSuperAdmin
    },
    {
      href: "/admin/audit-logs",
      labelVi: "Nhật Ký (Audit Log)",
      labelEn: "Audit Logs",
      icon: FileText,
      allowed: isSuperAdmin
    }
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 py-6">
      {/* Top Admin Bar */}
      <div className="flex items-center justify-between pb-4 mb-6 border-b border-zen-border">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-xl bg-amber-900 text-white flex items-center justify-center font-bold text-xs">
            <ShieldCheck className="w-4 h-4" />
          </div>
          <div>
            <span className="font-serif font-bold text-sm text-zen-ink block">
              {t("Trang Quản Trị Hệ Thống", "Admin Dashboard")}
            </span>
            <span className="text-[11px] text-zen-muted">
              {t("Người vận hành:", "Operator:")} {user.fullName} ({user.role})
            </span>
          </div>
        </div>

        <Link
          href="/"
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-zen-border bg-zen-paper hover:bg-zen-surface text-xs font-semibold text-zen-ink transition-colors"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>{t("Xem Giao Diện Học Viên", "View Student App")}</span>
        </Link>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">
        {/* Admin Sidebar Navigation */}
        <aside className="lg:col-span-1 space-y-1">
          {navLinks
            .filter((item) => item.allowed)
            .map((item) => {
              const Icon = item.icon;
              const isActive = pathname === item.href;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className={`flex items-center gap-2.5 px-3.5 py-2.5 rounded-2xl text-xs font-semibold transition-all ${
                    isActive
                      ? "bg-amber-900 text-white shadow-sm"
                      : "text-zen-ink hover:bg-zen-surface bg-zen-paper border border-zen-border/50"
                  }`}
                >
                  <Icon className="w-4 h-4 shrink-0" />
                  <span className="truncate">{t(item.labelVi, item.labelEn)}</span>
                </Link>
              );
            })}
        </aside>

        {/* Content Area */}
        <main className="lg:col-span-4">{children}</main>
      </div>
    </div>
  );
}
