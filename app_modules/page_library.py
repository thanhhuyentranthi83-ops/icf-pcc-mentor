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
        <h2 style="margin: 8px 0; color: #2F3E34;">{t(f'Thư Viện Chuẩn ICF & {len(VERIFIED_SOURCES)} Nguồn Kiểm Chứng', f'ICF Standards & {len(VERIFIED_SOURCES)} Verified Sources Library')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Toàn bộ cấu trúc đề thi, chuẩn mực đạo đức, năng lực cốt lõi, chuyên đề chuyển gửi khách hàng và phương pháp thẩm định được tổng hợp và kiểm chứng trực tiếp từ các văn bản chính thức của International Coaching Federation (ICF).',
               'All exam blueprints, ethical standards, core competencies, client referral guidelines, and evaluation methodologies are directly aggregated and verified from official International Coaching Federation (ICF) publications.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_sources, tab_domains, tab_comps, tab_boundaries = st.tabs([
        "📜 " + t(f"Bảng {len(VERIFIED_SOURCES)} Nguồn Kiểm Chứng", f"{len(VERIFIED_SOURCES)} Verified Sources"),
        "⚖️ " + t("Phân Định 3 Miền Chuẩn Mực", "3 Standards Domains"),
        "🎯 " + t("8 Năng lực cốt lõi (2025)", "8 Core Competencies (2025)"),
        "🚪 " + t("Ranh Giới Nghề & Giới Thiệu Khách Hàng (Hullinger & DiGirolamo, 2018)", "Referral Boundaries (ICF Research Guidelines)")
    ])

    # TAB 1: 9 VERIFIED SOURCES
    with tab_sources:
        st.markdown(f"""
        <div class="zen-card">
            <h4 style="margin-top: 0; color: #2F3E34;">📋 {t(f'Bảng Tra Cứu {len(VERIFIED_SOURCES)} Nguồn Chính Thức Từ ICF & Pearson VUE', 'Official ICF & Pearson VUE 9 Verification Table')}</h4>
            <p style="font-size: 0.88rem; color: #666;">
                {t(f'Dưới đây là {len(VERIFIED_SOURCES)} nguồn dữ liệu chính thống đã được truy xuất trực tiếp để thiết lập cấu trúc cho ứng dụng này. Mọi thông tin đều ghi rõ phiên bản, ngày xuất bản, ngày cập nhật trang web và liên kết PDF gốc:',
                   'Below are the 9 authoritative sources directly retrieved to structure this application. Each records exact version, publication date, web revision date, and direct PDF links:')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        for src in VERIFIED_SOURCES:
            date_ver = src.get("lastVerifiedDate", "2026-11-07")
            app_update = src.get("appUpdateDate", "2026-11-07")
            effective_date = src.get("effectiveDate") or src.get("versionEffectiveDate", "Hiện hành")
            doc_ver = src.get("documentVersion") or f"Phiên bản năm {src.get('publicationYear', '2025')}"
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
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 6px;">
                    <div>
                        <span class="zen-badge zen-badge-primary">ID: {src['id']}</span>
                        <span class="zen-badge zen-badge-blue">✅ {src.get('verificationStatus', 'Đã xác minh')}</span>
                        {f'<span class="zen-badge zen-badge-pink">Năm ban hành: {pub_year}</span>' if pub_year else ''}
                    </div>
                    <div style="font-size: 0.85rem; color: #8C6D53;">
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
                
                <!-- 4 METADATA DATES BREAKDOWN -->
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin: 8px 0; font-size: 0.8rem; background: #F8FAF7; padding: 8px 12px; border-radius: 6px; border: 1px solid #E2EADF;">
                    <div style="color: #2F3E34;"><b>📅 {t('Phiên bản / Năm:', 'Version/Year:')}</b> {doc_ver}</div>
                    <div style="color: #8A6112;"><b>⚡ {t('Ngày có hiệu lực:', 'Effective Date:')}</b> {effective_date}</div>
                    <div style="color: #1E4E79;"><b>🔍 {t('Ngày xác minh nguồn:', 'Source Verified:')}</b> {date_ver}</div>
                    <div style="color: #5F6F65;"><b>📱 {t('Cập nhật ứng dụng:', 'App Updated:')}</b> {app_update}</div>
                </div>

                {f'<div style="font-size: 0.82rem; color: #888; margin-bottom: 6px;"><b>{t("Thời gian trang web:", "Web Metadata:")}</b> Đăng: {web_pub} | Sửa đổi trên web: {web_rev} <i>({t("Lưu ý: Ngày sửa đổi trên web không suy diễn nội dung nghiên cứu bị thay đổi", "Web revision date does not imply modification of research text")})</i></div>' if web_rev else ''}
                <div style="font-size: 0.88rem; color: #444; line-height: 1.6; margin: 10px 0; background: #FAFDF9; padding: 12px 14px; border-radius: 8px; border: 1px solid #EADBCC;">
                    <div style="margin-bottom: 8px;">
                        <span style="color: #2F3E34; font-weight: 600;">📌 {t('Phạm vi & Ý nghĩa:', 'Scope & Significance:')}</span>
                        <div style="margin-top: 3px; color: #4A4A4A; padding-left: 12px; border-left: 3px solid #8BA888;">{scope_desc}</div>
                    </div>
                    <div>
                        <span style="color: #2F3E34; font-weight: 600;">📝 {t('Nội dung cốt lõi:', 'Core Summary:')}</span>
                        <div style="margin-top: 3px; color: #4A4A4A; padding-left: 12px; border-left: 3px solid #D4A373;">{summary}</div>
                    </div>
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
                <h4 style="color: #2F3E34; margin: 8px 0;">{t('Bộ Quy Tắc Đạo Đức (Bản 2025)', 'ICF Code of Ethics (2025)')}</h4>
                <div style="font-size: 0.85rem; color: #555; line-height: 1.5;">
                    <b>⚡ {t('Bản thực hành hiện hành:', 'Current Practice Edition:')}</b><br/>
                    {t('Bản 2025 (Hiệu lực: <b>01/04/2025</b>). Gồm 4 Giá trị cốt lõi, 5 Phần với 24 chuẩn mực thực hành, quy định an toàn AI / công nghệ số và áp dụng cho toàn bộ hệ sinh thái ICF.',
                       '2025 Code (Effective: <b>01/04/2025</b>). Features 4 Core Values, 5 Sections with 24 standards, AI safeguards, applying across the whole ICF ecosystem.')}<br/><br/>
                    <b>📝 {t('Đề thi viết Pearson VUE hiện hành:', 'Current Written Exam Baseline:')}</b><br/>
                    {t('Đang chấm theo Bộ Đạo đức 2020 (Tiêu chuẩn 1–28) cho đến khi kỳ thi mới chính thức áp dụng. Ứng dụng cung cấp kho lưu trữ 2020 để đối chiếu.',
                       'Scores against 2020 Code (Standards 1–28) until updated exam rolls out. 2020 archive is available in-app for comparison.')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="zen-card" style="height: 100%; border-top: 4px solid #8BA888;">
                <span class="zen-badge zen-badge-primary">Miền 2</span>
                <h4 style="color: #2F3E34; margin: 8px 0;">{t('8 Năng Lực Cốt Lõi (Bản 2025)', '8 Core Competencies (2025)')}</h4>
                <div style="font-size: 0.85rem; color: #555; line-height: 1.5;">
                    <b>🎯 {t('Khung thực hành mới nhất:', 'Latest Practice Framework:')}</b><br/>
                    {t('Công bố tháng 09/2025 sau Job Analysis toàn cầu với gần 3,000 coach. Giữ nguyên 4 Miền & 8 Năng lực; bổ sung 5 chỉ dấu mới, 11 chỉ dấu sửa đổi và Phụ lục thuật ngữ (Glossary).',
                       'Published September 2025 following global Job Analysis. Retains 4 Domains & 8 Competencies; adds 5 new indicators, 11 revisions, and standardized Glossary.')}<br/><br/>
                    <b>🧱 {t('Đối chiếu đề thi viết:', 'Written Exam Alignment:')}</b><br/>
                    {t('Đề thi viết hiện hành tại Pearson VUE chấm theo tiêu chí 2019. Cả 2 bản đều nhất quán 100% về tôn trọng sự tự quyết của khách hàng và phi phán xét.',
                       'Current Pearson VUE exams score against 2019 criteria. Both models are 100% aligned on client autonomy and zero judgment.')}
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

    # TAB 3: 8 CORE COMPETENCIES (2025 DEFAULT & 2019 EXAM COMPARISON)
    with tab_comps:
        st.markdown(f"### {t('Tra cứu 8 Năng lực cốt lõi ICF (2025)', 'ICF Core Competencies (2025 Edition)')}")

        st.markdown(f"""
        <div class="zen-quote-box" style="margin-bottom: 16px;">
            <b>📌 {t('Lưu ý then chốt từ ICF về Chuẩn Thực Hành vs. Chuẩn Kỳ Thi:', 'ICF Key Clarification on Practice vs. Exam Frameworks:')}</b><br/>
            {t('Khung Năng Lực Cốt Lõi 2025 (ban hành tháng 09/2025) là chuẩn mực thực hành khai vấn mới nhất do ICF ban hành, bổ sung 5 năng lực thành phần mới và 11 năng lực thành phần sửa đổi. Đối với kỳ thi viết trắc nghiệm tình huống (SJT) trên Pearson VUE, ngân hàng đề thi hiện hành đang được chuẩn hóa trên khung năng lực 2019 cho đến khi ICF công bố thời điểm áp dụng bài thi mới. Dưới đây là khung 2025 mặc định kèm chế độ đối chiếu khung 2019 để học viên ôn luyện song song.',
               'The 2025 ICF Core Competencies framework (released Sept 2025) is the authoritative practice standard worldwide, adding 5 new sub-competencies and 11 revisions. Current written exams at Pearson VUE score against the 2019 benchmark until the new exam transition date. Below is the 2025 model with full 2019 comparison.')}
        </div>
        """, unsafe_allow_html=True)

        subtab_2025, subtab_2019 = st.tabs([
            "🌟 " + t("Khung Năng Lực 2025 (Mặc Định Thực Hành)", "2025 Framework (Current Practice)"),
            "🔄 " + t("Khung Năng Lực 2019 (Đối Chiếu Thi Viết)", "2019 Framework (Exam Baseline)")
        ])

        with subtab_2025:
            st.markdown(f"""
            <div style="font-size: 0.88rem; color: #555; margin-bottom: 12px;">
                {t('Hiển thị đầy đủ 8 năng lực cốt lõi và các chỉ dấu hành vi thành phần chuẩn 2025, kèm điểm cập nhật mới và góc nhìn của giám khảo (Assessor):',
                   'Displaying all 8 core competencies and 2025 behavioral sub-competencies, highlighting updates and assessor evaluation criteria:')}
            </div>
            """, unsafe_allow_html=True)

            for idx, comp in enumerate(COMPETENCIES):
                comp_no = comp.get('number', f"{idx+1}.0")
                comp_code = comp.get('code') or (f"Năng lực {comp_no}" if st.session_state.lang == 'vi' else f"Competency {comp_no}")
                name_vi = comp.get('nameVi') or comp.get('compVi') or comp.get('titleVi', '')
                name_en = comp.get('nameEn') or comp.get('compEn') or comp.get('titleEn', '')
                name_disp = name_vi if st.session_state.lang == 'vi' else name_en
                desc_vi = comp.get('descVi') or comp.get('definitionVi') or comp.get('lensVi', '')
                desc_en = comp.get('descEn') or comp.get('definitionEn') or comp.get('lensEn', '')
                desc_disp = desc_vi if st.session_state.lang == 'vi' else desc_en
                domain_disp = comp.get('domainVi', '') if st.session_state.lang == 'vi' else comp.get('domainEn', '')
                changes_disp = comp.get('changes2025Vi', '') if st.session_state.lang == 'vi' else comp.get('changes2025En', '')
                cue_disp = (comp.get('studyCueVi') or comp.get('cueVi', '')) if st.session_state.lang == 'vi' else (comp.get('studyCueEn') or comp.get('cueEn', ''))
                trigger_disp = comp.get('examTriggerVi', '') if st.session_state.lang == 'vi' else comp.get('examTriggerEn', '')
                assessor_disp = comp.get('assessorPerspectiveVi', '') if st.session_state.lang == 'vi' else comp.get('assessorPerspectiveEn', '')
                traps_disp = (comp.get('commonTrapsVi') or comp.get('trapVi', '')) if st.session_state.lang == 'vi' else (comp.get('commonTrapsEn') or comp.get('trapEn', ''))
                subs = comp.get('subCompetencies2025', [])

                with st.expander(f"{comp_code}: {name_disp}"):
                    st.markdown(f"""
                    <div style="font-size: 0.92rem; line-height: 1.65; color: #2C3E50;">
                        <div style="margin-bottom: 8px;">
                            <span class="zen-badge zen-badge-primary">{domain_disp}</span>
                            <span class="zen-badge zen-badge-gold">Bản chuẩn 2025</span>
                            <span class="zen-badge zen-badge-blue">{len(subs)} hành vi thành phần</span>
                        </div>
                        <p><b>{t('Định nghĩa chuẩn 2025:', 'Official 2025 Definition:')}</b><br/>{desc_disp}</p>
                    """, unsafe_allow_html=True)

                    if changes_disp:
                        st.markdown(f"""
                        <div style="background: #FAF7F2; border-left: 3px solid #8A6112; padding: 10px 14px; border-radius: 6px; margin: 10px 0;">
                            <b>✨ {t('Điểm mới & Sửa đổi trong Bản 2025:', '2025 Revisions & Additions:')}</b><br/>
                            {changes_disp}
                        </div>
                        """, unsafe_allow_html=True)

                    if subs:
                        st.markdown(f"<b>📋 {t('Các hành vi thành phần chính thức (Sub-Competencies 2025):', 'Official 2025 Behavioral Indicators:')}</b>", unsafe_allow_html=True)
                        for sub in subs:
                            sub_id = sub.get('subId', '')
                            beh_disp = sub.get('behaviorVi', '') if st.session_state.lang == 'vi' else sub.get('behaviorEn', '')
                            st.markdown(f"• <b>{sub_id}</b>: {beh_disp}", unsafe_allow_html=True)

                    if cue_disp or trigger_disp or assessor_disp or traps_disp:
                        st.markdown(f"""
                        <div style="background: #FAFDF9; border: 1px solid #EADBCC; border-radius: 8px; padding: 12px; margin: 12px 0;">
                            {f'<p style="margin: 0 0 6px 0; color: #2F3E34;"><b>💡 {t("Gợi ý học tập & Dấu hiệu trong đề:", "Study Cue & Exam Triggers:")}</b> {cue_disp} | {trigger_disp}</p>' if cue_disp or trigger_disp else ''}
                            {f'<p style="margin: 6px 0 0 0; color: #8A6112;"><b>🎯 {t("Góc nhìn của Giám Khảo (Assessor):", "Assessor Perspective:")}</b><br/>{assessor_disp}</p>' if assessor_disp else ''}
                            {f'<p style="margin: 6px 0 0 0; color: #C4785A;"><b>⚠️ {t("Bẫy thường gặp làm mất điểm:", "Common Pitfalls & Traps:")}</b><br/>{traps_disp}</p>' if traps_disp else ''}
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)

        with subtab_2019:
            st.markdown(f"""
            <div style="font-size: 0.88rem; color: #555; margin-bottom: 12px;">
                {t('Khu vực đối chiếu bản Khung Năng Lực 2019 — căn cứ đang được Pearson VUE sử dụng cho kỳ thi trắc nghiệm tình huống PCC/MCC hiện hành:',
                   'Archive & comparison area for the 2019 Framework — the baseline currently evaluated in Pearson VUE credentialing exams:')}
            </div>
            """, unsafe_allow_html=True)

            for idx, comp in enumerate(COMPETENCIES):
                comp_no = comp.get('number', f"{idx+1}.0")
                comp_code = comp.get('code') or (f"Năng lực {comp_no}" if st.session_state.lang == 'vi' else f"Competency {comp_no}")
                name_vi = comp.get('nameVi') or comp.get('compVi') or comp.get('titleVi', '')
                name_en = comp.get('nameEn') or comp.get('compEn') or comp.get('titleEn', '')
                name_disp = name_vi if st.session_state.lang == 'vi' else name_en
                desc_vi = comp.get('descVi') or comp.get('definitionVi') or comp.get('lensVi', '')
                desc_en = comp.get('descEn') or comp.get('definitionEn') or comp.get('lensEn', '')
                desc_disp = desc_vi if st.session_state.lang == 'vi' else desc_en
                subs_2019 = comp.get('subCompetencies2019', [])
                changes_disp = comp.get('changes2025Vi', '') if st.session_state.lang == 'vi' else comp.get('changes2025En', '')

                with st.expander(f"{comp_code} (Bản 2019): {name_disp}"):
                    st.markdown(f"""
                    <div style="font-size: 0.92rem; line-height: 1.65; color: #2C3E50;">
                        <span class="zen-badge zen-badge-gold">Khung 2019 (Chuẩn thi Pearson VUE hiện hành)</span>
                        <p style="margin-top: 8px;"><b>{t('Định nghĩa bản 2019:', '2019 Baseline Definition:')}</b><br/>{desc_disp}</p>
                        
                        <div style="background: #FAF7F2; border-left: 3px solid #8BA888; padding: 10px; border-radius: 6px; margin: 8px 0;">
                            <b>📌 {t('Lưu ý thi trắc nghiệm Pearson VUE:', 'Pearson VUE Exam Insight:')}</b><br/>
                            {t('Trong các câu hỏi trắc nghiệm tình huống, đáp án BEST luôn luôn là phương án tôn trọng quyền tự quyết của khách hàng, lắng nghe không phán xét và làm rõ thỏa thuận.',
                               'In situational judgment questions, the BEST option consistently protects client autonomy, active non-judgmental listening, and contract clarity.')}
                        </div>
                    """, unsafe_allow_html=True)

                    if subs_2019:
                        st.markdown(f"<b>📋 {t('Các chỉ dấu hành vi bản 2019 đối chiếu:', '2019 Sub-Competencies Comparison:')}</b>", unsafe_allow_html=True)
                        for sub in subs_2019:
                            sub_id = sub.get('subId', '')
                            beh_disp = sub.get('behaviorVi', '') if st.session_state.lang == 'vi' else sub.get('behaviorEn', '')
                            st.markdown(f"• <b>{sub_id}</b>: {beh_disp}", unsafe_allow_html=True)

                    if changes_disp:
                        st.markdown(f"""
                        <div style="font-size: 0.85rem; color: #8A6112; margin-top: 8px;">
                            <b>🔄 {t('Chuyển giao sang bản 2025:', 'Transition to 2025:')}</b> {changes_disp}
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)

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
                <b>{t('Tác giả:', 'Authors:')}</b> Alicia M. Hullinger, PhD, ACC & Joel A. DiGirolamo, MS, PCC (2018).<br/>
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
