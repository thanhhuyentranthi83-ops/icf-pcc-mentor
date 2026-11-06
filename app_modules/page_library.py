# -*- coding: utf-8 -*-
"""
Library & Verified Sources Page for PCC Learning & Practice
"""
import streamlit as st

def render_library_page(DATA, VERIFIED_SOURCES, COMPETENCIES, t):
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-blue">🏛️ {t('Căn Cứ Chính Thức Đã Kiểm Chứng', 'Directly Verified Official Evidence')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Thư Viện Chuẩn ICF & Nguồn Kiểm Chứng', 'ICF Standards & Verified Sources Library')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Toàn bộ cấu trúc đề thi, chuẩn mực đạo đức, năng lực cốt lõi và phương pháp thẩm định được tổng hợp và kiểm chứng trực tiếp từ các văn bản chính thức của International Coaching Federation (ICF).',
               'All exam blueprints, ethical standards, core competencies, and evaluation methodologies are directly aggregated and verified from official International Coaching Federation (ICF) publications.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_sources, tab_domains, tab_comps, tab_boundaries = st.tabs([
        "📜 " + t("Bảng 7 Nguồn Kiểm Chứng", "7 Verified Sources"),
        "⚖️ " + t("Phân Định 3 Miền Chuẩn Mực", "3 Standards Domains"),
        "🎯 " + t("8 Năng Lực Cốt Lõi (2019)", "8 Core Competencies"),
        "🚪 " + t("Ranh Giới Nghề & Chuyển Giới Thiệu", "Referral Boundaries")
    ])

    # TAB 1: 7 VERIFIED SOURCES
    with tab_sources:
        st.markdown(f"""
        <div class="zen-card">
            <h4 style="margin-top: 0; color: #2F3E34;">📋 {t('Bảng Tra Cứu Nguồn Chính Thức Từ ICF & Pearson VUE', 'Official ICF & Pearson VUE Verification Table')}</h4>
            <p style="font-size: 0.88rem; color: #666;">
                {t('Dưới đây là 7 nguồn dữ liệu chính thống đã được truy xuất trực tiếp để thiết lập cấu trúc cho ứng dụng này:',
                   'Below are the 7 authoritative sources directly retrieved to structure this application:')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        for src in VERIFIED_SOURCES:
            st.markdown(f"""
            <div class="zen-card" style="padding: 16px 20px; margin-bottom: 14px; border-left: 4px solid #8BA888;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <span class="zen-badge zen-badge-primary">ID: {src['id']}</span>
                        <span class="zen-badge zen-badge-gold">Kiểm chứng: {src['dateVerified']}</span>
                        <span class="zen-badge zen-badge-blue">✅ {src['verificationStatus']}</span>
                    </div>
                    <div style="font-size: 0.85rem; color: #8C6D53; margin-top: 4px;">
                        🔗 <a href="{src['url']}" target="_blank" style="color: #1E4E79; text-decoration: underline; font-weight: 500;">
                            {t('Truy cập nguồn gốc ICF', 'Visit Official Source')} ↗
                        </a>
                    </div>
                </div>
                <h4 style="margin: 10px 0 6px 0; color: #2F3E34; font-size: 1.05rem;">
                    {src['titleVi'] if st.session_state.lang == 'vi' else src['titleEn']}
                </h4>
                <div style="font-size: 0.88rem; color: #555; line-height: 1.5; margin-bottom: 6px;">
                    <b>{t('Mục đích & Ý nghĩa:', 'Scope & Significance:')}</b><br/>
                    {src['purposeVi'] if st.session_state.lang == 'vi' else src['purposeEn']}
                </div>
                <div style="font-size: 0.82rem; color: #777; background: #FAF7F2; padding: 6px 10px; border-radius: 6px; word-break: break-all;">
                    <b>URL:</b> {src['url']}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="zen-quote-box">
            <b>💡 {t('Lưu ý về hình thức thi Pearson VUE:', 'Pearson VUE Delivery Notes:')}</b><br/>
            {t('Kỳ thi ICF Credentialing Exam được tổ chức tại các trung tâm khảo thí Pearson VUE ủy quyền hoặc trực tuyến qua OnVUE. Thí sinh có 30 ngày kể từ khi nhận lời mời để đặt lịch thi. Bài thi trên máy tính có chức năng Flag (đánh dấu) và đồng hồ đếm ngược chính xác.',
               'The ICF Credentialing Exam is administered at authorized Pearson VUE test centers or online via OnVUE. Candidates have 30 days from invitation to schedule. The computer-based test interface features Flag for review and an onscreen countdown timer.')}
        </div>
        """, unsafe_allow_html=True)

    # TAB 2: 3 STANDARDS DOMAINS
    with tab_domains:
        st.markdown(f"""
        <div class="zen-card">
            <h3 style="color: #2F3E34; margin-top: 0;">🧭 {t('Phân Định Rõ Ràng 3 Miền Chuẩn Mực ICF', 'Distinct Delineation of 3 ICF Standards Domains')}</h3>
            <p style="font-size: 0.92rem; color: #555; line-height: 1.6;">
                {t('Một trong những nhầm lẫn phổ biến nhất của thí sinh ôn thi PCC là đánh đồng Bộ chỉ báo hành vi (PCC Markers) với Đề thi trắc nghiệm tình huống (SJT), hoặc nhầm lẫn giữa bản Đạo đức thực hành với đề thi.',
                   'One of the most frequent misconceptions among PCC candidates is conflating audio PCC Markers with written Situational Judgment Tests (SJT), or confusing practice ethics with exam baselines.')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div class="zen-card" style="height: 100%; border-top: 4px solid #9C4158;">
                <span class="zen-badge zen-badge-pink">Miền 1</span>
                <h4 style="color: #2F3E34; margin: 8px 0;">{t('Bộ Quy Tắc Đạo Đức', 'ICF Code of Ethics')}</h4>
                <div style="font-size: 0.85rem; color: #555; line-height: 1.5;">
                    <b>📅 {t('Bản thực hành hiện hành:', 'Current Practice Edition:')}</b><br/>
                    {t('Bản 2025 (Hiệu lực từ 01/04/2025). Đã cập nhật định nghĩa coaching, xung đột lợi ích và hướng dẫn ứng dụng công nghệ/AI.',
                       '2025 Code (Effective April 1, 2025). Updates coaching definition, conflicts of interest, and AI/tech guidance.')}<br/><br/>
                    <b>📝 {t('Đề thi viết hiện hành:', 'Current Written Exam:')}</b><br/>
                    {t('Dùng bản 2020 cho đến trước khi kỳ thi cập nhật chính thức áp dụng.',
                       'Uses 2020 Code baseline until updated exam takes effect.')}<br/><br/>
                    <b>🚀 {t('Đề thi cập nhật:', 'Updated Exam (Nov 2026):')}</b><br/>
                    {t('Tích hợp đầy đủ bản 2025.', 'Fully integrates 2025 revisions.')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="zen-card" style="height: 100%; border-top: 4px solid #8BA888;">
                <span class="zen-badge zen-badge-primary">Miền 2</span>
                <h4 style="color: #2F3E34; margin: 8px 0;">{t('8 Năng Lực Cốt Lõi (2019)', '8 Core Competencies')}</h4>
                <div style="font-size: 0.85rem; color: #555; line-height: 1.5;">
                    <b>🎯 {t('Vai trò:', 'Role:')}</b><br/>
                    {t('Khung tư duy năng lực nền tảng cho TẤT CẢ các cấp chứng chỉ ICF (ACC, PCC, MCC) và mọi định dạng bài thi.',
                       'Foundational competency framework underpinning ALL ICF credentials (ACC, PCC, MCC) across all exam formats.')}<br/><br/>
                    <b>🧱 {t('Cấu trúc 4 Trụ cột:', '4 Pillars Structure:')}</b><br/>
                    1. Foundation (Đạo đức & Tư duy)<br/>
                    2. Co-Creating Relationship (Hợp đồng & Tin cậy)<br/>
                    3. Communicating Effectively (Hiện diện & Lắng nghe)<br/>
                    4. Cultivating Learning & Growth (Khơi gợi & Phát triển)
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="zen-card" style="height: 100%; border-top: 4px solid #8A6112;">
                <span class="zen-badge zen-badge-gold">Miền 3</span>
                <h4 style="color: #2F3E34; margin: 8px 0;">{t('PCC Markers (37 Chỉ Báo)', 'PCC Markers (37 Indicators)')}</h4>
                <div style="font-size: 0.85rem; color: #555; line-height: 1.5;">
                    <b>🎙️ {t('Mục đích độc quyền:', 'Exclusive Purpose:')}</b><br/>
                    {t('Dùng để thẩm định bằng chứng hành vi thính giác trong các bản ghi âm phiên coach thực tế (Performance Evaluation).',
                       'Designed exclusively to assess auditory behavioral evidence in recorded performance evaluation sessions.')}<br/><br/>
                    <b>⚠️ {t('Cảnh báo quan trọng:', 'Crucial Distinction:')}</b><br/>
                    {t('PCC Markers KHÔNG PHẢI là công thức rập khuôn cơ học cho bài thi trắc nghiệm tình huống (SJT). Bài thi viết đo lường năng lực phán đoán tình huống đạo đức và tính tự chủ của khách hàng.',
                       'PCC Markers are NOT a mechanical scoring formula for written SJTs. The written exam tests contextual situational judgment and client autonomy.')}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # TAB 3: 8 CORE COMPETENCIES
    with tab_comps:
        st.markdown(f"### {t('Tra Cứu Nhanh 8 Năng Lực Cốt Lõi ICF (2019)', 'ICF Core Competencies Quick Reference')}")
        for comp in COMPETENCIES:
            with st.expander(f"{comp['code']}: {comp['nameVi'] if st.session_state.lang == 'vi' else comp['nameEn']}"):
                st.markdown(f"""
                <div style="font-size: 0.92rem; line-height: 1.6;">
                    <p><b>{t('Mô tả chuẩn:', 'Definition:')}</b> {comp['descVi'] if st.session_state.lang == 'vi' else comp['descEn']}</p>
                    <p style="color: #8C6D53;"><b>💡 {t('Trọng tâm phán đoán trong đề thi:', 'Exam Judgment Focus:')}</b><br/>
                    {t('Coach phải luôn tôn trọng sự tự chủ của khách hàng, không áp đặt giải pháp, không suy diễn võ đoán, và giữ vững ranh giới đạo đức nghề nghiệp.',
                       'The coach must consistently honor client autonomy, avoid imposing solutions or unsolicited interpretations, and safeguard professional ethical boundaries.')}
                    </p>
                </div>
                """, unsafe_allow_html=True)

    # TAB 4: REFERRAL BOUNDARIES
    with tab_boundaries:
        st.markdown(f"""
        <div class="zen-card">
            <h3 style="color: #2F3E34; margin-top: 0;">🚪 {t('Ranh Giới Nghề Nghiệp & Chuyển Giới Thiệu Khách Hàng', 'Professional Boundaries & Client Referral')}</h3>
            <p style="font-size: 0.92rem; color: #555; line-height: 1.6;">
                {t('Theo Chuẩn mực Đạo đức ICF và Nguyên tắc Vàng của PCC: Coaching không phải là Trị liệu (Therapy), Tư vấn chuyên gia (Consulting), Khai vấn cố vấn (Mentoring) hay Đào tạo (Training). Khi khách hàng có dấu hiệu vượt ngoài phạm vi huấn luyện, coach có trách nhiệm đạo đức chuyển giao khách hàng.',
                   'Under the ICF Code of Ethics and PCC standards: Coaching is not Therapy, Consulting, Mentoring, or Training. When client needs exceed the coaching scope, the coach has an ethical duty to refer.')}
            </p>
            <div style="background: #FAF7F2; padding: 14px; border-radius: 8px; margin-top: 10px;">
                <b>🚨 {t('Các dấu hiệu phải dừng coaching và chuyển tuyến chuyên gia:', 'Signs Requiring Immediate Professional Referral:')}</b>
                <ul style="margin: 8px 0 0 20px; font-size: 0.9rem; color: #444;">
                    <li>{t('Khách hàng có ý định tự hại, trầm cảm nặng hoặc mất khả năng điều tiết cảm xúc sinh hoạt thường nhật.', 'Severe emotional distress, depression, or indications of self-harm.')}</li>
                    <li>{t('Vấn đề gốc rễ nằm ở chấn thương tâm lý quá khứ (trauma) cần can thiệp tâm lý trị liệu chuyên sâu.', 'Root causes rooted in past psychological trauma requiring clinical therapy.')}</li>
                    <li>{t('Khách hàng phụ thuộc hoàn toàn vào coach để đưa ra quyết định thay vì tự chủ.', 'Unhealthy dependency where client seeks direct advice rather than exploring autonomy.')}</li>
                    <li>{t('Xuất hiện hành vi vi phạm pháp luật hoặc xung đột lợi ích nghiêm trọng không thể khắc phục.', 'Unlawful conduct or unresolvable ethical conflicts of interest.')}</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
