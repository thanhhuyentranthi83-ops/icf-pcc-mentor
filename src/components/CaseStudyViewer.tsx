"use client";

import React, { useState } from "react";
import { CaseStudy } from "@/types";
import { useLanguage } from "@/context/LanguageContext";
import { MessageSquare, Sparkles, ChevronDown, ChevronUp, CheckCircle, Award } from "lucide-react";

interface Props {
  caseStudy: CaseStudy;
}

export default function CaseStudyViewer({ caseStudy }: Props) {
  const { t } = useLanguage();
  const [showAnswer, setShowAnswer] = useState(false);

  return (
    <div className="rounded-3xl border border-zen-border bg-zen-paper p-6 sm:p-8 shadow-zen-card">
      {/* Title & Tag */}
      <div className="flex flex-wrap items-center justify-between gap-3 mb-6 pb-4 border-b border-zen-border/60">
        <div>
          <span className="text-[11px] font-bold uppercase tracking-wider text-zen-ochre-dark bg-zen-ochre/15 px-2.5 py-1 rounded-full">
            {t("Tình huống thực tế (Case Study)", "Real-world Case Study")}
          </span>
          <h3 className="font-serif text-xl sm:text-2xl font-bold text-zen-ink mt-2">
            {t(caseStudy.titleVi, caseStudy.titleEn)}
          </h3>
        </div>
      </div>

      {/* Dialogue Script Box */}
      <div className="bg-zen-surface/60 rounded-2xl p-5 border border-zen-border/50 space-y-4 mb-6">
        <div className="flex items-center gap-2 text-xs font-semibold text-zen-moss-dark uppercase tracking-wider">
          <MessageSquare className="w-4 h-4 text-zen-moss-dark" />
          <span>{t("Trích đoạn phiên khai vấn", "Coaching Session Excerpt")}</span>
        </div>

        <div className="prose prose-sm max-w-none text-zen-ink leading-relaxed whitespace-pre-line font-sans">
          {t(caseStudy.scenarioDialogueVi, caseStudy.scenarioDialogueEn)}
        </div>
      </div>

      {/* Analysis Questions */}
      <div className="bg-white/80 rounded-2xl p-5 border border-zen-border/80 mb-6">
        <h4 className="text-xs font-bold text-zen-ink uppercase tracking-wider mb-2 flex items-center gap-1.5">
          <Sparkles className="w-4 h-4 text-zen-ochre" />
          {t("Câu hỏi phân tích tình huống:", "Analysis Questions:")}
        </h4>
        <div className="text-sm text-zen-ink/90 whitespace-pre-line leading-relaxed">
          {t(caseStudy.analysisQuestionsVi, caseStudy.analysisQuestionsEn)}
        </div>
      </div>

      {/* Toggle Suggested Answer */}
      <button
        onClick={() => setShowAnswer(!showAnswer)}
        className="w-full flex items-center justify-between px-5 py-3 rounded-2xl border border-zen-moss-dark/30 bg-zen-moss/10 hover:bg-zen-moss/20 text-zen-moss-dark text-xs font-semibold transition-colors"
      >
        <span>
          {showAnswer
            ? t("Ẩn đáp án gợi ý & phân tích", "Hide suggested answers & rationale")
            : t("Xem đáp án gợi ý & phân tích chuẩn PCC", "View suggested answers & PCC rationale")}
        </span>
        {showAnswer ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
      </button>

      {/* Revealed Answer & PCC Marker Alignment */}
      {showAnswer && (
        <div className="mt-4 p-5 rounded-2xl bg-zen-surface border border-zen-moss/40 text-sm text-zen-ink space-y-4 animate-in fade-in duration-200">
          <div>
            <h5 className="font-bold text-zen-moss-dark flex items-center gap-1.5 text-xs uppercase tracking-wider mb-2">
              <CheckCircle className="w-4 h-4 text-zen-moss-dark" />
              {t("Phân tích đáp án chuẩn mực:", "Official Evaluation Rationale:")}
            </h5>
            <div className="text-sm leading-relaxed whitespace-pre-line text-zen-ink/90">
              {t(caseStudy.suggestedAnswersVi, caseStudy.suggestedAnswersEn)}
            </div>
          </div>

          {/* PCC Markers Benchmarking */}
          <div className="pt-3 border-t border-zen-border/60">
            <div className="flex items-center gap-1.5 text-xs font-bold text-zen-wood uppercase tracking-wider mb-2">
              <Award className="w-4 h-4 text-zen-wood" />
              <span>{t("Đối chiếu ICF Core Competencies & PCC Markers:", "ICF Competencies & PCC Markers:")}</span>
            </div>
            <p className="text-xs text-zen-muted mb-2 font-medium">
              {caseStudy.competencyMapping}
            </p>
            <div className="flex flex-wrap gap-2">
              {caseStudy.pccMarkers.map((marker, i) => (
                <span
                  key={i}
                  className="px-2.5 py-1 rounded-xl bg-zen-moss/15 text-zen-moss-dark text-xs font-medium border border-zen-moss/20"
                >
                  {marker}
                </span>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
