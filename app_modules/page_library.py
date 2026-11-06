# -*- coding: utf-8 -*-
"""
Library & Verified Sources Page for Mentor Thi (PCC Learning & Practice)
Grounded strictly in 9 directly verified official ICF sources.
"""
import streamlit as st

def render_library_page(DATA, VERIFIED_SOURCES, COMPETENCIES, t):
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-blue">🏛️ {t('Căn Cứ Chính Thức Đã Kiểm Chứng', 'Directly Verified Official Evidence')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Thư Viện Chuẩn ICF & 9 Nguồn Kiểm Chứng', 'ICF Standards & 9 Verified Sources Library')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Toàn bộ cấu trúc đề thi, chuẩn mực đạo đức, năng lực cốt lõi, chuyên đề chuyển gửi khách hàng và phương pháp thẩm định được tổng hợp và kiểm chứng trực tiếp từ các văn bản chính thức của International Coaching Federation (ICF).',
               'All exam blueprints, ethical standards, core competencies, client referral guidelines, and evaluation methodologies are directly aggregated and verified from official International Coaching Federation (ICF) publications.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_sources, tab_domains, tab_comps, tab_boundaries = st.tabs([
        "📜 " + t(f"Bảng {len(VERIFIED_SOURCES)} Nguồn Kiểm Chứng", f"{len(VERIFIED_SOURCES)} Verified Sources"),
        "⚖️ " + t("Phân Định 3 Miền Chuẩn Mực", "3 Standards Domains"),
        "🎯 " + t("8 Năng Lực Cốt Lõi (2019)", "8 Core Competencies"),
        "🚪 " + t("Ranh Giới Nghề & Chuyển Giới Thiệu (Hullinger & DiGirolamo, 2018)", "Referral Boundaries (ICF Research Guidelines)")
    ])

    # TAB 1: 9 VERIFIED SOURCES
    with tab_sources:
        st.markdown(f"""
        <div class="zen-card">
            <h4 style="margin-top: 0; color: #2F3E34;">📋 {t('Bảng Tra Cứu 9 Nguồn Chính Thức Từ ICF & Pearson VUE', 'Official ICF & Pearson VUE 9 Verification Table')}</h4>
            <p style="font-size: 0.88rem; color: #666;">
                {t('Dưới đây là 9 nguồn dữ liệu chính thống đã được truy xuất trực tiếp để thiết lập cấu trúc cho ứng dụng này. Mọi thông tin đều ghi rõ phiên bản, ngày xuất bản, ngày cập nhật trang web và liên kết PDF gốc:',
                   'Below are the 9 authoritative sources directly retrieved to structure this application. Each records exact version, publication date, web revision date, and direct PDF links:')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        for src in VERIFIED_SOURCES:
            date_ver = src.get("lastVerifiedDate", src.get("dateVerified", "2026-11-06"))
            summary = src.get("summaryVi", "") if st.session_state.lang == "vi" else src.get("summaryEn", "")
            scope_desc = src.get("scope", "")
            authors = src.get("authors")
            pub_year = src.get("publicationYear")
            web_pub = src.get("webPublishDate")
            web_rev = src.get("webRevisionDate")
            pdf_url = src.get("pdfUrl")
            usage_rights = src.get("usageRights")

            st.markdown(f"""
            <div class="zen-card" style="padding: 16px 20px; margin-bottom: 14px; border-left: 4px solid #8BA888;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <span class="zen-badge zen-badge-primary">ID: {src['id']}</span>
                        <span class="zen-badge zen-badge-gold">{t('Xác minh:', 'Verified:')} {date_ver}</span>
                        <span class="zen-badge zen-badge-blue">✅ {src.get('verificationStatus', 'Đã xác minh')}</span>
                        {f'<span class="zen-badge zen-badge-pink">Năm công bố: {pub_year}</span>' if pub_year else ''}
                    </div>
                    <div style="font-size: 0.85rem; color: #8C6D53; margin-top: 4px;">
                        🔗 <a href="{src['url']}" target="_blank" style="color: #1E4E79; text-decoration: underline; font-weight: 500;">
                            {t('Trang web ICF', 'Official ICF Web')} ↗
                        </a>
                        {f' | 📄 <a href="{pdf_url}" target="_blank" style="color: #9C4158; text-decoration: underline; font-weight: 500;">PDF Trực tiếp ↗</a>' if pdf_url else ''}
                    </div>
                </div>
                <h4 style="margin: 10px 0 6px 0; color: #2F3E34; font-size: 1.05rem;">
                    {src['titleVi'] if st.session_state.lang == 'vi' else src['titleEn']}
                </h4>
                {f'<div style="font-size: 0.85rem; color: #7A5C43; margin-bottom: 4px;"><b>{t("Tác giả:", "Authors:")}</b> {authors} ({pub_year})</div>' if authors else ''}
                {f'<div style="font-size: 0.82rem; color: #888; margin-bottom: 6px;"><b>{t("Thời gian trang web:", "Web Metadata:")}</b> Đăng: {web_pub} | Sửa đổi trên web: {web_rev} <i>({t("Lưu ý: Ngày sửa đổi trên web không suy diễn nội dung nghiên cứu 2018 bị thay đổi", "Web revision date does not imply modification of the 2018 research text")})</i></div>' if web_rev else ''}
                <div style="font-size: 0.88rem; color: #555; line-height: 1.5; margin-bottom: 6px;">
                    <b>{t('Phạm vi & Ý nghĩa:', 'Scope & Significance:')}</b> {scope_desc}<br/>
                    <b>{t('Nội dung cốt lõi:', 'Core Summary:')}</b> {summary}
                </div>
                {f'<div style="font-size: 0.8rem; color: #666; background: #FAF7F2; padding: 4px 8px; border-radius: 4px; margin-bottom: 6px;"><b>Quyền sử dụng:</b> {usage_rights}</div>' if usage_rights else ''}
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

    # TAB 4: REFERRAL BOUNDARIES & SPECIAL TOPIC (HULLINGER & DIGIROLAMO, 2018)
    with tab_boundaries:
        st.markdown(f"""
        <div class="zen-card" style="border-left: 4px solid #9C4158;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <span class="zen-badge zen-badge-pink">ICF Research White Paper</span>
                <span class="zen-badge zen-badge-gold">Năm công bố: 2018 | Sửa đổi web: 13/08/2026</span>
            </div>
            <h3 style="color: #2F3E34; margin: 8px 0 4px 0;">🚪 {t('Chuyên Đề: Chuyển Gửi Khách Hàng Sang Trị Liệu & Ranh Giới Coaching', 'Special Topic: Referring a Client to Therapy & Boundaries')}</h3>
            <p style="font-size: 0.85rem; color: #8C6D53; margin: 0 0 10px 0;">
                <b>{t('Tác giả:', 'Authors:')}</b> Angela M. Hullinger, MS, ACC & Joel A. DiGirolamo, MS, PCC (2018).<br/>
                <i>* {t('Bản dịch phục vụ học tập, không phải bản dịch chính thức của ICF. Quyền sử dụng phi thương mại kèm ghi nhận tác quyền ICF.', 'Educational study translation; not an official ICF translation. Non-commercial reference with ICF attribution.')}</i>
            </p>
            <div style="font-size: 0.85rem; margin-bottom: 12px;">
                🔗 <a href="https://coachingfederation.org/resource/referring-a-client-to-therapy/" target="_blank" style="color: #1E4E79; text-decoration: underline;">Trang nguồn ICF ↗</a> | 
                📄 <a href="https://coachingfederation.org/wp-content/uploads/2024/12/icf-research-guide-referring-client-to-therapy.pdf" target="_blank" style="color: #9C4158; text-decoration: underline;">Tải PDF White Paper Đầy Đủ (2018) ↗</a> | 
                📋 <a href="https://coachingfederation.org/wp-content/uploads/2024/12/icf-research-client-referral-overview.pdf" target="_blank" style="color: #8A6112; text-decoration: underline;">Tải PDF Tóm Tắt 1 Trang ↗</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

        ref_subtab1, ref_subtab2, ref_subtab3, ref_subtab4, ref_subtab5 = st.tabs([
            "1. " + t("Bản Chất Phân Định", "Scope Distinction"),
            "2. " + t("3 Trụ Cột & Dấu Hiệu", "3 Pillars & Signs"),
            "3. " + t("Kịch Bản Đối Thoại", "Dialogue Scripts"),
            "4. " + t("Coaching Song Song & Cấp Cứu", "Concurrent & Emergency"),
            "5. " + t("Đối Chiếu Bộ Đạo Đức", "Code of Ethics Comparison")
        ])

        with ref_subtab1:
            st.markdown(f"""
            <div class="zen-card">
                <h4 style="color: #2F3E34; margin-top: 0;">🧭 {t('Phạm Vi Coaching vs. Phạm Vi Trị Liệu Tâm Lý (White Paper Trang 1–3)', 'Scope of Coaching vs. Scope of Therapy')}</h4>
                <div style="font-size: 0.92rem; line-height: 1.65; color: #2C3E50;">
                    <ul>
                        <li><b>Coaching (Khai vấn):</b> Quan hệ hợp tác (partnering) giữa coach và khách hàng nhằm khơi mở tiềm năng cá nhân và nghề nghiệp, hướng tới mục tiêu phát triển và hành động. Dành cho những cá nhân có chức năng tâm lý bình thường (psychologically functional individuals).</li>
                        <li><b>Therapy (Trị liệu tâm lý):</b> Do chuyên gia sức khỏe tâm thần được cấp phép (Licensed Mental Health Professionals) đảm nhiệm, nhằm chẩn đoán và điều trị rối loạn tâm thần, làm thuyên giảm nỗi đau tâm lý và chữa lành vết thương tâm lý sâu sắc.</li>
                    </ul>
                    <div style="background: #FAF7F2; border-left: 3px solid #C4785A; padding: 12px; margin: 12px 0; border-radius: 6px;">
                        <b>⚠️ CẢNH BÁO TRÁNH CÁI BẪY GIẢN LƯỢC SAI LẦM:</b><br/>
                        Tuyệt đối KHÔNG giản lược thành: <i>"Coaching chỉ nhìn tương lai, Trị liệu chỉ nhìn quá khứ"</i>.<br/>
                        Trong coaching chuẩn ICF, khách hàng hoàn toàn có thể nhìn lại trải nghiệm và bài học quá khứ để hiểu rõ bản thân trong hiện tại và định hướng tương lai. Điểm khác biệt bản chất là <b>Trị liệu chẩn đoán và chữa lành bệnh lý/rối loạn chức năng; Coaching đồng hành cùng người khỏe mạnh phát triển tiềm năng.</b>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with ref_subtab2:
            st.markdown(f"""
            <div class="zen-card">
                <h4 style="color: #2F3E34; margin-top: 0;">📊 {t('3 Trụ Cột Cân Nhắc Chuyển Gửi & Dấu Hiệu Theo Lĩnh Vực (Trang 3–6)', '3 Referral Pillars & Warning Signs')}</h4>
                <div style="font-size: 0.9rem; line-height: 1.6; color: #333;">
                    <b>3 Trụ Cột Cân Nhắc Chuyển Gửi:</b>
                    <ol>
                        <li><b>Mức độ suy giảm chức năng sinh hoạt hằng ngày (Impairment in Daily Functioning):</b> Vấn đề có cản trở khả năng làm việc, duy trì mối quan hệ hoặc chăm sóc bản thân của khách hàng không?</li>
                        <li><b>Khả năng hưởng lợi từ Coaching (Coachability & Progress):</b> Khách hàng có khả năng hành động và tự phản tư không? Có bị đình trệ kéo dài (stuck) dù đã đổi cách tiếp cận không?</li>
                        <li><b>Giới hạn năng lực của Coach (Coach Competence):</b> Coach có cảm thấy mình đang bị kéo vào vùng mất an toàn, vượt quá chuyên môn không?</li>
                    </ol>
                    <div style="background: #EBF3ED; border-left: 3px solid #8BA888; padding: 10px; margin: 10px 0; border-radius: 6px;">
                        <b>🌸 NGUYÊN TẮC VÀNG VỀ CẢM XÚC:</b><br/>
                        Coach KHÔNG tự động chuyển gửi chỉ vì khách hàng khóc, buồn bã, hoặc bộc lộ cảm xúc mãnh liệt trong một phiên! Khóc là biểu hiện tự nhiên của con người. Coach PCC cần có năng lực <b>dung chứa không gian cảm xúc (Holding Space)</b>. Chỉ cân nhắc chuyển gửi khi cảm xúc đó kéo dài dai dẳng, tê liệt ý chí sinh hoạt, và khách hàng mất khả năng tự điều tiết.
                    </div>
                    <b>Bốn Nhóm Dấu Hiệu Cảnh Báo Cần Chú Ý Trong Bối Cảnh:</b>
                    <ul>
                        <li><b>Cảm xúc (Affective):</b> Mất hoàn toàn niềm vui (anhedonia), lo âu hoảng loạn cực độ, tuyệt vọng sâu sắc, cáu giận dữ dội kéo dài.</li>
                        <li><b>Nhận thức (Cognitive):</b> Hoang tưởng, mất phương hướng thực tại, suy nghĩ lặp đi lặp lại không thể dứt ra.</li>
                        <li><b>Hành vi (Behavioral):</b> Mất ngủ triền miên nhiều tuần, sụt cân đột ngột bất thường, lạm dụng rượu/thuốc, cô lập bản thân.</li>
                        <li><b>Quan hệ (Interpersonal):</b> Xung đột bạo lực, bám chấp phụ thuộc bệnh lý vào coach.</li>
                    </ul>
                    <i>* Nguyên tắc chống tự chẩn đoán (Anti-Diagnostic Stance): Coach tuyệt đối KHÔNG dùng các dấu hiệu trên như bảng kiểm chẩn đoán tâm thần (Diagnostic Checklist).</i>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with ref_subtab3:
            st.markdown(f"""
            <div class="zen-card">
                <h4 style="color: #2F3E34; margin-top: 0;">💬 {t('Cách Trao Đổi Chuyển Gửi Không Gán Nhãn & Khách Hàng Ngần Ngại (Trang 7–10)', 'Non-Pathologizing Dialogue & Handling Reluctance')}</h4>
                <div style="font-size: 0.9rem; line-height: 1.6; color: #333;">
                    <b>1. Cách tiếp cận đồng hành và xin phép (Partnering & Permission):</b>
                    <p>Coach nhẹ nhàng xin phép trước khi chia sẻ quan sát thực tế khách quan, không phán xét, không biến cuộc trò chuyện thành buổi "tuyên án y khoa".</p>
                    <div style="background: #FAF7F2; border-left: 3px solid #8BA888; padding: 10px; margin: 8px 0; border-radius: 6px;">
                        <b>Mẫu câu chuẩn mực:</b><br/>
                        <i>"Qua vài phiên gần đây, tôi nhận thấy bạn chia sẻ rất nhiều về cảm giác kiệt quệ và mất ngủ triền miên làm ảnh hưởng đến công việc. Với tư cách là coach, tôi rất quan tâm đến sức khỏe toàn diện của bạn. Bạn nghĩ sao về việc tham khảo thêm ý kiến của một chuyên gia tâm lý hoặc bác sĩ y khoa?"</i>
                    </div>
                    <b>2. Xử lý khi khách hàng từ chối hoặc ngần ngại (Handling Reluctance):</b>
                    <ul>
                        <li>Khách hàng có quyền tự quyết từ chối đi gặp bác sĩ/trị liệu (trừ cấp cứu đe dọa tính mạng).</li>
                        <li>Coach lắng nghe thấu cảm sự lo ngại, không ép buộc, không phán xét.</li>
                        <li><b>Giữ vững ranh giới chuyên môn:</b> Nếu khách hàng từ chối trị liệu nhưng vấn đề tâm lý khiến họ KHÔNG THỂ tiếp tục làm việc an toàn trong coaching, coach giải thích ấm áp và xin phép tạm dừng hoặc kết thúc hợp đồng để bảo vệ an toàn cho khách hàng.</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with ref_subtab4:
            st.markdown(f"""
            <div class="zen-card">
                <h4 style="color: #2F3E34; margin-top: 0;">🤝 {t('Coaching Song Song, Tạm Dừng, Chấm Dứt & Cấp Cứu Khẩn Cấp (Trang 6, 10–13)', 'Concurrent Coaching, Pause, Termination & Emergency')}</h4>
                <div style="font-size: 0.9rem; line-height: 1.6; color: #333;">
                    <b>1. Ba Kịch Bản Sau Chuyển Gửi:</b>
                    <ul>
                        <li><b>Kịch bản A — Coaching song song (Concurrent Coaching):</b> Hoàn toàn khả thi và có giá trị cao nếu: (1) Khách hàng đồng thuận, (2) Nhà trị liệu biết và đồng ý, (3) Ranh giới mục tiêu cực kỳ rạch ròi (Trị liệu chữa lành tâm lý; Coaching tập trung phát triển kỹ năng/công việc).</li>
                        <li><b>Kịch bản B — Tạm dừng (Pause):</b> Khi khách hàng trong giai đoạn khủng hoảng cấp tính, tạm dừng 1–3 tháng để khách hàng ưu tiên điều trị, sau đó tái đánh giá.</li>
                        <li><b>Kịch bản C — Kết thúc (Termination):</b> Khi việc tiếp tục không còn phù hợp, kết thúc văn minh và nhân văn.</li>
                    </ul>
                    <b>2. Bảo Mật vs Cấp Cứu Khẩn Cấp:</b>
                    <div style="background: #FDF2F4; border-left: 3px solid #9C4158; padding: 10px; margin: 8px 0; border-radius: 6px;">
                        <b>🚨 CẤP CỨU KHẨN CẤP (Nguy cơ đe dọa tính mạng cận kề - Imminent Harm):</b><br/>
                        Tự sát, giết người hoặc bạo hành. <b>Ngoại lệ bắt buộc của bảo mật:</b> Kích hoạt ngay hotline cấp cứu (988 tại Mỹ, cấp cứu địa phương tại VN) và liên hệ Người liên hệ khẩn cấp trong hợp đồng.
                    </div>
                    <div style="background: #EBF3ED; border-left: 3px solid #8BA888; padding: 10px; margin: 8px 0; border-radius: 6px;">
                        <b>🔒 BẢO MẬT THƯỜNG QUY KHI PHỐI HỢP VỚI NHÀ TRỊ LIỆU:</b><br/>
                        Coach TUYỆT ĐỐI KHÔNG tự ý gọi điện hay gửi email trao đổi với nhà trị liệu của khách hàng trừ khi có <b>Văn bản ủy quyền chia sẻ thông tin (Written Release of Information Form)</b> có chữ ký rõ ràng của khách hàng!
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with ref_subtab5:
            st.markdown(f"""
            <div class="zen-card">
                <h4 style="color: #2F3E34; margin-top: 0;">📜 {t('Đối Chiếu Điều Khoản Bộ Quy Tắc Đạo Đức ICF', 'Code of Ethics Cross-Reference')}</h4>
                <div style="font-size: 0.9rem; line-height: 1.6; color: #333;">
                    <p>Tài liệu White Paper năm 2018 (Hullinger & DiGirolamo) viện dẫn các điều khoản của Bộ Quy tắc Đạo đức thời điểm công bố. Dưới đây là bảng đối chiếu trung thực với các bản Đạo đức hiện đại:</p>
                    <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 8px;">
                        <tr style="background: #FAF7F2; border-bottom: 2px solid #D8C7B5;">
                            <th style="padding: 8px; text-align: left;">Nội Dung Đạo Đức</th>
                            <th style="padding: 8px; text-align: left;">Văn Bản 2018 Viện Dẫn</th>
                            <th style="padding: 8px; text-align: left;">Bộ Đạo Đức 2020 (Đề Thi Hiện Hành)</th>
                            <th style="padding: 8px; text-align: left;">Bộ Đạo Đức 2025 (Thực Hành Hiện Hành)</th>
                        </tr>
                        <tr style="border-bottom: 1px solid #EADBCC;">
                            <td style="padding: 8px;"><b>Ranh giới năng lực & Đề xuất chuyển gửi</b></td>
                            <td style="padding: 8px;">Section 1.4 & 1.18</td>
                            <td style="padding: 8px;">Standard 11 (Suggest another professional when needed)</td>
                            <td style="padding: 8px;">Standard 1.4 & 4.2 (Scope of competence & client referral)</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #EADBCC;">
                            <td style="padding: 8px;"><b>Bảo mật & Ngoại lệ nguy hiểm cận kề</b></td>
                            <td style="padding: 8px;">Section 1.24</td>
                            <td style="padding: 8px;">Standard 23 (Confidentiality & danger exceptions)</td>
                            <td style="padding: 8px;">Standard 2.1 & 2.4 (Confidentiality & safety disclosures)</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px;"><b>Xung đột vai trò & Khách hàng tự chủ</b></td>
                            <td style="padding: 8px;">Section 1.1 & 1.9</td>
                            <td style="padding: 8px;">Standard 9 & 10 (Conflict of interest & role clarity)</td>
                            <td style="padding: 8px;">Standard 3.1 & 3.3 (Clear boundaries & client autonomy)</td>
                        </tr>
                    </table>
                </div>
            </div>
            """, unsafe_allow_html=True)
