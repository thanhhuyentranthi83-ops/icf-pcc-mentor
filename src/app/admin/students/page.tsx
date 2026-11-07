"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import { useAuth } from "@/context/AuthContext";
import { Tier } from "@/types";
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
  RefreshCw
} from "lucide-react";

interface AdminStudentItem {
  id: string;
  email: string;
  fullName: string;
  role: string;
  tier: Tier;
  tierExpiresAt: string | null;
  streakCount: number;
  lastActiveDate: string;
  createdAt: string;
  completedLessonsCount: number;
  quizPassedCount: number;
  lotusCount: number;
  notesCount: number;
  needsReviewCount: number;
  milestones: Array<{
    type: string;
    lessonId: string;
    at: string;
    score?: number;
  }>;
}

export default function AdminStudentsPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user: currentAdmin } = useAuth();

  const [students, setStudents] = useState<AdminStudentItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState("");
  const [search, setSearch] = useState("");
  const [editingUserId, setEditingUserId] = useState<string | null>(null);
  const [selectedTier, setSelectedTier] = useState<Tier>("free");
  const [msg, setMsg] = useState("");
  const [selectedStudentMilestones, setSelectedStudentMilestones] = useState<AdminStudentItem | null>(null);

  const loadStudents = async () => {
    setLoading(true);
    setErrorMsg("");
    try {
      const res = await fetch("/api/admin/students");
      const data = await res.json();
      if (data.success) {
        const normalized: AdminStudentItem[] = data.students.map((s: any) => ({
          ...s,
          completedLessonsCount: s.stats?.completedLessons ?? s.completedLessonsCount ?? 0,
          quizPassedCount: s.stats?.passedQuizzes ?? s.quizPassedCount ?? 0,
          lotusCount: s.stats?.lotusesBloomed ?? s.lotusCount ?? 0,
          notesCount: s.stats?.notesCount ?? s.notesCount ?? 0,
          needsReviewCount: s.stats?.flaggedLessonsCount ?? s.needsReviewCount ?? 0,
          milestones: (s.milestones || []).map((m: any) => ({
            type: m.status || m.type || "read",
            lessonId: m.lessonId,
            at: m.updatedAt || m.at || new Date().toISOString(),
            score: m.score
          }))
        }));
        setStudents(normalized);
      } else {
        setErrorMsg(data.error || "Không thể tải danh sách học viên từ máy chủ.");
      }
    } catch {
      setErrorMsg("Lỗi kết nối máy chủ quản trị.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadStudents();
  }, []);

  const handleOpenEdit = (s: AdminStudentItem) => {
    setEditingUserId(s.id);
    setSelectedTier(s.tier);
  };

  const handleSaveTier = async (s: AdminStudentItem) => {
    try {
      const res = await fetch("/api/admin/students", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          studentId: s.id,
          tier: selectedTier,
          tierExpiresAt:
            selectedTier === "free"
              ? null
              : new Date(Date.now() + 30 * 86400000).toISOString()
        })
      });
      if (res.ok) {
        setStudents(prev =>
          prev.map(item => {
            if (item.id === s.id) {
              return {
                ...item,
                tier: selectedTier,
                tierExpiresAt:
                  selectedTier === "free"
                    ? null
                    : new Date(Date.now() + 30 * 86400000).toISOString()
              };
            }
            return item;
          })
        );
        ringBell();
        setMsg(t(`Đã cập nhật gói của học viên ${s.fullName} thành ${selectedTier}!`, `Updated student tier to ${selectedTier}!`));
      } else {
        setErrorMsg("Không thể cập nhật gói trên máy chủ.");
      }
    } catch {
      setErrorMsg("Lỗi kết nối khi cập nhật gói.");
    } finally {
      setEditingUserId(null);
      setTimeout(() => setMsg(""), 3500);
    }
  };

  const filteredStudents = students.filter((s) => {
    if (!search.trim()) return true;
    const q = search.toLowerCase();
    return s.fullName.toLowerCase().includes(q) || s.email.toLowerCase().includes(q);
  });

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card flex flex-wrap items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-100 text-amber-900 text-xs font-semibold mb-2">
            <Users className="w-3.5 h-3.5 text-amber-800" />
            <span>{t("Quản Trị Học Viên & Tiến Độ Học Tập", "Student Progress & Account Portal")}</span>
          </div>
          <h1 className="font-serif text-2xl font-bold text-zen-ink">
            {t("Danh Sách Học Viên & Mốc Nhận Sen", "Student Accounts & Lotus Milestones")}
          </h1>
          <p className="text-xs text-zen-muted mt-1 leading-relaxed">
            {t(
              "Xem danh sách tài khoản học viên, gói học, tiến độ hoàn thành bài, kết quả trắc nghiệm và số đóa sen đã ghi nhận. Hỗ trợ tra cứu mốc học tập khi học viên báo mất tiến độ.",
              "Inspect verified student accounts, active tiers, completed lessons, quiz outcomes, and recorded lotuses. Review milestones to resolve lost progress inquiries."
            )}
          </p>
        </div>

        <button
          onClick={loadStudents}
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

      {/* Privacy Notice Banner */}
      <div className="rounded-2xl border border-zen-border/70 bg-zen-surface/60 p-4 text-xs text-zen-ink flex items-start gap-3">
        <Lock className="w-4 h-4 text-zen-moss-dark shrink-0 mt-0.5" />
        <div className="space-y-0.5">
          <p className="font-semibold text-zen-ink">
            {t("Nguyên Tắc Bảo Mật Ghi Chú Cá Nhân Học Viên", "Student Note Privacy Policy")}
          </p>
          <p className="text-zen-muted text-[11px] leading-relaxed">
            {t(
              "Nội dung văn bản trong Sổ học tập của học viên là không gian chiêm nghiệm riêng tư, được bảo mật ở cấp độ máy chủ. Quản trị viên chỉ xem được số lượng ghi chú đã tạo và số mốc bài học đã lưu để hỗ trợ kỹ thuật, không thể đọc nội dung nhật ký.",
              "Student journal note text is strictly private and safeguarded at the server level. Administrators can only see count metrics and milestone completion timestamps."
            )}
          </p>
        </div>
      </div>

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
        <span className="text-zen-muted font-medium">
          {filteredStudents.length} {t("tài khoản học viên", "student accounts")}
        </span>
      </div>

      {/* Students Table */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper shadow-zen-card overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-zen-border/70 bg-zen-surface/60 text-zen-muted uppercase text-[10px] font-bold tracking-wider">
                <th className="py-3 px-4">{t("Học Viên", "Student")}</th>
                <th className="py-3 px-4">{t("Gói Học & Hạn Dùng", "Active Tier")}</th>
                <th className="py-3 px-4">{t("Tiến Độ Bài Học", "Lesson Progress")}</th>
                <th className="py-3 px-4">{t("Đóa Sen Đã Nở", "Lotuses Bloomed")}</th>
                <th className="py-3 px-4">{t("Ghi Chú", "Notes")}</th>
                <th className="py-3 px-4 text-right">{t("Hành Động", "Actions")}</th>
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
                    {t("Không tìm thấy học viên nào khớp với tìm kiếm.", "No matching students found.")}
                  </td>
                </tr>
              ) : (
                filteredStudents.map((s) => {
                  const isEditing = editingUserId === s.id;
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

                      <td className="py-3.5 px-4 capitalize">
                        {isEditing ? (
                          <select
                            value={selectedTier}
                            onChange={(e) => setSelectedTier(e.target.value as Tier)}
                            className="px-2 py-1 bg-white border border-zen-border rounded-lg text-xs"
                          >
                            <option value="free">Free Tier</option>
                            <option value="1_month">1 Tháng</option>
                            <option value="6_months">6 Tháng</option>
                            <option value="12_months">12 Tháng</option>
                          </select>
                        ) : (
                          <div>
                            <span className="font-semibold text-zen-moss-dark block">
                              {s.tier === "free" ? "Free Tier" : s.tier.replace("_", " ")}
                            </span>
                            <span className="text-[10px] text-zen-muted">
                              {s.tierExpiresAt
                                ? new Date(s.tierExpiresAt).toLocaleDateString("vi-VN")
                                : "Vô thời hạn"}
                            </span>
                          </div>
                        )}
                      </td>

                      <td className="py-3.5 px-4">
                        <div className="font-semibold text-zen-ink">
                          {s.completedLessonsCount} {t("bài hoàn thành", "completed")}
                        </div>
                        <div className="text-[11px] text-zen-muted">
                          ✅ {s.quizPassedCount} {t("đậu trắc nghiệm", "passed quiz")}
                        </div>
                      </td>

                      <td className="py-3.5 px-4">
                        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-zen-moss/15 text-zen-moss-dark font-bold text-xs">
                          <span>🪷</span>
                          <span>{s.lotusCount}</span>
                        </div>
                      </td>

                      <td className="py-3.5 px-4">
                        <span className="text-xs text-stone-600 font-medium">
                          📝 {s.notesCount} {t("ghi chú", "notes")}
                        </span>
                      </td>

                      <td className="py-3.5 px-4 text-right">
                        <div className="flex items-center justify-end gap-1.5">
                          <button
                            onClick={() => setSelectedStudentMilestones(s)}
                            title={t("Kiểm tra mốc học tập đã lưu", "Inspect stored learning milestones")}
                            className="px-2.5 py-1 rounded-xl bg-amber-50 hover:bg-amber-100/80 text-amber-900 border border-amber-200 font-semibold text-[11px] shadow-zen-subtle transition-all flex items-center gap-1"
                          >
                            <History className="w-3 h-3 text-amber-700" />
                            <span>{t("Mốc học tập", "Milestones")}</span>
                          </button>

                          {isEditing ? (
                            <div className="flex items-center gap-1">
                              <button
                                onClick={() => handleSaveTier(s)}
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
                              onClick={() => handleOpenEdit(s)}
                              className="px-2.5 py-1 rounded-xl border border-zen-border bg-white hover:bg-zen-surface text-zen-ink font-semibold text-[11px] shadow-zen-subtle transition-all"
                            >
                              {t("Đổi gói", "Change Tier")}
                            </button>
                          )}
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

      {/* Milestones Inspection Modal */}
      {selectedStudentMilestones && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in duration-150">
          <div className="bg-white rounded-3xl border border-zen-border shadow-zen-floating max-w-2xl w-full p-6 space-y-5 max-h-[85vh] flex flex-col">
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
                  {selectedStudentMilestones.completedLessonsCount}
                </span>
              </div>
              <div>
                <span className="text-[10px] text-zen-muted block">{t("Đậu trắc nghiệm", "Passed Quizzes")}</span>
                <span className="font-serif text-lg font-bold text-emerald-700">
                  {selectedStudentMilestones.quizPassedCount}
                </span>
              </div>
              <div>
                <span className="text-[10px] text-zen-muted block">{t("Đóa sen đã nhận", "Lotuses Awarded")}</span>
                <span className="font-serif text-lg font-bold text-zen-moss-dark">
                  🪷 {selectedStudentMilestones.lotusCount}
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
                        {m.type === "quiz_passed" ? "🎯" : "📖"}
                      </span>
                      <div>
                        <span className="font-semibold text-zen-ink block">
                          {m.type === "quiz_passed"
                            ? t(`Vượt qua trắc nghiệm bài: ${m.lessonId}`, `Passed quiz for: ${m.lessonId}`)
                            : t(`Đã đọc xong bài: ${m.lessonId}`, `Completed reading: ${m.lessonId}`)}
                        </span>
                        <span className="text-[10px] text-zen-muted">
                          {t("Thời điểm ghi nhận:", "Recorded at:")} {new Date(m.at).toLocaleString("vi-VN")}
                          {m.score !== undefined ? ` • Điểm: ${m.score}/100` : ""}
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
                className="px-4 py-1.5 rounded-xl bg-zen-moss text-white font-semibold text-xs shadow-sm hover:bg-zen-moss-dark transition-colors"
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
