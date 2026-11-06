# -*- coding: utf-8 -*-
"""
Exam Profile configurations for ICF Credentialing Exams:
1. Legacy Credentialing Exam (78 Situational Judgment Scenarios)
2. Updated PCC-MCC Exam (80 Items: 36 Knowledge MCQs + 44 Scenarios)
"""

EXAM_PROFILES = [
    {
        "id": "legacy_78_sjt",
        "nameVi": "ICF Credentialing Exam (Cấu hình hiện hành)",
        "nameEn": "ICF Credentialing Exam (Current Format)",
        "statusBadgeVi": "Áp dụng đến 31/03/2027",
        "statusBadgeEn": "Available through Mar 31, 2027",
        "totalItems": 78,
        "knowledgeItems": 0,
        "scenarioItems": 78,
        "totalTimeMinutes": 180,
        "breakMinutes": 10,
        "sections": [
            {
                "sectionNumber": 1,
                "nameVi": "Phần 1: Tình huống phán đoán thực tế (SJT)",
                "nameEn": "Part 1: Situational Judgment Scenarios",
                "questionCount": 39,
                "type": "scenario_sjt"
            },
            {
                "sectionNumber": "break",
                "nameVi": "Khoảng nghỉ giải lao (Tùy chọn)",
                "nameEn": "Optional Break",
                "durationMinutes": 10,
                "type": "break"
            },
            {
                "sectionNumber": 2,
                "nameVi": "Phần 2: Tình huống phán đoán thực tế (SJT)",
                "nameEn": "Part 2: Situational Judgment Scenarios",
                "questionCount": 39,
                "type": "scenario_sjt"
            }
        ],
        "scoringRuleVi": "Mỗi tình huống chọn 1 BEST (+1đ) và 1 WORST (+1đ). Điểm thi công bố dạng điểm chuẩn hóa (Scaled Score) từ 200 đến 600. Điểm đỗ yêu cầu: 460/600.",
        "scoringRuleEn": "Each scenario requires choosing 1 BEST (+1 pt) and 1 WORST (+1 pt). Reported as scaled score from 200 to 600. Passing score: 460.",
        "ethicsBaselineVi": "Bộ Quy tắc Đạo đức ICF 2020 (ICF Code of Ethics 2020) & 8 Năng lực Cốt lõi",
        "ethicsBaselineEn": "2020 ICF Code of Ethics & 8 ICF Core Competencies",
        "verificationUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
    },
    {
        "id": "updated_80_items",
        "nameVi": "Updated PCC-MCC Exam (Cấu hình mới)",
        "nameEn": "Updated PCC-MCC Exam (New Format)",
        "statusBadgeVi": "Bắt đầu từ 10/11/2026",
        "statusBadgeEn": "Launches Nov 10, 2026",
        "totalItems": 80,
        "knowledgeItems": 36,
        "scenarioItems": 44,
        "totalTimeMinutes": 150,
        "breakMinutes": 10,
        "sections": [
            {
                "sectionNumber": 1,
                "nameVi": "Phần 1: Câu hỏi kiểm tra kiến thức đa lựa chọn (MCQ)",
                "nameEn": "Section 1: Multiple-Choice Knowledge Questions",
                "questionCount": 18,
                "type": "knowledge_mcq"
            },
            {
                "sectionNumber": 2,
                "nameVi": "Phần 2: Tình huống phán đoán (SJT)",
                "nameEn": "Section 2: Scenario-Based Situational Judgment",
                "questionCount": 22,
                "type": "scenario_sjt"
            },
            {
                "sectionNumber": "break",
                "nameVi": "Khoảng nghỉ giải lao (Tùy chọn)",
                "nameEn": "Optional Break",
                "durationMinutes": 10,
                "type": "break"
            },
            {
                "sectionNumber": 3,
                "nameVi": "Phần 3: Câu hỏi kiểm tra kiến thức đa lựa chọn (MCQ)",
                "nameEn": "Section 3: Multiple-Choice Knowledge Questions",
                "questionCount": 18,
                "type": "knowledge_mcq"
            },
            {
                "sectionNumber": 4,
                "nameVi": "Phần 4: Tình huống phán đoán (SJT)",
                "nameEn": "Section 4: Scenario-Based Situational Judgment",
                "questionCount": 22,
                "type": "scenario_sjt"
            }
        ],
        "scoringRuleVi": "Câu kiến thức chọn 1 đáp án đúng (+1đ). Câu tình huống chọn 1 BEST (+1đ) và 1 WORST (+1đ). Điểm chuẩn hóa tương đương chuẩn đỗ hiện hành.",
        "scoringRuleEn": "Knowledge questions: 1 single correct answer (+1 pt). Scenario questions: 1 BEST (+1 pt) and 1 WORST (+1 pt). Equivalent passing standard.",
        "ethicsBaselineVi": "Bộ Quy tắc Đạo đức ICF 2025 (Hiệu lực 01/04/2025) & 8 Năng lực Cốt lõi sửa đổi",
        "ethicsBaselineEn": "2025 ICF Code of Ethics & Revised 8 Core Competencies",
        "verificationUrl": "https://coachingfederation.org/blog/candidates-guide-to-updated-credentialing-exam/"
    }
]

def get_exam_profiles():
    return EXAM_PROFILES
