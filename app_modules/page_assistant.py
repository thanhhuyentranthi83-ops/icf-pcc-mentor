# -*- coding: utf-8 -*-
"""
Socratic AI Learning Assistant for PCC Learning & Practice
Grounded strictly in the 7 directly verified official ICF sources and core competency standards.
"""
import streamlit as st

VERIFIED_KNOWLEDGE_BASE = [
    {
        "keywords": ["chuyển tuyến", "bác sĩ", "tâm lý", "trị liệu", "referral", "therapy", "ranh giới"],
        "question": "Khi nào Coach bắt buộc phải dừng phiên và chuyển tuyến chuyên gia y tế / tâm lý?",
        "shortSummary": "Khi vấn đề của khách hàng vượt khỏi phạm vi phát triển hiện tại và tương lai, chạm vào chấn thương quá khứ, trầm cảm nặng hoặc ý định tự hại.",
        "detailedAnswer": """
**1. Các dấu hiệu nhận diện chuyển tuyến bắt buộc (Referral Indicators):**
- Khách hàng biểu hiện các triệu chứng rối loạn cảm xúc trầm trọng, mất khả năng sinh hoạt hoặc làm việc bình thường.
- Có ý nghĩ, lời nói hoặc kế hoạch tự gây hại bản thân hoặc người khác (Duty to warn / bảo vệ sự an toàn).
- Vấn đề cốt lõi bắt nguồn từ sang chấn tâm lý quá khứ (trauma, PTSD) cần liệu pháp phân tâm hoặc phục hồi chuyên khoa.
- Khách hàng có dấu hiệu nghiện ngập, lạm dụng chất kích thích làm suy giảm năng lực nhận thức.

**2. Nguyên tắc hành động chuẩn mực của Coach:**
- Không chẩn đoán bệnh lý tâm thần (Coach không đóng vai bác sĩ hay nhà tâm lý học).
- Tổ chức một cuộc trò chuyện tôn trọng, ấm áp, ghi nhận sự dũng cảm của khách hàng và giải thích rõ ranh giới chuyên môn của Coaching.
- Khuyến nghị khách hàng tìm kiếm sự trợ giúp chuyên khoa phù hợp và có thể tạm hoãn hoặc chấm dứt hợp đồng coaching nếu việc tiếp tục có thể gây tổn thương cho khách hàng.
        """,
        "sourceCitation": "SRC-04 (ICF Code of Ethics Tiêu chuẩn 1.4 & 1.18) & SRC-05 (Insights and Considerations for Ethics)"
    },
    {
        "keywords": ["2020", "2025", "đạo đức", "ethics", "cập nhật", "khác biệt"],
        "question": "Điểm khác biệt cốt lõi giữa Bộ Quy tắc Đạo đức ICF 2020 và 2025 là gì?",
        "shortSummary": "Bản 2025 cập nhật định nghĩa coaching hiện đại, bổ sung chuẩn mực về công nghệ/AI, làm rõ xung đột lợi ích tài chính và bảo mật dữ liệu.",
        "detailedAnswer": """
**1. Sự phân bổ theo lộ trình kỳ thi:**
- **Bài thi hiện hành:** Sử dụng nền tảng Bộ Quy tắc Đạo đức 2020 cho đến trước khi kỳ thi cập nhật chính thức có hiệu lực.
- **Bài thi cập nhật (áp dụng từ 10/11/2026, bắt buộc từ 01/04/2027):** Tích hợp hoàn toàn các sửa đổi của Bộ Quy tắc Đạo đức 2025.

**2. Các nội dung cập nhật trọng tâm trong bản 2025:**
- **Ứng dụng Trí tuệ Nhân tạo & Công nghệ:** Bổ sung hướng dẫn đạo đức về việc sử dụng các công cụ công nghệ, AI trợ lý trong phiên coach mà vẫn bảo đảm 100% tính bảo mật và sự đồng thuận của khách hàng.
- **Minh bạch xung đột lợi ích:** Quy định chặt chẽ hơn về việc nhận hoa hồng, lợi ích phụ, hoặc vừa làm coach vừa giữ vai trò nhà đầu tư/tư vấn trong các doanh nghiệp đối thủ.
- **Trách nhiệm bảo mật dữ liệu số:** Nâng cao tiêu chuẩn lưu trữ và hủy bỏ dữ liệu điện tử của khách hàng.
        """,
        "sourceCitation": "SRC-02 (A Candidate's Guide to the Updated Credentialing Exam) & SRC-04 (ICF Code of Ethics 2025)"
    },
    {
        "keywords": ["marker", "pcc markers", "ghi âm", "khác nhau", "sjt", "trắc nghiệm"],
        "question": "Tại sao không được dùng PCC Markers làm công thức rập khuôn cho bài thi trắc nghiệm tình huống (SJT)?",
        "shortSummary": "PCC Markers là 37 chỉ báo hành vi thính giác dành riêng cho việc chấm băng ghi âm; còn bài thi SJT đo lường năng lực phán đoán tình huống theo ngữ cảnh và tự chủ.",
        "detailedAnswer": """
**1. Bản chất của PCC Markers (Miền 3):**
- Được thiết kế độc quyền cho các Giám khảo ICF (Assessors) để lắng nghe và đánh giá bằng chứng hành vi qua âm thanh trong phiên coach thực tế kéo dài 30–60 phút (Performance Evaluation).
- Đo lường xem coach có ngắt lời khách hàng không, có dùng từ ngữ của khách hàng không, có khơi gợi để khách hàng đặt câu hỏi không...

**2. Bản chất của bài thi trắc nghiệm tình huống (SJT):**
- Đặt thí sinh vào một tình huống tiến thoái lưỡng nan cụ thể (dilemma) và yêu cầu chọn hành động TỐT NHẤT (BEST) và TỆ NHẤT (WORST).
- Một câu nói có thể đúng chuẩn Marker nhưng nếu áp dụng sai ngữ cảnh (ví dụ: khách hàng đang khóc mà coach lại hỏi dồn dập về mục tiêu) thì lại là hành động WORST!
- **Quy tắc vàng:** Trong bài thi viết, luôn ưu tiên TÍNH TỰ CHỦ CỦA KHÁCH HÀNG, SỰ MINH BẠCH ĐẠO ĐỨC và SỰ HIỆN DIỆN TĨNH TẠI, không máy móc đếm số lượng Marker.
        """,
        "sourceCitation": "SRC-01 (ICF PCC-MCC Exam Blueprint) & SRC-06 (PCC Minimum Skills Requirements)"
    },
    {
        "keywords": ["suy diễn", "projection", "năng lực 7", "khơi gợi", "câu hỏi mở", "áp đặt"],
        "question": "Thế nào là câu hỏi không suy diễn áp đặt theo Năng lực 7 (Evoking Awareness)?",
        "shortSummary": "Câu hỏi thuần khiết mở không mang theo định kiến, giả định hay chẩn đoán ngầm của coach, mà hoàn toàn bám rễ vào trải nghiệm và lời nói của khách hàng.",
        "detailedAnswer": """
**1. Nhận diện lỗi suy diễn áp đặt (Coach Projection):**
- *Ví dụ lỗi:* "Điều gì khiến việc buông bớt quyền kiểm soát trở nên khó khăn với bạn như vậy?"  
  -> Coach đã tự ý gán nhãn rằng khách hàng đang "khó khăn trong việc buông quyền kiểm soát", trong khi khách hàng chưa hề khẳng định điều đó! Đây là lỗi áp đặt giả định của coach lên khách hàng.

**2. Cách tiếp cận chuẩn mực cấp độ PCC:**
- Khách hàng: "Tôi luôn cảm thấy mình phải tự tay quán xuyến mọi việc ở dự án này."
- Coach phản hồi chuẩn: *"Khi bạn nói 'tự tay quán xuyến mọi việc', điều đó mang ý nghĩa gì đối với bạn lúc này?"* hoặc *"Điều gì là quan trọng nhất đối với bạn trong cách bạn đang đồng hành cùng dự án?"*
- Coach đóng vai trò tấm gương phản chiếu trong trẻo, mời gọi khách hàng tự khám phá thay vì hướng dẫn họ theo suy nghĩ của mình.
        """,
        "sourceCitation": "SRC-01 (ICF Core Competency 7: Evokes Awareness) & PCC Markers 7.1–7.8"
    },
    {
        "keywords": ["best", "worst", "nguyên lý", "chiến lược", "chấm điểm", "4 mức"],
        "question": "Nguyên lý xác định BEST và WORST và cách tính điểm trong đề thi ICF?",
        "shortSummary": "BEST trao quyền tự quyết tối đa và giữ vững đạo đức; WORST tước đoạt tự chủ hoặc vi phạm bảo mật. Chấm 4 mức: 2 điểm (đúng cả 2), 1 điểm (đúng 1), 0 điểm (sai cả 2).",
        "detailedAnswer": """
**1. Ma trận lựa chọn BEST:**
- Tôn trọng tối đa tính tự chủ (Client Autonomy) và quyền tự quyết của khách hàng.
- Giữ vững hợp đồng coaching và ranh giới bảo mật.
- Khơi gợi nhận thức sâu sắc mà không áp đặt lời khuyên, giải pháp hay quan điểm cá nhân.
- Tĩnh tại, hiện diện và đồng hành bình đẳng (Partnering).

**2. Ma trận nhận diện WORST:**
- Coach đưa ra lời khuyên trực tiếp, chỉ đạo khách hàng phải làm gì (Consulting / Mentoring trái phép).
- Che giấu hoặc coi nhẹ xung đột lợi ích tiềm ẩn.
- Tự ý chia sẻ nội dung phiên coach cho bên thứ ba (Sponsor / HR) mà không có sự đồng thuận.
- Đưa ra giả định, định kiến hoặc phán xét cảm xúc của khách hàng.

**3. Cơ chế tính điểm quy chuẩn:**
- Mỗi câu SJT có 2 điểm tối đa:
  - Đúng cả BEST và WORST: 2/2 điểm (100%).
  - Đúng BEST hoặc WORST: 1/2 điểm (50%).
  - Sai cả hai: 0/2 điểm (0%).
- Thang điểm quy đổi chuẩn: 200–600, điểm đạt chuẩn là 460.
        """,
        "sourceCitation": "SRC-01 (ICF Exam Scoring Model) & SRC-03 (Official ICF Sample Questions Rationale)"
    }
]

