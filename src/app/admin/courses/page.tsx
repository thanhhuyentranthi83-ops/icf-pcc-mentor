"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { CourseRecord } from "@/types";
import { ICF_7_MODULES } from "@/lib/curriculumData";
import {
  BookOpen,
  Plus,
  Edit2,
  Trash2,
  Eye,
  EyeOff,
  CheckCircle2,
  Layers,
  Sparkles,
  ExternalLink,
  Save,
  X
} from "lucide-react";

export default function AdminCoursesPage() {
  const { t } = useLanguage();
  const [courses, setCourses] = useState<CourseRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  const [editingCourse, setEditingCourse] = useState<Partial<CourseRecord>>({
    id: "",
    titleVi: "",
    titleEn: "",
    descriptionVi: "",
    descriptionEn: "",
    moduleIds: ["mod-1", "mod-2"],
    previewLessonIds: ["mod1-les1"],
    isPublished: true,
    badge: "Phổ biến",
    orderIndex: 1
  });
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);

  const fetchCourses = async () => {
    try {
      setLoading(true);
      const res = await fetch("/api/courses?all=true");
      const data = await res.json();
      if (data.success && data.courses) {
        setCourses(data.courses);
      }
    } catch (err) {
      console.error("Error fetching courses:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  const handleOpenCreate = () => {
    setEditingCourse({
      id: `crs-${Date.now().toString(36)}`,
      titleVi: "",
      titleEn: "",
      descriptionVi: "",
      descriptionEn: "",
      moduleIds: ["mod-1", "mod-2"],
      previewLessonIds: ["mod1-les1"],
      isPublished: true,
      badge: "Mới",
      orderIndex: courses.length + 1
    });
    setIsEditing(true);
    setMessage(null);
  };

  const handleOpenEdit = (course: CourseRecord) => {
    setEditingCourse({ ...course });
    setIsEditing(true);
    setMessage(null);
  };

  const handleTogglePublish = async (course: CourseRecord) => {
    try {
      const updated = { ...course, isPublished: !course.isPublished };
      const res = await fetch("/api/courses", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updated)
      });
      const data = await res.json();
      if (data.success) {
        setCourses(courses.map(c => (c.id === course.id ? updated : c)));
      }
    } catch (err) {
      console.error("Toggle publish error:", err);
    }
  };

  const handleDelete = async (id: string, name: string) => {
    if (!window.confirm(`Bạn có chắc chắn muốn xóa khóa học "${name}"?`)) return;
    try {
      const res = await fetch(`/api/courses?id=${encodeURIComponent(id)}`, {
        method: "DELETE"
      });
      const data = await res.json();
      if (data.success) {
        setCourses(courses.filter(c => c.id !== id));
        setMessage({ type: "success", text: `Đã xóa khóa học "${name}".` });
      } else {
        setMessage({ type: "error", text: data.error || "Không thể xóa khóa học." });
      }
    } catch (err) {
      setMessage({ type: "error", text: "Lỗi kết nối máy chủ." });
    }
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingCourse.titleVi || !editingCourse.moduleIds || editingCourse.moduleIds.length === 0) {
      setMessage({ type: "error", text: "Vui lòng nhập tên khóa học và chọn ít nhất 1 học phần." });
      return;
    }

    try {
      setSaving(true);
      setMessage(null);
      const res = await fetch("/api/courses", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(editingCourse)
      });
      const data = await res.json();
      if (data.success) {
        setIsEditing(false);
        setMessage({ type: "success", text: "Đã lưu thông tin khóa học thành công!" });
        fetchCourses();
      } else {
        setMessage({ type: "error", text: data.error || "Không thể lưu khóa học." });
      }
    } catch (err) {
      setMessage({ type: "error", text: "Lỗi kết nối máy chủ." });
    } finally {
      setSaving(false);
    }
  };

  const toggleModuleSelection = (modId: string) => {
    const current = editingCourse.moduleIds || [];
    if (current.includes(modId)) {
      setEditingCourse({
        ...editingCourse,
        moduleIds: current.filter(id => id !== modId)
      });
    } else {
      setEditingCourse({
        ...editingCourse,
        moduleIds: [...current, modId]
      });
    }
  };

  const togglePreviewLesson = (lesId: string) => {
    const current = editingCourse.previewLessonIds || [];
    if (current.includes(lesId)) {
      setEditingCourse({
        ...editingCourse,
        previewLessonIds: current.filter(id => id !== lesId)
      });
    } else {
      setEditingCourse({
        ...editingCourse,
        previewLessonIds: [...current, lesId]
      });
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-6 rounded-3xl bg-zen-paper border border-zen-border">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <BookOpen className="w-5 h-5 text-amber-800" />
            <h1 className="font-serif text-xl font-bold text-zen-ink">
              {t("Quản Lý Khóa Học & Học Phần", "Course & Module Management")}
            </h1>
          </div>
          <p className="text-xs text-zen-muted">
            {t(
              "Tạo, chỉnh sửa khóa học, phân bổ 7 học phần ICF chuẩn 2025, chọn bài học thử miễn phí và quản lý hiển thị trong danh mục.",
              "Create, edit courses, assign 7 ICF modules, configure preview lessons, and control catalog visibility."
            )}
          </p>
        </div>

        <button
          onClick={handleOpenCreate}
          className="inline-flex items-center gap-2 px-4 py-2.5 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-all shadow-sm"
        >
          <Plus className="w-4 h-4" />
          <span>{t("Tạo Khóa Học Mới", "Create Course")}</span>
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

      {/* Courses List */}
      {loading ? (
        <div className="p-12 text-center text-xs text-zen-muted">
          <div className="w-6 h-6 border-2 border-amber-800/30 border-t-amber-800 rounded-full animate-spin mx-auto mb-2" />
          {t("Đang tải danh sách khóa học...", "Loading courses...")}
        </div>
      ) : courses.length === 0 ? (
        <div className="p-12 rounded-3xl bg-zen-paper border border-zen-border text-center text-xs text-zen-muted space-y-3">
          <BookOpen className="w-8 h-8 text-zen-muted mx-auto" />
          <p>{t("Chưa có khóa học nào. Hãy tạo khóa học đầu tiên!", "No courses found. Create your first course!")}</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {courses.map((course) => {
            const moduleCount = course.moduleIds.length;
            const previewCount = course.previewLessonIds?.length || 0;

            return (
              <div
                key={course.id}
                className={`relative flex flex-col justify-between p-5 rounded-3xl border transition-all ${
                  course.isPublished
                    ? "bg-zen-paper border-zen-border shadow-sm hover:border-amber-300"
                    : "bg-zen-surface/40 border-dashed border-zen-border opacity-80"
                }`}
              >
                {/* Header */}
                <div className="space-y-3">
                  <div className="flex items-start justify-between gap-2">
                    <span className="text-[10px] font-mono uppercase tracking-wider text-zen-muted bg-zen-surface px-2 py-0.5 rounded-lg border border-zen-border/60">
                      ID: {course.id}
                    </span>
                    <div className="flex items-center gap-1.5">
                      {course.badge && (
                        <span className="text-[10px] font-semibold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">
                          {course.badge}
                        </span>
                      )}
                      <button
                        onClick={() => handleTogglePublish(course)}
                        title={course.isPublished ? "Đang hiển thị (bấm để ẩn)" : "Đang ẩn (bấm để hiển thị)"}
                        className={`p-1 rounded-lg text-xs font-medium transition-colors ${
                          course.isPublished
                            ? "text-emerald-700 bg-emerald-50 hover:bg-emerald-100"
                            : "text-stone-500 bg-stone-100 hover:bg-stone-200"
                        }`}
                      >
                        {course.isPublished ? <Eye className="w-3.5 h-3.5" /> : <EyeOff className="w-3.5 h-3.5" />}
                      </button>
                    </div>
                  </div>

                  <div>
                    <h3 className="font-serif font-bold text-base text-zen-ink leading-snug">
                      {course.titleVi}
                    </h3>
                    {course.titleEn && (
                      <p className="text-xs text-zen-muted font-sans mt-0.5">{course.titleEn}</p>
                    )}
                  </div>

                  <p className="text-xs text-zen-muted leading-relaxed line-clamp-3">
                    {course.descriptionVi}
                  </p>

                  {/* Modules & Previews */}
                  <div className="pt-2 border-t border-zen-border/50 space-y-1.5 text-xs text-zen-ink">
                    <div className="flex items-center justify-between">
                      <span className="text-zen-muted flex items-center gap-1.5">
                        <Layers className="w-3.5 h-3.5 text-amber-700" />
                        {t("Học phần:", "Modules:")}
                      </span>
                      <span className="font-semibold text-zen-ink">
                        {moduleCount} / 7 học phần
                      </span>
                    </div>

                    <div className="flex flex-wrap gap-1 pt-1">
                      {course.moduleIds.map((mId) => {
                        const m = ICF_7_MODULES.find((mod) => mod.id === mId);
                        return (
                          <span
                            key={mId}
                            className="text-[10px] px-2 py-0.5 rounded-md bg-zen-surface text-zen-ink border border-zen-border/60"
                          >
                            HP {m?.number || mId.replace("mod-", "")}
                          </span>
                        );
                      })}
                    </div>

                    <div className="flex items-center justify-between pt-1">
                      <span className="text-zen-muted flex items-center gap-1.5">
                        <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
                        {t("Bài học thử:", "Preview:")}
                      </span>
                      <span className="font-semibold text-emerald-800 text-[11px]">
                        {previewCount > 0 ? `${previewCount} bài miễn phí` : "Không có"}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Actions Footer */}
                <div className="pt-4 mt-4 border-t border-zen-border flex items-center justify-between">
                  <span className="text-[11px] text-zen-muted">
                    {t("Thứ tự:", "Order:")} #{course.orderIndex}
                  </span>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => handleOpenEdit(course)}
                      className="inline-flex items-center gap-1 px-3 py-1.5 rounded-xl border border-zen-border bg-white hover:bg-zen-surface text-xs font-medium text-zen-ink transition-colors shadow-2xs"
                    >
                      <Edit2 className="w-3 h-3 text-amber-700" />
                      <span>{t("Sửa", "Edit")}</span>
                    </button>
                    <button
                      onClick={() => handleDelete(course.id, course.titleVi)}
                      className="p-1.5 rounded-xl border border-rose-200 bg-white hover:bg-rose-50 text-rose-700 transition-colors"
                      title={t("Xóa khóa học", "Delete course")}
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Course Edit/Create Modal */}
      {isEditing && (
        <div className="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs flex items-center justify-center p-4 overflow-y-auto">
          <div className="bg-zen-paper border border-zen-border rounded-3xl max-w-2xl w-full p-6 my-8 shadow-xl space-y-5 animate-in fade-in duration-200">
            <div className="flex items-center justify-between pb-3 border-b border-zen-border">
              <div className="flex items-center gap-2">
                <BookOpen className="w-5 h-5 text-amber-800" />
                <h2 className="font-serif text-lg font-bold text-zen-ink">
                  {editingCourse.id && courses.some(c => c.id === editingCourse.id)
                    ? t("Chỉnh Sửa Khóa Học", "Edit Course")
                    : t("Tạo Khóa Học Mới", "Create Course")}
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
                    {t("Mã Khóa Học (Course ID)", "Course ID")} *
                  </label>
                  <input
                    type="text"
                    required
                    value={editingCourse.id || ""}
                    onChange={(e) => setEditingCourse({ ...editingCourse, id: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface font-mono text-xs focus:outline-hidden focus:border-amber-700"
                    placeholder="crs-ten-khoa"
                  />
                </div>

                <div>
                  <label className="block font-semibold text-zen-ink mb-1">
                    {t("Huy Hiệu (Badge)", "Badge")}
                  </label>
                  <input
                    type="text"
                    value={editingCourse.badge || ""}
                    onChange={(e) => setEditingCourse({ ...editingCourse, badge: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                    placeholder="Phổ biến nhất / Toàn diện / Cơ bản"
                  />
                </div>
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Tên Khóa Học (Tiếng Việt)", "Course Title (Vietnamese)")} *
                </label>
                <input
                  type="text"
                  required
                  value={editingCourse.titleVi || ""}
                  onChange={(e) => setEditingCourse({ ...editingCourse, titleVi: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  placeholder="Ví dụ: Lộ Trình Nền Tảng Khai Vấn Chuyên Nghiệp"
                />
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Tên Khóa Học (Tiếng Anh)", "Course Title (English)")}
                </label>
                <input
                  type="text"
                  value={editingCourse.titleEn || ""}
                  onChange={(e) => setEditingCourse({ ...editingCourse, titleEn: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  placeholder="e.g. Professional Coaching Foundation Pathway"
                />
              </div>

              <div>
                <label className="block font-semibold text-zen-ink mb-1">
                  {t("Mô Tả Khóa Học (Tiếng Việt)", "Description (Vietnamese)")}
                </label>
                <textarea
                  rows={2}
                  value={editingCourse.descriptionVi || ""}
                  onChange={(e) => setEditingCourse({ ...editingCourse, descriptionVi: e.target.value })}
                  className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden focus:border-amber-700"
                  placeholder="Mô tả mục tiêu, đối tượng học viên và lợi ích khóa học..."
                />
              </div>

              {/* Module selection */}
              <div>
                <label className="block font-semibold text-zen-ink mb-2">
                  {t("Chọn Các Học Phần ICF Thuộc Khóa Này (7 Học Phần Chuẩn 2025):", "Select ICF Modules for this course:")}
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 max-h-48 overflow-y-auto p-3 rounded-2xl bg-zen-surface border border-zen-border">
                  {ICF_7_MODULES.map((mod) => {
                    const isSelected = (editingCourse.moduleIds || []).includes(mod.id);
                    return (
                      <label
                        key={mod.id}
                        className={`flex items-start gap-2 p-2 rounded-xl border cursor-pointer transition-colors ${
                          isSelected
                            ? "bg-amber-50/80 border-amber-300 text-amber-900"
                            : "bg-white border-zen-border/70 text-zen-ink hover:bg-zen-surface"
                        }`}
                      >
                        <input
                          type="checkbox"
                          checked={isSelected}
                          onChange={() => toggleModuleSelection(mod.id)}
                          className="mt-0.5 rounded text-amber-800 focus:ring-amber-800"
                        />
                        <div className="text-[11px] leading-tight">
                          <span className="font-semibold block">{mod.titleVi}</span>
                          <span className="text-zen-muted text-[10px]">{mod.lessons.length} bài học</span>
                        </div>
                      </label>
                    );
                  })}
                </div>
              </div>

              {/* Preview Lessons selection */}
              <div>
                <label className="block font-semibold text-zen-ink mb-2">
                  {t("Chọn Bài Học Cho Phép Học Thử Miễn Phí (Preview Lessons):", "Select Free Preview Lessons:")}
                </label>
                <div className="max-h-40 overflow-y-auto p-3 rounded-2xl bg-zen-surface border border-zen-border space-y-1">
                  {ICF_7_MODULES.filter((m) => (editingCourse.moduleIds || []).includes(m.id)).flatMap((m) =>
                    m.lessons.map((les) => {
                      const isPreview = (editingCourse.previewLessonIds || []).includes(les.id);
                      return (
                        <label
                          key={les.id}
                          className="flex items-center justify-between p-1.5 rounded-lg hover:bg-white cursor-pointer text-[11px]"
                        >
                          <div className="flex items-center gap-2 truncate pr-2">
                            <input
                              type="checkbox"
                              checked={isPreview}
                              onChange={() => togglePreviewLesson(les.id)}
                              className="rounded text-emerald-700 focus:ring-emerald-700"
                            />
                            <span className="truncate">{les.titleVi}</span>
                          </div>
                          <span className="text-[10px] font-mono text-zen-muted shrink-0">
                            {les.id}
                          </span>
                        </label>
                      );
                    })
                  )}
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center pt-2">
                <div>
                  <label className="block font-semibold text-zen-ink mb-1">
                    {t("Thứ Tự Hiển Thị", "Order Index")}
                  </label>
                  <input
                    type="number"
                    value={editingCourse.orderIndex ?? 1}
                    onChange={(e) =>
                      setEditingCourse({ ...editingCourse, orderIndex: parseInt(e.target.value) || 1 })
                    }
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-zen-surface text-xs focus:outline-hidden"
                  />
                </div>

                <div className="pt-4">
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="checkbox"
                      checked={editingCourse.isPublished ?? true}
                      onChange={(e) =>
                        setEditingCourse({ ...editingCourse, isPublished: e.target.checked })
                      }
                      className="rounded text-amber-800 focus:ring-amber-800"
                    />
                    <span className="font-semibold text-zen-ink text-xs">
                      {t("Hiển thị trong danh mục học viên", "Published in Course Catalog")}
                    </span>
                  </label>
                </div>
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
                  <span>{saving ? t("Đang lưu...", "Saving...") : t("Lưu Khóa Học", "Save Course")}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
