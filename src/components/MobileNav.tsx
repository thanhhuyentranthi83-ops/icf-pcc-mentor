"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLanguage } from "@/context/LanguageContext";
import { Home, BookOpen, GraduationCap, Search, Sparkles, User } from "lucide-react";

export default function MobileNav() {
  const pathname = usePathname();
  const { t } = useLanguage();

  const navItems = [
    { href: "/", label: t("Trang chủ", "Home"), icon: Home },
    { href: "/curriculum", label: t("Lộ trình", "Curriculum"), icon: GraduationCap },
    { href: "/mock-exam", label: t("Luyện thi", "Exam"), icon: BookOpen },
    { href: "/journal", label: t("Sổ học tập", "Journal"), icon: Sparkles },
    { href: "/profile", label: t("Tài khoản", "Account"), icon: User }
  ];

  return (
    <nav className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-zen-bg/95 backdrop-blur-md border-t border-zen-border/70 pb-safe">
      <div className="flex items-center justify-around h-16 px-2">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex flex-col items-center justify-center flex-1 h-full min-w-[44px] min-h-[44px] transition-colors ${
                isActive ? "text-zen-moss-dark font-semibold" : "text-zen-muted hover:text-zen-ink"
              }`}
            >
              <div
                className={`p-1 rounded-xl transition-transform ${
                  isActive ? "bg-zen-moss/20 scale-105" : ""
                }`}
              >
                <Icon className="w-5 h-5 stroke-[1.75]" />
              </div>
              <span className="text-[10px] mt-0.5 tracking-tight">{item.label}</span>
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
