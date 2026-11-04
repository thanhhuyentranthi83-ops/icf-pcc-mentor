"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import { getOrders, updateOrderStatus, addAuditLog, getUsers } from "@/lib/db";
import { Order, UserProfile } from "@/types";
import { formatVnd } from "@/lib/vietqr";
import {
  CreditCard,
  CheckCircle,
  XCircle,
  Eye,
  Clock,
  Check,
  Search,
  Filter
} from "lucide-react";

export default function AdminOrdersPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user } = useAuth();

  const [orders, setOrders] = useState<Order[]>([]);
  const [usersMap, setUsersMap] = useState<Map<string, UserProfile>>(new Map());
  const [selectedReceipt, setSelectedReceipt] = useState<string | null>(null);
  const [filterStatus, setFilterStatus] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [actionSuccessMsg, setActionSuccessMsg] = useState("");

  useEffect(() => {
    loadData();
  }, []);

  const loadData = () => {
    const ordList = getOrders();
    setOrders(ordList);
    const uList = getUsers();
    setUsersMap(new Map(uList.map((u) => [u.id, u])));
  };

  const handleApprove = (orderId: string, orderCode: string) => {
    const updated = updateOrderStatus(orderId, "approved", user.id);
    if (updated) {
      loadData();
      addAuditLog(user.id, user.fullName, "Duyệt đơn hàng", `Duyệt đơn ${orderCode} cho học viên ${updated.userId}`);
      ringBell();
      showMsg(t(`Đã duyệt đơn ${orderCode} và kích hoạt gói thành công!`, `Order ${orderCode} approved & tier activated!`));
    }
  };

  const handleReject = (orderId: string, orderCode: string) => {
    const updated = updateOrderStatus(orderId, "rejected", user.id);
    if (updated) {
      loadData();
      addAuditLog(user.id, user.fullName, "Từ chối đơn hàng", `Từ chối đơn ${orderCode}`);
      ringBell();
      showMsg(t(`Đã từ chối đơn ${orderCode}.`, `Order ${orderCode} rejected.`));
    }
  };

  const showMsg = (msg: string) => {
    setActionSuccessMsg(msg);
    setTimeout(() => setActionSuccessMsg(""), 3500);
  };

  const filteredOrders = orders.filter((o) => {
    if (filterStatus !== "all" && o.status !== filterStatus) return false;
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      const codeMatch = o.orderCode.toLowerCase().includes(q);
      const student = usersMap.get(o.userId);
      const nameMatch = student?.fullName.toLowerCase().includes(q);
      return codeMatch || nameMatch;
    }
    return true;
  });

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="font-serif text-2xl font-bold text-zen-ink">
            {t("Quản Lý Đơn Hàng & Duyệt Thanh Toán", "Orders & Payment Management")}
          </h1>
          <p className="text-xs text-zen-muted mt-1">
            {t(
              "Đối chiếu giao dịch chuyển khoản VietQR, kiểm tra ảnh biên lai và bấm Duyệt để kích hoạt gói học viên.",
              "Review VietQR bank transfers, inspect receipt proofs, and approve to instantly activate subscriptions."
            )}
          </p>
        </div>
      </div>

      {actionSuccessMsg && (
        <div className="p-3.5 rounded-2xl bg-emerald-50 border border-emerald-300 text-xs font-semibold text-emerald-800 flex items-center gap-2 animate-in fade-in duration-200">
          <Check className="w-4 h-4 text-emerald-600" />
          <span>{actionSuccessMsg}</span>
        </div>
      )}

      {/* Filter & Search Bar */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-4 shadow-zen-card flex flex-wrap items-center justify-between gap-3 text-xs">
        <div className="flex items-center gap-3 w-full sm:w-auto">
          <div className="flex items-center gap-2 bg-white rounded-xl border border-zen-border px-3 py-1.5 shadow-zen-subtle">
            <Search className="w-3.5 h-3.5 text-zen-muted" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder={t("Tìm theo mã đơn hoặc tên học viên...", "Search order code or student...")}
              className="bg-transparent text-xs text-zen-ink focus:outline-none w-48"
            />
          </div>

          <div className="flex items-center gap-1.5">
            <Filter className="w-3.5 h-3.5 text-zen-muted" />
            <select
              value={filterStatus}
              onChange={(e) => setFilterStatus(e.target.value)}
              className="bg-white border border-zen-border rounded-xl px-3 py-1.5 text-xs text-zen-ink focus:outline-none"
            >
              <option value="all">{t("Tất cả trạng thái", "All Statuses")}</option>
              <option value="pending_approval">{t("Chờ phê duyệt", "Pending Review")}</option>
              <option value="approved">{t("Đã duyệt", "Approved")}</option>
              <option value="rejected">{t("Từ chối", "Rejected")}</option>
            </select>
          </div>
        </div>

        <span className="text-zen-muted font-medium">
          {filteredOrders.length} {t("đơn hàng", "orders")}
        </span>
      </div>

      {/* Orders Table */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper shadow-zen-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-zen-border/70 bg-zen-surface/60 text-zen-muted uppercase text-[10px] font-bold tracking-wider">
                <th className="py-3 px-4">{t("Mã Đơn", "Order Code")}</th>
                <th className="py-3 px-4">{t("Học Viên", "Student")}</th>
                <th className="py-3 px-4">{t("Gói Học", "Tier")}</th>
                <th className="py-3 px-4">{t("Số Tiền", "Amount")}</th>
                <th className="py-3 px-4">{t("Thời Gian", "Date")}</th>
                <th className="py-3 px-4">{t("Biên Lai", "Receipt")}</th>
                <th className="py-3 px-4">{t("Trạng Thái", "Status")}</th>
                <th className="py-3 px-4 text-right">{t("Hành Động", "Actions")}</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-zen-border/40 text-zen-ink">
              {filteredOrders.map((ord) => {
                const student = usersMap.get(ord.userId);
                return (
                  <tr key={ord.id} className="hover:bg-zen-surface/40 transition-colors">
                    <td className="py-3 px-4 font-mono font-bold text-zen-moss-dark">
                      {ord.orderCode}
                    </td>
                    <td className="py-3 px-4 font-medium">
                      <div>{student?.fullName || ord.userId}</div>
                      <div className="text-[10px] text-zen-muted">{student?.email}</div>
                    </td>
                    <td className="py-3 px-4 capitalize font-medium">
                      {ord.tierId.replace("_", " ")}
                    </td>
                    <td className="py-3 px-4 font-bold">
                      {formatVnd(ord.amount)}
                    </td>
                    <td className="py-3 px-4 text-zen-muted text-[11px]">
                      {new Date(ord.createdAt).toLocaleString("vi-VN")}
                    </td>
                    <td className="py-3 px-4">
                      {ord.receiptUrl ? (
                        <button
                          onClick={() => setSelectedReceipt(ord.receiptUrl || null)}
                          className="flex items-center gap-1 text-[11px] font-semibold text-zen-moss-dark hover:underline"
                        >
                          <Eye className="w-3.5 h-3.5" />
                          <span>{t("Xem ảnh", "Inspect")}</span>
                        </button>
                      ) : (
                        <span className="text-zen-muted text-[11px]">Chưa tải</span>
                      )}
                    </td>
                    <td className="py-3 px-4">
                      <span
                        className={`inline-block px-2.5 py-0.5 rounded-full text-[10px] font-bold ${
                          ord.status === "approved"
                            ? "bg-emerald-100 text-emerald-800"
                            : ord.status === "pending_approval"
                            ? "bg-amber-100 text-amber-800"
                            : "bg-rose-100 text-rose-800"
                        }`}
                      >
                        {ord.status === "approved"
                          ? t("Đã duyệt", "Approved")
                          : ord.status === "pending_approval"
                          ? t("Chờ duyệt", "Pending")
                          : t("Từ chối", "Rejected")}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-right">
                      {ord.status === "pending_approval" ? (
                        <div className="flex items-center justify-end gap-1.5">
                          <button
                            onClick={() => handleApprove(ord.id, ord.orderCode)}
                            className="px-2.5 py-1 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-[11px] shadow-sm transition-colors"
                          >
                            {t("Duyệt", "Approve")}
                          </button>
                          <button
                            onClick={() => handleReject(ord.id, ord.orderCode)}
                            className="px-2.5 py-1 rounded-xl border border-rose-200 bg-rose-50 hover:bg-rose-100 text-rose-700 font-semibold text-[11px] transition-colors"
                          >
                            {t("Từ chối", "Reject")}
                          </button>
                        </div>
                      ) : (
                        <span className="text-[11px] text-zen-muted">
                          {ord.status === "approved" ? t("Hoàn tất", "Completed") : t("Đã đóng", "Closed")}
                        </span>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Receipt Preview Modal */}
      {selectedReceipt && (
        <div
          onClick={() => setSelectedReceipt(null)}
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
        >
          <div
            onClick={(e) => e.stopPropagation()}
            className="bg-white rounded-3xl p-6 max-w-lg w-full space-y-4 shadow-zen-floating border border-zen-border"
          >
            <div className="flex justify-between items-center pb-2 border-b">
              <h3 className="font-serif font-bold text-sm text-zen-ink">
                {t("Biên Lai Chuyển Khoản Ngân Hàng", "Bank Transfer Receipt Preview")}
              </h3>
              <button
                onClick={() => setSelectedReceipt(null)}
                className="text-xs text-zen-muted hover:text-zen-ink font-bold"
              >
                ✕
              </button>
            </div>
            <div className="rounded-2xl overflow-hidden bg-zen-surface p-2 flex items-center justify-center max-h-[400px]">
              <img
                src={selectedReceipt}
                alt="Receipt"
                className="max-h-[380px] object-contain rounded-xl"
              />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
