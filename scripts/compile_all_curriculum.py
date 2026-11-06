# -*- coding: utf-8 -*-
"""
Master compilation script to assemble the expanded ICF PCC Mentor curriculum:
- 9 Verified Official ICF Sources (including Hullinger & DiGirolamo 2018 White Paper & Summary)
- 2 Configurable Exam Profiles (Legacy 78 SJT & Updated 80 Items)
- 8 Official Public ICF Sample Questions
- 36 Knowledge-Based MCQs for Updated Exam Format
- 55 Authentic SJT Practice Questions (Q01 - Q50 + REF01 - REF05)
- 10 Pure-PCC Case Studies (Zero coach projection, including Referral Case)
- 100 Leitner Flashcards (10 per section x 10 sections)
- 100 Diagnostic Mini Quizzes (10 per section x 10 sections)
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
from referral_guidelines_data import get_referral_curriculum

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
system_settings["appName"] = "Mentor Thi"
system_settings["appSubtitle"] = "Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching."
system_settings["motto"] = "Vì ước mơ đưa Coaching thành lối sống"
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
case_studies = list(CASE_STUDIES)
flashcards = generate_flashcards()
quizzes = generate_quizzes()
practice_questions = generate_sjt_50()

# 3. Integrate Referral Guidelines (Hullinger & DiGirolamo, 2018)
referral_data = get_referral_curriculum()
ref_theories = referral_data["theories"]
ref_flashcards = referral_data["flashcards"]
ref_quizzes = referral_data["quizzes"]
ref_practice = referral_data["practiceQuestions"]

# 3.1 Ensure Referral Section in sections
referral_section = {
    "id": "sec-referral-special",
    "parentId": "sec-a1",
    "titleVi": "Chuyên Đề Đặc Biệt: Chuyển Gửi Khách Hàng & Ranh Giới Coaching",
    "titleEn": "Special Topic: Referring a Client to Therapy & Coaching Boundaries",
    "estimatedMinutes": 35
}
if not any(s["id"] == "sec-referral-special" for s in sections):
    sections.append(referral_section)

# 3.2 Add Referral Theory (7 Lessons combined)
combined_ref_vi = """### CHUYÊN ĐỀ ĐẶC BIỆT: CHUYỂN GỬI KHÁCH HÀNG SANG TRỊ LIỆU (ICF GUIDELINES)
*Căn cứ tài liệu: Hullinger, A. M., & DiGirolamo, J. A. (2018). Referring a client to therapy: A set of guidelines for coaches. International Coaching Federation.*
*Ghi chú: Bản dịch phục vụ học tập, không phải bản dịch chính thức của ICF.*

---
""" + "\n\n---\n\n".join([f"### {th['titleVi']} ({th['pdfLocation']})\n{th['contentVi']}" for th in ref_theories])

combined_ref_en = """### SPECIAL TOPIC: REFERRING A CLIENT TO THERAPY (ICF GUIDELINES)
*Source: Hullinger, A. M., & DiGirolamo, J. A. (2018). Referring a client to therapy: A set of guidelines for coaches. International Coaching Federation.*
*Educational study translation; not an official ICF translation.*

