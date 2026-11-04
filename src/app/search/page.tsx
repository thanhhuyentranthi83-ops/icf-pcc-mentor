"use client";

import React, { useState, useEffect, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import { searchAllContent, getSections, SearchResultItem } from "@/lib/db";
import { Section } from "@/types";
import { Search, Filter, Lock, ArrowRight, BookOpen, KeyRound, HelpCircle, Layers } from "lucide-react";

function SearchContent() {
  const searchParams = useSearchParams();
  const initialQuery = searchParams.get("q") || "";

  const { t } = useLanguage();
  const { user } = useAuth();

  const [query, setQuery] = useState(initialQuery);
  const [sections, setSections] = useState<Section[]>([]);
  const [filterSection, setFilterSection] = useState<string>("");
  const [results, setResults] = useState<SearchResultItem[]>([]);
  const [activeTypeTab, setActiveTypeTab] = useState<string>("all");

  useEffect(() => {
    setSections(getSections());
  }, []);

  useEffect(() => {
    if (query.trim()) {
      const res = searchAllContent(query, filterSection || undefined, user.tier);
      setResults(res);
    } else {
      setResults([]);
    }
  }, [query, filterSection, user.tier]);

  const filteredResults =
    activeTypeTab === "all"
      ? results
      : results.filter((r) => r.type === activeTypeTab);

  const getTypeIcon = (type: string) => {
    switch (type) {
      case "theory":
        return <BookOpen className="w-4 h-4 text-zen-moss-dark" />;
      case "keyword":
        return <KeyRound className="w-4 h-4 text-zen-wood" />;
      case "case_study":
        return <HelpCircle className="w-4 h-4 text-zen-ochre-dark" />;
      default:
        return <Layers className="w-4 h-4 text-zen-muted" />;
    }
  };

  const getTypeLabel = (type: string) => {
    switch (type) {
      case "theory":
        return t("Lý thuyết", "Theory");
      case "keyword":
        return t("Từ khóa / Mẹo", "Keyword / Cue");
      case "case_study":
        return t("Case Study", "Case Study");
      default:
        return t("Nội dung", "Content");
    }
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 sm:py-12 space-y-6">
      {/* Title */}
      <div className="text-center max-w-xl mx-auto space-y-2">
        <h1 className="font-serif text-3xl font-bold text-zen-ink">
          {t("Tra Cứu Toàn Cục Chánh Niệm", "Global Coaching Search")}
        </h1>
        <p className="text-xs sm:text-sm text-zen-muted">
          {t(
            "Tìm kiếm trong lý thuyết, từ khóa, mẹo ghi nhớ, case study và câu hỏi. Hỗ trợ gõ tiếng Việt không dấu.",
            "Search across all lectures, mnemonics, case studies and questions. Supports unaccented Vietnamese."
          )}
        </p>
      </div>

      {/* Search Input & Section Filter Bar */}
      <div className="rounded-3xl border border-zen-border bg-zen-paper p-4 sm:p-6 shadow-zen-card space-y-4">
        <div className="flex items-center gap-3 bg-white rounded-2xl border border-zen-border px-4 py-3 shadow-zen-subtle focus-within:border-zen-moss-dark transition-all">
          <Search className="w-5 h-5 text-zen-muted shrink-0" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder={t(
              "Gõ từ khóa cần tìm (VD: bao mat, xung dot, dao duc, lang nghe, pcc marker...)",
              "Type query (e.g. confidentiality, conflict of interest, active listening, presence...)"
            )}
            className="w-full bg-transparent text-sm text-zen-ink placeholder:text-zen-muted/70 focus:outline-none"
            autoFocus
          />
          {query && (
            <button
              onClick={() => setQuery("")}
              className="text-xs text-zen-muted hover:text-zen-ink px-2 py-0.5 rounded-lg hover:bg-zen-surface"
            >
              {t("Xóa", "Clear")}
            </button>
          )}
        </div>

        {/* Filters */}
        <div className="flex flex-wrap items-center justify-between gap-3 text-xs">
          {/* Section Filter Dropdown */}
          <div className="flex items-center gap-2">
            <Filter className="w-3.5 h-3.5 text-zen-muted" />
            <span className="text-zen-muted">{t("Lọc theo phần:", "Filter by Section:")}</span>
            <select
              value={filterSection}
              onChange={(e) => setFilterSection(e.target.value)}
              className="bg-white border border-zen-border rounded-xl px-3 py-1.5 text-xs text-zen-ink focus:outline-none focus:border-zen-moss-dark"
            >
              <option value="">{t("Tất cả các phần", "All Sections")}</option>
              {sections.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.code} - {t(s.titleVi, s.titleEn)}
                </option>
              ))}
            </select>
          </div>

          {/* Result Count */}
          <span className="text-zen-muted font-medium">
            {t("Tìm thấy:", "Found:")} {filteredResults.length} {t("kết quả", "results")}
          </span>
        </div>
      </div>

      {/* Content Type Tabs */}
      {results.length > 0 && (
        <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none text-xs">
          {["all", "theory", "keyword", "case_study"].map((typeKey) => {
            const count =
              typeKey === "all"
                ? results.length
                : results.filter((r) => r.type === typeKey).length;
            const label =
              typeKey === "all"
                ? t("Tất cả", "All")
                : getTypeLabel(typeKey);

            return (
              <button
                key={typeKey}
                onClick={() => setActiveTypeTab(typeKey)}
                className={`px-3.5 py-1.5 rounded-xl font-semibold transition-all ${
                  activeTypeTab === typeKey
                    ? "bg-zen-moss-dark text-white shadow-sm"
                    : "bg-zen-paper text-zen-ink hover:bg-zen-surface border border-zen-border/70"
                }`}
              >
                {label} ({count})
              </button>
            );
          })}
        </div>
      )}

      {/* Results List */}
      <div className="space-y-4">
        {filteredResults.map((item) => (
          <div
            key={item.id}
            className={`rounded-3xl border bg-zen-paper p-6 shadow-zen-card hover:shadow-zen-floating transition-all flex flex-col justify-between relative ${
              item.isLocked ? "border-amber-200/80 bg-amber-50/20" : "border-zen-border"
            }`}
          >
            <div>
              {/* Type Badge & Section */}
              <div className="flex items-center justify-between text-xs mb-2">
                <div className="flex items-center gap-1.5 font-bold uppercase tracking-wider text-zen-moss-dark">
                  {getTypeIcon(item.type)}
                  <span>{getTypeLabel(item.type)}</span>
                  <span className="text-zen-muted font-normal">•</span>
                  <span className="text-zen-muted font-medium">
                    {t(item.sectionTitleVi, item.sectionTitleEn)}
                  </span>
                </div>

                {item.isLocked && (
                  <span className="flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800 text-[10px] font-bold">
                    <Lock className="w-3 h-3" />
                    {t("Gói trả phí", "Paid tier")}
                  </span>
                )}
              </div>

              {/* Title */}
              <h3 className="font-serif text-lg font-bold text-zen-ink mb-1.5">
                {t(item.titleVi, item.titleEn)}
              </h3>

              {/* Snippet (Blurred if locked) */}
              <div className="relative">
                <p
                  className={`text-xs sm:text-sm text-zen-ink/80 leading-relaxed ${
                    item.isLocked ? "filter blur-[3px] select-none opacity-60" : ""
                  }`}
                >
                  {t(item.snippetVi, item.snippetEn)}
                </p>

                {item.isLocked && (
                  <div className="absolute inset-0 flex items-center justify-center">
                    <Link
                      href="/pricing"
                      className="px-4 py-2 rounded-xl bg-zen-ochre hover:bg-zen-ochre-dark text-white text-xs font-semibold shadow-sm transition-all flex items-center gap-1.5"
                    >
                      <Lock className="w-3.5 h-3.5" />
                      <span>{t("Nâng cấp gói để xem chi tiết", "Upgrade to view")}</span>
                    </Link>
                  </div>
                )}
              </div>
            </div>

            {/* Jump to lesson link */}
            {!item.isLocked && (
              <div className="mt-4 pt-3 border-t border-zen-border/50 flex justify-end">
                <Link
                  href={`/sections/${item.sectionId}`}
                  className="inline-flex items-center gap-1.5 text-xs font-semibold text-zen-moss-dark hover:underline"
                >
                  <span>{t("Đi tới bài học", "Jump to Lesson")}</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </Link>
              </div>
            )}
          </div>
        ))}

        {query.trim() && results.length === 0 && (
          <div className="p-12 text-center rounded-3xl border border-zen-border bg-zen-paper space-y-2">
            <p className="font-serif text-base text-zen-ink font-semibold">
              {t("Không tìm thấy kết quả phù hợp", "No matching results found")}
            </p>
            <p className="text-xs text-zen-muted max-w-sm mx-auto">
              {t(
                "Bạn hãy thử tìm với từ khóa ngắn hơn, hoặc kiểm tra lại bộ lọc theo Phần.",
                "Try searching with fewer words or remove section filters."
              )}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default function SearchPage() {
  return (
    <Suspense fallback={<div className="p-12 text-center text-xs text-zen-muted">Đang tải trang tìm kiếm...</div>}>
      <SearchContent />
    </Suspense>
  );
}
