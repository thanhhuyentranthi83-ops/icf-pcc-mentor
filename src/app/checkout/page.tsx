"use client";

import React, { useState, useEffect, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import Image from "next/image";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import { getSystemSettings, createOrder } from "@/lib/db";
import { generateVietQrUrl, formatVnd } from "@/lib/vietqr";
import { Tier, Order } from "@/types";
import {
  Copy,
  Check,
  UploadCloud,
  CheckCircle2,
  Clock,
  ArrowLeft,
  QrCode,
  ShieldAlert
} from "lucide-react";

function CheckoutContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user } = useAuth();
  const settings = getSystemSettings();

  const tierParam = (searchParams.get("tier") as Tier) || "6_months";
  const promoCodeParam = searchParams.get("code") || "";

  const tierInfo = settings.pricing[tierParam] || settings.pricing["6_months"];
  const originalPrice = tierInfo.price;

  // Calculate discount if promo code present
  let discountAmount = 0;
  if (promoCodeParam.toUpperCase() === "PCC2026") discountAmount = originalPrice * 0.2;
  else if (promoCodeParam.toUpperCase() === "ZENCOACH") discountAmount = originalPrice * 0.15;
  else if (promoCodeParam.toUpperCase() === "LANGMAI") discountAmount = originalPrice * 0.1;

  const finalAmount = Math.max(0, originalPrice - discountAmount);

  // Generate unique order code: PCC-<userSubId>-<rand4>
  const [orderCode, setOrderCode] = useState("");
  const [copiedField, setCopiedField] = useState<string | null>(null);
  const [receiptPreview, setReceiptPreview] = useState<string | null>(null);
  const [orderStatus, setOrderStatus] = useState<
    "pending_payment" | "pending_approval" | "approved"
  >("pending_payment");

  useEffect(() => {
    const userSubId = user.id.replace("usr-", "").slice(0, 4).toUpperCase();
    const randPart = Math.floor(1000 + Math.random() * 9000);
    const code = `PCC-${userSubId || "STUD"}-${randPart}`;
    setOrderCode(code);
  }, [user.id]);

  const vietQrUrl = orderCode
    ? generateVietQrUrl({
        bankBin: settings.bankBin,
        accountNumber: settings.accountNumber,
        accountHolder: settings.accountHolder,
        amount: finalAmount,
        orderCode: orderCode
      })
    : "";

  const handleCopy = (text: string, fieldName: string) => {
    navigator.clipboard.writeText(text);
    setCopiedField(fieldName);
    ringBell();
    setTimeout(() => setCopiedField(null), 2000);
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setReceiptPreview(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmitProof = () => {
    const newOrder: Order = {
      id: `ord-${Date.now()}`,
      userId: user.id,
      orderCode,
      tierId: tierParam,
      amount: finalAmount,
      discountCode: promoCodeParam || undefined,
      discountAmount,
      status: "pending_approval",
      receiptUrl: receiptPreview || "/receipts/sample-receipt.png",
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    createOrder(newOrder);
    setOrderStatus("pending_approval");
    ringBell();
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 sm:py-12 space-y-8">
      {/* Back button */}
      <div className="flex items-center justify-between text-xs text-zen-muted">
        <Link
          href="/pricing"
          className="flex items-center gap-1.5 font-medium hover:text-zen-ink transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>{t("Quay lại chọn gói", "Back to Tiers")}</span>
        </Link>
        <span className="font-mono text-zen-moss-dark font-bold">
          {t("Mã đơn:", "Order Code:")} {orderCode}
        </span>
      </div>

      {orderStatus === "pending_approval" ? (
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-8 sm:p-12 text-center space-y-4 shadow-zen-card max-w-xl mx-auto">
          <div className="w-16 h-16 rounded-full bg-zen-moss/20 text-zen-moss-dark mx-auto flex items-center justify-center">
            <Clock className="w-8 h-8 text-zen-moss-dark animate-pulse" />
          </div>

          <h2 className="font-serif text-2xl font-bold text-zen-ink">
            {t("Đã Tiếp Nhận Thông Tin Chuyển Khoản", "Payment Confirmation Received")}
          </h2>
          <p className="text-xs sm:text-sm text-zen-muted leading-relaxed">
            {t(
              `Cảm ơn bạn! Đơn hàng mã ${orderCode} đang được Kế toán (Billing) đối chiếu với tài khoản ngân hàng. Gói ${t(
                tierInfo.nameVi,
                tierInfo.nameEn
              )} sẽ được tự động kích hoạt ngay sau khi duyệt.`,
              `Thank you! Order ${orderCode} is now in queue for Billing review. Your tier will be activated immediately upon approval.`
            )}
          </p>

          <div className="p-4 rounded-2xl bg-zen-surface text-xs text-zen-ink text-left space-y-1.5 max-w-sm mx-auto">
            <div className="flex justify-between">
              <span className="text-zen-muted">{t("Mã đơn:", "Order Code:")}</span>
              <span className="font-mono font-bold text-zen-moss-dark">{orderCode}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-zen-muted">{t("Số tiền:", "Amount:")}</span>
              <span className="font-bold">{formatVnd(finalAmount)}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-zen-muted">{t("Trạng thái:", "Status:")}</span>
              <span className="font-semibold text-amber-700">
                {t("Chờ kế toán xác nhận", "Pending Billing Review")}
              </span>
            </div>
          </div>

          <div className="pt-4 flex flex-wrap justify-center gap-3">
            <Link
              href="/"
              className="px-6 py-2.5 rounded-2xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-colors shadow-zen-subtle"
            >
              {t("Về Trang Chủ Học Thử", "Return to Home")}
            </Link>
            <Link
              href="/admin/orders"
              className="px-6 py-2.5 rounded-2xl border border-zen-border bg-white text-xs font-semibold text-amber-900 hover:bg-amber-50 transition-colors shadow-zen-subtle"
            >
              {t("Vào Admin Duyệt Nhanh (Demo)", "Quick Approve via Admin")}
            </Link>
          </div>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Left: VietQR Image & Instruction */}
          <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card flex flex-col items-center text-center space-y-4">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark text-xs font-bold uppercase tracking-wider">
              <QrCode className="w-3.5 h-3.5" />
              <span>{t("Quét Mã VietQR Chuyển Khoản", "Scan VietQR to Pay")}</span>
            </div>

            <h3 className="font-serif text-lg font-bold text-zen-ink">
              {t("Mở ứng dụng Ngân hàng để quét", "Open Mobile Banking App to Scan")}
            </h3>
            <p className="text-xs text-zen-muted max-w-xs">
              {t(
                "Mã QR tự động điền sẵn chính xác số tiền và mã nội dung chuyển khoản duy nhất của bạn.",
                "VietQR automatically fills in the exact amount and unique transfer description."
              )}
            </p>

            {/* VietQR Image Container */}
            <div className="relative w-64 h-64 sm:w-72 sm:h-72 rounded-2xl bg-white p-3 border-2 border-zen-border shadow-zen-subtle overflow-hidden flex items-center justify-center">
              {vietQrUrl ? (
                <img
                  src={vietQrUrl}
                  alt="VietQR Code"
                  className="w-full h-full object-contain"
                />
              ) : (
                <div className="text-xs text-zen-muted">{t("Đang tạo mã QR...", "Generating QR...")}</div>
              )}
            </div>

            <p className="text-[11px] text-zen-muted italic">
              {t(
                "Hỗ trợ 40+ ngân hàng tại Việt Nam (Vietcombank, MB, Techcombank, VPBank, BIDV, v.v.)",
                "Supports 40+ Vietnamese banks (Vietcombank, MB, Techcombank, VPBank, etc.)"
              )}
            </p>
          </div>

          {/* Right: Bank Details & Upload Receipt */}
          <div className="space-y-6">
            {/* Account Details Box */}
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card space-y-4">
              <h3 className="font-serif text-lg font-bold text-zen-ink border-b border-zen-border/50 pb-3">
                {t("Thông Tin Chuyển Khoản Thủ Công", "Manual Transfer Information")}
              </h3>

              <div className="space-y-3 text-xs">
                {/* Bank Name */}
                <div className="flex justify-between items-center py-1">
                  <span className="text-zen-muted">{t("Ngân hàng:", "Bank:")}</span>
                  <span className="font-semibold text-zen-ink text-right max-w-[200px]">
                    {settings.bankName}
                  </span>
                </div>

                {/* Account Number */}
                <div className="flex justify-between items-center py-1.5 border-t border-zen-border/40">
                  <span className="text-zen-muted">{t("Số tài khoản:", "Account Number:")}</span>
                  <div className="flex items-center gap-2">
                    <span className="font-mono font-bold text-sm text-zen-moss-dark">
                      {settings.accountNumber}
                    </span>
                    <button
                      onClick={() => handleCopy(settings.accountNumber, "stk")}
                      className="p-1 rounded-md border border-zen-border hover:bg-zen-surface text-zen-muted hover:text-zen-ink transition-colors"
                      title={t("Sao chép", "Copy")}
                    >
                      {copiedField === "stk" ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
                    </button>
                  </div>
                </div>

                {/* Account Holder */}
                <div className="flex justify-between items-center py-1.5 border-t border-zen-border/40">
                  <span className="text-zen-muted">{t("Chủ tài khoản:", "Account Holder:")}</span>
                  <span className="font-bold text-zen-ink uppercase">{settings.accountHolder}</span>
                </div>

                {/* Amount */}
                <div className="flex justify-between items-center py-1.5 border-t border-zen-border/40">
                  <span className="text-zen-muted">{t("Số tiền thanh toán:", "Amount to pay:")}</span>
                  <div className="flex items-center gap-2">
                    <span className="font-serif font-bold text-base text-zen-ochre-dark">
                      {formatVnd(finalAmount)}
                    </span>
                    <button
                      onClick={() => handleCopy(String(finalAmount), "amount")}
                      className="p-1 rounded-md border border-zen-border hover:bg-zen-surface text-zen-muted hover:text-zen-ink transition-colors"
                      title={t("Sao chép", "Copy")}
                    >
                      {copiedField === "amount" ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
                    </button>
                  </div>
                </div>

                {/* Transfer Content */}
                <div className="flex justify-between items-center py-1.5 border-t border-zen-border/40 bg-amber-50/70 p-2.5 rounded-xl border border-amber-200/80">
                  <span className="text-amber-900 font-semibold">{t("Nội dung chuyển khoản:", "Transfer memo:")}</span>
                  <div className="flex items-center gap-2">
                    <span className="font-mono font-bold text-sm text-amber-900">{orderCode}</span>
                    <button
                      onClick={() => handleCopy(orderCode, "code")}
                      className="p-1 rounded-md bg-white border border-amber-300 hover:bg-amber-100 text-amber-900 transition-colors"
                      title={t("Sao chép nội dung", "Copy memo")}
                    >
                      {copiedField === "code" ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
                    </button>
                  </div>
                </div>
              </div>
            </div>

            {/* Receipt Upload Box */}
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
              <h4 className="text-xs font-bold uppercase tracking-wider text-zen-ink flex items-center gap-1.5">
                <UploadCloud className="w-4 h-4 text-zen-moss-dark" />
                <span>{t("Tải Lên Ảnh Biên Lai (Để Đối Chiếu Nhanh)", "Upload Receipt Screenshot")}</span>
              </h4>

              <div className="border-2 border-dashed border-zen-border rounded-2xl p-4 text-center hover:bg-zen-surface/40 transition-colors cursor-pointer relative">
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleFileUpload}
                  className="absolute inset-0 opacity-0 cursor-pointer w-full h-full"
                />
                {receiptPreview ? (
                  <div className="flex flex-col items-center space-y-2">
                    <img
                      src={receiptPreview}
                      alt="Receipt Preview"
                      className="h-32 object-contain rounded-xl border border-zen-border"
                    />
                    <span className="text-xs text-zen-moss-dark font-medium">
                      ✓ {t("Đã chọn ảnh biên lai (Bấm để đổi)", "Receipt selected (click to change)")}
                    </span>
                  </div>
                ) : (
                  <div className="space-y-1.5 py-4">
                    <UploadCloud className="w-8 h-8 text-zen-muted mx-auto" />
                    <p className="text-xs text-zen-ink font-medium">
                      {t("Bấm vào đây để tải ảnh chụp màn hình chuyển khoản", "Click here to upload payment receipt")}
                    </p>
                    <p className="text-[11px] text-zen-muted">
                      {t("Hỗ trợ định dạng JPG, PNG", "Supports JPG, PNG")}
                    </p>
                  </div>
                )}
              </div>

              {/* Confirm Button */}
              <button
                onClick={handleSubmitProof}
                className="w-full py-3.5 rounded-2xl bg-zen-moss-dark hover:bg-zen-moss-deep text-white text-xs font-semibold transition-all shadow-zen-card flex items-center justify-center gap-2"
              >
                <CheckCircle2 className="w-4 h-4" />
                <span>{t("Tôi Đã Chuyển Khoản — Xác Nhận Đơn Hàng", "I Have Transferred — Confirm Order")}</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default function CheckoutPage() {
  return (
    <Suspense fallback={<div className="p-12 text-center text-xs text-zen-muted">Đang tải trang thanh toán...</div>}>
      <CheckoutContent />
    </Suspense>
  );
}
