"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { PackageRecord, FeatureKey, CourseRecord } from "@/types";
import {
  Package,
  Plus,
  Edit2,
  Trash2,
  CheckCircle2,
  Clock,
  Tag,
  ShieldCheck,
  Check,
  Save,
  X,
  Layers,
  Sparkles,
  ToggleLeft,
  ToggleRight
} from "lucide-react";

const AVAILABLE_FEATURES: { key: FeatureKey; labelVi: string; labelEn: string; descVi: string }[] = [
  {
    key: "curriculum",
    labelVi: "Lộ Trình Học Lý Thuyết & Quiz",
    labelEn: "Curriculum & Lessons",
    descVi: "Toàn bộ bài giảng 7 học phần và 26 bài học chuẩn ICF"
  },
  {
    key: "daily_sjt_10",
    labelVi: "Luyện 10 Câu SJT / Ngày",
    labelEn: "Daily 10 SJT",
    descVi: "Luyện phản xạ phán đoán tình huống mỗi ngày"
  },
  {
    key: "mock_exam_sjt",
    labelVi: "Thi Thử Mô Phỏng Đề Thi ICF",
    labelEn: "Mock Exam SJT",
    descVi: "Phòng thi tính giờ chuẩn Pearson VUE kèm phân tích Best/Worst"
  },
  {
    key: "glossary_search",
    labelVi: "Tra Cứu Thuật Ngữ Song Ngữ",
    labelEn: "Glossary Search",
    descVi: "Bộ từ điển đối chiếu Anh-Việt chuẩn hóa 2025"
  },
  {
    key: "tea_micro",
    labelVi: "Góc Trà Đàm & Phản Tư",
    labelEn: "Tea Micro-Reflection",
    descVi: "Bài tập rèn luyện tâm thế và hiện diện của người khai vấn"
  },
  {
    key: "resource_download",
    labelVi: "Tải Học Liệu & Bản Chuẩn",
    labelEn: "Resource Downloads",
    descVi: "Tải tài liệu PDF chuẩn ICF và sổ tay khai vấn"
  }
];