---
""" + "\n\n---\n\n".join([f"### {th['titleEn']} ({th['pdfLocation']})\n{th['contentEn']}" for th in ref_theories])

ref_theory_item = {
    "sectionId": "sec-referral-special",
    "titleVi": "Chuyên Đề: Hướng Dẫn Chuyển Gửi Khách Hàng Sang Trị Liệu & Ranh Giới Coaching (7 Bài Học)",
    "titleEn": "Special Topic: Referring a Client to Therapy Guidelines & Boundaries (7 Lessons)",
    "contentVi": combined_ref_vi,
    "contentEn": combined_ref_en,
    "keyPointsVi": [
        "Coach tuyệt đối KHÔNG chẩn đoán hoặc điều trị bệnh lý tâm thần (Không dùng bảng dấu hiệu làm Diagnostic Checklist).",
        "KHÔNG tự động chuyển gửi chỉ vì khách hàng khóc hoặc có cảm xúc mạnh; chỉ chuyển gửi khi chức năng sinh hoạt hằng ngày bị suy giảm nghiêm trọng kéo dài.",
        "Tránh cách giản lược sai lầm 'coaching chỉ tương lai, trị liệu chỉ quá khứ' - Coaching có thể phản tư quá khứ để hiểu hiện tại và tương lai.",
        "Coaching song song (Concurrent Coaching) hoàn toàn khả thi nếu mục tiêu rạch ròi, khách hàng đồng thuận và nhà trị liệu nhất trí.",
        "Trao đổi chuyển gửi nhẹ nhàng, xin phép chia sẻ quan sát thực tế khách quan, không dán nhãn bệnh lý.",
        "Tuyệt đối giữ bảo mật; chỉ trao đổi với nhà trị liệu khi có văn bản ủy quyền chia sẻ thông tin (Release of Information) do khách hàng ký.",
        "Phân biệt rõ chuyển gửi hợp tác thông thường với trường hợp cấp cứu khẩn cấp (đe dọa tính mạng kích hoạt hotline/cấp cứu ngay)."
    ],
    "keyPointsEn": [
        "Coaches must NEVER diagnose or treat psychological pathology.",
        "DO NOT refer automatically simply because a client weeps or shows strong emotion; holding compassionate space is core PCC competence.",
        "Avoid oversimplification ('coaching is only future, therapy is only past'); past reflections are valid in coaching.",
        "Concurrent coaching is viable and valuable when goals remain distinct, with client consent and therapist concurrence.",
        "Initiate referral conversation respectfully, based on observable facts, without diagnostic labeling.",
        "Strict confidentiality: Never contact a therapist without a signed written Release of Information.",
        "Distinguish routine collaborative referrals from emergency crises requiring immediate life-saving intervention."
    ],
    "lessons": ref_theories
}

theories = [th for th in theories if th.get("sectionId") != "sec-referral-special"]
theories.append(ref_theory_item)

# 3.3 Add Referral Case Study
ref_case_study = {
    "sectionId": "sec-referral-special",
    "titleVi": "Tình Huống Thực Tế: Ranh Giới Giữa Kiệt Sức Nghề Nghiệp & Trầm Cảm Kéo Dài",
    "titleEn": "Real-World Case: Boundaries Between Burnout and Persistent Depression",
    "contextVi": "Khách hàng là Giám đốc Tài chính (CFO), trong phiên thứ 3 chia sẻ rằng đã 4 tuần qua anh không thể ngủ quá 2 tiếng mỗi đêm, mất hết cảm giác thèm ăn, sút 6kg, không còn cảm nhận được niềm vui với bất kỳ việc gì và cảm thấy cuộc đời hoàn toàn vô nghĩa. Anh hỏi: 'Tôi có phải đang bị kiệt sức không coach? Coach hãy giúp tôi tìm lại năng lượng làm việc.'",
    "contextEn": "Client is a CFO. In session 3, he reveals that for 4 weeks he has slept less than 2 hours per night, lost appetite, lost 6kg, feels complete anhedonia and meaningless despair. He asks: 'Am I just burned out? Can you coach me back to having work energy?'",
    "coachResponseVi": "Coach bày tỏ sự quan tâm chân thành và xin phép được chia sẻ quan sát: 'Tôi rất trân trọng sự tin cậy của bạn khi chia sẻ điều này. Tôi nhận thấy các dấu hiệu mất ngủ triền miên, sụt cân và cảm giác kiệt quệ sâu sắc đang ảnh hưởng rất lớn đến sức khỏe thể chất và tinh thần của bạn hằng ngày. Với tư cách là coach, tôi không có chuyên môn y khoa để đánh giá những triệu chứng này. Để đảm bảo an toàn cao nhất cho bạn, bạn nghĩ sao về việc cùng lúc tham khảo ý kiến của bác sĩ y khoa hoặc chuyên gia sức khỏe tâm thần để được kiểm tra toàn diện? Chúng ta có thể cùng xem xét lộ trình coaching phù hợp nhất sau khi bạn có kết quả kiểm tra.'",
    "coachResponseEn": "Coach expresses sincere care and requests permission to share observations: 'I truly appreciate your openness. I notice that chronic severe sleeplessness, weight loss, and profound exhaustion are heavily impacting your daily well-being. As a coach, I am not medically qualified to assess these symptoms. To safeguard your health, how would you feel about consulting a physician or mental health specialist for a comprehensive medical check? We can explore how coaching can best support you once you have professional medical input.'",
    "reflectionQuestionsVi": [
        "Tại sao coach không vội vàng kết luận khách hàng bị trầm cảm hay kiệt sức?",
        "Việc xin phép và quan sát dựa trên dữ kiện thực tế (mất ngủ, sụt cân) khác với việc gán nhãn y khoa như thế nào?",
        "Vì sao việc đề xuất khám y khoa lại là hành động thể hiện trách nhiệm đạo đức cao nhất của một PCC coach?"
    ],
    "reflectionQuestionsEn": [
        "Why did the coach refrain from diagnosing burnout or depression?",
        "How does permission-based factual observation differ from clinical labeling?",
        "Why is recommending medical consultation the highest ethical standard of care for a PCC coach?"
    ]
}
case_studies = [cs for cs in case_studies if cs.get("sectionId") != "sec-referral-special"]
case_studies.append(ref_case_study)

# 3.4 Append Referral Flashcards & Quizzes & Practice Questions
flashcards = [fc for fc in flashcards if fc.get("sectionId") != "sec-referral-special"]
flashcards.extend(ref_flashcards)

quizzes = [qz for qz in quizzes if qz.get("sectionId") != "sec-referral-special"]
quizzes.extend(ref_quizzes)

ref_q_ids = {q["id"] for q in ref_practice}
practice_questions = [pq for pq in practice_questions if pq.get("id") not in ref_q_ids]
practice_questions.extend(ref_practice)

# 4. Assemble complete mentor dataset
mentor_data = {
    "appName": "Mentor Thi",
    "appSubtitle": "Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching.",
    "motto": "Vì ước mơ đưa Coaching thành lối sống",
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

# 5. Strict Validations
print("--- RUNNING MASTER VALIDATION CHECKS ---")
raw_json = json.dumps(mentor_data, ensure_ascii=False)

# Check 1: No "thân chủ"
tc_count = raw_json.lower().count("thân chủ")
assert tc_count == 0, f"Found {tc_count} occurrences of 'thân chủ'!"
print("✅ Verification Passed: 0 occurrences of 'thân chủ' (100% 'khách hàng')")

# Check 2: No coach projection flaw
assert "buông bớt quyền kiểm soát" not in raw_json, "Flawed case study line detected!"
print("✅ Verification Passed: Flawed case study projection removed!")

# Check 3: Counts
assert len(verified_sources) == 9, f"Expected 9 verified sources, got {len(verified_sources)}"
print(f"✅ Verified Sources count: {len(verified_sources)} (Includes Hullinger & DiGirolamo 2018 White Paper & Summary)")

assert len(exam_profiles) == 2, f"Expected 2 exam profiles, got {len(exam_profiles)}"
print(f"✅ Exam Profiles count: {len(exam_profiles)} (Legacy 78-SJT & Updated 80-Item)")

assert len(official_samples) == 8, f"Expected 8 official sample questions, got {len(official_samples)}"
print(f"✅ Official Sample Questions count: {len(official_samples)} (1 per Competency)")

assert len(knowledge_questions) == 36, f"Expected 36 knowledge questions, got {len(knowledge_questions)}"
print(f"✅ Knowledge Questions count: {len(knowledge_questions)} (MCQs)")

assert len(practice_questions) == 55, f"Expected 55 SJT questions (50 standard + 5 referral), got {len(practice_questions)}"
print(f"✅ Practice Questions count: {len(practice_questions)} (SJT)")

assert len(case_studies) == 10, f"Expected 10 case studies (9 standard + 1 referral), got {len(case_studies)}"
print(f"✅ Case Studies count: {len(case_studies)} (1 per leaf section)")

assert len(flashcards) == 100, f"Expected 100 flashcards (10 per section x 10 sections), got {len(flashcards)}"
print(f"✅ Flashcards count: {len(flashcards)} (10 per section x 10 sections)")

assert len(quizzes) == 100, f"Expected 100 quizzes (10 per section x 10 sections), got {len(quizzes)}"
print(f"✅ Mini Quizzes count: {len(quizzes)} (10 per section x 10 sections)")

# 6. Write to data/mentor_data.json
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(mentor_data, f, indent=2, ensure_ascii=False)
print(f"✅ Saved updated data to {DATA_PATH} ({os.path.getsize(DATA_PATH):,} bytes)")

# 7. Generate src/lib/seedData.ts
ts_content = f"""// AUTO-GENERATED BY scripts/compile_all_curriculum.py
// DO NOT EDIT DIRECTLY. Run `python3 scripts/compile_all_curriculum.py` to regenerate.

export const APP_INFO = {{
  name: "Mentor Thi",
  subtitle: "Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching.",
  motto: "Vì ước mơ đưa Coaching thành lối sống",
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

print("\n🎉 ALL MASTER CURRICULUM DATA COMPILED AND VERIFIED SUCCESSFULLY!")
