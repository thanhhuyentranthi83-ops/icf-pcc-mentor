"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import { getUsers, getOrders, getSections } from "@/lib/db";
import { formatVnd } from "@/lib/vietqr";
import { Users, CreditCard, Layers, Clock, ArrowRight, TrendingUp } from "lucide-react";

export default function AdminDashboardPage() {
  const { t } = useLanguage();
  const { user } = useAuth();

  const [students, setStudents] = useState<any[]>([]);
  const [orders, setOrders] = useState<any[]>([]);
  const [sections, setSections] = useState<any[]>([]);

  useEffect(() => {
    setStudents(getUsers().filter((u) => u.role === "student"));
    setOrders(getOrders());
    setSections(getSections());
  }, []);

  const pendingOrders = orders.filter((o) => o.status === "pending_approval");
  const approvedOrders = orders.filter((o) => o.status === "approved");
  const totalRevenue = approvedOrders.reduce((sum, o) => sum + (o.amount || 0), 0);

  const tierCounts = {
    free: students.filter((s) => s.tier === "free").length,
    "1_month": students.filter((s) => s.tier === "1_month").length,
    "6_months": students.filter((s) => s.tier === "6_months").length,
    "12_months": students.filter((s) => s.tier === "12_months").length
  };

  return (
    <div className="space-y-6">
      {/* Welcome Banner */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card">
        <h1 className="font-serif text-2xl font-bold text-zen-ink">
          {t("Tổng Quan Vận Hành", "Operational Dashboard")}
        </h1>
        <p className="text-xs text-zen-muted mt-1">
          {t(
            "Theo dõi học viên, doanh thu chuyển khoản VietQR và trạng thái nội dung ôn thi PCC.",
            "Monitor students, VietQR bank transfer revenue, and PCC curriculum status."
          )}
        </p>
      </div>

      {/* 4 Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Total Students */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-5 shadow-zen-card flex items-center justify-between">
          <div>
            <span className="text-xs text-zen-muted block">{t("Tổng học viên", "Total Students")}</span>
            <span className="font-serif text-2xl font-bold text-zen-ink mt-1 block">
              {students.length}
            </span>
            <span className="text-[11px] text-zen-moss-dark font-medium">
              +12% {t("tháng này", "this month")}
            </span>
          </div>
          <div className="w-10 h-10 rounded-2xl bg-zen-moss/20 text-zen-moss-dark flex items-center justify-center">
            <Users className="w-5 h-5" />
          </div>
        </div>

        {/* Pending Orders */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-5 shadow-zen-card flex items-center justify-between">
          <div>
            <span className="text-xs text-zen-muted block">{t("Đơn chờ duyệt", "Pending Orders")}</span>
            <span className="font-serif text-2xl font-bold text-amber-700 mt-1 block">
              {pendingOrders.length}
            </span>
            <Link
              href="/admin/orders"
              className="text-[11px] text-amber-800 font-semibold hover:underline"
            >
              {t("Duyệt ngay →", "Review now →")}
            </Link>
          </div>
          <div className="w-10 h-10 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center">
            <Clock className="w-5 h-5" />
          </div>
        </div>

        {/* Total Revenue */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-5 shadow-zen-card flex items-center justify-between">
          <div>
            <span className="text-xs text-zen-muted block">{t("Doanh thu đã duyệt", "Approved Revenue")}</span>
            <span className="font-serif text-xl font-bold text-zen-moss-dark mt-1 block">
              {formatVnd(totalRevenue)}
            </span>
            <span className="text-[11px] text-zen-muted">
              {approvedOrders.length} {t("đơn thành công", "orders")}
            </span>
          </div>
          <div className="w-10 h-10 rounded-2xl bg-zen-moss/20 text-zen-moss-dark flex items-center justify-center">
            <CreditCard className="w-5 h-5" />
          </div>
        </div>

        {/* Curriculum Sections */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-5 shadow-zen-card flex items-center justify-between">
          <div>
            <span className="text-xs text-zen-muted block">{t("Tổng mục nội dung", "Sections & Modules")}</span>
            <span className="font-serif text-2xl font-bold text-zen-ink mt-1 block">
              {sections.length}
            </span>
            <span className="text-[11px] text-zen-muted">{t("8 Năng lực + Đạo đức", "8 Comps + Ethics")}</span>
          </div>
          <div className="w-10 h-10 rounded-2xl bg-zen-wood/15 text-zen-wood flex items-center justify-center">
            <Layers className="w-5 h-5" />
          </div>
        </div>
      </div>

      {/* Tier Distribution & Pending Orders Quick View */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Tier Distribution */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
          <h3 className="font-serif text-base font-bold text-zen-ink">
            {t("Phân bố Học viên theo Gói", "Student Tier Distribution")}
          </h3>
          <div className="space-y-3">
            {[
              { key: "12_months", label: t("Gói 12 Tháng (Trọn Vẹn)", "12-Month Mastery"), count: tierCounts["12_months"], color: "bg-zen-ochre" },
              { key: "6_months", label: t("Gói 6 Tháng (Đồng Hành)", "6-Month Companion"), count: tierCounts["6_months"], color: "bg-zen-moss-dark" },
              { key: "1_month", label: t("Gói 1 Tháng (Tinh Tấn)", "1-Month Diligence"), count: tierCounts["1_month"], color: "bg-zen-moss" },
              { key: "free", label: t("Gói Khởi Đầu (Miễn phí)", "Free Starter"), count: tierCounts["free"], color: "bg-gray-400" },
            ].map((tItem) => (
              <div key={tItem.key} className="space-y-1">
                <div className="flex justify-between text-xs font-medium">
                  <span className="text-zen-ink">{tItem.label}</span>
                  <span className="text-zen-muted">{tItem.count} học viên</span>
                </div>
                <div className="w-full h-2 rounded-full bg-zen-border/50 overflow-hidden">
                  <div
                    className={`h-full ${tItem.color}`}
                    style={{
                      width: `${Math.max(10, (tItem.count / Math.max(1, students.length)) * 100)}%`
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Pending Orders Box */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-serif text-base font-bold text-zen-ink">
              {t("Đơn Hàng Chờ Phê Duyệt", "Pending Payment Confirmations")}
            </h3>
            <Link
              href="/admin/orders"
              className="text-xs text-amber-800 font-semibold hover:underline flex items-center gap-1"
            >
              <span>{t("Xem tất cả", "View all")}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          {pendingOrders.length === 0 ? (
            <p className="text-xs text-zen-muted py-8 text-center">
              {t("Không có đơn hàng nào đang chờ duyệt.", "No pending orders at this moment.")}
            </p>
          ) : (
            <div className="space-y-2.5">
              {pendingOrders.slice(0, 3).map((ord) => (
                <div
                  key={ord.id}
                  className="flex items-center justify-between p-3 rounded-2xl bg-amber-50/70 border border-amber-200 text-xs"
                >
                  <div>
                    <span className="font-mono font-bold text-amber-950 block">{ord.orderCode}</span>
                    <span className="text-[11px] text-amber-800">
                      Gói: {ord.tierId} • {formatVnd(ord.amount)}
                    </span>
                  </div>
                  <Link
                    href="/admin/orders"
                    className="px-3 py-1 rounded-xl bg-amber-800 text-white font-semibold text-[11px] hover:bg-amber-900 transition-colors"
                  >
                    {t("Đối chiếu", "Inspect")}
                  </Link>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