def render_assistant_page(t):
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-primary">🤖 {t('Trí Tuệ Tỉnh Thức — Dẫn Nguồn Kiểm Chứng', 'Socratic Study Guide — Verified Citations')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Trợ Lý Học Tập Tỉnh Thức (Socratic Study Assistant)', 'ICF Socratic Study Assistant')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Trợ lý học tập được xây dựng trên nền tảng 7 tài liệu gốc đã kiểm chứng từ ICF. Mọi giải đáp đều có căn cứ chuẩn mực, dẫn chứng điều khoản và làm rõ tư duy phán đoán tình huống.',
               'A dedicated study companion grounded strictly in the 7 verified ICF source documents. Every insight is paired with explicit ethical standards and situational judgment rationales.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"#### 💡 {t('Các Chủ Đề Thắc Mắc Phổ Biến:', 'Frequently Explored Inquiries:')}")
    cols = st.columns(len(VERIFIED_KNOWLEDGE_BASE))
    for i, item in enumerate(VERIFIED_KNOWLEDGE_BASE):
        with cols[i % len(cols)]:
            if st.button(f"📌 {item['question'][:32]}...", key=f"btn_ask_preset_{i}", use_container_width=True):
                st.session_state["active_assistant_query"] = item["question"]

    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 16px 0;'/>", unsafe_allow_html=True)

    # Search / Query Input
    user_query = st.text_input(
        "🔍 " + t("Nhập câu hỏi hoặc từ khóa bạn muốn giải đáp chuẩn mực:", "Enter your question or keyword to explore:"),
        value=st.session_state.get("active_assistant_query", ""),
        placeholder=t("Ví dụ: ranh giới chuyển tuyến, đạo đức 2025, suy diễn áp đặt, nguyên lý chọn Best/Worst...",
                      "e.g., referral boundaries, ethics 2025, coach projection, best/worst principles...")
    )

    if user_query.strip():
        # Search in knowledge base
        q_lower = user_query.lower()
        matched_items = []
        for item in VERIFIED_KNOWLEDGE_BASE:
            match_score = 0
            if any(kw in q_lower for kw in item["keywords"]): match_score += 3
            if any(word in item["question"].lower() for word in q_lower.split()): match_score += 2
            if any(word in item["shortSummary"].lower() for word in q_lower.split()): match_score += 1
            if match_score > 0:
                matched_items.append((match_score, item))

        matched_items.sort(key=lambda x: x[0], reverse=True)

        if matched_items:
            best_match = matched_items[0][1]
            st.markdown(f"""
            <div class="zen-card" style="border-left: 4px solid #8BA888; margin-top: 16px;">
                <span class="zen-badge zen-badge-primary">🏛️ {t('Căn Cứ Kiểm Chứng', 'Verified Grounding')}</span>
                <h3 style="margin: 8px 0; color: #2F3E34;">{best_match['question']}</h3>
                <div style="background: #FAF7F2; padding: 12px 16px; border-radius: 8px; margin-bottom: 14px; font-weight: 500; color: #8C6D53; border-left: 3px solid #8BA888;">
                    💡 <b>{t('Điểm cốt lõi:', 'Key Takeaway:')}</b> {best_match['shortSummary']}
                </div>
                <div style="font-size: 0.95rem; line-height: 1.7; color: #2C3E50;">
                    {best_match['detailedAnswer']}
                </div>
                <div style="margin-top: 16px; font-size: 0.85rem; color: #1E4E79; background: #EBF3FA; padding: 8px 12px; border-radius: 6px;">
                    <b>📌 {t('Dẫn nguồn kiểm chứng:', 'Verified Citation:')}</b> {best_match['sourceCitation']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="zen-card" style="margin-top: 16px;">
                <h4>🌿 {t('Phản Hồi Từ Khung Chuẩn Mực ICF', 'ICF Standards Reflection')}</h4>
                <p style="font-size: 0.92rem; line-height: 1.6; color: #555;">
                    {t('Theo 8 Năng lực Cốt lõi và Bộ Quy tắc Đạo đức ICF, mọi hành động khai vấn đều cần tôn trọng sự tự chủ của khách hàng, duy trì tính bảo mật, và phản chiếu khách quan.',
                       'Under the ICF Core Competencies and Code of Ethics, every coaching action must honor client autonomy, safeguard confidentiality, and maintain objective presence.')}
                </p>
                <div style="font-size: 0.85rem; color: #8C6D53;">
                    {t('Gợi ý: Hãy thử chọn một trong các câu hỏi gợi ý bên trên hoặc nhập từ khóa liên quan đến đạo đức, năng lực, hoặc tình huống.',
                       'Tip: Try clicking one of the preset inquiries above or enter keywords related to ethics, competencies, or situational dilemmas.')}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info(t("Hãy bấm vào một trong các câu hỏi gợi ý bên trên hoặc nhập từ khóa để tra cứu câu trả lời chuẩn mực có dẫn nguồn!",
                  "Click any suggested question above or type your inquiry to explore verified standards with citations!"))
