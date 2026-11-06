# -*- coding: utf-8 -*-
"""
Home Page for Mentor Thi (PCC Learning & Practice)
Zen Edition with prominent 7-Module ICF Curriculum Pathway, genuine lotus tracking, and 'Một Tách Trà Học' entry point.
"""
import streamlit as st
from app_modules.styles import render_breathing_widget, render_disclaimer_banner
from scripts.icf_curriculum_data import get_icf_7_modules, get_tea_micro_lessons

def render_home_page(DATA, EXAM_PROFILES, PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t, set_page):
    prof_id = st.session_state.exam_profile_id
    prof = EXAM_PROFILES.get(prof_id, list(EXAM_PROFILES.values())[0])
    all_modules = get_icf_7_modules()
    tea_lessons = get_tea_micro_lessons()

    # 1. WELCOME HEADER
    st.markdown(f"""
    <div style="text-align: center; max-width: 860px; margin: 0 auto 12px auto;">
        <span class="zen-badge zen-badge-primary">🌱 {t('Tự Học Tỉnh Thức — Chuẩn Hóa Phán Đoán', 'Mindful Mastery — Verifiable Standards')}</span>
        <h1 style="font-size: 2.3rem; margin: 8px 0; color: #2F3E34;">🪷 Mentor Thi</h1>
        <div style="font-size: 1.12rem; color: #8C6D53; font-weight: 500; margin-bottom: 4px;">
            {t('Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching', 'Master Standards — Hone Judgment — Elevate Coaching Mastery')}
        </div>
        <div style="font-size: 0.92rem; color: #5F6F65; font-style: italic; margin-bottom: 10px;">
            "{t('Vì ước mơ đưa Coaching thành lối sống', 'Making Coaching a Way of Life')}"
        </div>
        <p style="font-size: 0.92rem; color: #5F6F65; line-height: 1.6; margin-bottom: 0;">
            {t('Môi trường tự học và rèn luyện phán đoán tình huống độc lập, bồi đắp toàn diện 7 nhóm tài liệu chuẩn mực đã được kiểm chứng trực tiếp từ ICF.',
               'An independent self-study sanctuary grounded in the 7 verified official ICF documentation groups.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Disclaimer banner
    render_disclaimer_banner(t)

    # 2. PROMINENT SECTION: LỘ TRÌNH HỌC TÀI LIỆU ICF (PLACED DIRECTLY BELOW WELCOME)
    cur_mod_id = st.session_state.get("active_module_id", "mod-1")
    cur_les_id = st.session_state.get("active_lesson_id", "mod1-les1")
    cur_mod_obj = next((m for m in all_modules if m["id"] == cur_mod_id), all_modules[0])
    cur_les_obj = next((les for les in cur_mod_obj.get("lessons", []) if les["id"] == cur_les_id), None)
    if not cur_les_obj and cur_mod_obj.get("lessons"):
        cur_les_obj = cur_mod_obj["lessons"][0]

    # Calculate real statistics
    progress = st.session_state.get("curriculum_progress", {})
    total_lessons = sum(len(m.get("lessons", [])) for m in all_modules if m.get("lessons"))
    completed_lessons = sum(1 for p in progress.values() if p.get("status") in ["read", "quiz_passed"])
    passed_quizzes = sum(1 for p in progress.values() if p.get("status") == "quiz_passed")
    overall_pct = int((completed_lessons / max(total_lessons, 1)) * 100)

    st.markdown(f"""
    <div class="zen-card" style="border: 2px solid #8BA888; background: #FAFDF9; margin-bottom: 20px; padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div>
                <span class="zen-badge zen-badge-primary">📚 {t('Lộ Trình Học Tài Liệu ICF', 'Official ICF Document Learning Pathway')}</span>
                <span class="zen-badge zen-badge-gold">{t('Tiến độ toàn lộ trình:', 'Overall Progress:')} {overall_pct}% ({completed_lessons}/{total_lessons} {t('bài', 'lessons')})</span>
            </div>
            <div style="font-size: 0.85rem; color: #8C6D53; font-weight: 500;">
                {t('Thứ tự học chuẩn 7 Học phần từ ICF', 'Standard 7-Module Order from ICF')}
            </div>
        </div>
        
        <div style="margin: 14px 0 10px 0; background: #EADBCC; height: 8px; border-radius: 4px; overflow: hidden;">
            <div style="background: #2F3E34; height: 100%; width: {overall_pct}%;"></div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-top: 12px;">
            <div>
                <div style="font-size: 0.85rem; color: #5F6F65; text-transform: uppercase; font-weight: 600;">
                    {t('Học phần & Bài đang học gần nhất:', 'Currently Active Module & Lesson:')}
                </div>
                <h3 style="margin: 4px 0; color: #2F3E34; font-size: 1.25rem;">
                    {cur_mod_obj['icon']} {cur_mod_obj['titleVi'] if st.session_state.lang == 'vi' else cur_mod_obj['titleEn']}
                </h3>
                <div style="font-size: 0.95rem; color: #8C6D53; font-weight: 500;">
                    📖 {cur_les_obj['titleVi'] if cur_les_obj and st.session_state.lang == 'vi' else (cur_les_obj['titleEn'] if cur_les_obj else t('Thuật ngữ & Tra cứu', 'Glossary Reference'))}
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c_resume1, c_resume2 = st.columns([2, 1])
    with c_resume1:
        resume_btn_label = "👉 " + t("Tiếp Tục Học Bài Này", "Resume This Lesson")
        if st.button(resume_btn_label, type="primary", use_container_width=True, key="btn_resume_pathway"):
            set_page("curriculum", module_id=cur_mod_id, lesson_id=cur_les_obj["id"] if cur_les_obj else None)
            st.rerun()
    with c_resume2:
        if st.button("🚀 " + t("Bắt Đầu Lộ Trình (Học Phần 1)", "Start Pathway (Module 1)"), use_container_width=True, key="btn_start_pathway"):
            set_page("curriculum", module_id="mod-1", lesson_id="mod1-les1")
            st.rerun()

    # Visual Pathway: 7 Modules Grid
    st.markdown(f"<h4 style='color: #2F3E34; margin: 16px 0 10px 0;'>🌱 {t('7 Học Phần Theo Đúng Thứ Tự Chuẩn ICF:', '7 Sequential ICF Study Modules:')}</h4>", unsafe_allow_html=True)
    mod_cols = st.columns(4)
    for idx, mod in enumerate(all_modules):
        col_target = mod_cols[idx % 4]
        with col_target:
            mod_lessons = mod.get("lessons", [])
            mod_comp = sum(1 for les in mod_lessons if progress.get(les["id"], {}).get("status") in ["read", "quiz_passed"])
            mod_total = len(mod_lessons)
            is_active = (mod["id"] == cur_mod_id)

            status_badge = "Chưa học"
            badge_class = "zen-badge-gold"
            if mod_total > 0 and mod_comp == mod_total:
                status_badge = "Đã hoàn thành"
                badge_class = "zen-badge-primary"
            elif mod_comp > 0:
                status_badge = f"Đang học ({mod_comp}/{mod_total})"
                badge_class = "zen-badge-blue"
            elif mod["id"] == "mod-7":
                status_badge = "Tra cứu & Flashcard"
                badge_class = "zen-badge-pink"

            st.markdown(f"""
            <div class="zen-card" style="padding: 12px 14px; margin-bottom: 12px; border-top: 3px solid {'#2F3E34' if is_active else '#8BA888'}; height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <span style="font-size: 1.1rem;">{mod['icon']}</span>
                        <span class="zen-badge {badge_class}" style="font-size: 0.72rem;">{status_badge}</span>
                    </div>
                    <div style="font-size: 0.88rem; font-weight: 600; color: #2F3E34; line-height: 1.3;">
                        {mod['titleVi'] if st.session_state.lang == 'vi' else mod['titleEn']}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Vào học HP {mod['number']}", key=f"btn_jump_mod_{mod['id']}", use_container_width=True):
                first_les = mod_lessons[0]["id"] if mod_lessons else None
                set_page("curriculum", module_id=mod["id"], lesson_id=first_les)
                st.rerun()

    # 3. MOTIVATION & MINDFULNESS SECTION: VƯỜN SEN & MỘT TÁCH TRÀ HỌC
    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 16px 0 20px 0;'/>", unsafe_allow_html=True)
    c_mind1, c_mind2 = st.columns([1, 1])

    with c_mind1:
        # VƯỜN SEN CHÁNH NIỆM CỦA TÔI (REAL DATA CONNECTION)
        real_bloomed = st.session_state.lotus_bloomed
        st.markdown(f"""
        <div class="zen-card" style="border-left: 4px solid #9C4158; height: 100%;">
            <span class="zen-badge zen-badge-pink">🪷 {t('Vườn Sen Chánh Niệm Của Tôi', 'My Mindful Lotus Garden')}</span>
            <h3 style="margin: 8px 0; color: #2F3E34; font-size: 1.15rem;">
                {t('Thành Tựu Học Tập Thực Tế', 'Verified Personal Study Garden')}
            </h3>
            <div style="font-size: 1.6rem; color: #9C4158; margin: 6px 0;">
                {'🪷 ' * min(real_bloomed, 10)}
            </div>
            <div style="font-size: 0.9rem; color: #5F6F65; line-height: 1.6;">
                • <b>{real_bloomed}</b> {t('đóa sen đã nở', 'lotuses bloomed')} (kết nối trực tiếp từ bài học và bài kiểm tra thực chất).<br/>
                • <b>{completed_lessons}</b> {t('bài học đã hoàn thành', 'lessons completed')}.<br/>
                • <b>{passed_quizzes}</b> {t('bài kiểm tra đạt chuẩn', 'quizzes successfully passed')}.<br/>
                <i>*{t('Hệ thống cam kết không hiển thị ngày học hay thành tích ảo.', 'System strictly displays real verified progress; zero fabricated streaks.')}</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_mind2:
        # MỘT TÁCH TRÀ HỌC (PORTAL TO A BITE-SIZED LESSON)
        tea_idx = (completed_lessons) % len(tea_lessons)
        tea = tea_lessons[tea_idx]
        st.markdown(f"""
        <div class="zen-card" style="border-left: 4px solid #8BA888; height: 100%;">
            <span class="zen-badge zen-badge-primary">🍵 {t('Một Tách Trà Học', 'A Mindful Cup of Study Tea')}</span>
            <h3 style="margin: 8px 0; color: #2F3E34; font-size: 1.15rem;">
                {tea['titleVi'] if st.session_state.lang == 'vi' else tea['titleEn']}
            </h3>
            <p style="font-size: 0.9rem; color: #8C6D53; font-style: italic; margin-bottom: 6px;">
                "{tea['quoteVi'] if st.session_state.lang == 'vi' else tea['quoteVi']}"
            </p>
            <p style="font-size: 0.85rem; color: #555; line-height: 1.5; margin-bottom: 12px;">
                {tea['promptVi']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(tea['linkTextVi'], key="btn_enter_tea_lesson", type="secondary", use_container_width=True):
            set_page("curriculum", module_id=tea["moduleId"], lesson_id=tea["lessonId"])
            st.rerun()

    # 4. ACTIVE EXAM PROFILE & PRACTICE MODES
    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 16px 0 20px 0;'/>", unsafe_allow_html=True)
    
    col_prof1, col_prof2 = st.columns([3, 1])
    with col_prof1:
        st.markdown(f"""
        <div class="zen-card" style="padding: 14px 18px; margin-bottom: 16px; border-left: 4px solid #8BA888;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="zen-badge zen-badge-gold">🎯 {t('Cấu Hình Kỳ Thi Đang Kích Hoạt', 'Active Exam Profile')}</span>
                <span class="zen-badge zen-badge-blue">{prof['statusBadgeVi'] if st.session_state.lang == 'vi' else prof['statusBadgeEn']}</span>
            </div>
            <h4 style="margin: 6px 0 2px 0; font-size: 1.15rem; color: #2F3E34;">
                {prof['nameVi'] if st.session_state.lang == 'vi' else prof['nameEn']}
            </h4>
            <div style="font-size: 0.85rem; color: #555;">
                ⏱️ <b>{t('Thời gian:', 'Duration:')}</b> {prof['totalTimeMinutes']} {t('phút', 'mins')} ({prof['totalItems']} {t('câu hỏi', 'items')}) | 
                ☕ <b>{t('Nghỉ:', 'Break:')}</b> {prof['breakMinutes']} {t('phút', 'mins')} | 
                📜 <b>{t('Chuẩn Đạo đức:', 'Ethics:')}</b> {prof['ethicsBaselineVi'] if st.session_state.lang == 'vi' else prof['ethicsBaselineEn']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_prof2:
        st.write("")
        if st.button("🔄 " + t("Đổi Cấu Hình Thi", "Switch Exam Profile"), use_container_width=True):
            new_id = "updated_80_items" if prof_id == "legacy_78_sjt" else "legacy_78_sjt"
            st.session_state.exam_profile_id = new_id
            st.rerun()

    # Quick Action Cards
    col_act1, col_act2, col_act3 = st.columns(3)
    with col_act1:
        st.markdown(f"""
        <div class="zen-card" style="height: 185px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <span class="zen-badge zen-badge-primary">📑 {t('Khảo Sát Đề Gốc', 'Official Samples')}</span>
                <h4 style="margin: 6px 0; color: #2F3E34;">{t('8 Câu Mẫu Chuẩn ICF', '8 Official ICF Samples')}</h4>
                <p style="font-size: 0.85rem; color: #666; line-height: 1.5;">
                    {t('8 tình huống nguyên bản tiếng Anh có đáp án công bố trên website ICF, dịch nghĩa và phân tích đa chiều.',
                       '8 authentic English scenarios with official answer key published on the ICF website.')}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 " + t("Xem 8 Câu Mẫu", "View 8 Samples"), key="btn_go_official", use_container_width=True):
            set_page("official_samples")
            st.rerun()

    with col_act2:
        st.markdown(f"""
        <div class="zen-card" style="height: 185px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <span class="zen-badge zen-badge-gold">⚡ {t('Rèn Phán Đoán', 'Daily Drill')}</span>
                <h4 style="margin: 6px 0; color: #2F3E34;">{t('Luyện 10 Câu / Ngày', 'Daily 10 Drill')}</h4>
                <p style="font-size: 0.85rem; color: #666; line-height: 1.5;">
                    {t('Luyện tập không lặp lại tình huống: 10 câu Best/Worst hoặc câu hỏi kiến thức kèm phản hồi tức thì.',
                       'Non-repeating drill: 10 Best/Worst SJT items or Knowledge MCQs with immediate feedback.')}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 " + t("Vào Luyện 10 Câu", "Start Daily Drill"), key="btn_go_daily", use_container_width=True):
            set_page("daily_practice")
            st.rerun()

    with col_act3:
        st.markdown(f"""
        <div class="zen-card" style="height: 185px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <span class="zen-badge zen-badge-pink">⚖️ {t('Mô Phỏng Thực Tế', 'Exam Simulator')}</span>
                <h4 style="margin: 6px 0; color: #2F3E34;">{t('Phòng Thi Thử Mô Phỏng', 'Mock Exam Simulator')}</h4>
                <p style="font-size: 0.85rem; color: #666; line-height: 1.5;">
                    {t('Mô phỏng chân thực: Cấu hình 78 SJT (180p) hoặc 80 câu 4 phần (150p). Chấm 4 mức điểm quy đổi 200–600.',
                       'Adaptively simulates 78 SJT (180m) or 80 items (150m). Timed, 4-tier grading.')}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("👉 " + t("Bắt Đầu Thi Thử", "Enter Exam Simulator"), key="btn_go_sjt", use_container_width=True):
            set_page("sjt")
            st.rerun()

    st.write("")
    render_breathing_widget(t)