export default function AdminPackagesPage() {
  const { t } = useLanguage();
  const [packages, setPackages] = useState<PackageRecord[]>([]);
  const [courses, setCourses] = useState<CourseRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  const [editingPkg, setEditingPkg] = useState<Partial<PackageRecord>>({
    id: "",
    nameVi: "",
    nameEn: "",
    descriptionVi: "",
    descriptionEn: "",
    price: 0,
    durationDays: 30,
    isRegistrationOpen: true,
    allowedCourseIds: ["*"],
    allowedFeatures: ["curriculum", "daily_sjt_10", "glossary_search"],
    badge: "",
    isDefaultTrial: false
  });
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [resPkg, resCrs] = await Promise.all([
        fetch("/api/packages?all=true"),
        fetch("/api/courses?all=true")
      ]);
      const dataPkg = await resPkg.json();
      const dataCrs = await resCrs.json();

      if (dataPkg.success && dataPkg.packages) {
        setPackages(dataPkg.packages);
      }
      if (dataCrs.success && dataCrs.courses) {
        setCourses(dataCrs.courses);
      }
    } catch (err) {
      console.error("Fetch packages error:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleOpenCreate = () => {
    setEditingPkg({
      id: `pkg-${Date.now().toString(36)}`,
      nameVi: "",
      nameEn: "",
      descriptionVi: "",
      descriptionEn: "",
      price: 0,
      durationDays: 30,
      isRegistrationOpen: true,
      allowedCourseIds: ["*"],
      allowedFeatures: ["curriculum", "daily_sjt_10"],
      badge: "Mới",
      isDefaultTrial: false
    });
    setIsEditing(true);
    setMessage(null);
  };

  const handleOpenEdit = (pkg: PackageRecord) => {
    setEditingPkg({ ...pkg });
    setIsEditing(true);
    setMessage(null);
  };

  const handleToggleRegistration = async (pkg: PackageRecord) => {
    try {
      const updated = { ...pkg, isRegistrationOpen: !pkg.isRegistrationOpen };
      const res = await fetch("/api/packages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updated)
      });
      const data = await res.json();
      if (data.success) {
        setPackages(packages.map(p => (p.id === pkg.id ? updated : p)));
      }
    } catch (err) {
      console.error("Toggle registration error:", err);
    }
  };

  const handleDelete = async (id: string, name: string) => {
    if (!window.confirm(`Bạn có chắc muốn xóa gói "${name}"?`)) return;
    try {
      const res = await fetch(`/api/packages?id=${encodeURIComponent(id)}`, {
        method: "DELETE"
      });
      const data = await res.json();
      if (data.success) {
        setPackages(packages.filter(p => p.id !== id));
        setMessage({ type: "success", text: `Đã xóa gói "${name}".` });
      } else {
        setMessage({ type: "error", text: data.error || "Không thể xóa gói." });
      }
    } catch (err) {
      setMessage({ type: "error", text: "Lỗi kết nối máy chủ." });
    }
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingPkg.nameVi || !editingPkg.allowedFeatures || editingPkg.allowedFeatures.length === 0) {
      setMessage({ type: "error", text: "Vui lòng nhập tên gói và chọn ít nhất 1 tính năng được mở." });
      return;
    }

    try {
      setSaving(true);
      setMessage(null);
      const res = await fetch("/api/packages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(editingPkg)
      });
      const data = await res.json();
      if (data.success) {
        setIsEditing(false);
        setMessage({ type: "success", text: "Đã lưu cấu hình gói học viên thành công!" });
        fetchData();
      } else {
        setMessage({ type: "error", text: data.error || "Không thể lưu gói học viên." });
      }
    } catch (err) {
      setMessage({ type: "error", text: "Lỗi kết nối máy chủ." });
    } finally {
      setSaving(false);
    }
  };

  const toggleFeature = (featKey: FeatureKey) => {
    const current = editingPkg.allowedFeatures || [];
    if (current.includes(featKey)) {
      setEditingPkg({
        ...editingPkg,
        allowedFeatures: current.filter(f => f !== featKey)
      });
    } else {
      setEditingPkg({
        ...editingPkg,
        allowedFeatures: [...current, featKey]
      });
    }
  };

  const toggleCourse = (courseId: string) => {
    let current = [...(editingPkg.allowedCourseIds || [])];
    if (courseId === "*") {
      setEditingPkg({
        ...editingPkg,
        allowedCourseIds: current.includes("*") ? [] : ["*"]
      });
      return;
    }

    current = current.filter(c => c !== "*");
    if (current.includes(courseId)) {
      current = current.filter(c => c !== courseId);
    } else {
      current.push(courseId);
    }
    setEditingPkg({
      ...editingPkg,
      allowedCourseIds: current
    });
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-6 rounded-3xl bg-zen-paper border border-zen-border">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <Package className="w-5 h-5 text-amber-800" />
            <h1 className="font-serif text-xl font-bold text-zen-ink">
              {t("Cấu Hình Gói Học Viên & Phân Quyền", "Student Package & Entitlement Configuration")}
            </h1>
          </div>
          <p className="text-xs text-zen-muted">
            {t(
              "Thiết lập các cấp độ gói (Học thử, Nền tảng, Luyện thi, Toàn diện), thời hạn mặc định, tính năng được mở và trạng thái đăng ký.",
              "Configure package tiers (Trial, Foundation, Exam Prep, All-in-One), default duration, feature grants, and registration states."
            )}
          </p>
        </div>

        <button
          onClick={handleOpenCreate}
          className="inline-flex items-center gap-2 px-4 py-2.5 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-all shadow-sm"
        >
          <Plus className="w-4 h-4" />
          <span>{t("Tạo Gói Học Mới", "Create Package")}</span>
        </button>
      </div>

      {message && (
        <div
          className={`p-4 rounded-2xl text-xs font-medium border ${
            message.type === "success"
              ? "bg-emerald-50 text-emerald-800 border-emerald-200"
              : "bg-rose-50 text-rose-800 border-rose-200"
          }`}
        >
          {message.text}
        </div>
      )}

      {/* Packages Grid */}
      {loading ? (
        <div className="p-12 text-center text-xs text-zen-muted">
          <div className="w-6 h-6 border-2 border-amber-800/30 border-t-amber-800 rounded-full animate-spin mx-auto mb-2" />
          {t("Đang tải danh sách gói...", "Loading packages...")}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
          {packages.map((pkg) => {
            const isAllCourses = pkg.allowedCourseIds.includes("*");

            return (
              <div
                key={pkg.id}
                className={`relative flex flex-col justify-between p-6 rounded-3xl border transition-all ${
                  pkg.isRegistrationOpen
                    ? "bg-zen-paper border-zen-border shadow-sm hover:border-amber-300"
                    : "bg-zen-surface/50 border-dashed border-zen-border opacity-75"
                }`}
              >
                <div className="space-y-4">
                  {/* Top line */}
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] font-mono text-zen-muted bg-zen-surface px-2 py-0.5 rounded-lg border border-zen-border/60">
                        {pkg.id}
                      </span>
                      {pkg.isDefaultTrial && (
                        <span className="text-[10px] font-semibold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                          {t("Học thử mặc định", "Default Trial")}
                        </span>
                      )}
                      {pkg.badge && (
                        <span className="text-[10px] font-semibold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">
                          {pkg.badge}
                        </span>
                      )}
                    </div>

                    <button
                      onClick={() => handleToggleRegistration(pkg)}
                      title={pkg.isRegistrationOpen ? "Đang mở đăng ký" : "Đã ngừng đăng ký"}
                      className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold transition-colors ${
                        pkg.isRegistrationOpen
                          ? "bg-emerald-50 text-emerald-800 border border-emerald-200"
                          : "bg-stone-100 text-stone-600 border border-stone-200"
                      }`}
                    >
                      {pkg.isRegistrationOpen ? (
                        <>
                          <CheckCircle2 className="w-3 h-3 text-emerald-600" />
                          <span>{t("Mở đăng ký", "Open")}</span>
                        </>
                      ) : (
                        <span>{t("Đã tạm dừng", "Paused")}</span>
                      )}
                    </button>
                  </div>

                  {/* Title & Price */}
                  <div>
                    <div className="flex items-baseline justify-between gap-2">
                      <h3 className="font-serif font-bold text-lg text-zen-ink">
                        {pkg.nameVi}
                      </h3>
                      <span className="font-serif font-bold text-base text-amber-900 shrink-0">
                        {pkg.price === 0
                          ? t("Miễn Phí", "Free")
                          : `${pkg.price.toLocaleString("vi-VN")} đ`}
                      </span>
                    </div>
                    {pkg.nameEn && (
                      <p className="text-xs text-zen-muted mt-0.5">{pkg.nameEn}</p>
                    )}
                  </div>

                  <p className="text-xs text-zen-muted leading-relaxed">
                    {pkg.descriptionVi}
                  </p>

                  {/* Stats Info */}
                  <div className="grid grid-cols-2 gap-2 p-3 rounded-2xl bg-zen-surface text-xs border border-zen-border/50">
                    <div>
                      <span className="text-[10px] text-zen-muted block mb-0.5">
                        {t("Thời hạn mặc định:", "Duration:")}
                      </span>
                      <span className="font-semibold text-zen-ink flex items-center gap-1">
                        <Clock className="w-3 h-3 text-amber-700" />
                        {pkg.durationDays === 0
                          ? t("Vĩnh viễn", "Unlimited")
                          : `${pkg.durationDays} ${t("ngày", "days")}`}
                      </span>
                    </div>

                    <div>
                      <span className="text-[10px] text-zen-muted block mb-0.5">
                        {t("Phạm vi khóa học:", "Courses:")}
                      </span>
                      <span className="font-semibold text-zen-ink truncate block">
                        {isAllCourses
                          ? t("Tất cả khóa (*)", "All courses (*)")
                          : `${pkg.allowedCourseIds.length} khóa`}
                      </span>
                    </div>
                  </div>

                  {/* Features List */}
                  <div className="space-y-1.5 pt-1">
                    <span className="text-[11px] font-semibold text-zen-muted block">
                      {t("Tính năng & Quyền hạn được mở:", "Unlocked Features:")}
                    </span>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5">
                      {AVAILABLE_FEATURES.map((feat) => {
                        const hasFeat = pkg.allowedFeatures.includes(feat.key);
                        return (
                          <div
                            key={feat.key}
                            className={`flex items-center gap-1.5 text-[11px] px-2 py-1 rounded-lg border ${
                              hasFeat
                                ? "bg-emerald-50/70 border-emerald-200 text-emerald-900 font-medium"
                                : "bg-stone-50 border-stone-200/60 text-stone-400 line-through"
                            }`}
                          >
                            {hasFeat ? (
                              <Check className="w-3 h-3 text-emerald-600 shrink-0" />
                            ) : (
                              <X className="w-3 h-3 text-stone-300 shrink-0" />
                            )}
                            <span className="truncate">{feat.labelVi}</span>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                </div>

                {/* Footer buttons */}
                <div className="pt-4 mt-5 border-t border-zen-border flex items-center justify-end gap-2">
                  <button
                    onClick={() => handleOpenEdit(pkg)}
                    className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl border border-zen-border bg-white hover:bg-zen-surface text-xs font-medium text-zen-ink transition-colors shadow-2xs"
                  >
                    <Edit2 className="w-3 h-3 text-amber-700" />
                    <span>{t("Chỉnh sửa gói", "Edit Package")}</span>
                  </button>
                  <button
                    onClick={() => handleDelete(pkg.id, pkg.nameVi)}
                    className="p-1.5 rounded-xl border border-rose-200 bg-white hover:bg-rose-50 text-rose-700 transition-colors"
                    title={t("Xóa gói", "Delete package")}
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Package Edit/Create Modal */}
      {isEditing && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4 overflow-y-auto">
          <div className="bg-zen-paper border border-zen-border rounded-3xl max-w-2xl w-full p-6 my-8 shadow-xl space-y-5 animate-in fade-in duration-200">
            <div className="flex items-center justify-between pb-3 border-b border-zen-border">
              <div className="flex items-center gap-2">
                <Package className="w-5 h-5 text-amber-800" />
                <h2 className="font-serif text-lg font-bold text-zen-ink">
                  {editingPkg.id && packages.some(p => p.id === editingPkg.id)
                    ? t("Chỉnh Sửa Gói Học Viên", "Edit Student Package")
                    : t("Tạo Gói Học Viên Mới", "Create Student Package")}
                </h2>
              </div>
              <button
                onClick={() => setIsEditing(false)}
                className="p-1.5 rounded-full hover:bg-zen-surface text-zen-muted"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <form onSubmit={handleSave} className="space-y-4 text-xs">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block font-semibold text-zen-ink mb-1">
                    {t("Mã Gói (Package ID)", "Package ID")} *
                  </label>
                  <input
                    type="text"
                    required
                    value={editingPkg.id || ""}
                    onChange={(e) => setEditingPkg({ ...editingPkg, id: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface font-mono text-xs focus:outline-hidden focus:border-amber-700"
                    placeholder="pkg-foundation / pkg-exam-prep"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-zen-ink mb-1">
                    {t("Huy Hiệu (Badge)", "Badge")}
                  </label>
                  <input
                    type="text"
                    value={editingPkg.badge || ""}
                    onChange={(e) => setEditingPkg({ ...editingPkg, badge: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                    placeholder="Phổ biến nhất / Tiết kiệm 40% / VIP"
                  />
                </div>
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Tên Gói (Tiếng Việt)", "Package Name (Vietnamese)")} *
                </label>
                <input
                  type="text"
                  required
                  value={editingPkg.nameVi || ""}
                  onChange={(e) => setEditingPkg({ ...editingPkg, nameVi: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  placeholder="Ví dụ: Gói Luyện Thi ICF Credentialing"
                />
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Tên Gói (Tiếng Anh)", "Package Name (English)")}
                </label>
                <input
                  type="text"
                  value={editingPkg.nameEn || ""}
                  onChange={(e) => setEditingPkg({ ...editingPkg, nameEn: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  placeholder="e.g. ICF Credentialing Exam Preparation Package"
                />
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Mô Tả Gói Học", "Description")}
                </label>
                <textarea
                  rows={2}
                  value={editingPkg.descriptionVi || ""}
                  onChange={(e) => setEditingPkg({ ...editingPkg, descriptionVi: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  placeholder="Mô tả quyền lợi và đối tượng học viên của gói..."
                />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block font-semibold text-zen-ink mb-1">
                    {t("Giá Gói (VNĐ)", "Price (VND)")} (0 = {t("Miễn phí", "Free")})
                  </label>
                  <input
                    type="number"
                    min={0}
                    step={1000}
                    value={editingPkg.price ?? 0}
                    onChange={(e) =>
                      setEditingPkg({ ...editingPkg, price: parseInt(e.target.value) || 0 })
                    }
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-zen-ink mb-1">
                    {t("Thời Hạn Mặc Định (Ngày)", "Default Duration (Days)")} (0 = {t("Vô thời hạn", "Unlimited")})
                  </label>
                  <input
                    type="number"
                    min={0}
                    value={editingPkg.durationDays ?? 30}
                    onChange={(e) =>
                      setEditingPkg({ ...editingPkg, durationDays: parseInt(e.target.value) || 0 })
                    }
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  />
                </div>
              </div>

              {/* Course Selection */}
              <div>
                <label className="block font-semibold text-zen-ink mb-2">
                  {t("Phạm Vi Khóa Học Được Mở:", "Allowed Courses:")}
                </label>
                <div className="space-y-2 p-3 rounded-2xl bg-zen-surface border border-zen-border">
                  <label className="flex items-center gap-2 cursor-pointer font-semibold text-amber-900 pb-2 border-b border-zen-border/60">
                    <input
                      type="checkbox"
                      checked={(editingPkg.allowedCourseIds || []).includes("*")}
                      onChange={() => toggleCourse("*")}
                      className="rounded text-amber-800 focus:ring-amber-800"
                    />
                    <span>{t("Mở toàn bộ khóa học (*) (Khuyên dùng cho gói VIP)", "Allow all courses (*)")}</span>
                  </label>

                  {courses.map((c) => {
                    const isAll = (editingPkg.allowedCourseIds || []).includes("*");
                    const isChecked = isAll || (editingPkg.allowedCourseIds || []).includes(c.id);
                    return (
                      <label
                        key={c.id}
                        className={`flex items-center justify-between p-1.5 rounded-lg text-[11px] cursor-pointer ${
                          isAll ? "opacity-60 cursor-not-allowed" : "hover:bg-white"
                        }`}
                      >
                        <div className="flex items-center gap-2">
                          <input
                            type="checkbox"
                            disabled={isAll}
                            checked={isChecked}
                            onChange={() => toggleCourse(c.id)}
                            className="rounded text-amber-800 focus:ring-amber-800"
                          />
                          <span>{c.titleVi}</span>
                        </div>
                        <span className="font-mono text-[10px] text-zen-muted">{c.id}</span>
                      </label>
                    );
                  })}
                </div>
              </div>

              {/* Feature checkboxes */}
              <div>
                <label className="block font-semibold text-zen-ink mb-2">
                  {t("Các Tính Năng & Quyền Hạn Được Mở Theo Gói:", "Select Unlocked Features:")}
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 p-3 rounded-2xl bg-zen-surface border border-zen-border">
                  {AVAILABLE_FEATURES.map((feat) => {
                    const isChecked = (editingPkg.allowedFeatures || []).includes(feat.key);
                    return (
                      <label
                        key={feat.key}
                        className={`flex items-start gap-2 p-2 rounded-xl border cursor-pointer transition-colors ${
                          isChecked
                            ? "bg-amber-50/80 border-amber-300 text-amber-900"
                            : "bg-white border-zen-border/70 text-zen-ink hover:bg-zen-surface"
                        }`}
                      >
                        <input
                          type="checkbox"
                          checked={isChecked}
                          onChange={() => toggleFeature(feat.key)}
                          className="mt-0.5 rounded text-amber-800 focus:ring-amber-800"
                        />
                        <div className="text-[11px] leading-tight">
                          <span className="font-semibold block">{feat.labelVi}</span>
                          <span className="text-zen-muted text-[10px] leading-snug block mt-0.5">
                            {feat.descVi}
                          </span>
                        </div>
                      </label>
                    );
                  })}
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-6 pt-2">
                <label className="flex items-center gap-2 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={editingPkg.isRegistrationOpen ?? true}
                    onChange={(e) =>
                      setEditingPkg({ ...editingPkg, isRegistrationOpen: e.target.checked })
                    }
                    className="rounded text-amber-800 focus:ring-amber-800"
                  />
                  <span className="font-semibold text-zen-ink text-xs">
                    {t("Mở nhận đăng ký học viên", "Open for Registration")}
                  </span>
                </label>

                <label className="flex items-center gap-2 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={editingPkg.isDefaultTrial ?? false}
                    onChange={(e) =>
                      setEditingPkg({ ...editingPkg, isDefaultTrial: e.target.checked })
                    }
                    className="rounded text-emerald-700 focus:ring-emerald-700"
                  />
                  <span className="font-semibold text-zen-ink text-xs">
                    {t("Gán làm gói học thử mặc định cho tài khoản mới", "Default Trial Package for New Accounts")}
                  </span>
                </label>
              </div>

              {/* Modal Buttons */}
              <div className="pt-4 border-t border-zen-border flex items-center justify-end gap-3">
                <button
                  type="button"
                  onClick={() => setIsEditing(false)}
                  className="px-4 py-2 rounded-xl border border-zen-border bg-white text-zen-muted hover:bg-zen-surface font-medium transition-colors"
                >
                  {t("Hủy bỏ", "Cancel")}
                </button>
                <button
                  type="submit"
                  disabled={saving}
                  className="inline-flex items-center gap-1.5 px-5 py-2 rounded-xl bg-amber-900 text-white font-semibold hover:bg-amber-950 transition-colors shadow-sm disabled:opacity-50"
                >
                  <Save className="w-3.5 h-3.5" />
                  <span>{saving ? t("Đang lưu...", "Saving...") : t("Lưu Cấu Hình Gói", "Save Package")}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
