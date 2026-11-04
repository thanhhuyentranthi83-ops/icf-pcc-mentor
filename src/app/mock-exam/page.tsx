"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { useLanguage } from "@/context/LanguageContext";
import { useAuth } from "@/context/AuthContext";
import { getFullMockExam } from "@/lib/db";
import { QuizQuestion } from "@/types";
import SjtExamRunner from "@/components/SjtExamRunner";
import BreathingModal from "@/components/BreathingModal";
import { Mountain, Sparkles, Lock, ArrowLeft, PlayCircle, ShieldCheck } from "lucide-react";

export default function MockExamPage() {
  const { t } = useLanguage();
  const { user, canAccessPaidContent } = useAuth();

  const [questions, setQuestions] = useState<QuizQuestion[]>([]);
  const [showBreathing, setShowBreathing] = useState(false);
  const [hasStarted, setHasStarted] = useState(false);

  useEffect(() => {
    setQuestions(getFullMockExam());
  }, []);

  const hasAccess = canAccessPaidContent();

  const handleStartExamFlow = () => {
    setShowBreathing(true);
  };

  const handleBreathingComplete = () => {
    setShowBreathing(false);
    setHasStarted(true);
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-6 sm:py-8 space-y-6">
      {/* Top back link */}
      <div className="flex items-center justify-between text-xs text-zen-muted">
        <Link
          href="/"
          className="flex items-center gap-1.5 font-medium hover:text-zen-ink transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>{t("Quay về Trang chủ", "Back to Home")}</span>
        </Link>
      </div>

      {/* Breathing Modal Triggered Before Exam */}
      <BreathingModal
        isOpen={showBreathing}
        onComplete={handleBreathingComplete}
        onClose={() => setShowBreathing(false)}
      />

      {/* Main View */}
      {!hasStarted ? (
        <div className="max-w-3xl mx-auto rounded-3xl border border-zen-border bg-zen-paper p-8 sm:p-12 shadow-zen-card text-center space-y-6">
          <div className="w-16 h-16 rounded-full bg-zen-ochre/20 text-zen-ochre-dark mx-auto flex items-center justify-center shadow-zen-subtle">
            <Mountain className="w-8 h-8" />
          </div>

          <div className="space-y-2">
            <span className="text-xs font-bold uppercase tracking-wider text-zen-ochre-dark bg-zen-ochre/15 px-3 py-1 rounded-full">
              {t("Đề Thi Tổng Hợp Toàn Diện", "Comprehensive Mock Exam")}
            </span>
            <h1 className="font-serif text-3xl sm:text-4xl font-bold text-zen-ink">
              {t("Thi Thử Tổng PCC — Chuẩn ICF", "Full ICF PCC Credentialing Mock Exam")}
            </h1>
            <p className="text-sm text-zen-muted max-w-xl mx-auto leading-relaxed">
              {t(
                "Đề thi gồm 16 tình huống phán đoán chuẩn quốc tế (Situational Judgment Test). Với mỗi tình huống, hãy chọn 1 phản hồi TỐT NHẤT (BEST) và 1 phản hồi TỆ NHẤT (WORST).",
                "Consists of 16 official Situational Judgment scenarios. For each scenario, choose 1 BEST response and 1 WORST response based on the 2025 ICF Core Competencies & Code of Ethics."
              )}
            </p>
          </div>

          {/* Exam Specs */}
          <div className="grid grid-cols-3 gap-3 max-w-md mx-auto pt-2">
            <div className="p-3.5 rounded-2xl bg-zen-surface/60 border border-zen-border text-center">
              <span className="text-xs text-zen-muted block">{t("Số câu hỏi", "Questions")}</span>
              <span className="font-serif text-lg font-bold text-zen-ink">16 SJT</span>
            </div>
            <div className="p-3.5 rounded-2xl bg-zen-surface/60 border border-zen-border text-center">
              <span className="text-xs text-zen-muted block">{t("Thời gian", "Time")}</span>
              <span className="font-serif text-lg font-bold text-zen-ink">30 {t("phút", "mins")}</span>
            </div>
            <div className="p-3.5 rounded-2xl bg-zen-surface/60 border border-zen-border text-center">
              <span className="text-xs text-zen-muted block">{t("Độ khó", "Level")}</span>
              <span className="font-serif text-lg font-bold text-zen-moss-dark">PCC 2025</span>
            </div>
          </div>

          {/* Calming Pre-exam Reminder */}
          <div className="p-4 rounded-2xl bg-zen-surface/80 border border-zen-moss/30 max-w-md mx-auto text-xs text-zen-ink/90 flex items-center gap-3 text-left">
            <Sparkles className="w-5 h-5 text-zen-ochre shrink-0" />
            <span>
              {t(
                "Trước khi bắt đầu, hệ thống sẽ đồng hành cùng bạn 3 hơi thở chánh niệm để an định tâm trí.",
                "Before beginning, we will guide you through 3 mindful breaths to center your mind."
              )}
            </span>
          </div>

          {/* Action Button */}
          {!hasAccess ? (
            <div className="space-y-3 pt-2">
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-100 text-amber-800 text-xs font-semibold">
                <Lock className="w-3.5 h-3.5" />
                <span>{t("Thi thử tổng PCC dành cho học viên gói trả phí", "Full mock exam reserved for paid tiers")}</span>
              </div>
              <div>
                <Link
                  href="/pricing"
                  className="inline-flex items-center gap-2 px-8 py-3.5 rounded-2xl bg-zen-ochre hover:bg-zen-ochre-dark text-white font-semibold text-sm shadow-zen-card transition-all"
                >
                  <Sparkles className="w-4 h-4" />
                  <span>{t("Nâng cấp gói để vào thi ngay", "Upgrade to take exam")}</span>
                </Link>
              </div>
            </div>
          ) : (
            <div className="pt-2">
              <button
                onClick={handleStartExamFlow}
                className="inline-flex items-center gap-2 px-8 py-3.5 rounded-2xl bg-zen-moss-dark hover:bg-zen-moss-deep text-white font-semibold text-sm shadow-zen-card hover:shadow-zen-floating transition-all"
              >
                <PlayCircle className="w-5 h-5" />
                <span>{t("Bắt đầu thi thử (Ba hơi thở trước khi thi)", "Begin Exam (3 Mindful Breaths)")}</span>
              </button>
            </div>
          )}
        </div>
      ) : (
        <SjtExamRunner
          questions={questions}
          examTitleVi="Đề Thi Thử Tổng Hợp Cấp Độ PCC (Situational Judgment)"
          examTitleEn="Comprehensive PCC Credentialing Mock Exam"
          examType="full_pcc_mock"
          durationMinutes={30}
        />
      )}
    </div>
  );
}
