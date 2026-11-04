"use client";

import React, { useState, useEffect } from "react";
import { useLanguage } from "@/context/LanguageContext";
import { useSound } from "@/context/SoundContext";
import {
  getSections,
  saveSections,
  getTheoryBySectionId,
  saveTheory,
  getKeywordsBySectionId,
  getFlashcardsBySectionId,
  getCaseStudiesBySectionId,
  getQuizzesBySectionId,
  addAuditLog
} from "@/lib/db";
import { useAuth } from "@/context/AuthContext";
import { Section, Theory, Keyword, Flashcard, CaseStudy, QuizQuestion, NatureIcon as NatureIconType } from "@/types";
import NatureIcon from "@/components/NatureIcon";
import {
  Plus,
  Trash2,
  Edit2,
  Save,
  Check,
  Download,
  Upload,
  ArrowUp,
  ArrowDown,
  Layers,
  Sparkles,
  BookOpen,
  KeyRound,
  FileQuestion,
  HelpCircle
} from "lucide-react";

export default function AdminSectionsPage() {
  const { t } = useLanguage();
  const { ringBell } = useSound();
  const { user } = useAuth();

  const [sections, setSections] = useState<Section[]>([]);
  const [selectedSectionId, setSelectedSectionId] = useState<string | null>(null);
  const [isEditingSection, setIsEditingSection] = useState(false);

  // Edit Section Form State
  const [secForm, setSecForm] = useState<Partial<Section>>({});

  // Active Tab for editing 6 tabs content
  const [editTab, setEditTab] = useState<"info" | "theory" | "keyword" | "flashcard" | "case_study" | "quiz">("info");

  // Theory Form
  const [theoryContentVi, setTheoryContentVi] = useState("");
  const [theoryContentEn, setTheoryContentEn] = useState("");
  const [saveSuccessMsg, setSaveSuccessMsg] = useState("");

  useEffect(() => {
    const list = getSections();
    setSections(list);
    if (list.length > 0 && !selectedSectionId) {
      setSelectedSectionId(list[0].id);
      loadSectionData(list[0]);
    }
  }, []);

  const loadSectionData = (sec: Section) => {
    setSecForm(sec);
    const th = getTheoryBySectionId(sec.id);
    if (th) {
      setTheoryContentVi(th.contentVi);
      setTheoryContentEn(th.contentEn);
    } else {
      setTheoryContentVi("");
      setTheoryContentEn("");
    }
  };

  const handleSelectSection = (sec: Section) => {
    setSelectedSectionId(sec.id);
    loadSectionData(sec);
  };

  const handleSaveSectionInfo = () => {
    if (!selectedSectionId) return;
    const updated = sections.map((s) => (s.id === selectedSectionId ? ({ ...s, ...secForm } as Section) : s));
    saveSections(updated);
    setSections(updated);
    addAuditLog(user.id, user.fullName, "Cập nhật mục nội dung", `Sửa thông tin mục ${secForm.code}`);
    ringBell();
    showSuccess(t("Đã lưu thông tin mục thành công!", "Section saved!"));
  };

  const handleSaveTheory = () => {
    if (!selectedSectionId) return;
    const existing = getTheoryBySectionId(selectedSectionId);
    const updatedTh: Theory = {
      id: existing ? existing.id : `th-${selectedSectionId}`,
      sectionId: selectedSectionId,
      titleVi: existing?.titleVi || secForm.titleVi || "Lý thuyết bài giảng",
      titleEn: existing?.titleEn || secForm.titleEn || "Lecture Theory",
      contentVi: theoryContentVi,
      contentEn: theoryContentEn,
      isFree: secForm.isFree || false
    };
    saveTheory(updatedTh);
    addAuditLog(user.id, user.fullName, "Cập nhật bài giảng lý thuyết", `Cập nhật lý thuyết ${selectedSectionId}`);
    ringBell();
    showSuccess(t("Đã lưu bài giảng lý thuyết thành công!", "Theory saved!"));
  };

  const handleAddNewSection = () => {
    const newId = `sec-custom-${Date.now()}`;
    const newSec: Section = {
      id: newId,
      parentId: selectedSectionId,
      code: "NEW.1",
      titleVi: "Chủ Đề Mới (Tiếng Việt)",
      titleEn: "New Topic (English)",
      descriptionVi: "Mô tả ngắn gọn về chủ đề này",
      descriptionEn: "Brief description of this topic",
      natureIcon: "seed",
      orderIndex: sections.length + 1,
      isFree: false,
      isPublished: true
    };
    const updated = [...sections, newSec];
    saveSections(updated);
    setSections(updated);
    setSelectedSectionId(newId);
    loadSectionData(newSec);
    addAuditLog(user.id, user.fullName, "Thêm mục nội dung mới", `Tạo mục ${newId}`);
    ringBell();
  };

  const handleDeleteSection = (id: string) => {
    if (!confirm(t("Bạn có chắc chắn muốn xóa mục này và các bài học con?", "Delete this section and its sub-topics?"))) {
      return;
    }
    const updated = sections.filter((s) => s.id !== id && s.parentId !== id);
    saveSections(updated);
    setSections(updated);
    if (selectedSectionId === id && updated.length > 0) {
      setSelectedSectionId(updated[0].id);
      loadSectionData(updated[0]);
    }
    addAuditLog(user.id, user.fullName, "Xóa mục nội dung", `Xóa mục ${id}`);
    ringBell();
  };

  const handleMoveOrder = (id: string, direction: "up" | "down") => {
    const idx = sections.findIndex((s) => s.id === id);
    if (idx < 0) return;
    const targetIdx = direction === "up" ? idx - 1 : idx + 1;
    if (targetIdx < 0 || targetIdx >= sections.length) return;

    const copy = [...sections];
    const temp = copy[idx];
    copy[idx] = copy[targetIdx];
    copy[targetIdx] = temp;

    // re-assign orderIndex
    copy.forEach((s, i) => (s.orderIndex = i + 1));
    saveSections(copy);
    setSections(copy);
    ringBell();
  };

  const showSuccess = (msg: string) => {
    setSaveSuccessMsg(msg);
    setTimeout(() => setSaveSuccessMsg(""), 3000);
  };

  // Export to JSON/CSV format
  const handleExportJson = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(sections, null, 2));
    const downloadAnchor = document.createElement("a");
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `icf_pcc_sections_${Date.now()}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
    ringBell();
  };

  return (
    <div className="space-y-6">
      {/* Top Banner */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="font-serif text-2xl font-bold text-zen-ink">
            {t("Quản Lý Cây Nội Dung Động & Soạn Thảo 6 Tab", "Curriculum Tree & 6 Tabs Editor")}
          </h1>
          <p className="text-xs text-zen-muted mt-1">
            {t(
              "Thêm, sửa, sắp xếp thứ tự các phần/mục và chỉnh sửa chi tiết nội dung song ngữ của cả 6 tab.",
              "Manage section tree hierarchy, reorder, and edit bilingual content across all 6 tabs."
            )}
          </p>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={handleExportJson}
            className="flex items-center gap-1.5 px-3.5 py-2 rounded-2xl border border-zen-border bg-white text-xs font-semibold text-zen-ink hover:bg-zen-surface transition-colors shadow-zen-subtle"
          >
            <Download className="w-3.5 h-3.5 text-zen-moss-dark" />
            <span>{t("Xuất Dữ Liệu (JSON)", "Export Data")}</span>
          </button>
          <button
            onClick={handleAddNewSection}
            className="flex items-center gap-1.5 px-4 py-2 rounded-2xl bg-zen-moss-dark text-white text-xs font-semibold hover:bg-zen-moss-deep transition-colors shadow-zen-subtle"
          >
            <Plus className="w-4 h-4" />
            <span>{t("Thêm Mục Mới", "Add Section")}</span>
          </button>
        </div>
      </div>

      {saveSuccessMsg && (
        <div className="p-3 rounded-2xl bg-emerald-50 border border-emerald-300 text-xs font-semibold text-emerald-800 flex items-center gap-2 animate-in fade-in duration-200">
          <Check className="w-4 h-4 text-emerald-600" />
          <span>{saveSuccessMsg}</span>
        </div>
      )}

      {/* Main 2-Column Split */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left: Section Tree List (1 Col) */}
        <div className="rounded-3xl border border-zen-border bg-zen-paper p-4 sm:p-5 shadow-zen-card space-y-2 max-h-[750px] overflow-y-auto">
          <div className="flex items-center justify-between pb-2 border-b border-zen-border/50 text-xs font-bold uppercase tracking-wider text-zen-muted">
            <span>{t("Cây Mục Lục", "Curriculum Tree")}</span>
            <span>{sections.length} mục</span>
          </div>

          <div className="space-y-1.5 pt-1">
            {sections.map((sec) => {
              const isSelected = sec.id === selectedSectionId;
              const isRoot = !sec.parentId;

              return (
                <div
                  key={sec.id}
                  onClick={() => handleSelectSection(sec)}
                  className={`flex items-center justify-between p-2.5 rounded-2xl border text-xs cursor-pointer transition-all ${
                    isSelected
                      ? "border-zen-moss-dark bg-zen-moss/15 shadow-sm font-semibold text-zen-moss-dark"
                      : "border-zen-border/60 bg-white hover:bg-zen-surface text-zen-ink"
                  } ${!isRoot ? "ml-4" : ""}`}
                >
                  <div className="flex items-center gap-2 truncate">
                    <NatureIcon icon={sec.natureIcon} size={14} className="shrink-0 text-zen-moss-dark" />
                    <span className="font-mono font-bold text-[11px] shrink-0">{sec.code}</span>
                    <span className="truncate">{sec.titleVi}</span>
                  </div>

                  <div className="flex items-center gap-1 shrink-0 ml-2">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleMoveOrder(sec.id, "up");
                      }}
                      className="p-1 text-zen-muted hover:text-zen-ink"
                      title="Move Up"
                    >
                      <ArrowUp className="w-3 h-3" />
                    </button>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleMoveOrder(sec.id, "down");
                      }}
                      className="p-1 text-zen-muted hover:text-zen-ink"
                      title="Move Down"
                    >
                      <ArrowDown className="w-3 h-3" />
                    </button>
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        handleDeleteSection(sec.id);
                      }}
                      className="p-1 text-rose-500 hover:text-rose-700"
                      title="Delete"
                    >
                      <Trash2 className="w-3 h-3" />
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Right: Section Editor Tabs (2 Cols) */}
        <div className="lg:col-span-2 space-y-4">
          {/* Subtabs for current section */}
          <div className="flex items-center gap-2 overflow-x-auto pb-1 text-xs">
            <button
              onClick={() => setEditTab("info")}
              className={`px-3.5 py-2 rounded-2xl font-bold transition-all ${
                editTab === "info"
                  ? "bg-amber-900 text-white shadow-sm"
                  : "bg-zen-paper text-zen-ink border border-zen-border"
              }`}
            >
              ⚙️ {t("Thông Tin Mục", "Section Info")}
            </button>
            <button
              onClick={() => setEditTab("theory")}
              className={`px-3.5 py-2 rounded-2xl font-bold transition-all ${
                editTab === "theory"
                  ? "bg-amber-900 text-white shadow-sm"
                  : "bg-zen-paper text-zen-ink border border-zen-border"
              }`}
            >
              📖 {t("Soạn Lý Thuyết", "Theory Content")}
            </button>
          </div>

          {/* Form: Section Info */}
          {editTab === "info" && (
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
              <h3 className="font-serif text-lg font-bold text-zen-ink">
                {t("Chỉnh sửa thông tin mục:", "Edit Section Metadata:")} {secForm.code}
              </h3>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                <div>
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Mã định danh (Code)", "Code")}</label>
                  <input
                    type="text"
                    value={secForm.code || ""}
                    onChange={(e) => setSecForm({ ...secForm, code: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs text-zen-ink"
                  />
                </div>

                <div>
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Biểu tượng thiên nhiên", "Nature Icon")}</label>
                  <select
                    value={secForm.natureIcon || "seed"}
                    onChange={(e) => setSecForm({ ...secForm, natureIcon: e.target.value as NatureIconType })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs text-zen-ink"
                  >
                    <option value="seed">Hạt giống (Seed - Nền tảng)</option>
                    <option value="sprout">Chồi non (Sprout - Mối quan hệ)</option>
                    <option value="bamboo">Lá tre (Bamboo - Giao tiếp)</option>
                    <option value="lotus">Hoa sen (Lotus - Phát triển)</option>
                    <option value="mountain">Ngọn núi (Mountain - Thi thử)</option>
                  </select>
                </div>

                <div>
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Tiêu đề tiếng Việt", "Title (VI)")}</label>
                  <input
                    type="text"
                    value={secForm.titleVi || ""}
                    onChange={(e) => setSecForm({ ...secForm, titleVi: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs text-zen-ink"
                  />
                </div>

                <div>
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Tiêu đề tiếng Anh", "Title (EN)")}</label>
                  <input
                    type="text"
                    value={secForm.titleEn || ""}
                    onChange={(e) => setSecForm({ ...secForm, titleEn: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs text-zen-ink"
                  />
                </div>

                <div className="sm:col-span-2">
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Mô tả tóm tắt (Tiếng Việt)", "Description (VI)")}</label>
                  <textarea
                    rows={2}
                    value={secForm.descriptionVi || ""}
                    onChange={(e) => setSecForm({ ...secForm, descriptionVi: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs text-zen-ink"
                  />
                </div>

                <div className="sm:col-span-2">
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Mô tả tóm tắt (Tiếng Anh)", "Description (EN)")}</label>
                  <textarea
                    rows={2}
                    value={secForm.descriptionEn || ""}
                    onChange={(e) => setSecForm({ ...secForm, descriptionEn: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-zen-border bg-white text-xs text-zen-ink"
                  />
                </div>

                {/* Flags */}
                <div className="sm:col-span-2 flex items-center gap-6 pt-2">
                  <label className="flex items-center gap-2 cursor-pointer font-medium text-zen-ink">
                    <input
                      type="checkbox"
                      checked={!!secForm.isFree}
                      onChange={(e) => setSecForm({ ...secForm, isFree: e.target.checked })}
                      className="rounded text-zen-moss-dark"
                    />
                    <span>{t("Cho phép học thử Miễn Phí (Free)", "Allow Free Access")}</span>
                  </label>

                  <label className="flex items-center gap-2 cursor-pointer font-medium text-zen-ink">
                    <input
                      type="checkbox"
                      checked={secForm.isPublished !== false}
                      onChange={(e) => setSecForm({ ...secForm, isPublished: e.target.checked })}
                      className="rounded text-zen-moss-dark"
                    />
                    <span>{t("Xuất bản ngay (Published)", "Published")}</span>
                  </label>
                </div>
              </div>

              <div className="pt-4 border-t border-zen-border/50 flex justify-end">
                <button
                  onClick={handleSaveSectionInfo}
                  className="flex items-center gap-2 px-6 py-2.5 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-colors shadow-zen-subtle"
                >
                  <Save className="w-4 h-4" />
                  <span>{t("Lưu Thay Đổi", "Save Changes")}</span>
                </button>
              </div>
            </div>
          )}

          {/* Form: Theory Content */}
          {editTab === "theory" && (
            <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 shadow-zen-card space-y-4">
              <h3 className="font-serif text-lg font-bold text-zen-ink">
                {t("Soạn thảo bài giảng Lý thuyết:", "Edit Theory Lecture:")} {secForm.code}
              </h3>

              <div className="space-y-4 text-xs">
                <div>
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Nội dung bài học (Tiếng Việt)", "Content (VI)")}</label>
                  <textarea
                    rows={8}
                    value={theoryContentVi}
                    onChange={(e) => setTheoryContentVi(e.target.value)}
                    className="w-full p-3.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink font-mono leading-relaxed"
                  />
                </div>

                <div>
                  <label className="block font-semibold mb-1 text-zen-ink">{t("Nội dung bài học (Tiếng Anh)", "Content (EN)")}</label>
                  <textarea
                    rows={8}
                    value={theoryContentEn}
                    onChange={(e) => setTheoryContentEn(e.target.value)}
                    className="w-full p-3.5 rounded-2xl border border-zen-border bg-white text-xs text-zen-ink font-mono leading-relaxed"
                  />
                </div>
              </div>

              <div className="pt-4 border-t border-zen-border/50 flex justify-end">
                <button
                  onClick={handleSaveTheory}
                  className="flex items-center gap-2 px-6 py-2.5 rounded-2xl bg-amber-900 text-white text-xs font-semibold hover:bg-amber-950 transition-colors shadow-zen-subtle"
                >
                  <Save className="w-4 h-4" />
                  <span>{t("Lưu Bài Giảng", "Save Lecture")}</span>
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
