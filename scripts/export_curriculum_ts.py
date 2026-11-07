# -*- coding: utf-8 -*-
"""
Export 7-Module ICF Curriculum Data to TypeScript for Next.js App
Generates: src/lib/curriculumData.ts
"""
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from icf_curriculum_data import (
    get_icf_7_modules,
    get_glossary_terms,
    get_tea_micro_lessons,
    GLOSSARY_EXERCISES
)

modules = get_icf_7_modules()
glossary = get_glossary_terms()
tea_lessons = get_tea_micro_lessons()

target_file = os.path.join(BASE_DIR, "src", "lib", "curriculumData.ts")

ts_code = f"""// AUTO-GENERATED FROM scripts/icf_curriculum_data.py
// Complete 7-Module ICF Curriculum Data for Next.js Frontend

export interface QuizOption {{
  key: string;
  textVi: string;
  textEn: string;
}}

export interface LessonQuiz {{
  id?: string;
  sectionId?: string;
  questionVi: string;
  questionEn: string;
  options: QuizOption[];
  correctAnswer: string;
  explanationVi: string;
  explanationEn?: string;
  [key: string]: any;
}}

export interface CaseWorkflow {{
  step1_scenarioVi: string;
  step1_scenarioEn: string;
  step2_stakeholdersVi: string;
  step2_stakeholdersEn: string;
  step3_selfReflectionPromptVi: string;
  step3_selfReflectionPromptEn: string;
  step4_sourceAnalysisVi: string;
  step4_sourceAnalysisEn: string;
  step5_takeawaysVi: string;
}}

export interface FaqItem {{
  faqId: string;
  tag: string;
  questionVi: string;
  questionEn: string;
  answerVi: string;
  answerEn: string;
  relatedStandard?: string;
  verifiedDate: string;
}}

export interface Lesson {{
  id: string;
  moduleId: string;
  lessonNumber: number;
  titleVi: string;
  titleEn: string;
  estimatedMinutes: number;
  objectivesVi?: string[];
  objectivesEn?: string[];
  sourceDocument?: string;
  sourceVersion?: string;
  sourceLink?: string;
  originalExcerptEn?: string;
  translationVi?: string;
  commentaryVi?: string;
  commentaryEn?: string;
  exampleType?: string;
  exampleContentVi?: string;
  exampleContentEn?: string;
  pdfLink?: string;
  comparison2019Vi?: string;
  comparison2019En?: string;
  quiz?: LessonQuiz;
  caseWorkflow?: CaseWorkflow;
  faqs?: FaqItem[];
  [key: string]: any;
}}

export interface GlossaryTerm {{
  id: string;
  category: string;
  categoryVi: string;
  termEn: string;
  termVi: string;
  definitionEn: string;
  definitionVi: string;
  source: string;
  version: string;
  isOfficial: boolean;
  nearSynonyms?: string[];
}}

export interface GlossaryExercise {{
  id: string;
  termPair: string;
  questionVi: string;
  questionEn: string;
  options: QuizOption[];
  correctAnswer: string;
  explanationVi: string;
}}

export interface CurriculumModule {{
  id: string;
  number: number;
  titleVi: string;
  titleEn: string;
  icon: string;
  sourceDoc: string;
  sourceUrl: string;
  summaryVi: string;
  summaryEn: string;
  lessons: Lesson[];
  glossaryTerms?: GlossaryTerm[];
  glossaryExercises?: GlossaryExercise[];
  wrapUpQuiz?: any;
}}

export interface TeaMicroLesson {{
  id: string;
  moduleId: string;
  lessonId: string;
  titleVi: string;
  titleEn: string;
  quoteVi: string;
  promptVi: string;
  linkTextVi: string;
}}

export interface UserLessonProgress {{
  status: "unread" | "read" | "quiz_passed";
  score?: number;
  note?: string;
  needsReview?: boolean;
  updatedAt?: string;
}}

export const ICF_7_MODULES: CurriculumModule[] = {json.dumps(modules, ensure_ascii=False, indent=2)};

export const GLOSSARY_TERMS: GlossaryTerm[] = {json.dumps(glossary, ensure_ascii=False, indent=2)};

export const GLOSSARY_EXERCISES: GlossaryExercise[] = {json.dumps(GLOSSARY_EXERCISES, ensure_ascii=False, indent=2)};

export const TEA_MICRO_LESSONS: TeaMicroLesson[] = {json.dumps(tea_lessons, ensure_ascii=False, indent=2)};

// Storage keys
const PROGRESS_STORAGE_KEY = "icf_curriculum_progress_v2";

export function getCurriculumProgress(): Record<string, UserLessonProgress> {{
  if (typeof window === "undefined") return {{}};
  try {{
    const val = localStorage.getItem(PROGRESS_STORAGE_KEY);
    if (!val) return {{}};
    return JSON.parse(val);
  }} catch {{
    return {{}};
  }}
}}

export function saveLessonProgress(
  lessonId: string,
  update: Partial<UserLessonProgress>
): Record<string, UserLessonProgress> {{
  if (typeof window === "undefined") return {{}};
  try {{
    const cur = getCurriculumProgress();
    const existing = cur[lessonId] || {{ status: "unread" }};
    
    // Do not downgrade quiz_passed to read
    let nextStatus = update.status || existing.status;
    if (existing.status === "quiz_passed" && update.status === "read") {{
      nextStatus = "quiz_passed";
    }}

    cur[lessonId] = {{
      ...existing,
      ...update,
      status: nextStatus,
      updatedAt: new Date().toISOString()
    }};

    localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(cur));
    return cur;
  }} catch {{
    return {{}};
  }}
}}

export function computeModuleProgress(moduleId: string, progress: Record<string, UserLessonProgress>): {{
  total: number;
  completed: number;
  percent: number;
}} {{
  const mod = ICF_7_MODULES.find((m) => m.id === moduleId);
  if (!mod) return {{ total: 0, completed: 0, percent: 0 }};
  
  if (mod.id === "mod-7") {{
    // Glossary terms mastery
    const total = (mod.glossaryTerms?.length || 12) + (mod.glossaryExercises?.length || 2);
    const completed = Object.keys(progress).filter(k => k.startsWith("gl-") && progress[k]?.status === "quiz_passed").length;
    const percent = Math.min(100, Math.round((completed / total) * 100));
    return {{ total, completed, percent }};
  }}

  const total = mod.lessons.length;
  if (total === 0) return {{ total: 0, completed: 0, percent: 0 }};
  
  const completed = mod.lessons.filter((les) => {{
    const p = progress[les.id];
    return p && (p.status === "read" || p.status === "quiz_passed");
  }}).length;

  const percent = Math.min(100, Math.round((completed / total) * 100));
  return {{ total, completed, percent }};
}}

export function computeOverallProgress(progress: Record<string, UserLessonProgress>): {{
  totalLessons: number;
  completedLessons: number;
  overallPercent: number;
}} {{
  let totalLessons = 0;
  let completedLessons = 0;

  ICF_7_MODULES.forEach((mod) => {{
    const stats = computeModuleProgress(mod.id, progress);
    totalLessons += stats.total;
    completedLessons += stats.completed;
  }});

  const overallPercent = totalLessons > 0 ? Math.min(100, Math.round((completedLessons / totalLessons) * 100)) : 0;
  return {{ totalLessons, completedLessons, overallPercent }};
}}
"""

with open(target_file, "w", encoding="utf-8") as f:
    f.write(ts_code)

print(f"Successfully generated {target_file} ({len(ts_code)} bytes)")
