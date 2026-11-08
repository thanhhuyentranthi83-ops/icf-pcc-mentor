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
import { Order, Sticker, PackageRecord, EnrollmentRecord, EnrollmentRequestRecord } from "@/types";
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
  ChevronRight,
  Package,
  RotateCw,
  Send,
  Check,
  CheckCircle2,
  X,
  AlertTriangle
} from "lucide-react";
import { formatVnd } from "@/lib/vietqr";

export default function ProfilePage() {
  const { t } = useLanguage();
  const { user, updateCurrentUser, userEnrollments, requestEnrollment, refreshEnrollments } = useAuth();

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
  const [packages, setPackages] = useState<PackageRecord[]>([]);
  const [requests, setRequests] = useState<EnrollmentRequestRecord[]>([]);
  const [activeTab, setActiveTab] = useState<"packages" | "progress" | "orders" | "settings">("packages");

  // Request modal state
  const [modalPkg, setModalPkg] = useState<{ pkg: PackageRecord; type: "register" | "renew" } | null>(null);
  const [requestNote, setRequestNote] = useState("");
  const [submittingReq, setSubmittingReq] = useState(false);
  const [requestMsg, setRequestMsg] = useState("");

  useEffect(() => {
    setGarden(getLotusGarden(user.id));
    setExamSessions(getExamSessions(user.id));
    setOrders(getOrders().filter((o) => o.userId === user.id));
    setStickers(getStickers());

    // Fetch packages & user's requests
    const fetchProfileData = async () => {
      try {
        const [resPkg, resEnr] = await Promise.all([
          fetch("/api/packages"),
          fetch("/api/enrollments")
        ]);
        const dataPkg = await resPkg.json();
        const dataEnr = await resEnr.json();
        if (dataPkg.success && dataPkg.packages) {
          setPackages(dataPkg.packages);
        }
        if (dataEnr.success && dataEnr.requests) {
          setRequests(dataEnr.requests);
        }
      } catch (err) {
        console.warn("Profile fetch error:", err);
      }
    };

    fetchProfileData();
  }, [user.id]);

  const toggleMinimalMode = () => {
    updateCurrentUser({ minimalMode: !user.minimalMode });
  };

  const handleSelectStickerPack = (code: string) => {
    updateCurrentUser({ selectedStickerPack: code });
  };

  const handleRequestSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!modalPkg) return;
    try {
      setSubmittingReq(true);
      setRequestMsg("");
      const res = await requestEnrollment(modalPkg.pkg.id, modalPkg.type, requestNote);
      if (res.success) {
        setRequestMsg("Đã gửi yêu cầu thành công! Ban quản trị sẽ sớm duyệt và mở quyền cho bạn.");
        setTimeout(() => {
          setModalPkg(null);
          setRequestNote("");
          setRequestMsg("");
        }, 2200);
        // refresh requests
        const resEnr = await fetch("/api/enrollments");
        const dataEnr = await resEnr.json();
        if (dataEnr.success && dataEnr.requests) {
          setRequests(dataEnr.requests);
        }
      } else {
        setRequestMsg(res.error || "Không thể gửi yêu cầu.");
      }
    } catch {
      setRequestMsg("Lỗi kết nối máy chủ.");
    } finally {
      setSubmittingReq(false);
    }
  };

  const activeEnrollments = userEnrollments.filter(
    (e) => e.status === "active" && (!e.expiresAt || e.expiresAt > new Date().toISOString())
  );
  const expiredEnrollments = userEnrollments.filter(
    (e) => e.status === "expired" || (e.expiresAt && e.expiresAt < new Date().toISOString())
  );

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
                {activeEnrollments.length > 0
                  ? activeEnrollments[0].packageName
                  : user.tier === "free"
                  ? "Chưa Có Gói"
                  : `Gói ${user.tier.replace("_", " ")}`}
              </span>
            </div>
          </div>
        </div>

        {/* Upgrade / Pricing button */}
        <button
          onClick={() => setActiveTab("packages")}
          className="px-5 py-2.5 rounded-2xl bg-amber-900 hover:bg-amber-950 text-white text-xs font-semibold shadow-zen-subtle transition-all shrink-0 flex items-center gap-1.5"
        >
          <Sparkles className="w-4 h-4" />
          <span>{t("Xem Gói Học Của Tôi", "My Packages & Tiers")}</span>
        </button>
      </div>

      {/* Tabs */}
      <div className="flex items-center gap-2 border-b border-zen-border/70 pb-2 overflow-x-auto">
        <button
          onClick={() => setActiveTab("packages")}
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all shrink-0 ${
            activeTab === "packages"
              ? "bg-amber-900 text-white shadow-sm"
              : "bg-zen-paper hover:bg-zen-surface text-zen-ink border border-zen-border/70"
          }`}
        >
          🎓 {t("Gói Học Của Tôi", "My Packages")} {userEnrollments.length > 0 && `(${userEnrollments.length})`}
        </button>
        <button
          onClick={() => setActiveTab("progress")}
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all shrink-0 ${
            activeTab === "progress"
              ? "bg-zen-moss-dark text-white shadow-sm"
              : "bg-zen-paper hover:bg-zen-surface text-zen-ink border border-zen-border/70"
          }`}
        >
          🌸 {t("Tiến Độ & Vườn Sen", "Progress & Garden")}
        </button>
        <button
          onClick={() => setActiveTab("orders")}
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all shrink-0 ${
            activeTab === "orders"
              ? "bg-zen-moss-dark text-white shadow-sm"
              : "bg-zen-paper hover:bg-zen-surface text-zen-ink border border-zen-border/70"
          }`}
        >
          💳 {t("Lịch Sử Thanh Toán", "Order History")} ({orders.length})
        </button>
        <button
          onClick={() => setActiveTab("settings")}
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all shrink-0 ${
            activeTab === "settings"
              ? "bg-zen-moss-dark text-white shadow-sm"
              : "bg-zen-paper hover:bg-zen-surface text-zen-ink border border-zen-border/70"
          }`}
        >
          ⚙️ {t("Cài Đặt Chánh Niệm", "Mindful Settings")}
        </button>
      </div>

      {/* Tab: Packages & Entitlements */}
      {activeTab === "packages" && (
        <div className="space-y-6">
          {/* Active Packages */}
          <div className="space-y-4">
            <h3 className="font-serif text-lg font-bold text-zen-ink flex items-center gap-2">
              <Package className="w-5 h-5 text-amber-800" />
              <span>{t("Gói Học Hiện Có Của Bạn", "Your Active Packages")}</span>
            </h3>

            {userEnrollments.length === 0 ? (
              <div className="p-8 rounded-3xl border border-zen-border bg-zen-paper text-center space-y-3">
                <Package className="w-8 h-8 text-zen-muted mx-auto" />
                <p className="text-xs text-zen-muted max-w-md mx-auto leading-relaxed">
                  {t(
                    "Tài khoản của bạn hiện chưa được cấp gói học chính thức. Bạn vẫn có thể trải nghiệm bài học thử miễn phí (Module 1 & 6). Đăng ký một gói bên dưới để mở toàn bộ học phần!",
                    "You have no active packages. Free preview lessons (Modules 1 & 6) are accessible. Choose a package below to unlock all lessons!"
                  )}
                </p>
                <div className="pt-2">
                  <Link
                    href="/curriculum?module=mod-1&lesson=mod1-les1"
                    className="inline-flex items-center gap-1.5 px-4 py-2 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-colors"
                  >
                    <span>{t("Vào Học Thử Miễn Phí", "Start Free Preview")}</span>
                    <ChevronRight className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {userEnrollments.map((enr) => {
                  const now = new Date();
                  const isExp = enr.status === "expired" || (enr.expiresAt && new Date(enr.expiresAt) < now);
                  const isRev = enr.status === "revoked";
                  const pkgInfo = packages.find((p) => p.id === enr.packageId);

                  return (
                    <div
                      key={enr.id}
                      className={`p-6 rounded-3xl border flex flex-col justify-between space-y-4 transition-all ${
                        isExp || isRev
                          ? "bg-zen-surface/60 border-dashed border-zen-border"
                          : "bg-zen-paper border-zen-border shadow-zen-card hover:border-amber-300"
                      }`}
                    >
                      <div className="space-y-3">
                        <div className="flex items-center justify-between">
                          <span className="font-mono text-[10px] text-zen-muted bg-zen-surface px-2 py-0.5 rounded-lg border border-zen-border">
                            {enr.packageId}
                          </span>
                          <span
                            className={`px-2.5 py-0.5 rounded-full text-[10px] font-semibold ${
                              isExp
                                ? "bg-rose-50 text-rose-800 border border-rose-200"
                                : isRev
                                ? "bg-stone-100 text-stone-600 border border-stone-200"
                                : "bg-emerald-50 text-emerald-800 border border-emerald-200"
                            }`}
                          >
                            {isExp ? "Đã hết hạn" : isRev ? "Đã thu hồi" : "Đang hoạt động"}
                          </span>
                        </div>

                        <div>
                          <h4 className="font-serif font-bold text-base text-zen-ink">
                            {enr.packageName}
                          </h4>
                          <p className="text-xs text-zen-muted mt-0.5">
                            {enr.expiresAt ? (
                              isExp ? (
                                <span className="text-rose-700">
                                  Hết hạn vào: {new Date(enr.expiresAt).toLocaleDateString("vi-VN")}
                                </span>
                              ) : (
                                <span className="text-emerald-800 flex items-center gap-1">
                                  <Clock className="w-3.5 h-3.5" />
                                  Hạn sử dụng đến: {new Date(enr.expiresAt).toLocaleDateString("vi-VN")}
                                </span>
                              )
                            ) : (
                              <span className="text-zen-moss-dark">Thời hạn: Vô thời hạn</span>
                            )}
                          </p>
                        </div>

                        {/* Unlocked Features */}
                        <div className="p-3 rounded-2xl bg-zen-surface border border-zen-border/60 text-xs space-y-1">
                          <span className="text-[10px] font-bold text-zen-muted uppercase tracking-wider block mb-1">
                            {t("Quyền hạn được mở:", "Unlocked privileges:")}
                          </span>
                          <div className="grid grid-cols-1 gap-1 text-[11px] text-zen-ink">
                            <span className="flex items-center gap-1.5">
                              <CheckCircle2 className="w-3 h-3 text-emerald-600 shrink-0" />
                              Toàn bộ 7 học phần & 26 bài học ICF
                            </span>
                            <span className="flex items-center gap-1.5">
                              <CheckCircle2 className="w-3 h-3 text-emerald-600 shrink-0" />
                              Luyện tập 10 câu tình huống SJT mỗi ngày
                            </span>
                            <span className="flex items-center gap-1.5">
                              <CheckCircle2 className="w-3 h-3 text-emerald-600 shrink-0" />
                              Thi thử mô phỏng Pearson VUE có tính giờ
                            </span>
                            <span className="flex items-center gap-1.5">
                              <CheckCircle2 className="w-3 h-3 text-emerald-600 shrink-0" />
                              Bảo toàn 100% hoa sen và ghi chú
                            </span>
                          </div>
                        </div>
                      </div>

                      {/* Action buttons */}
                      <div className="pt-3 border-t border-zen-border flex items-center justify-between gap-2">
                        {isExp || isRev ? (
                          <button
                            onClick={() =>
                              setModalPkg({
                                pkg: pkgInfo || {
                                  id: enr.packageId,
                                  nameVi: enr.packageName,
                                  nameEn: "",
                                  descriptionVi: "",
                                  descriptionEn: "",
                                  price: 0,
                                  durationDays: 30,
                                  isRegistrationOpen: true,
                                  allowedCourseIds: ["*"],
                                  allowedFeatures: ["curriculum"]
                                },
                                type: "renew"
                              })
                            }
                            className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-amber-900 text-white font-semibold text-xs hover:bg-amber-950 transition-colors shadow-sm"
                          >
                            <RotateCw className="w-3.5 h-3.5" />
                            <span>{t("Yêu Cầu Gia Hạn", "Request Renewal")}</span>
                          </button>
                        ) : (
                          <Link
                            href="/curriculum"
                            className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-amber-900 text-white font-semibold text-xs hover:bg-amber-950 transition-colors shadow-sm"
                          >
                            <span>{t("Tiếp Tục Học Ngay", "Resume Learning")}</span>
                            <ChevronRight className="w-3.5 h-3.5" />
                          </Link>
                        )}

                        <span className="text-[10px] text-zen-muted">
                          Cấp bởi: {enr.grantedBy}
                        </span>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </div>

          {/* Available Packages to Register */}
          <div className="space-y-4 pt-4 border-t border-zen-border">
            <h3 className="font-serif text-lg font-bold text-zen-ink flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-amber-800" />
              <span>{t("Các Gói Học Đang Mở Đăng Ký", "Available Packages")}</span>
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {packages
                .filter((p) => p.isRegistrationOpen)
                .map((pkg) => (
                  <div
                    key={pkg.id}
                    className="p-5 rounded-3xl border border-zen-border bg-zen-paper shadow-zen-subtle flex flex-col justify-between space-y-3"
                  >
                    <div>
                      <div className="flex items-center justify-between gap-1 mb-1">
                        <span className="font-bold text-sm text-zen-ink">{pkg.nameVi}</span>
                        {pkg.badge && (
                          <span className="text-[10px] font-semibold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">
                            {pkg.badge}
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-zen-muted line-clamp-2">{pkg.descriptionVi}</p>
                      <div className="pt-2 text-xs font-semibold text-amber-900">
                        {pkg.price === 0 ? "Miễn phí" : `${pkg.price.toLocaleString("vi-VN")} đ`} •{" "}
                        {pkg.durationDays === 0 ? "Vô thời hạn" : `${pkg.durationDays} ngày`}
                      </div>
                    </div>

                    <button
                      onClick={() => setModalPkg({ pkg, type: "register" })}
                      className="w-full py-2 rounded-xl bg-white hover:bg-zen-surface text-amber-900 border border-amber-300 font-semibold text-xs transition-colors flex items-center justify-center gap-1.5"
                    >
                      <Send className="w-3 h-3" />
                      <span>{t("Gửi Yêu Cầu Đăng Ký", "Request Enrollment")}</span>
                    </button>
                  </div>
                ))}
            </div>
          </div>

          {/* Student's Requests History */}
          {requests.length > 0 && (
            <div className="space-y-3 pt-4 border-t border-zen-border">
              <h4 className="font-serif text-sm font-bold text-zen-ink">
                {t("Lịch Sử Yêu Cầu Của Bạn", "Your Request History")}
              </h4>
              <div className="space-y-2">
                {requests.map((r) => (
                  <div
                    key={r.id}
                    className="p-3.5 rounded-2xl bg-zen-surface border border-zen-border flex items-center justify-between text-xs"
                  >
                    <div>
                      <span className="font-semibold text-zen-ink block">
                        {r.packageName} ({r.type === "renew" ? "Gia hạn" : "Đăng ký mới"})
                      </span>
                      <span className="text-[10px] text-zen-muted">
                        Gửi lúc: {new Date(r.requestedAt).toLocaleString("vi-VN")}
                        {r.userNote ? ` • Ghi chú: ${r.userNote}` : ""}
                      </span>
                    </div>

                    <span
                      className={`px-2.5 py-1 rounded-full text-[10px] font-semibold ${
                        r.status === "approved"
                          ? "bg-emerald-50 text-emerald-800 border border-emerald-200"
                          : r.status === "pending"
                          ? "bg-amber-50 text-amber-800 border border-amber-200"
                          : "bg-rose-50 text-rose-800 border border-rose-200"
                      }`}
                    >
                      {r.status === "approved"
                        ? "Đã phê duyệt"
                        : r.status === "pending"
                        ? "Đang chờ duyệt"
                        : "Đã từ chối"}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* Modal: Request Registration / Renewal */}
      {modalPkg && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-zen-paper border border-zen-border rounded-3xl max-w-md w-full p-6 shadow-xl space-y-4 animate-in fade-in duration-150">
            <div className="flex items-center justify-between pb-3 border-b border-zen-border">
              <div className="flex items-center gap-2">
                <Send className="w-5 h-5 text-amber-800" />
                <h3 className="font-serif font-bold text-base text-zen-ink">
                  {modalPkg.type === "renew"
                    ? t("Gửi Yêu Cầu Gia Hạn Gói", "Request Package Renewal")
                    : t("Gửi Yêu Cầu Đăng Ký Gói", "Request Package Enrollment")}
                </h3>
              </div>
              <button
                onClick={() => setModalPkg(null)}
                className="p-1 rounded-full hover:bg-zen-surface text-zen-muted"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="p-3 rounded-2xl bg-zen-surface border border-zen-border text-xs space-y-1">
              <div className="font-semibold text-zen-ink">{modalPkg.pkg.nameVi}</div>
              <div className="text-[11px] text-zen-muted">
                {modalPkg.pkg.price === 0 ? "Miễn phí" : `${modalPkg.pkg.price.toLocaleString("vi-VN")} đ`} •{" "}
                {modalPkg.pkg.durationDays === 0 ? "Vô thời hạn" : `${modalPkg.pkg.durationDays} ngày`}
              </div>
            </div>

            <form onSubmit={handleRequestSubmit} className="space-y-3 text-xs">
              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Lời Nhắn / Ghi Chú Cho Ban Quản Trị", "Note for Admin")}
                </label>
                <textarea
                  rows={2}
                  value={requestNote}
                  onChange={(e) => setRequestNote(e.target.value)}
                  placeholder={t(
                    "Ví dụ: Em đã chuyển khoản qua VietQR / Mong được hỗ trợ mở khóa...",
                    "e.g. Paid via VietQR / Please approve..."
                  )}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs focus:outline-hidden focus:border-amber-700"
                />
              </div>

              {requestMsg && (
                <div
                  className={`p-3 rounded-xl text-[11px] font-medium ${
                    requestMsg.includes("thành công")
                      ? "bg-emerald-50 text-emerald-800 border border-emerald-200"
                      : "bg-rose-50 text-rose-800 border border-rose-200"
                  }`}
                >
                  {requestMsg}
                </div>
              )}

              <div className="pt-3 border-t border-zen-border flex items-center justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setModalPkg(null)}
                  className="px-4 py-2 rounded-xl border border-zen-border bg-white text-zen-muted hover:bg-zen-surface font-medium"
                >
                  {t("Hủy bỏ", "Cancel")}
                </button>
                <button
                  type="submit"
                  disabled={submittingReq}
                  className="px-5 py-2 rounded-xl bg-amber-900 text-white font-semibold hover:bg-amber-950 shadow-sm disabled:opacity-50"
                >
                  {submittingReq ? t("Đang gửi...", "Sending...") : t("Gửi Yêu Cầu", "Submit Request")}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

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
