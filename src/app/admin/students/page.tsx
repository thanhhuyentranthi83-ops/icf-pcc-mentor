"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import {
  PackageRecord,
  EnrollmentRecord,
  EnrollmentRequestRecord,
  EnrollmentHistoryRecord
} from "@/types";
import {
  Users,
  Search,
  Check,
  ShieldAlert,
  Calendar,
  History,
  X,
  Sparkles,
  BookOpen,
  Lock,
  RefreshCw,
  PlusCircle,
  Clock,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  RotateCw,
  ShieldCheck,
  Filter,
  Package
} from "lucide-react";

interface AdminStudentItem {
  id: string;
  email: string;
  fullName: string;
  role: string;
  tier: string;
  tierExpiresAt: string | null;
  streakCount: number;
  lastActiveDate: string;
  createdAt: string;
  enrollments: EnrollmentRecord[];
  enrollmentStatus: "active" | "trial" | "expired" | "pending" | "revoked" | "none";
  stats: {
    completedLessons: number;
    passedQuizzes: number;
    lotusesBloomed: number;
    flaggedLessonsCount: number;
    notesCount: number;
    bookmarksCount: number;
    examSessionsCount: number;
  };
  milestones: Array<{
    status: string;
    lessonId: string;
    score: number | null;
    updatedAt: string;
  }>;
}

