# -*- coding: utf-8 -*-
"""
Question Helpers: Detailed Option-by-Option (A-D) Analysis and ICF Source Citations
"""

def get_source_anchor(q):
    """Return explicit ICF source citation for a question."""
    comp = q.get("primaryCompetency", q.get("domain", ""))
    qid = q.get("id", "")

    if qid.startswith("OSQ"):
        return {
            "sourceCode": "SRC-03 (ICF Official Public Release)",
            "sourceName": "Official ICF Credentialing Exam Sample Questions",
            "referenceStandard": f"ICF Core Competencies (2019) — {comp}",
            "verifiedUrl": "https://coachingfederation.org/resource/icf-credentialing-exam-sample-questions/"
        }
    elif "Ethic" in comp or "1." in comp or "Đạo đức" in comp:
        return {
            "sourceCode": "SRC-04 / SRC-05 (ICF Code of Ethics & ICE)",
            "sourceName": "ICF Code of Ethics (2020 & 2025 Editions) & Insights for Ethics",
            "referenceStandard": "Section 1: Responsibility to Clients / Section 3: Professional Practice",
            "verifiedUrl": "https://coachingfederation.org/credentialing/coaching-ethics/icf-code-of-ethics/"
        }
    elif "2." in comp or "Mindset" in comp:
        return {
            "sourceCode": "SRC-01 / SRC-02 (ICF Core Competency 2)",
            "sourceName": "ICF Core Competencies — Embodies a Coaching Mindset",
            "referenceStandard": "Competency 2: Ongoing reflective practice, client autonomy, intuition awareness",
            "verifiedUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
        }
    elif "3." in comp or "Agreement" in comp:
        return {
            "sourceCode": "SRC-01 (ICF Core Competency 3)",
            "sourceName": "ICF Core Competencies — Establishes and Maintains Agreements",
            "referenceStandard": "Competency 3: Recontracting, session outcome definition, measure of success",
            "verifiedUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
        }
    elif "4." in comp or "Trust" in comp:
        return {
            "sourceCode": "SRC-01 (ICF Core Competency 4)",
            "sourceName": "ICF Core Competencies — Cultivates Trust and Safety",
            "referenceStandard": "Competency 4: Psychological safety, non-judgmental acceptance, empathy",
            "verifiedUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
        }
    elif "5." in comp or "Presence" in comp:
        return {
            "sourceCode": "SRC-01 (ICF Core Competency 5)",
            "sourceName": "ICF Core Competencies — Maintains Presence",
            "referenceStandard": "Competency 5: Comfortable with not knowing, silence, emotional containment",
            "verifiedUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
        }
    elif "6." in comp or "Listening" in comp:
        return {
            "sourceCode": "SRC-01 (ICF Core Competency 6)",
            "sourceName": "ICF Core Competencies — Listens Actively",
            "referenceStandard": "Competency 6: Hearing beyond words, noticing energy shifts, metaphors",
            "verifiedUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
        }
    elif "7." in comp or "Awareness" in comp:
        return {
            "sourceCode": "SRC-01 (ICF Core Competency 7)",
            "sourceName": "ICF Core Competencies — Evokes Awareness",
            "referenceStandard": "Competency 7: Powerful inquiry without projection or unsolicited interpretation",
            "verifiedUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
        }
    else:
        return {
            "sourceCode": "SRC-01 (ICF Core Competency 8)",
            "sourceName": "ICF Core Competencies — Facilitates Client Growth",
            "referenceStandard": "Competency 8: Client autonomy in accountability, celebration, integration",
            "verifiedUrl": "https://coachingfederation.org/credentialing/icf-credential-exams/pcc-mcc-exam/"
        }

def format_ad_analysis(q, lang="vi"):
    """
    Produce a complete, structured A-D option-by-option rationale breakdown.
    """
    options = q.get("options", [])
    best_key = q.get("bestAnswer", q.get("officialBest"))
    worst_key = q.get("worstAnswer", q.get("officialWorst"))
    comp = q.get("primaryCompetency", q.get("domain", "ICF Standard"))
    explanation = q.get("explanationVi" if lang == "vi" else "explanationEn", q.get("pedagogicalExplanationVi", ""))
    clue = q.get("keyClueVi" if lang == "vi" else "keyClueEn", "")

    analysis_blocks = []
    for opt in options:
        k = opt["key"]
        opt_text = opt.get("textVi" if lang == "vi" else "textEn", "")
        if k == best_key:
            tag = "🌟 [BEST - TỐT NHẤT]" if lang == "vi" else "🌟 [BEST ACTION]"
            tag_color = "#2E7D32"
            why = (f"Hành động gương mẫu nhất theo {comp}. Giữ trọn sự tự chủ, bảo mật và trách nhiệm đạo đức cao nhất đối với khách hàng."
                   if lang == "vi" else f"Exemplary action under {comp}. Fully honors client autonomy, confidentiality, and professional integrity.")
        elif k == worst_key:
            tag = "⚠️ [WORST - TỆ NHẤT]" if lang == "vi" else "⚠️ [WORST ACTION]"
            tag_color = "#C62828"
            why = (f"Hành động nguy hại hoặc vi phạm chuẩn mực. Áp đặt suy diễn, xâm phạm tự quyết hoặc vi phạm nghiêm trọng tính bảo mật / đạo đức."
                   if lang == "vi" else f"Most detrimental action. Breaches ethical standards, strips away client agency, or imposes unsolicited coach assumptions.")
        else:
            tag = "⚪ [Phương Án Trung Gian / Bán Phần]" if lang == "vi" else "⚪ [Intermediate Option]"
            tag_color = "#666666"
            why = (f"Phương án chưa đạt hiệu quả tối ưu. Có thể giải quyết một phần nhưng chưa trao quyền trọn vẹn cho khách hàng như Best."
                   if lang == "vi" else f"Sub-optimal action. Partially addresses the scenario but falls short of the full client empowerment achieved by the Best action.")

        analysis_blocks.append({
            "key": k,
            "text": opt_text,
            "tag": tag,
            "tagColor": tag_color,
            "why": why
        })

    anchor = get_source_anchor(q)
    return {
        "bestKey": best_key,
        "worstKey": worst_key,
        "explanation": explanation,
        "clue": clue,
        "options": analysis_blocks,
        "source": anchor
    }
