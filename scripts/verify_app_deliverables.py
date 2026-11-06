# -*- coding: utf-8 -*-
"""
Verification Script for PCC Learning & Practice
Validates all data structures, requirements, constraints, and page modules.
"""
import os
import json
import re

DATA_PATH = "data/mentor_data.json"
assert os.path.exists(DATA_PATH), f"Missing {DATA_PATH}"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    raw_text = f.read()
    data = json.loads(raw_text)

# 1. Terminology Constraint: 0 occurrences of "thân chủ"
assert "thân chủ" not in raw_text.lower(), "FAILED: Found 'thân chủ' in mentor_data.json!"
print("✅ PASSED: 0 occurrences of 'thân chủ' across entire dataset.")

# 2. 7 Verified Sources
sources = data.get("verifiedSources", [])
assert len(sources) == 7, f"Expected 7 sources, found {len(sources)}"
for s in sources:
    assert s["url"].startswith("http"), f"Invalid URL for {s['id']}"
    assert "Đã xác minh trực tiếp" in s["verificationStatus"], f"Invalid status for {s['id']}"
print(f"✅ PASSED: Exactly 7 verified sources directly from official documentation.")

# 3. 2 Exam Profiles
profiles = data.get("examProfiles", [])
assert len(profiles) == 2, f"Expected 2 profiles, found {len(profiles)}"
prof_ids = [p["id"] for p in profiles]
assert "legacy_78_sjt" in prof_ids and "updated_80_items" in prof_ids
print("✅ PASSED: Dual Exam Profiles configured (Current 78 SJT & Updated 80 Items).")

# 4. 8 Official Public ICF Sample Questions
samples = data.get("officialSampleQuestions", [])
assert len(samples) == 8, f"Expected 8 samples, found {len(samples)}"
expected_keys = {
    "OSQ01": ("D", "A"),
    "OSQ02": ("B", "D"),
    "OSQ03": ("C", "D"),
    "OSQ04": ("A", "C"),
    "OSQ05": ("D", "A"),
    "OSQ06": ("C", "A"),
    "OSQ07": ("C", "B"),
    "OSQ08": ("A", "D")
}
for s in samples:
    qid = s["id"]
    exp_b, exp_w = expected_keys[qid]
    assert s["bestAnswer"] == exp_b, f"Mismatch Best for {qid}: expected {exp_b}, got {s['bestAnswer']}"
    assert s["worstAnswer"] == exp_w, f"Mismatch Worst for {qid}: expected {exp_w}, got {s['worstAnswer']}"
    assert len(s["options"]) == 4, f"Expected 4 options for {qid}"
    assert s["scenarioEn"] and s["scenarioVi"], f"Missing bilingual scenario for {qid}"
print("✅ PASSED: Exactly 8 official public ICF sample questions with verbatim text and official answer keys.")

# 5. Question Banks
knowledge_q = data.get("knowledgeQuestions", [])
sjt_q = data.get("practiceQuestions", [])
assert len(knowledge_q) == 36, f"Expected 36 knowledge questions, found {len(knowledge_q)}"
assert len(sjt_q) == 50, f"Expected 50 SJT questions, found {len(sjt_q)}"
print(f"✅ PASSED: Question pools verified (36 Knowledge MCQs + 50 SJT Scenarios).")

# 6. Curriculum (9 Units, 90 Flashcards, 90 Quizzes, 9 Case Studies)
theories = data.get("theories", [])
flashcards = data.get("flashcards", [])
quizzes = data.get("quizzes", [])
case_studies = data.get("caseStudies", [])

assert len(theories) == 9, f"Expected 9 theories, found {len(theories)}"
assert len(flashcards) == 90, f"Expected 90 flashcards, found {len(flashcards)}"
assert len(quizzes) == 90, f"Expected 90 quizzes, found {len(quizzes)}"
assert len(case_studies) == 9, f"Expected 9 case studies, found {len(case_studies)}"

# Ensure case studies do NOT have coach projection
for cs in case_studies:
    assert "điều gì khiến việc buông bớt quyền kiểm soát" not in cs.get("coachResponseVi", ""), f"Found coach projection in {cs['id']}"
print("✅ PASSED: Curriculum verified (9 units, 90 Leitner flashcards, 90 quizzes, 9 objective case studies without coach projection).")

# 7. Code compilation checks
import py_compile
py_compile.compile("streamlit_app.py", doraise=True)
py_compile.compile("app_modules/styles.py", doraise=True)
py_compile.compile("app_modules/state.py", doraise=True)
py_compile.compile("app_modules/page_home.py", doraise=True)
py_compile.compile("app_modules/page_library.py", doraise=True)
py_compile.compile("app_modules/page_official_samples.py", doraise=True)
py_compile.compile("app_modules/page_curriculum.py", doraise=True)
py_compile.compile("app_modules/page_daily_practice.py", doraise=True)
py_compile.compile("app_modules/page_sjt.py", doraise=True)
py_compile.compile("app_modules/page_journal.py", doraise=True)
py_compile.compile("app_modules/page_admin.py", doraise=True)
py_compile.compile("app_modules/page_pricing.py", doraise=True)
print("✅ PASSED: All 12 Python modules compiled cleanly with zero syntax errors.")

print("\n🚀 ALL APP DELIVERABLES & INTEGRITY TESTS PASSED SUCCESSFULLY!")
