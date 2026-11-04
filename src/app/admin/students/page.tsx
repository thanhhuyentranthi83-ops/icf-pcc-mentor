"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import { getUsers, saveUser, addAuditLog } from "@/lib/db";
import { UserProfile, Tier } from "@/types";
import { Users, Search, Edit3, KeyRound, Check, Shield } from "lucide-react";

export default function AdminStudentsPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user: currentAdmin } = useAuth();

  const [users, setUsers] = useState<UserProfile[]>([]);
  const [search, setSearch] = useState("");
  const [editingUserId, setEditingUserId] = useState<string | null>(null);
  const [selectedTier, setSelectedTier] = useState<Tier>("free");
  const [msg, setMsg] = useState("");

  useEffect(() => {
    loadUsers();
  }, []);

  const loadUsers = () => {
    setUsers(getUsers());
  };

  const handleOpenEdit = (u: UserProfile) => {
    setEditingUserId(u.id);
    setSelectedTier(u.tier);
  };

  const handleSaveTier = (u: UserProfile) => {
    const updated = { ...u, tier: selectedTier };
    if (selectedTier !== "free") {
      const d = new Date();
      d.setMonth(d.getMonth() + (selectedTier === "1_month" ? 1 : selectedTier === "6_months" ? 6 : 12));
      updated.tierExpiresAt = d.toISOString();
    } else {
      updated.tierExpiresAt = null;
    }
    saveUser(updated);
    loadUsers();
    setEditingUserId(null);
    addAuditLog(currentAdmin.id, currentAdmin.fullName, "Đổi gói học viên", `Đổi gói của ${u.fullName} thành ${selectedTier}`);
    ringBell();
    setMsg(t("Đã cập nhật gói học viên thành công!", "Student tier updated!"));
    setTimeout(() => setMsg(""), 3000);
  };

  const filteredUsers = users.filter((u) => {
    if (!search.trim()) return true;
    const q = search.toLowerCase();
    return u.fullName.toLowerCase().includes(q) || u.email.toLowerCase().includes(q);
  });

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="font-serif text-2xl font-bold text-zen-ink">
            {t("Quản Lý Học Viên & Quyền Học Tập", "Student & Account Management")}
          </h1>
          <p className="text-xs text-zen-muted mt-1">
            {t(
              "Xem danh sách tài khoản, tiến độ học, điều chỉnh gói thủ công và cấp quyền truy cập.",
              "Manage student accounts, view streaks, adjust subscription tiers manually."
            )}
          </p>
        </div>
      </div>

      {msg && (
        <div className="p-3.5 rounded-2xl bg-emerald-50 border border-emerald-300 text-xs font-semibold text-emerald-800 flex items-center gap-2">
          <Check className="w-4 h-4 text-emerald-600" />
          <span>{msg}</span>
        </div>
      )}

      {/* Search Bar */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-4 shadow-zen-card flex items-center justify-between gap-3 text-xs">
        <div className="flex items-center gap-2 bg-white rounded-xl border border-zen-border px-3 py-1.5 shadow-zen-subtle w-72">
          <Search className="w-3.5 h-3.5 text-zen-muted" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder={t("Tìm theo tên hoặc email...", "Search name or email...")}
            className="bg-transparent text-xs text-zen-ink focus:outline-none w-full"
          />
        </div>
        <span className="text-zen-muted font-medium">{filteredUsers.length} tài khoản</span>
      </div>

      {/* Students Table */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper shadow-zen-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-zen-border/70 bg-zen-surface/60 text-zen-muted uppercase text-[10px] font-bold tracking-wider">
                <th className="py-3 px-4">{t("Học Viên", "Student")}</th>
                <th className="py-3 px-4">{t("Vai Trò", "Role")}</th>
                <th className="py-3 px-4">{t("Gói Hiện Tại", "Active Tier")}</th>
                <th className="py-3 px-4">{t("Hạn Sử Dụng", "Expires At")}</th>
                <th className="py-3 px-4">{t("Chuỗi Ngày (Streak)", "Streak")}</th>
                <th className="py-3 px-4 text-right">{t("Hành Động", "Actions")}</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-zen-border/40 text-zen-ink">
              {filteredUsers.map((u) => {
                const isEditing = editingUserId === u.id;
                return (
                  <tr key={u.id} className="hover:bg-zen-surface/40 transition-colors">
                    <td className="py-3 px-4">
                      <div className="font-semibold text-zen-ink">{u.fullName}</div>
                      <div className="text-[11px] text-zen-muted">{u.email}</div>
                    </td>
                    <td className="py-3 px-4 capitalize font-medium">
                      <span className="px-2 py-0.5 rounded-md bg-zen-surface text-[10px] font-bold">
                        {u.role}
                      </span>
                    </td>
                    <td className="py-3 px-4 capitalize font-semibold text-zen-moss-dark">
                      {isEditing ? (
                        <select
                          value={selectedTier}
                          onChange={(e) => setSelectedTier(e.target.value as Tier)}
                          className="px-2 py-1 bg-white border border-zen-border rounded-lg text-xs"
                        >
                          <option value="free">Free</option>
                          <option value="1_month">1 Tháng</option>
                          <option value="6_months">6 Tháng</option>
                          <option value="12_months">12 Tháng</option>
                        </select>
                      ) : (
                        u.tier.replace("_", " ")
                      )}
                    </td>
                    <td className="py-3 px-4 text-zen-muted text-[11px]">
                      {u.tierExpiresAt ? new Date(u.tierExpiresAt).toLocaleDateString("vi-VN") : "Vô thời hạn (Free)"}
                    </td>
                    <td className="py-3 px-4 font-bold text-zen-ochre-dark">
                      🔥 {u.streakCount} ngày
                    </td>
                    <td className="py-3 px-4 text-right">
                      {isEditing ? (
                        <div className="flex items-center justify-end gap-1.5">
                          <button
                            onClick={() => handleSaveTier(u)}
                            className="px-2.5 py-1 rounded-xl bg-emerald-600 text-white font-semibold text-[11px]"
                          >
                            Lưu
                          </button>
                          <button
                            onClick={() => setEditingUserId(null)}
                            className="px-2.5 py-1 rounded-xl border border-zen-border text-zen-muted text-[11px]"
                          >
                            Hủy
                          </button>
                        </div>
                      ) : (
                        <button
                          onClick={() => handleOpenEdit(u)}
                          className="px-2.5 py-1 rounded-xl border border-zen-border bg-white hover:bg-zen-surface text-zen-ink font-semibold text-[11px] shadow-zen-subtle"
                        >
                          {t("Đổi gói", "Change Tier")}
                        </button>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
