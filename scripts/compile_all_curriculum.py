# -*- coding: utf-8 -*-
"""
Master compilation script to assemble the expanded ICF PCC Mentor curriculum:
- 7 Verified Official ICF Sources (checked 2026-11-06)
- 2 Configurable Exam Profiles (Legacy 78 SJT & Updated 80 Items)
- 8 Official Public ICF Sample Questions
- 36 Knowledge-Based MCQs for Updated Exam Format
- 50 Authentic SJT Practice Questions (Q01 - Q50)
- 9 Pure-PCC Case Studies (Zero coach projection)
- 90 Leitner Flashcards (10 per section x 9 sections)
- 90 Diagnostic Mini Quizzes (10 per section x 9 sections)
- 100% standardized "khách hàng" terminology
"""

import json
import os
import sys

# Ensure local scripts dir in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from verified_sources_data import get_verified_sources
from exam_profiles_data import get_exam_profiles
from official_samples_data import get_official_samples
from knowledge_questions_data import get_knowledge_questions
from case_studies_data import CASE_STUDIES
from flashcards_data import generate_flashcards
from quizzes_data import generate_quizzes
from sjt_50_data import generate_sjt_50

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "mentor_data.json")
SEED_TS_PATH = os.path.join(BASE_DIR, "src", "lib", "seedData.ts")

# 1. Load base data
with open(DATA_PATH, "r", encoding="utf-8") as f:
    existing = json.load(f)

sections = existing["sections"]
competencies = existing["competencies"]
theories = existing["theories"]
keywords = existing["keywords"]
mindfulness_messages = existing["mindfulnessMessages"]
stickers = existing["stickers"]
system_settings = existing["systemSettings"]
discount_codes = existing["discountCodes"]

# Update system branding in settings
system_settings["appName"] = "PCC Learning & Practice"
system_settings["appSubtitle"] = "Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching."
system_settings["disclaimer"] = "Ứng dụng độc lập phục vụ học tập; không tự nhận được ICF bảo trợ, chứng nhận hoặc phê duyệt. Không sử dụng logo ICF nếu chưa được phép."

# 2. Get all components
verified_sources = get_verified_sources()
exam_profiles = get_exam_profiles()
official_samples = get_official_samples()
for s in official_samples:
    s["bestAnswer"] = s["officialBest"]
    s["worstAnswer"] = s["officialWorst"]
    s["explanationVi"] = s["pedagogicalExplanationVi"]
    s["explanationEn"] = s["pedagogicalExplanationEn"]
    s["questionVi"] = s["scenarioVi"]
    s["questionEn"] = s["scenarioEn"]
    s["competencyAnalysisVi"] = s.get("pedagogicalExplanationVi", "")

knowledge_questions = get_knowledge_questions()
case_studies = CASE_STUDIES
flashcards = generate_flashcards()
quizzes = generate_quizzes()
practice_questions = generate_sjt_50()

# 3. Assemble complete mentor dataset
mentor_data = {
    "appName": "PCC Learning & Practice",
    "appSubtitle": "Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching.",
    "disclaimer": "Ứng dụng độc lập phục vụ học tập; không tự nhận được ICF bảo trợ, chứng nhận hoặc phê duyệt. Không sử dụng logo ICF nếu chưa được phép.",
    "systemSettings": system_settings,
    "verifiedSources": verified_sources,
    "examProfiles": exam_profiles,
    "officialSampleQuestions": official_samples,
    "knowledgeQuestions": knowledge_questions,
    "sections": sections,
    "competencies": competencies,
    "theories": theories,
    "keywords": keywords,
    "flashcards": flashcards,
    "caseStudies": case_studies,
    "quizzes": quizzes,
    "practiceQuestions": practice_questions,
    "mindfulnessMessages": mindfulness_messages,
    "stickers": stickers,
    "discountCodes": discount_codes
}

# 4. Strict Validations
print("--- RUNNING VALIDATION CHECKS ---")
raw_json = json.dumps(mentor_data, ensure_ascii=False)

# Check 1: No "thân chủ"
tc_count = raw_json.lower().count("thân chủ")
assert tc_count == 0, f"Found {tc_count} occurrences of 'thân chủ'!"
print("✅ Verification Passed: 0 occurrences of 'thân chủ' (100% 'khách hàng')")

# Check 2: No coach projection flaw
assert "buông bớt quyền kiểm soát" not in raw_json, "Flawed case study line detected!"
print("✅ Verification Passed: Flawed case study projection removed!")

