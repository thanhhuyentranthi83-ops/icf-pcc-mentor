"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import { Bell, BellOff, Globe, Search, Sparkles, User, ShieldCheck, ChevronDown, Check } from "lucide-react";

export default function Header() {
  const pathname = usePathname();
  const { lang, toggleLang, t } = useLanguage();
  const { soundEnabled, toggleSound, ringBell } = useSound();
  const { user, allDemoUsers, switchUser, isSuperAdmin, isEditor, isBilling } = useAuth();
  const [userDropdownOpen, setUserDropdownOpen] = useState(false);

  const isAdminSection = pathname.startsWith("/admin");

  return (
    <header className="sticky top-0 z-40 bg-zen-bg/90 backdrop-blur-md border-b border-zen-border/70 transition-colors">
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        {/* Brand */}
        <Link href="/" className="flex items-center gap-2.5 group">
          <div className="w-9 h-9 rounded-full bg-zen-moss-dark text-white flex items-center justify-center shadow-zen-subtle group-hover:scale-105 transition-transform">
            <span className="text-base font-serif">蓮</span>
          </div>
          <div>
            <span className="font-serif font-semibold text-lg text-zen-ink tracking-tight flex items-center gap-1.5">
              Mentor thi ICF PCC
              <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-zen-moss/20 text-zen-moss-dark font-sans font-medium">
                Zen Edition
              </span>
            </span>
            <p className="text-[11px] text-zen-muted -mt-0.5">
              {t("Luyện thi chứng chỉ quốc tế", "Credentialing Exam Prep")}
            </p>
          </div>
        </Link>

        {/* Center / Navigation Links on Desktop */}
        <nav className="hidden md:flex items-center gap-5 text-sm text-zen-ink/80 font-medium">
          <Link
            href="/"
            className={`hover:text-zen-moss-dark transition-colors ${
              pathname === "/" ? "text-zen-moss-dark font-semibold" : ""
            }`}
          >
            {t("Trang chủ", "Home")}
          </Link>
          <Link
            href="/mock-exam"
            className={`hover:text-zen-moss-dark transition-colors ${
              pathname === "/mock-exam" ? "text-zen-moss-dark font-semibold" : ""
            }`}
          >
            {t("Thi thử tổng PCC", "PCC Mock Exam")}
          </Link>
          <Link
            href="/search"
            className={`hover:text-zen-moss-dark transition-colors ${
              pathname === "/search" ? "text-zen-moss-dark font-semibold" : ""
            }`}
          >
            {t("Tra cứu", "Search")}
          </Link>
          <Link
            href="/pricing"
            className={`hover:text-zen-moss-dark transition-colors ${
              pathname === "/pricing" ? "text-zen-moss-dark font-semibold" : ""
            }`}
          >
            {t("Gói học phí", "Pricing")}
          </Link>
          <Link
            href="/design"
            className={`hover:text-zen-moss-dark transition-colors ${
              pathname === "/design" ? "text-zen-moss-dark font-semibold" : ""
            }`}
          >
            {t("Design System", "Design")}
          </Link>
        </nav>

        {/* Action Controls */}
        <div className="flex items-center gap-2">
          {/* Bell Sound Trigger */}
          <button
            onClick={() => {
              ringBell();
            }}
            title={t("Thỉnh chuông chánh niệm", "Ring mindfulness bell")}
            className="p-2 rounded-xl text-zen-moss-dark hover:bg-zen-surface transition-colors"
          >
            <Sparkles className="w-4 h-4 text-zen-ochre" />
          </button>

          {/* Sound Toggle */}
          <button
            onClick={toggleSound}
            title={soundEnabled ? t("Tắt tiếng chuông", "Mute bell") : t("Bật tiếng chuông", "Unmute bell")}
            className={`p-2 rounded-xl transition-colors ${
              soundEnabled ? "text-zen-moss-dark hover:bg-zen-surface" : "text-gray-400 hover:bg-zen-surface"
            }`}
          >
            {soundEnabled ? <Bell className="w-4 h-4" /> : <BellOff className="w-4 h-4" />}
          </button>

          {/* Language Switch */}
          <button
            onClick={toggleLang}
            className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-zen-border bg-zen-paper hover:bg-zen-surface text-xs font-semibold text-zen-ink transition-all shadow-zen-subtle"
            title={t("Chuyển sang tiếng Anh", "Switch to Vietnamese")}
          >
            <Globe className="w-3.5 h-3.5 text-zen-moss-dark" />
            <span>{lang.toUpperCase()}</span>
          </button>

          {/* Search Button (Mobile & Desktop) */}
          <Link
            href="/search"
            className="p-2 rounded-xl border border-zen-border bg-zen-paper hover:bg-zen-surface text-zen-ink transition-colors shadow-zen-subtle"
            title={t("Tìm kiếm toàn cục", "Global Search")}
          >
            <Search className="w-4 h-4 text-zen-muted" />
          </Link>

          {/* User / Demo Role Switcher */}
          <div className="relative">
            <button
              onClick={() => setUserDropdownOpen(!userDropdownOpen)}
              className="flex items-center gap-1.5 pl-2 pr-2.5 py-1 rounded-xl border border-zen-border bg-zen-paper hover:bg-zen-surface transition-colors shadow-zen-subtle"
            >
              <div className="w-6 h-6 rounded-full bg-zen-moss/20 flex items-center justify-center text-zen-moss-dark text-xs font-semibold">
                {user.fullName.slice(0, 1)}
              </div>
              <span className="text-xs font-medium text-zen-ink hidden sm:inline max-w-[90px] truncate">
                {user.fullName}
              </span>
              <ChevronDown className="w-3 h-3 text-zen-muted" />
            </button>

            {userDropdownOpen && (
              <div
                className="absolute right-0 mt-2 w-64 rounded-2xl bg-white border border-zen-border shadow-zen-floating p-2 z-50 animate-in fade-in zoom-in-95 duration-150"
                onClick={() => setUserDropdownOpen(false)}
              >
                <div className="px-3 py-2 border-b border-zen-border/50 mb-1">
                  <p className="text-xs font-semibold text-zen-ink">{user.fullName}</p>
                  <p className="text-[11px] text-zen-muted">{user.email}</p>
                  <div className="mt-1 flex items-center gap-1.5">
                    <span className="text-[10px] uppercase font-bold px-1.5 py-0.5 rounded-md bg-zen-ochre/15 text-zen-ochre-dark">
                      {user.role}
                    </span>
                    <span className="text-[10px] px-1.5 py-0.5 rounded-md bg-zen-moss/15 text-zen-moss-dark">
                      {user.tier === "free" ? "Free Tier" : user.tier.replace("_", " ")}
                    </span>
                  </div>
                </div>

                {/* Profile Link */}
                <Link
                  href="/profile"
                  className="flex items-center gap-2 px-3 py-2 text-xs font-medium text-zen-ink hover:bg-zen-surface rounded-xl transition-colors"
                >
                  <User className="w-3.5 h-3.5 text-zen-moss-dark" />
                  {t("Hồ sơ & Vườn sen của tôi", "My Profile & Lotus Garden")}
                </Link>

                {/* Admin Portal Link */}
                {(isSuperAdmin || isEditor || isBilling) && (
                  <Link
                    href="/admin"
                    className="flex items-center gap-2 px-3 py-2 text-xs font-medium text-amber-900 bg-amber-50 hover:bg-amber-100/70 rounded-xl transition-colors mt-1"
                  >
                    <ShieldCheck className="w-3.5 h-3.5 text-amber-700" />
                    {t("Vào Trang Quản Trị (Admin)", "Enter Admin Portal")}
                  </Link>
                )}

                {/* Demo Switcher Quick Menu */}
                <div className="mt-2 pt-2 border-t border-zen-border/50">
                  <p className="px-3 text-[10px] font-semibold text-zen-muted uppercase tracking-wider mb-1">
                    {t("Chuyển vai trò thử nghiệm", "Switch Demo Role")}
                  </p>
                  <div className="space-y-0.5 max-h-48 overflow-y-auto">
                    {allDemoUsers.map((u) => (
                      <button
                        key={u.id}
                        onClick={() => switchUser(u.id)}
                        className={`w-full flex items-center justify-between px-3 py-1.5 text-left text-xs rounded-lg transition-colors ${
                          u.id === user.id
                            ? "bg-zen-moss/15 text-zen-moss-dark font-semibold"
                            : "hover:bg-zen-surface text-zen-ink/80"
                        }`}
                      >
                        <div>
                          <div>{u.fullName}</div>
                          <div className="text-[10px] text-zen-muted capitalize">
                            {u.role.replace("_", " ")} • {u.tier}
                          </div>
                        </div>
                        {u.id === user.id && <Check className="w-3.5 h-3.5 text-zen-moss-dark" />}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}
