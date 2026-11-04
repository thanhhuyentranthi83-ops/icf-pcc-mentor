"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { getAuditLogs } from "@/lib/db";
import { AuditLog } from "@/types";
import { FileText, ShieldAlert } from "lucide-react";

export default function AdminAuditLogsPage() {
  const { t } = useLanguage();
  const [logs, setLogs] = useState<AuditLog[]>([]);

  useEffect(() => {
    setLogs(getAuditLogs());
  }, []);

  return (
    <div className="space-y-6">
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card">
        <h1 className="font-serif text-2xl font-bold text-zen-ink">
          {t("Nhật Ký Hoạt Động Hệ Thống (Audit Logs)", "System Audit Logs")}
        </h1>
        <p className="text-xs text-zen-muted mt-1">
          {t(
            "Ghi lại minh bạch mọi thao tác của Super Admin, Editor và Billing trên toàn hệ thống.",
            "Immutable audit log recording administrative operations across all roles."
          )}
        </p>
      </div>

      <div className="rounded-3xl border border-zen-border bg-zen-paper shadow-zen-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-zen-border/70 bg-zen-surface/60 text-zen-muted uppercase text-[10px] font-bold tracking-wider">
                <th className="py-3 px-4">{t("Thời Gian", "Timestamp")}</th>
                <th className="py-3 px-4">{t("Người Thực Hiện", "Operator")}</th>
                <th className="py-3 px-4">{t("Hành Động", "Action")}</th>
                <th className="py-3 px-4">{t("Chi Tiết", "Details")}</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-zen-border/40 text-zen-ink font-mono text-[11px]">
              {logs.map((log) => (
                <tr key={log.id} className="hover:bg-zen-surface/40">
                  <td className="py-3 px-4 text-zen-muted whitespace-nowrap">
                    {new Date(log.createdAt).toLocaleString("vi-VN")}
                  </td>
                  <td className="py-3 px-4 font-sans font-semibold text-zen-ink">
                    {log.userName}
                  </td>
                  <td className="py-3 px-4 font-sans font-bold text-zen-moss-dark">
                    {log.action}
                  </td>
                  <td className="py-3 px-4 font-sans text-zen-ink/90">
                    {log.details}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
