# -*- coding: utf-8 -*-
"""
Home Page for PCC Learning & Practice
"""
import streamlit as st
from app_modules.styles import render_breathing_widget, render_disclaimer_banner

def render_home_page(DATA, EXAM_PROFILES, PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t, set_page):
    prof_id = st.session_state.exam_profile_id
    prof = EXAM_PROFILES.get(prof_id, list(EXAM_PROFILES.values())[0])

    st.markdown(f"""
    <div style="text-align: center; max-width: 860px; margin: 0 auto 16px auto;">
        <span class="zen-badge zen-badge-primary">🌱 {t('Tự Học Tỉnh Thức — Chuẩn Hóa Phán Đoán', 'Mindful Mastery — Verifiable Standards')}</span>
        <h1 style="font-size: 2.3rem; margin: 10px 0; color: #2F3E34;">PCC Learning & Practice</h1>
        <div style="font-size: 1.15rem; color: #8C6D53; font-weight: 500; margin-bottom: 8px;">
            {t('Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching', 'Master Standards — Hone Judgment — Elevate Coaching Mastery')}
        </div>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Môi trường tự học và rèn luyện phán đoán tình huống độc lập, bồi đắp 8 Năng lực Cốt lõi và Bộ Quy tắc Đạo đức theo đúng các chuẩn mực đã được kiểm chứng trực tiếp từ ICF.',
               'An independent self-study sanctuary to hone situational judgment, grounded in the 8 Core Competencies and Code of Ethics verified directly from official ICF documentation.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Disclaimer banner
    render_disclaimer_banner(t)

    # Active Exam Profile Card on Home
    col_prof1, col_prof2 = st.columns([3, 1])
    with col_prof1:
        st.markdown(f"""
        <div class="zen-card" style="padding: 16px 20px; margin-bottom: 16px; border-left: 4px solid #8BA888;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="zen-badge zen-badge-gold">🎯 {t('Cấu Hình Kỳ Thi Đang Kích Hoạt', 'Active Exam Profile')}</span>
                <span class="zen-badge zen-badge-blue">{prof['statusBadgeVi'] if st.session_state.lang == 'vi' else prof['statusBadgeEn']}</span>
            </div>
            <h3 style="margin: 8px 0 4px 0; font-size: 1.25rem; color: #2F3E34;">
                {prof['nameVi'] if st.session_state.lang == 'vi' else prof['nameEn']}
            </h3>
            <div style="font-size: 0.88rem; color: #555; line-height: 1.5;">
                ⏱️ <b>{t('Thời gian:', 'Duration:')}</b> {prof['totalTimeMinutes']} {t('phút', 'mins')} ({prof['totalItems']} {t('câu hỏi', 'items')}) | 
                ☕ <b>{t('Nghỉ giải lao:', 'Break:')}</b> {prof['breakMinutes']} {t('phút tùy chọn', 'mins optional')}<br/>
                📜 <b>{t('Nền tảng chuẩn mực:', 'Standards Baseline:')}</b> {prof['ethicsBaselineVi'] if st.session_state.lang == 'vi' else prof['ethicsBaselineEn']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_prof2:
        st.write("")
        if st.button("🔄 " + t("Đổi Cấu Hình Thi", "Switch Exam Profile"), use_container_width=True):
            new_id = "updated_80_items" if prof_id == "legacy_78_sjt" else "legacy_78_sjt"
            st.session_state.exam_profile_id = new_id
            st.rerun()

    # Dashboard Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        total_q = len(PRACTICE_QUESTIONS) + len(KNOWLEDGE_QUESTIONS) + len(OFFICIAL_SAMPLES)
        st.metric(label="📚 " + t("Tổng Kho Câu Hỏi", "Total Question Pool"), value=f"{total_q} {t('câu', 'items')}")
    with m2:
        bm_count = len(st.session_state.bookmarked_qids)
        st.metric(label="★ " + t("Đã Đánh Dấu", "Bookmarked"), value=f"{bm_count} {t('câu', 'items')}")
    with m3:
        history_count = len(st.session_state.exam_history)
        st.metric(label="📝 " + t("Phiên Thi Đã Lưu", "Saved Exam Attempts"), value=f"{history_count} {t('lượt', 'runs')}")
    with m4:
        st.metric(label="🪷 " + t("Vườn Sen Nở", "Lotus Blooms"), value=f"{st.session_state.lotus_bloomed} {t('đóa sen', 'lotuses')}")

    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 16px 0 24px 0;'/>", unsafe_allow_html=True)

    # 4 Quick Actions (2x2 grid)
    col_act1, col_act2 = st.columns(2)
    with col_act1:
        st.markdown(f"""
        <div class="zen-card" style="height: 200px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <span class="zen-badge zen-badge-primary">📑 {t('Khảo Sát Đề Gốc', 'Official Samples')}</span>
                <h3 style="margin: 8px 0; font-size: 1.15rem; color: #2F3E34;">
                    {t('8 Câu Mẫu Chuẩn ICF Công Khai', '8 Official Public ICF Samples')}
                </h3>
                <p style="font-size: 0.88rem; color: #666; line-height: 1.5;">
                    {t('8 tình huống nguyên bản tiếng Anh có đáp án công bố trên trang chính thức của ICF, dịch nghĩa chuẩn xác và phân tích đa chiều.',
                       '8 authentic English scenarios with official answer key published on the ICF website, paired with verified Vietnamese translation.')}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 " + t("Xem 8 Câu Mẫu ICF", "Explore Official Samples"), key="btn_go_official", use_container_width=True):
            set_page("official_samples")
            st.rerun()

    with col_act2:
        st.markdown(f"""
        <div class="zen-card" style="height: 200px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <span class="zen-badge zen-badge-gold">⚡ {t('Rèn Phán Đoán', 'Daily Drill')}</span>
                <h3 style="margin: 8px 0; font-size: 1.15rem; color: #2F3E34;">
                    {t('Luyện Tập 10 Câu / Ngày', 'Daily 10-Question Targeted Drill')}
                </h3>
                <p style="font-size: 0.88rem; color: #666; line-height: 1.5;">
                    {t('Luyện đều đặn mỗi ngày: 10 câu tình huống Best/Worst, câu hỏi kiến thức hoặc ôn tập câu đã đánh dấu. Kèm phản hồi tức thì.',
                       'Consistent daily discipline: 10 Best/Worst SJT items, Knowledge MCQs, or review bookmarked questions with immediate feedback.')}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 " + t("Vào Luyện 10 Câu", "Start Daily Drill"), key="btn_go_daily", use_container_width=True):
            set_page("daily_practice")
            st.rerun()

    col_act3, col_act4 = st.columns(2)
    with col_act3:
        st.markdown(f"""
        <div class="zen-card" style="height: 200px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <span class="zen-badge zen-badge-pink">⚖️ {t('Mô Phỏng Thực Tế', 'Exam Simulator')}</span>
                <h3 style="margin: 8px 0; font-size: 1.15rem; color: #2F3E34;">
                    {t('Phòng Thi Thử Mô Phỏng Động', 'Dynamic Mock Exam Simulator')}
                </h3>
                <p style="font-size: 0.88rem; color: #666; line-height: 1.5;">
                    {t('Tự động thích ứng theo cấu hình: Kỳ thi hiện hành (78 SJT, 180p) hoặc Kỳ thi cập nhật (80 câu 4 phần, 150p). Bấm giờ, chấm 4 mức điểm.',
                       'Dynamically adapts to active profile: Current Exam (78 SJT, 180m) or Updated Exam (80 items 4 sections, 150m). Timed, 4-tier grading.')}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 " + t("Bắt Đầu Thi Thử", "Enter Exam Simulator"), key="btn_go_sjt", use_container_width=True):
            set_page("sjt")
            st.rerun()

    with col_act4:
        st.markdown(f"""
        <div class="zen-card" style="height: 200px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <span class="zen-badge zen-badge-blue">🏛️ {t('Chuẩn Mực & Bằng Chứng', 'Evidence Library')}</span>
                <h3 style="margin: 8px 0; font-size: 1.15rem; color: #2F3E34;">
                    {t('Thư Viện Chuẩn ICF & Nguồn Kiểm Chứng', 'ICF Standards & Verified Sources')}
                </h3>
                <p style="font-size: 0.88rem; color: #666; line-height: 1.5;">
                    {t('Bảng 7 nguồn chính thức đã kiểm chứng trực tiếp từ coachingfederation.org, phân định rõ Đạo đức 2020 vs 2025, Năng lực cốt lõi và PCC Markers.',
                       'Directly verified 7 official sources from coachingfederation.org, delineating 2020 vs 2025 Ethics, Core Competencies, and PCC Markers.')}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 " + t("Tra Cứu Thư Viện", "Explore Standards Library"), key="btn_go_library", use_container_width=True):
            set_page("library")
            st.rerun()

    st.write("")
    render_breathing_widget(t)