export default function AdminStudentsPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user: currentAdmin } = useAuth();

  const [activeTab, setActiveTab] = useState<"students" | "requests" | "history">("students");
  const [students, setStudents] = useState<AdminStudentItem[]>([]);
  const [packages, setPackages] = useState<PackageRecord[]>([]);
  const [requests, setRequests] = useState<EnrollmentRequestRecord[]>([]);
  const [historyLogs, setHistoryLogs] = useState<EnrollmentHistoryRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState("");
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState<string>("all");
  const [msg, setMsg] = useState("");

  // Modals state
  const [selectedStudentMilestones, setSelectedStudentMilestones] = useState<AdminStudentItem | null>(null);
  const [grantingStudent, setGrantingStudent] = useState<AdminStudentItem | null>(null);
  const [renewingStudent, setRenewingStudent] = useState<{ student: AdminStudentItem; enrollment: EnrollmentRecord } | null>(null);
  const [revokingStudent, setRevokingStudent] = useState<{ student: AdminStudentItem; enrollment: EnrollmentRecord } | null>(null);

  // Form states for modals
  const [grantPackageId, setGrantPackageId] = useState<string>("");
  const [grantDurationDays, setGrantDurationDays] = useState<number>(30);
  const [grantNote, setGrantNote] = useState<string>("");

  const [renewExtensionDays, setRenewExtensionDays] = useState<number>(30);
  const [renewNote, setRenewNote] = useState<string>("");

  const [revokeReason, setRevokeReason] = useState<string>("");
  const [actionLoading, setActionLoading] = useState(false);

  const loadAllData = async () => {
    setLoading(true);
    setErrorMsg("");
    try {
      const [resStudents, resPkgs, resEnrs] = await Promise.all([
        fetch("/api/admin/students"),
        fetch("/api/packages?all=true"),
        fetch("/api/enrollments")
      ]);

      const dataStudents = await resStudents.json();
      const dataPkgs = await resPkgs.json();
      const dataEnrs = await resEnrs.json();

      if (dataStudents.success && dataStudents.students) {
        setStudents(dataStudents.students);
      }
      if (dataPkgs.success && dataPkgs.packages) {
        setPackages(dataPkgs.packages);
        if (dataPkgs.packages.length > 0 && !grantPackageId) {
          setGrantPackageId(dataPkgs.packages[0].id);
        }
      }
      if (dataEnrs.success) {
        setRequests(dataEnrs.requests || []);
        setHistoryLogs(dataEnrs.history || []);
      }
    } catch {
      setErrorMsg("Lỗi kết nối máy chủ quản trị.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadAllData();
  }, []);

  // Filter students
  const filteredStudents = students.filter((s) => {
    if (statusFilter !== "all" && s.enrollmentStatus !== statusFilter) {
      return false;
    }
    if (!search.trim()) return true;
    const q = search.toLowerCase();
    return s.fullName.toLowerCase().includes(q) || s.email.toLowerCase().includes(q);
  });

  const pendingRequestsCount = requests.filter((r) => r.status === "pending").length;

  // Handle Grant Package
  const handleConfirmGrant = async () => {
    if (!grantingStudent || !grantPackageId) return;
    try {
      setActionLoading(true);
      const res = await fetch("/api/enrollments/grant", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          userId: grantingStudent.id,
          packageId: grantPackageId,
          durationDays: grantDurationDays,
          note: grantNote
        })
      });
      const data = await res.json();
      if (data.success) {
        ringBell();
        setMsg(`Đã cấp quyền gói thành công cho học viên ${grantingStudent.fullName}!`);
        setGrantingStudent(null);
        setGrantNote("");
        loadAllData();
      } else {
        setErrorMsg(data.error || "Không thể cấp quyền gói.");
      }
    } catch {
      setErrorMsg("Lỗi khi kết nối máy chủ.");
    } finally {
      setActionLoading(false);
      setTimeout(() => setMsg(""), 3500);
    }
  };

  // Handle Renew Package
  const handleConfirmRenew = async () => {
    if (!renewingStudent) return;
    try {
      setActionLoading(true);
      const res = await fetch("/api/enrollments/renew", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          userId: renewingStudent.student.id,
          packageId: renewingStudent.enrollment.packageId,
          extensionDays: renewExtensionDays,
          note: renewNote
        })
      });
      const data = await res.json();
      if (data.success) {
        ringBell();
        setMsg(`Đã gia hạn thêm ${renewExtensionDays} ngày cho học viên ${renewingStudent.student.fullName}!`);
        setRenewingStudent(null);
        setRenewNote("");
        loadAllData();
      } else {
        setErrorMsg(data.error || "Không thể gia hạn.");
      }
    } catch {
      setErrorMsg("Lỗi kết nối khi gia hạn.");
    } finally {
      setActionLoading(false);
      setTimeout(() => setMsg(""), 3500);
    }
  };

  // Handle Revoke Package
  const handleConfirmRevoke = async () => {
    if (!revokingStudent) return;
    try {
      setActionLoading(true);
      const res = await fetch("/api/enrollments/revoke", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          userId: revokingStudent.student.id,
          packageId: revokingStudent.enrollment.packageId,
          reason: revokeReason
        })
      });
      const data = await res.json();
      if (data.success) {
        setMsg(`Đã thu hồi gói của học viên ${revokingStudent.student.fullName}.`);
        setRevokingStudent(null);
        setRevokeReason("");
        loadAllData();
      } else {
        setErrorMsg(data.error || "Không thể thu hồi quyền.");
      }
    } catch {
      setErrorMsg("Lỗi kết nối khi thu hồi quyền.");
    } finally {
      setActionLoading(false);
      setTimeout(() => setMsg(""), 3500);
    }
  };

  // Handle 1-click Approve / Reject Request
  const handleProcessRequest = async (requestId: string, approve: boolean) => {
    try {
      setActionLoading(true);
      const res = await fetch("/api/enrollments/process-request", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          requestId,
          approve,
          durationDays: 30,
          note: approve ? "Phê duyệt nhanh từ bảng yêu cầu" : "Từ chối yêu cầu"
        })
      });
      const data = await res.json();
      if (data.success) {
        if (approve) ringBell();
        setMsg(data.message || (approve ? "Đã phê duyệt và cấp gói!" : "Đã từ chối yêu cầu."));
        loadAllData();
      } else {
        setErrorMsg(data.error || "Không thể xử lý yêu cầu.");
      }
    } catch {
      setErrorMsg("Lỗi kết nối máy chủ.");
    } finally {
      setActionLoading(false);
      setTimeout(() => setMsg(""), 3500);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card flex flex-wrap items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-100 text-amber-900 text-xs font-semibold mb-2">
            <Users className="w-3.5 h-3.5 text-amber-800" />
            <span>{t("Quản Trị Học Viên & Quyền Truy Cập Gói", "Student Entitlements & Progress Portal")}</span>
          </div>
          <h1 className="font-serif text-2xl font-bold text-zen-ink">
            {t("Quản Lý Học Viên, Cấp Gói & Phê Duyệt", "Student Accounts, Packages & Approvals")}
          </h1>
          <p className="text-xs text-zen-muted mt-1 leading-relaxed">
            {t(
              "Cấp gói học, thiết lập ngày bắt đầu và hết hạn, gia hạn/thu hồi quyền, phê duyệt 1-click yêu cầu đăng ký và kiểm tra mốc học tập bảo toàn 100% dữ liệu.",
              "Grant packages, set active durations, renew/revoke access, 1-click approve student requests, and inspect milestone records with guaranteed data preservation."
            )}
          </p>
        </div>

        <button
          onClick={loadAllData}
          disabled={loading}
          className="flex items-center gap-2 px-4 py-2 rounded-2xl bg-white border border-zen-border text-xs font-semibold text-zen-ink hover:bg-zen-surface transition-all shadow-zen-subtle disabled:opacity-50"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? "animate-spin" : ""}`} />
          <span>{loading ? t("Đang làm mới...", "Refreshing...") : t("Làm mới dữ liệu", "Refresh")}</span>
        </button>
      </div>

      {msg && (
        <div className="p-3.5 rounded-2xl bg-emerald-50 border border-emerald-300 text-xs font-semibold text-emerald-800 flex items-center gap-2">
          <Check className="w-4 h-4 text-emerald-600" />
          <span>{msg}</span>
        </div>
      )}

      {errorMsg && (
        <div className="p-4 rounded-2xl bg-rose-50 border border-rose-300 text-xs font-semibold text-rose-800 flex items-center gap-2">
          <ShieldAlert className="w-4 h-4 text-rose-600 shrink-0" />
          <span>{errorMsg}</span>
        </div>
      )}

      {/* Tabs */}
      <div className="flex border-b border-zen-border gap-2 text-xs font-semibold">
        <button
          onClick={() => setActiveTab("students")}
          className={`flex items-center gap-2 px-4 py-2.5 border-b-2 transition-all ${
            activeTab === "students"
              ? "border-amber-800 text-amber-900"
              : "border-transparent text-zen-muted hover:text-zen-ink"
          }`}
        >
          <Users className="w-4 h-4" />
          <span>{t("Tất Cả Học Viên", "All Students")} ({students.length})</span>
        </button>

        <button
          onClick={() => setActiveTab("requests")}
          className={`flex items-center gap-2 px-4 py-2.5 border-b-2 transition-all relative ${
            activeTab === "requests"
              ? "border-amber-800 text-amber-900"
              : "border-transparent text-zen-muted hover:text-zen-ink"
          }`}
        >
          <Clock className="w-4 h-4" />
          <span>{t("Yêu Cầu Đăng Ký & Gia Hạn", "Enrollment Requests")}</span>
          {pendingRequestsCount > 0 && (
            <span className="px-1.5 py-0.2 rounded-full bg-amber-600 text-white text-[10px] font-bold">
              {pendingRequestsCount}
            </span>
          )}
        </button>

        <button
          onClick={() => setActiveTab("history")}
          className={`flex items-center gap-2 px-4 py-2.5 border-b-2 transition-all ${
            activeTab === "history"
              ? "border-amber-800 text-amber-900"
              : "border-transparent text-zen-muted hover:text-zen-ink"
          }`}
        >
          <History className="w-4 h-4" />
          <span>{t("Nhật Ký Cấp & Gia Hạn Quyền", "Audit Log")} ({historyLogs.length})</span>
        </button>
      </div>

      {/* TAB 1: ALL STUDENTS */}
      {activeTab === "students" && (
        <div className="space-y-4">
          {/* Filter Bar & Search */}
          <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 text-xs">
            <div className="flex flex-wrap items-center gap-1.5">
              {[
                { id: "all", label: "Tất cả" },
                { id: "active", label: "Đang học" },
                { id: "trial", label: "Học thử" },
                { id: "expired", label: "Hết hạn" },
                { id: "pending", label: "Chờ duyệt" },
                { id: "revoked", label: "Đã thu hồi" }
              ].map((f) => (
                <button
                  key={f.id}
                  onClick={() => setStatusFilter(f.id)}
                  className={`px-3 py-1.5 rounded-xl border text-[11px] font-medium transition-colors ${
                    statusFilter === f.id
                      ? "bg-amber-900 text-white border-amber-900 shadow-2xs"
                      : "bg-zen-paper text-zen-ink border-zen-border hover:bg-zen-surface"
                  }`}
                >
                  {f.label}
                </button>
              ))}
            </div>

            <div className="flex items-center gap-2 bg-white rounded-xl border border-zen-border px-3 py-1.5 shadow-zen-subtle w-full sm:w-72">
              <Search className="w-3.5 h-3.5 text-zen-muted shrink-0" />
              <input
                type="text"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                placeholder={t("Tìm theo tên hoặc email...", "Search name or email...")}
                className="bg-transparent text-xs text-zen-ink focus:outline-hidden w-full"
              />
            </div>
          </div>

          {/* Students Table */}
          <div className="rounded-3xl border border-zen-border bg-zen-paper shadow-zen-card overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs border-collapse">
                <thead>
                  <tr className="border-b border-zen-border/70 bg-zen-surface/60 text-zen-muted uppercase text-[10px] font-bold tracking-wider">
                    <th className="py-3 px-4">{t("Học Viên", "Student")}</th>
                    <th className="py-3 px-4">{t("Gói Học & Thời Hạn", "Package & Duration")}</th>
                    <th className="py-3 px-4">{t("Trạng Thái", "Status")}</th>
                    <th className="py-3 px-4">{t("Tiến Độ & Sen", "Progress & Lotuses")}</th>
                    <th className="py-3 px-4">{t("Ghi Chú", "Notes")}</th>
                    <th className="py-3 px-4 text-right">{t("Thao Tác Quyền", "Actions")}</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-zen-border/40 text-zen-ink">
                  {loading && students.length === 0 ? (
                    <tr>
                      <td colSpan={6} className="py-12 text-center text-xs text-zen-muted">
                        🌱 {t("Đang tải danh sách học viên từ máy chủ...", "Loading students from server...")}
                      </td>
                    </tr>
                  ) : filteredStudents.length === 0 ? (
                    <tr>
                      <td colSpan={6} className="py-12 text-center text-xs text-zen-muted">
                        {t("Không tìm thấy học viên nào phù hợp.", "No students matching filter.")}
                      </td>
                    </tr>
                  ) : (
                    filteredStudents.map((s) => {
                      const activeEnr = s.enrollments?.find(
                        e => e.status === "active" && (!e.expiresAt || e.expiresAt > new Date().toISOString())
                      );
                      const latestEnr = s.enrollments?.[0];

                      return (
                        <tr key={s.id} className="hover:bg-zen-surface/40 transition-colors">
                          <td className="py-3.5 px-4">
                            <div className="font-semibold text-zen-ink">{s.fullName}</div>
                            <div className="text-[11px] text-zen-muted break-all">{s.email}</div>
                            <div className="mt-1 flex items-center gap-1.5">
                              <span className="px-1.5 py-0.2 rounded-md bg-zen-surface text-[10px] font-semibold text-stone-600 capitalize">
                                {s.role}
                              </span>
                              <span className="text-[10px] text-zen-muted">
                                {t("Hoạt động:", "Active:")} {s.lastActiveDate || "Hôm nay"}
                              </span>
                            </div>
                          </td>

                          <td className="py-3.5 px-4">
                            {activeEnr ? (
                              <div>
                                <span className="font-semibold text-zen-ink block">
                                  {activeEnr.packageName}
                                </span>
                                <span className="text-[10px] text-zen-muted flex items-center gap-1 mt-0.5">
                                  <Clock className="w-3 h-3 text-amber-700" />
                                  {activeEnr.expiresAt
                                    ? `Hạn đến: ${new Date(activeEnr.expiresAt).toLocaleDateString("vi-VN")}`
                                    : "Vô thời hạn"}
                                </span>
                              </div>
                            ) : latestEnr ? (
                              <div>
                                <span className="text-stone-500 font-medium block">
                                  {latestEnr.packageName}
                                </span>
                                <span className="text-[10px] text-rose-600">
                                  {latestEnr.status === "revoked" ? "Đã thu hồi" : "Đã hết hạn"}
                                </span>
                              </div>
                            ) : (
                              <span className="text-stone-400 italic text-[11px]">
                                {t("Chưa có gói", "No package")}
                              </span>
                            )}
                          </td>

                          <td className="py-3.5 px-4">
                            {s.enrollmentStatus === "active" && (
                              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-[10px] font-semibold">
                                <CheckCircle2 className="w-3 h-3 text-emerald-600" />
                                <span>Đang học</span>
                              </span>
                            )}
                            {s.enrollmentStatus === "trial" && (
                              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-sky-50 text-sky-800 border border-sky-200 text-[10px] font-semibold">
                                <Sparkles className="w-3 h-3 text-sky-600" />
                                <span>Học thử</span>
                              </span>
                            )}
                            {s.enrollmentStatus === "expired" && (
                              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-rose-50 text-rose-800 border border-rose-200 text-[10px] font-semibold">
                                <Clock className="w-3 h-3 text-rose-600" />
                                <span>Hết hạn</span>
                              </span>
                            )}
                            {s.enrollmentStatus === "pending" && (
                              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-amber-50 text-amber-800 border border-amber-200 text-[10px] font-semibold">
                                <AlertTriangle className="w-3 h-3 text-amber-600" />
                                <span>Chờ duyệt</span>
                              </span>
                            )}
                            {s.enrollmentStatus === "revoked" && (
                              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-stone-100 text-stone-600 border border-stone-200 text-[10px] font-semibold">
                                <XCircle className="w-3 h-3 text-stone-500" />
                                <span>Thu hồi</span>
                              </span>
                            )}
                            {s.enrollmentStatus === "none" && (
                              <span className="text-stone-400 text-[11px]">-</span>
                            )}
                          </td>

                          <td className="py-3.5 px-4">
                            <div className="font-semibold text-zen-ink">
                              {s.stats?.completedLessons ?? 0} {t("bài hoàn thành", "completed")}
                            </div>
                            <div className="text-[11px] text-zen-muted flex items-center gap-2 mt-0.5">
                              <span>✅ {s.stats?.passedQuizzes ?? 0} quiz</span>
                              <span className="font-bold text-zen-moss-dark">
                                🪷 {s.stats?.lotusesBloomed ?? 0} sen
                              </span>
                            </div>
                          </td>

                          <td className="py-3.5 px-4">
                            <span className="text-xs text-stone-600 font-medium">
                              📝 {s.stats?.notesCount ?? 0} {t("ghi chú", "notes")}
                            </span>
                          </td>

                          <td className="py-3.5 px-4 text-right">
                            <div className="flex items-center justify-end gap-1.5">
                              {/* Cấp Gói Button */}
                              <button
                                onClick={() => {
                                  setGrantingStudent(s);
                                  setGrantDurationDays(30);
                                  setGrantNote("");
                                }}
                                title={t("Cấp gói học mới", "Grant package")}
                                className="px-2 py-1 rounded-xl bg-amber-900 text-white font-semibold text-[11px] shadow-2xs hover:bg-amber-950 transition-colors flex items-center gap-1"
                              >
                                <PlusCircle className="w-3 h-3" />
                                <span>{t("Cấp gói", "Grant")}</span>
                              </button>

                              {/* Gia hạn nếu có gói active hoặc expired */}
                              {activeEnr && (
                                <button
                                  onClick={() => {
                                    setRenewingStudent({ student: s, enrollment: activeEnr });
                                    setRenewExtensionDays(30);
                                    setRenewNote("");
                                  }}
                                  title={t("Gia hạn thêm ngày học", "Renew package")}
                                  className="px-2 py-1 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-200 font-semibold text-[11px] transition-colors flex items-center gap-1"
                                >
                                  <RotateCw className="w-3 h-3" />
                                  <span>{t("Gia hạn", "Renew")}</span>
                                </button>
                              )}

                              {/* Thu hồi nếu có gói active */}
                              {activeEnr && (
                                <button
                                  onClick={() => {
                                    setRevokingStudent({ student: s, enrollment: activeEnr });
                                    setRevokeReason("");
                                  }}
                                  title={t("Thu hồi quyền truy cập", "Revoke package")}
                                  className="p-1 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 border border-rose-200 transition-colors"
                                >
                                  <XCircle className="w-3.5 h-3.5" />
                                </button>
                              )}

                              {/* Milestones Button */}
                              <button
                                onClick={() => setSelectedStudentMilestones(s)}
                                title={t("Xem mốc bài học đã lưu", "Inspect stored learning milestones")}
                                className="px-2 py-1 rounded-xl bg-white hover:bg-zen-surface text-zen-ink border border-zen-border font-semibold text-[11px] transition-colors flex items-center gap-1"
                              >
                                <History className="w-3 h-3 text-amber-700" />
                                <span>{t("Mốc", "Milestones")}</span>
                              </button>
                            </div>
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: ENROLLMENT REQUESTS */}
      {activeTab === "requests" && (
        <div className="space-y-4">
          <div className="rounded-3xl border border-zen-border bg-zen-paper shadow-zen-card overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs border-collapse">
                <thead>
                  <tr className="border-b border-zen-border/70 bg-zen-surface/60 text-zen-muted uppercase text-[10px] font-bold tracking-wider">
                    <th className="py-3 px-4">{t("Thời Điểm", "Time")}</th>
                    <th className="py-3 px-4">{t("Học Viên", "Student")}</th>
                    <th className="py-3 px-4">{t("Gói Yêu Cầu", "Requested Package")}</th>
                    <th className="py-3 px-4">{t("Loại Yêu Cầu", "Type")}</th>
                    <th className="py-3 px-4">{t("Lời Nhắn Của Học Viên", "Student Note")}</th>
                    <th className="py-3 px-4">{t("Trạng Thái", "Status")}</th>
                    <th className="py-3 px-4 text-right">{t("Phê Duyệt", "Actions")}</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-zen-border/40 text-zen-ink">
                  {requests.length === 0 ? (
                    <tr>
                      <td colSpan={7} className="py-12 text-center text-xs text-zen-muted">
                        {t("Chưa có yêu cầu đăng ký hoặc gia hạn nào.", "No enrollment requests found.")}
                      </td>
                    </tr>
                  ) : (
                    requests.map((r) => {
                      const isPending = r.status === "pending";
                      return (
                        <tr key={r.id} className="hover:bg-zen-surface/40 transition-colors">
                          <td className="py-3.5 px-4 font-mono text-[11px] text-zen-muted">
                            {new Date(r.requestedAt).toLocaleString("vi-VN")}
                          </td>

                          <td className="py-3.5 px-4">
                            <div className="font-semibold text-zen-ink">{r.userName}</div>
                            <div className="text-[11px] text-zen-muted">{r.userEmail}</div>
                          </td>

                          <td className="py-3.5 px-4 font-medium text-amber-900">
                            {r.packageName}
                          </td>

                          <td className="py-3.5 px-4">
                            <span
                              className={`px-2 py-0.5 rounded-full text-[10px] font-semibold ${
                                r.type === "renew"
                                  ? "bg-purple-50 text-purple-800 border border-purple-200"
                                  : "bg-blue-50 text-blue-800 border border-blue-200"
                              }`}
                            >
                              {r.type === "renew" ? "Gia hạn" : "Đăng ký mới"}
                            </span>
                          </td>

                          <td className="py-3.5 px-4 max-w-xs truncate text-zen-muted">
                            {r.userNote || "-"}
                          </td>

                          <td className="py-3.5 px-4">
                            {r.status === "pending" && (
                              <span className="px-2 py-0.5 rounded-full bg-amber-50 text-amber-800 border border-amber-200 text-[10px] font-semibold">
                                Đang chờ duyệt
                              </span>
                            )}
                            {r.status === "approved" && (
                              <span className="px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 text-[10px] font-semibold">
                                Đã phê duyệt
                              </span>
                            )}
                            {r.status === "rejected" && (
                              <span className="px-2 py-0.5 rounded-full bg-stone-100 text-stone-600 border border-stone-200 text-[10px] font-semibold">
                                Đã từ chối
                              </span>
                            )}
                          </td>

                          <td className="py-3.5 px-4 text-right">
                            {isPending ? (
                              <div className="flex items-center justify-end gap-1.5">
                                <button
                                  disabled={actionLoading}
                                  onClick={() => handleProcessRequest(r.id, true)}
                                  className="px-2.5 py-1 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white font-semibold text-[11px] shadow-2xs transition-colors flex items-center gap-1"
                                >
                                  <Check className="w-3 h-3" />
                                  <span>{t("Phê duyệt", "Approve")}</span>
                                </button>
                                <button
                                  disabled={actionLoading}
                                  onClick={() => handleProcessRequest(r.id, false)}
                                  className="px-2 py-1 rounded-xl border border-rose-200 bg-white hover:bg-rose-50 text-rose-700 font-semibold text-[11px] transition-colors"
                                >
                                  {t("Từ chối", "Reject")}
                                </button>
                              </div>
                            ) : (
                              <span className="text-[10px] text-zen-muted">
                                Bởi: {r.processedBy || "admin"}
                              </span>
                            )}
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: AUDIT LOG (HISTORY) */}
      {activeTab === "history" && (
        <div className="space-y-4">
          <div className="rounded-3xl border border-zen-border bg-zen-paper shadow-zen-card overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs border-collapse">
                <thead>
                  <tr className="border-b border-zen-border/70 bg-zen-surface/60 text-zen-muted uppercase text-[10px] font-bold tracking-wider">
                    <th className="py-3 px-4">{t("Thời Điểm", "Time")}</th>
                    <th className="py-3 px-4">{t("Người Thao Tác", "Actor")}</th>
                    <th className="py-3 px-4">{t("Học Viên", "Student")}</th>
                    <th className="py-3 px-4">{t("Hành Động", "Action")}</th>
                    <th className="py-3 px-4">{t("Gói Học", "Package")}</th>
                    <th className="py-3 px-4">{t("Hạn Mới", "New Expiry")}</th>
                    <th className="py-3 px-4">{t("Ghi Chú", "Note")}</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-zen-border/40 text-zen-ink">
                  {historyLogs.length === 0 ? (
                    <tr>
                      <td colSpan={7} className="py-12 text-center text-xs text-zen-muted">
                        {t("Chưa có lịch sử thay đổi quyền nào.", "No audit logs found.")}
                      </td>
                    </tr>
                  ) : (
                    historyLogs.map((h) => (
                      <tr key={h.id} className="hover:bg-zen-surface/40 transition-colors">
                        <td className="py-3 px-4 font-mono text-[11px] text-zen-muted">
                          {new Date(h.timestamp).toLocaleString("vi-VN")}
                        </td>

                        <td className="py-3 px-4 text-zen-ink font-medium">
                          {h.actorEmail}
                        </td>

                        <td className="py-3 px-4 text-zen-ink">
                          {h.userEmail}
                        </td>

                        <td className="py-3 px-4">
                          <span
                            className={`px-2 py-0.5 rounded-full text-[10px] font-semibold ${
                              h.action === "grant"
                                ? "bg-emerald-50 text-emerald-800 border border-emerald-200"
                                : h.action === "renew"
                                ? "bg-purple-50 text-purple-800 border border-purple-200"
                                : "bg-rose-50 text-rose-800 border border-rose-200"
                            }`}
                          >
                            {h.action === "grant" ? "Cấp mới" : h.action === "renew" ? "Gia hạn" : "Thu hồi"}
                          </span>
                        </td>

                        <td className="py-3 px-4 font-medium text-amber-900">
                          {h.packageName}
                        </td>

                        <td className="py-3 px-4 text-[11px] text-zen-muted">
                          {h.newExpiresAt ? new Date(h.newExpiresAt).toLocaleDateString("vi-VN") : "Vô thời hạn"}
                        </td>

                        <td className="py-3 px-4 text-zen-muted max-w-xs truncate">
                          {h.note || "-"}
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* MODAL: GRANT PACKAGE */}
      {grantingStudent && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-zen-paper border border-zen-border rounded-3xl max-w-md w-full p-6 shadow-xl space-y-4 animate-in fade-in duration-150">
            <div className="flex items-center justify-between pb-3 border-b border-zen-border">
              <div className="flex items-center gap-2">
                <PlusCircle className="w-5 h-5 text-amber-800" />
                <h3 className="font-serif font-bold text-base text-zen-ink">
                  {t("Cấp Quyền Gói Cho Học Viên", "Grant Package to Student")}
                </h3>
              </div>
              <button
                onClick={() => setGrantingStudent(null)}
                className="p-1 rounded-full hover:bg-zen-surface text-zen-muted"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="p-3 rounded-2xl bg-zen-surface border border-zen-border text-xs space-y-1">
              <div className="font-semibold text-zen-ink">{grantingStudent.fullName}</div>
              <div className="text-[11px] text-zen-muted">{grantingStudent.email}</div>
            </div>

            <div className="space-y-3 text-xs">
              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Chọn Gói Học Viên", "Select Package")} *
                </label>
                <select
                  value={grantPackageId}
                  onChange={(e) => setGrantPackageId(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs font-medium"
                >
                  {packages.map((p) => (
                    <option key={p.id} value={p.id}>
                      {p.nameVi} ({p.durationDays === 0 ? "Vô thời hạn" : `${p.durationDays} ngày`}) - {p.price === 0 ? "Miễn phí" : `${p.price.toLocaleString("vi-VN")} đ`}
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Thời Hạn Sử Dụng (Số Ngày)", "Duration (Days)")} (0 = {t("Vô thời hạn", "Unlimited")})
                </label>
                <div className="flex items-center gap-2 mb-2">
                  {[7, 30, 90, 180, 365, 0].map((d) => (
                    <button
                      key={d}
                      type="button"
                      onClick={() => setGrantDurationDays(d)}
                      className={`px-2.5 py-1 rounded-lg border text-[11px] font-medium ${
                        grantDurationDays === d
                          ? "bg-amber-900 text-white border-amber-900"
                          : "bg-white text-zen-ink border-zen-border hover:bg-zen-surface"
                      }`}
                    >
                      {d === 0 ? "Vô hạn" : `${d}d`}
                    </button>
                  ))}
                </div>
                <input
                  type="number"
                  min={0}
                  value={grantDurationDays}
                  onChange={(e) => setGrantDurationDays(parseInt(e.target.value) || 0)}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs"
                />
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Ghi Chú Cấp Quyền (Lưu Vào Audit Log)", "Admin Note")}
                </label>
                <input
                  type="text"
                  value={grantNote}
                  onChange={(e) => setGrantNote(e.target.value)}
                  placeholder="Ví dụ: Đã nhận chuyển khoản qua VietQR / Học bổng"
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs"
                />
              </div>
            </div>

            <div className="pt-3 border-t border-zen-border flex items-center justify-end gap-2 text-xs">
              <button
                type="button"
                onClick={() => setGrantingStudent(null)}
                className="px-4 py-2 rounded-xl border border-zen-border bg-white text-zen-muted hover:bg-zen-surface font-medium"
              >
                {t("Hủy bỏ", "Cancel")}
              </button>
              <button
                type="button"
                disabled={actionLoading}
                onClick={handleConfirmGrant}
                className="px-5 py-2 rounded-xl bg-amber-900 text-white font-semibold hover:bg-amber-950 shadow-sm disabled:opacity-50"
              >
                {actionLoading ? t("Đang xử lý...", "Processing...") : t("Xác Nhận Cấp Gói", "Confirm Grant")}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* MODAL: RENEW PACKAGE */}
      {renewingStudent && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-zen-paper border border-zen-border rounded-3xl max-w-md w-full p-6 shadow-xl space-y-4 animate-in fade-in duration-150">
            <div className="flex items-center justify-between pb-3 border-b border-zen-border">
              <div className="flex items-center gap-2">
                <RotateCw className="w-5 h-5 text-emerald-700" />
                <h3 className="font-serif font-bold text-base text-zen-ink">
                  {t("Gia Hạn Gói Học", "Renew Student Package")}
                </h3>
              </div>
              <button
                onClick={() => setRenewingStudent(null)}
                className="p-1 rounded-full hover:bg-zen-surface text-zen-muted"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="p-3 rounded-2xl bg-zen-surface border border-zen-border text-xs space-y-1">
              <div className="font-semibold text-zen-ink">{renewingStudent.student.fullName}</div>
              <div className="text-[11px] text-zen-muted">
                {renewingStudent.enrollment.packageName} • Hạn hiện tại:{" "}
                {renewingStudent.enrollment.expiresAt
                  ? new Date(renewingStudent.enrollment.expiresAt).toLocaleDateString("vi-VN")
                  : "Vô thời hạn"}
              </div>
            </div>

            <div className="space-y-3 text-xs">
              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Số Ngày Gia Hạn Thêm", "Extension Days")}
                </label>
                <div className="flex items-center gap-2 mb-2">
                  {[30, 60, 90, 180, 365].map((d) => (
                    <button
                      key={d}
                      type="button"
                      onClick={() => setRenewExtensionDays(d)}
                      className={`px-3 py-1 rounded-lg border text-[11px] font-medium ${
                        renewExtensionDays === d
                          ? "bg-emerald-700 text-white border-emerald-700"
                          : "bg-white text-zen-ink border-zen-border hover:bg-zen-surface"
                      }`}
                    >
                      +{d} ngày
                    </button>
                  ))}
                </div>
                <input
                  type="number"
                  min={1}
                  value={renewExtensionDays}
                  onChange={(e) => setRenewExtensionDays(parseInt(e.target.value) || 30)}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs"
                />
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Ghi Chú Gia Hạn", "Note")}
                </label>
                <input
                  type="text"
                  value={renewNote}
                  onChange={(e) => setRenewNote(e.target.value)}
                  placeholder="Ví dụ: Gia hạn đợt 2 theo chương trình khuyến mãi"
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs"
                />
              </div>
            </div>

            <div className="pt-3 border-t border-zen-border flex items-center justify-end gap-2 text-xs">
              <button
                type="button"
                onClick={() => setRenewingStudent(null)}
                className="px-4 py-2 rounded-xl border border-zen-border bg-white text-zen-muted hover:bg-zen-surface font-medium"
              >
                {t("Hủy bỏ", "Cancel")}
              </button>
              <button
                type="button"
                disabled={actionLoading}
                onClick={handleConfirmRenew}
                className="px-5 py-2 rounded-xl bg-emerald-700 text-white font-semibold hover:bg-emerald-800 shadow-sm disabled:opacity-50"
              >
                {actionLoading ? t("Đang xử lý...", "Processing...") : t("Xác Nhận Gia Hạn", "Confirm Renew")}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* MODAL: REVOKE PACKAGE */}
      {revokingStudent && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-zen-paper border border-zen-border rounded-3xl max-w-md w-full p-6 shadow-xl space-y-4 animate-in fade-in duration-150">
            <div className="flex items-center justify-between pb-3 border-b border-zen-border">
              <div className="flex items-center gap-2">
                <AlertTriangle className="w-5 h-5 text-rose-700" />
                <h3 className="font-serif font-bold text-base text-rose-900">
                  {t("Thu Hồi Quyền Truy Cập Gói", "Revoke Package Access")}
                </h3>
              </div>
              <button
                onClick={() => setRevokingStudent(null)}
                className="p-1 rounded-full hover:bg-zen-surface text-zen-muted"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <p className="text-xs text-rose-800 leading-relaxed bg-rose-50 p-3 rounded-2xl border border-rose-200">
              {t(
                `Bạn có chắc chắn muốn thu hồi gói "${revokingStudent.enrollment.packageName}" của học viên ${revokingStudent.student.fullName}? Toàn bộ tiến độ và đóa sen của học viên vẫn được bảo toàn nguyên vẹn trên hệ thống.`,
                `Are you sure you want to revoke this package? Student progress, notes, and bloomed lotuses remain completely preserved.`
              )}
            </p>

            <div className="space-y-1 text-xs">
              <label className="block font-semibold text-zen-ink">
                {t("Lý Do Thu Hồi (Bắt Buộc)", "Reason for Revocation")}
              </label>
              <input
                type="text"
                required
                value={revokeReason}
                onChange={(e) => setRevokeReason(e.target.value)}
                placeholder="Ví dụ: Hoàn tiền theo yêu cầu / Hết thời gian chuyển đổi"
                className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs"
              />
            </div>

            <div className="pt-3 border-t border-zen-border flex items-center justify-end gap-2 text-xs">
              <button
                type="button"
                onClick={() => setRevokingStudent(null)}
                className="px-4 py-2 rounded-xl border border-zen-border bg-white text-zen-muted hover:bg-zen-surface font-medium"
              >
                {t("Hủy bỏ", "Cancel")}
              </button>
              <button
                type="button"
                disabled={actionLoading || !revokeReason.trim()}
                onClick={handleConfirmRevoke}
                className="px-5 py-2 rounded-xl bg-rose-700 text-white font-semibold hover:bg-rose-800 shadow-sm disabled:opacity-50"
              >
                {actionLoading ? t("Đang xử lý...", "Processing...") : t("Xác Nhận Thu Hồi", "Confirm Revoke")}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* MODAL: MILESTONES INSPECTION */}
      {selectedStudentMilestones && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl border border-zen-border shadow-zen-floating max-w-2xl w-full p-6 space-y-5 max-h-[85vh] flex flex-col animate-in fade-in duration-150">
            <div className="flex items-center justify-between border-b border-zen-border/70 pb-4">
              <div className="flex items-center gap-2.5">
                <div className="w-8 h-8 rounded-xl bg-amber-100 text-amber-900 flex items-center justify-center">
                  <History className="w-4 h-4 text-amber-800" />
                </div>
                <div>
                  <h3 className="font-serif font-bold text-base text-zen-ink">
                    {t("Mốc Học Tập Đã Lưu Trên Máy Chủ", "Server-Saved Learning Milestones")}
                  </h3>
                  <p className="text-[11px] text-zen-muted">
                    {selectedStudentMilestones.fullName} • {selectedStudentMilestones.email}
                  </p>
                </div>
              </div>
              <button
                onClick={() => setSelectedStudentMilestones(null)}
                className="p-1.5 rounded-xl hover:bg-zen-surface text-zen-muted transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* Overview Stats */}
            <div className="grid grid-cols-3 gap-3 p-3.5 rounded-2xl bg-zen-surface/70 border border-zen-border/60 text-center">
              <div>
                <span className="text-[10px] text-zen-muted block">{t("Bài đã hoàn thành", "Completed Lessons")}</span>
                <span className="font-serif text-lg font-bold text-zen-ink">
                  {selectedStudentMilestones.stats?.completedLessons ?? 0}
                </span>
              </div>
              <div>
                <span className="text-[10px] text-zen-muted block">{t("Đậu trắc nghiệm", "Passed Quizzes")}</span>
                <span className="font-serif text-lg font-bold text-emerald-700">
                  {selectedStudentMilestones.stats?.passedQuizzes ?? 0}
                </span>
              </div>
              <div>
                <span className="text-[10px] text-zen-muted block">{t("Đóa sen đã nhận", "Lotuses Awarded")}</span>
                <span className="font-serif text-lg font-bold text-zen-moss-dark">
                  🪷 {selectedStudentMilestones.stats?.lotusesBloomed ?? 0}
                </span>
              </div>
            </div>

            {/* Milestones Timeline */}
            <div className="overflow-y-auto space-y-2.5 pr-1 flex-1">
              {selectedStudentMilestones.milestones && selectedStudentMilestones.milestones.length > 0 ? (
                selectedStudentMilestones.milestones.map((m, idx) => (
                  <div
                    key={idx}
                    className="p-3 rounded-2xl border border-zen-border bg-zen-paper flex items-center justify-between text-xs"
                  >
                    <div className="flex items-center gap-2.5">
                      <span className="text-base">
                        {m.status === "quiz_passed" ? "🎯" : "📖"}
                      </span>
                      <div>
                        <span className="font-semibold text-zen-ink block">
                          {m.status === "quiz_passed"
                            ? t(`Vượt qua trắc nghiệm bài: ${m.lessonId}`, `Passed quiz for: ${m.lessonId}`)
                            : t(`Đã đọc xong bài: ${m.lessonId}`, `Completed reading: ${m.lessonId}`)}
                        </span>
                        <span className="text-[10px] text-zen-muted">
                          {t("Thời điểm ghi nhận:", "Recorded at:")} {new Date(m.updatedAt).toLocaleString("vi-VN")}
                          {m.score !== null && m.score !== undefined ? ` • Điểm: ${m.score}/100` : ""}
                        </span>
                      </div>
                    </div>
                    <span className="text-xs font-bold text-zen-moss-dark px-2 py-0.5 rounded-full bg-zen-moss/10">
                      +1 🪷 Sen
                    </span>
                  </div>
                ))
              ) : (
                <div className="py-8 text-center text-xs text-zen-muted">
                  {t(
                    "Học viên này chưa có mốc hoàn thành bài học nào được ghi nhận trên máy chủ.",
                    "No server milestones recorded for this student yet."
                  )}
                </div>
              )}
            </div>

            <div className="border-t border-zen-border/70 pt-3 flex items-center justify-between text-[11px] text-zen-muted">
              <span>🛡️ {t("Dữ liệu được xác thực và bảo mật", "Verified & tamper-proof server record")}</span>
              <button
                onClick={() => setSelectedStudentMilestones(null)}
                className="px-4 py-1.5 rounded-xl bg-amber-900 text-white font-semibold text-xs shadow-sm hover:bg-amber-950 transition-colors"
              >
                {t("Đóng", "Close")}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