# Check 3: Counts
assert len(verified_sources) == 7, f"Expected 7 verified sources, got {len(verified_sources)}"
print(f"✅ Verified Sources count: {len(verified_sources)}")

assert len(exam_profiles) == 2, f"Expected 2 exam profiles, got {len(exam_profiles)}"
print(f"✅ Exam Profiles count: {len(exam_profiles)} (Legacy 78-SJT & Updated 80-Item)")

assert len(official_samples) == 8, f"Expected 8 official sample questions, got {len(official_samples)}"
print(f"✅ Official Sample Questions count: {len(official_samples)} (1 per Competency)")

assert len(knowledge_questions) == 36, f"Expected 36 knowledge questions, got {len(knowledge_questions)}"
print(f"✅ Knowledge Questions count: {len(knowledge_questions)} (MCQs)")

assert len(practice_questions) == 50, f"Expected 50 SJT questions, got {len(practice_questions)}"
print(f"✅ Practice Questions count: {len(practice_questions)} (SJT)")

assert len(case_studies) == 9, f"Expected 9 case studies, got {len(case_studies)}"
print(f"✅ Case Studies count: {len(case_studies)} (1 per leaf section)")

assert len(flashcards) == 90, f"Expected 90 flashcards, got {len(flashcards)}"
print(f"✅ Flashcards count: {len(flashcards)} (10 per section x 9 sections)")

assert len(quizzes) == 90, f"Expected 90 quizzes, got {len(quizzes)}"
print(f"✅ Mini Quizzes count: {len(quizzes)} (10 per section x 9 sections)")

# 5. Write to data/mentor_data.json
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(mentor_data, f, indent=2, ensure_ascii=False)
print(f"✅ Saved updated data to {DATA_PATH} ({os.path.getsize(DATA_PATH):,} bytes)")

# 6. Generate src/lib/seedData.ts
ts_content = f"""// AUTO-GENERATED BY scripts/compile_all_curriculum.py
// DO NOT EDIT DIRECTLY. Run `python3 scripts/compile_all_curriculum.py` to regenerate.

export const APP_INFO = {{
  name: "PCC Learning & Practice",
  subtitle: "Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching.",
  disclaimer: "Ứng dụng độc lập phục vụ học tập; không tự nhận được ICF bảo trợ, chứng nhận hoặc phê duyệt. Không sử dụng logo ICF nếu chưa được phép."
}};

export const VERIFIED_SOURCES = {json.dumps(verified_sources, indent=2, ensure_ascii=False)};

export const EXAM_PROFILES = {json.dumps(exam_profiles, indent=2, ensure_ascii=False)};

export const OFFICIAL_SAMPLE_QUESTIONS = {json.dumps(official_samples, indent=2, ensure_ascii=False)};

export const KNOWLEDGE_QUESTIONS = {json.dumps(knowledge_questions, indent=2, ensure_ascii=False)};

export const SECTIONS = {json.dumps(sections, indent=2, ensure_ascii=False)};

export const COMPETENCIES = {json.dumps(competencies, indent=2, ensure_ascii=False)};

export const THEORIES = {json.dumps(theories, indent=2, ensure_ascii=False)};

export const KEYWORDS = {json.dumps(keywords, indent=2, ensure_ascii=False)};

export const FLASHCARDS = {json.dumps(flashcards, indent=2, ensure_ascii=False)};

export const CASE_STUDIES = {json.dumps(case_studies, indent=2, ensure_ascii=False)};

export const QUIZZES = {json.dumps(quizzes, indent=2, ensure_ascii=False)};

export const PRACTICE_QUESTIONS = {json.dumps(practice_questions, indent=2, ensure_ascii=False)};

export const MINDFULNESS_MESSAGES = {json.dumps(mindfulness_messages, indent=2, ensure_ascii=False)};

export const STICKERS = {json.dumps(stickers, indent=2, ensure_ascii=False)};

export const SYSTEM_SETTINGS = {json.dumps(system_settings, indent=2, ensure_ascii=False)};

export const DISCOUNT_CODES = {json.dumps(discount_codes, indent=2, ensure_ascii=False)};
"""

with open(SEED_TS_PATH, "w", encoding="utf-8") as f:
    f.write(ts_content)
print(f"✅ Saved updated seedData to {SEED_TS_PATH} ({os.path.getsize(SEED_TS_PATH):,} bytes)")

print("\n🎉 ALL CURRICULUM DATA COMPILED AND VERIFIED SUCCESSFULLY!")
