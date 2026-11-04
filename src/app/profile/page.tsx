"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import {
  getLotusGarden,
  getExamSessions,
  getOrders,
  getStickers,
  LotusGardenState,
  ExamSessionRecord
} from "@/lib/db";
import { Order, Sticker } from "@/types";
import LotusGarden from "@/components/LotusGarden";
import {
  User,
  Sparkles,
  Award,
  CreditCard,
  Moon,
  Sun,
  ShieldCheck,
  CheckCircle,
  Clock,
  ChevronRight
} from "lucide-react";
import { formatVnd } from "@/lib/vietqr";

export default function ProfilePage() {
  const { t } = useLanguage();
  const { user, updateCurrentUser } = useAuth();

  const [garden, setGarden] = useState<LotusGardenState>({
    seedsPlanted: 12,
    sproutsGrown: 8,
    lotusesBloomed: 4,
    butterfliesUnlocked: 2,
    dragonfliesUnlocked: 1
  });
  const [examSessions, setExamSessions] = useState<ExamSessionRecord[]>([]);
  const [orders, setOrders] = useState<Order[]>([]);
  const [stickers, setStickers] = useState<Sticker[]>([]);
  const [activeTab, setActiveTab] = useState<"progress" | "orders" | "settings">("progress");

  useEffect(() => {
    setGarden(getLotusGarden(user.id));
    setExamSessions(getExamSessions(user.id));
    setOrders(getOrders().filter((o) => o.userId === user.id));
    setStickers(getStickers());
  }, [user.id]);

  const toggleMinimalMode = () => {
    updateCurrentUser({ minimalMode: !user.minimalMode });
  };

  const handleSelectStickerPack = (code: string) => {
    updateCurrentUser({ selectedStickerPack: code });
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 sm:py-12 space-y-8">
      {/* Header Profile Card */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card flex flex-col sm:flex-row items-center sm:items-start justify-between gap-6">
        <div className="flex flex-col sm:flex-row items-center gap-4 text-center sm:text-left">
          <div className="w-16 h-16 rounded-full bg-zen-moss-dark text-white flex items-center justify-center font-serif text-2xl font-bold shadow-zen-subtle">
            {user.fullName.slice(0, 1)}
          </div>
          <div>
            <h1 className="font-serif text-2xl font-bold text-zen-ink">{user.fullName}</h1>
            <p className="text-xs text-zen-muted mt-0.5">{user.email}</p>
            <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2 mt-2">
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-zen-ochre/15 text-zen-ochre-dark">
                {user.role}
              </span>
              <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-zen-moss/15 text-zen-moss-dark">
                {user.tier === "free" ? "Gói Miễn Phí" : `Gói ${user.tier.replace("_", " ")}`}
              </span>
            </div>
          </div>
        </div>

        {/* Upgrade / Pricing button */}
        <Link
          href="/pricing"
          className="px-5 py-2.5 rounded-2xl bg-zen-ochre hover:bg-zen-ochre-dark text-white text-xs font-semibold shadow-zen-subtle transition-all shrink-0 flex items-center gap-1.5"
        >
          <Sparkles className="w-4 h-4" />
          <span>{t("Nâng cấp hoặc Gia hạn", "Upgrade or Renew")}</span>
        </Link>
      </div>

      {/* Tabs */}
      <div className="flex items-center gap-2 border-b border-zen-border/70 pb-2">
        <button
          onClick={() => setActiveTab("progress")}
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all ${
            activeTab === "progress"
              ? "bg-zen-moss-dark text-white shadow-sm"
              : "bg-zen-paper hover:bg-zen-surface text-zen-ink border border-zen-border/70"
          }`}
        >
          🌸 {t("Tiến Độ & Vườn Sen", "Progress & Garden")}
        </button>
        <button
          onClick={() => setActiveTab("orders")}
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all ${
            activeTab === "orders"
              ? "bg-zen-moss-dark text-white shadow-sm"
              : "bg-zen-paper hover:bg-zen-surface text-zen-ink border border-zen-border/70"
          }`}
        >
          💳 {t("Lịch Sử Thanh Toán", "Order History")} ({orders.length})
        </button>
        <button
          onClick={() => setActiveTab("settings")}
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all ${
            activeTab === "settings"
              ? "bg-zen-moss-dark text-white shadow-sm"
              : "bg-zen-paper hover:bg-zen-surface text-zen-ink border border-zen-border/70"
          }`}
        >
          ⚙️ {t("Cài Đặt Chánh Niệm", "Mindful Settings")}
        </button>
      </div>

      {/* Tab: Progress & Garden */}
      {activeTab === "progress" && (
        <div className="space-y-6">
          <LotusGarden garden={garden} streakCount={user.streakCount} />

          {/* Exam History Card */}
          <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card">
            <h3 className="font-serif text-lg font-bold text-zen-ink mb-4 flex items-center gap-2">
              <Award className="w-5 h-5 text-zen-ochre" />
              <span>{t("Lịch sử làm bài thi thử SJT", "Mock Exam History")}</span>
            </h3>

            {examSessions.length === 0 ? (
              <p className="text-xs text-zen-muted py-4 text-center">
                {t(
                  "Bạn chưa làm bài thi thử nào. Hãy vào 'Thi thử tổng PCC' để thử sức!",
                  "You haven't completed any mock exams yet. Take the PCC Mock Exam to get started!"
                )}
              </p>
            ) : (
              <div className="space-y-3">
                {examSessions.map((ex) => (
                  <div
                    key={ex.id}
                    className="flex flex-wrap items-center justify-between gap-3 p-4 rounded-2xl bg-zen-surface/60 border border-zen-border text-xs"
                  >
                    <div>
                      <span className="font-bold text-zen-ink block">
                        {ex.examType === "full_pcc_mock"
                          ? t("Thi thử tổng PCC Chuẩn ICF", "Full ICF PCC Mock Exam")
                          : t("Thi thử theo chuyên đề", "Section Mock Exam")}
                      </span>
                      <span className="text-[11px] text-zen-muted">
                        {new Date(ex.completedAt).toLocaleString("vi-VN")} •{" "}
                        {Math.floor(ex.durationSeconds / 60)} {t("phút", "mins")}
                      </span>
                    </div>

                    <div className="flex items-center gap-4">
                      <div className="text-right">
                        <span className="text-xs text-zen-muted block">
                          BEST: {ex.correctBestCount} | WORST: {ex.correctWorstCount}
                        </span>
                        <span className="font-serif font-bold text-base text-zen-moss-dark">
                          {ex.score}%
                        </span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}

      {/* Tab: Orders */}
      {activeTab === "orders" && (
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
          <h3 className="font-serif text-lg font-bold text-zen-ink mb-2">
            {t("Lịch sử đơn hàng & Gói học", "Order & Subscription History")}
          </h3>

          {orders.length === 0 ? (
            <p className="text-xs text-zen-muted py-6 text-center">
              {t("Bạn chưa có đơn hàng nào.", "No orders yet.")}
            </p>
          ) : (
            <div className="space-y-3">
              {orders.map((ord) => (
                <div
                  key={ord.id}
                  className="flex flex-wrap items-center justify-between gap-3 p-4 rounded-2xl bg-zen-surface/60 border border-zen-border text-xs"
                >
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="font-mono font-bold text-zen-moss-dark">{ord.orderCode}</span>
                      <span className="text-[11px] font-medium text-zen-muted">
                        {new Date(ord.createdAt).toLocaleDateString("vi-VN")}
                      </span>
                    </div>
                    <span className="text-[11px] text-zen-muted capitalize mt-0.5 block">
                      Gói: {ord.tierId.replace("_", " ")}
                    </span>
                  </div>

                  <div className="flex items-center gap-4">
                    <span className="font-bold text-sm text-zen-ink">
                      {formatVnd(ord.amount)}
                    </span>
                    <span
                      className={`px-3 py-1 rounded-xl text-[11px] font-bold ${
                        ord.status === "approved"
                          ? "bg-emerald-100 text-emerald-800"
                          : ord.status === "pending_approval"
                          ? "bg-amber-100 text-amber-800"
                          : "bg-gray-100 text-gray-700"
                      }`}
                    >
                      {ord.status === "approved"
                        ? t("Đã duyệt", "Approved")
                        : ord.status === "pending_approval"
                        ? t("Chờ duyệt", "Pending")
                        : ord.status}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Tab: Settings */}
      {activeTab === "settings" && (
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card space-y-6">
          <h3 className="font-serif text-lg font-bold text-zen-ink border-b border-zen-border/50 pb-3">
            {t("Tùy Chọn Chánh Niệm & Giao Diện", "Mindful Preferences")}
          </h3>

          {/* Minimalist mode */}
          <div className="flex items-center justify-between py-2 border-b border-zen-border/40">
            <div>
              <p className="text-xs font-bold text-zen-ink">
                {t("Chế độ tối giản (Không áp lực gamification)", "Minimalist Mode (No pressure)")}
              </p>
              <p className="text-[11px] text-zen-muted max-w-sm">
                {t(
                  "Ẩn huy hiệu và bộ đếm chuỗi ngày để bạn tập trung hoàn toàn vào việc học tĩnh lặng.",
                  "Hides badges and streak counter to foster calm, self-paced learning."
                )}
              </p>
            </div>
            <button
              onClick={toggleMinimalMode}
              className={`w-12 h-6 rounded-full transition-colors relative ${
                user.minimalMode ? "bg-zen-moss-dark" : "bg-zen-border"
              }`}
            >
              <div
                className={`w-5 h-5 rounded-full bg-white transition-transform absolute top-0.5 ${
                  user.minimalMode ? "left-6" : "left-0.5"
                }`}
              />
            </button>
          </div>

          {/* Choose favorite sticker */}
          <div>
            <h4 className="text-xs font-bold text-zen-ink mb-3">
              {t("Chọn Bạn Đồng Hành Chánh Niệm (Sticker yêu thích):", "Select Favorite Mindful Companion:")}
            </h4>
            <div className="grid grid-cols-3 sm:grid-cols-6 gap-3">
              {stickers.map((stk) => (
                <button
                  key={stk.id}
                  onClick={() => handleSelectStickerPack(stk.code)}
                  className={`p-3 rounded-2xl border text-center transition-all flex flex-col items-center ${
                    user.selectedStickerPack === stk.code
                      ? "border-zen-moss-dark bg-zen-moss/15 shadow-sm"
                      : "border-zen-border bg-white hover:bg-zen-surface"
                  }`}
                >
                  <div
                    className="w-10 h-10 mb-1"
                    dangerouslySetInnerHTML={{ __html: stk.svgContent }}
                  />
                  <span className="text-[10px] font-medium text-zen-ink line-clamp-1">
                    {t(stk.nameVi, stk.nameEn)}
                  </span>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
