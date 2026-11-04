"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import { getSystemSettings, saveSystemSettings, addAuditLog } from "@/lib/db";
import { SystemSettings } from "@/types";
import { Save, Check, QrCode, CreditCard, Tag, ShieldCheck } from "lucide-react";

export default function AdminSettingsPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user } = useAuth();

  const [settings, setSettings] = useState<SystemSettings | null>(null);
  const [successMsg, setSuccessMsg] = useState("");

  useEffect(() => {
    setSettings(getSystemSettings());
  }, []);

  if (!settings) return null;

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    saveSystemSettings(settings);
    addAuditLog(user.id, user.fullName, "Cập nhật cấu hình hệ thống", "Cập nhật ngân hàng VietQR & Bảng giá");
    ringBell();
    setSuccessMsg(t("Đã lưu cấu hình ngân hàng & hệ thống thành công!", "Settings saved successfully!"));
    setTimeout(() => setSuccessMsg(""), 3500);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card">
        <h1 className="font-serif text-2xl font-bold text-zen-ink">
          {t("Cấu Hình Tài Khoản Ngân Hàng & VietQR (Super Admin)", "Bank Transfer & VietQR Configuration")}
        </h1>
        <p className="text-xs text-zen-muted mt-1">
          {t(
            "Cập nhật tài khoản thụ hưởng để sinh mã VietQR tự động, quản lý giá 4 gói học và mã giảm giá.",
            "Update receiving bank account for VietQR dynamic generation, package prices, and coupons."
          )}
        </p>
      </div>

      {successMsg && (
        <div className="p-3.5 rounded-2xl bg-emerald-50 border border-emerald-300 text-xs font-semibold text-emerald-800 flex items-center gap-2">
          <Check className="w-4 h-4 text-emerald-600" />
          <span>{successMsg}</span>
        </div>
      )}

      <form onSubmit={handleSave} className="space-y-6">
        {/* 1. Bank Account & VietQR Config Box */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
          <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zen-moss-dark border-b border-zen-border/50 pb-3">
            <QrCode className="w-4 h-4" />
            <span>{t("Thông Tin Ngân Hàng Thụ Hưởng (VietQR)", "Receiving Bank Info for VietQR")}</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
            <div>
              <label className="block font-semibold mb-1 text-zen-ink">{t("Tên ngân hàng (BANK_NAME)", "Bank Name")}</label>
              <input
                type="text"
                value={settings.bankName}
                onChange={(e) => setSettings({ ...settings, bankName: e.target.value })}
                className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink"
                required
              />
            </div>

            <div>
              <label className="block font-semibold mb-1 text-zen-ink">
                {t("Mã định danh ngân hàng (BANK_BIN)", "Bank BIN Code")}
              </label>
              <input
                type="text"
                value={settings.bankBin}
                onChange={(e) => setSettings({ ...settings, bankBin: e.target.value })}
                placeholder="VD: 970436 (Vietcombank), 970422 (MB)"
                className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink font-mono"
                required
              />
              <span className="text-[10px] text-zen-muted mt-0.5 block">
                Mã BIN chuẩn để sinh QR: VCB=970436, MB=970422, TCB=970407, VPB=970432
              </span>
            </div>

            <div>
              <label className="block font-semibold mb-1 text-zen-ink">
                {t("Số tài khoản nhận tiền (ACCOUNT_NUMBER)", "Account Number")}
              </label>
              <input
                type="text"
                value={settings.accountNumber}
                onChange={(e) => setSettings({ ...settings, accountNumber: e.target.value })}
                className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink font-mono font-bold"
                required
              />
            </div>

            <div>
              <label className="block font-semibold mb-1 text-zen-ink">
                {t("Tên chủ tài khoản (ACCOUNT_HOLDER)", "Account Holder")}
              </label>
              <input
                type="text"
                value={settings.accountHolder}
                onChange={(e) => setSettings({ ...settings, accountHolder: e.target.value.toUpperCase() })}
                className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink uppercase font-bold"
                required
              />
            </div>
          </div>
        </div>

        {/* 2. Tier Pricing Box */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
          <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-zen-wood border-b border-zen-border/50 pb-3">
            <CreditCard className="w-4 h-4" />
            <span>{t("Cấu Hình Giá Các Gói Học", "Subscription Tier Prices")}</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
            <div>
              <label className="block font-semibold mb-1 text-zen-ink">{t("Giá gói 1 Tháng (VNĐ)", "1 Month Price")}</label>
              <input
                type="number"
                value={settings.pricing["1_month"].price}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    pricing: {
                      ...settings.pricing,
                      "1_month": { ...settings.pricing["1_month"], price: Number(e.target.value) }
                    }
                  })
                }
                className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs font-mono font-bold text-zen-ink"
              />
            </div>

            <div>
              <label className="block font-semibold mb-1 text-zen-ink">{t("Giá gói 6 Tháng (VNĐ)", "6 Months Price")}</label>
              <input
                type="number"
                value={settings.pricing["6_months"].price}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    pricing: {
                      ...settings.pricing,
                      "6_months": { ...settings.pricing["6_months"], price: Number(e.target.value) }
                    }
                  })
                }
                className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs font-mono font-bold text-zen-ink"
              />
            </div>

            <div>
              <label className="block font-semibold mb-1 text-zen-ink">{t("Giá gói 12 Tháng (VNĐ)", "12 Months Price")}</label>
              <input
                type="number"
                value={settings.pricing["12_months"].price}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    pricing: {
                      ...settings.pricing,
                      "12_months": { ...settings.pricing["12_months"], price: Number(e.target.value) }
                    }
                  })
                }
                className="w-full px-3.5 py-2.5 rounded-2xl border border-zen-border bg-white text-xs font-mono font-bold text-zen-ink"
              />
            </div>
          </div>
        </div>

        {/* Submit */}
        <div className="flex justify-end">
          <button
            type="submit"
            className="flex items-center gap-2 px-8 py-3 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-all shadow-zen-card"
          >
            <Save className="w-4 h-4" />
            <span>{t("Lưu Toàn Bộ Cấu Hình", "Save All Settings")}</span>
          </button>
        </div>
      </form>
    </div>
  );
}
