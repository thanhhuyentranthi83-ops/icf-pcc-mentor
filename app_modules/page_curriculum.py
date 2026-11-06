# -*- coding: utf-8 -*-
"""
Curriculum Page for Mentor Thi (PCC Learning & Practice)
Comprehensive 7-Module ICF Document Curriculum Suite:
1. Core Competencies (8 competencies, examples, tests, confusable pairs)
2. Code of Ethics (Purpose, Core Values, Standards 1-28, ICE, Pledge & Appendix)
3. PCC Markers & Criteria (37 markers, appropriate/inappropriate behaviors, audio vs written distinction)
4. Referring a Client to Therapy White Paper (Hullinger & DiGirolamo 2018, 7 lessons, anti-diagnostic, 3 pillars)
5. ICF Ethics Case Studies (Strict 5-step workflow with hidden analysis until revealed)
6. ICF FAQs (Categorized, official vs synthesized tags, verified dates)
7. Glossary & Definitions (Official vs support terms, accent-folding search EN/VI, flashcards, disambiguation drills)
"""
import streamlit as st
from app_modules.state import update_lesson_progress, t, set_page
from scripts.icf_curriculum_data import (
    get_icf_7_modules,
    get_glossary_terms,
    search_glossary,
    remove_accents
)

def render_curriculum_page(DATA, STUDY_SECTIONS, THEORIES, KEYWORDS, FLASHCARDS, CASE_STUDIES, QUIZZES, t_func):
    all_modules = get_icf_7_modules()
    progress = st.session_state.get("curriculum_progress", {})

    # Active module and lesson state
    active_mod_id = st.session_state.get("active_module_id", "mod-1")
    active_mod = next((m for m in all_modules if m["id"] == active_mod_id), all_modules[0])

    active_les_id = st.session_state.get("active_lesson_id", None)
    mod_lessons = active_mod.get("lessons", [])
    active_les = None
    if mod_lessons:
        active_les = next((les for les in mod_lessons if les["id"] == active_les_id), mod_lessons[0])
        if active_les["id"] != active_les_id:
            st.session_state.active_lesson_id = active_les["id"]

    # Header banner
    st.markdown(f"""
    <div style="margin-bottom: 16px;">
        <span class="zen-badge zen-badge-primary">📚 {t('Lộ Trình Học Tập Tỉnh Thức Chuẩn ICF', 'Mindful ICF Document Curriculum Suite')}</span>
        <h2 style="margin: 6px 0; color: #2F3E34;">
            {active_mod['icon']} {active_mod['titleVi'] if st.session_state.lang == 'vi' else active_mod['titleEn']}
        </h2>
        <div style="font-size: 0.88rem; color: #8C6D53;">
            📜 <b>{t('Tài liệu nguồn:', 'Source Document:')}</b> <a href="{active_mod['sourceUrl']}" target="_blank" style="color: #1E4E79; text-decoration: underline;">{active_mod['sourceDoc']} ↗</a>
        </div>
        <p style="font-size: 0.85rem; color: #666; margin-top: 4px; font-style: italic;">
            * {t('Bản dịch phục vụ học tập, không phải bản dịch chính thức của ICF. Phân định rõ ràng giữa quy chuẩn chính thức và phần diễn giải học tập.',
                 'Educational study translation; not an official ICF translation. Clear distinction between official standards and pedagogical commentary.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Language View Switcher for Lesson (Tiếng Việt, English, Song ngữ)
    col_lang1, col_lang2, col_lang3, col_lang4 = st.columns([2, 1, 1, 1])
    with col_lang1:
        st.markdown(f"<b>{t('Chế độ hiển thị bài học:', 'Lesson Display Mode:')}</b>", unsafe_allow_html=True)
    with col_lang2:
        if st.button("🇻🇳 Tiếng Việt", use_container_width=True, type="primary" if st.session_state.curriculum_lang_mode == "vi" else "secondary"):
            st.session_state.curriculum_lang_mode = "vi"
            st.rerun()
    with col_lang3:
        if st.button("🇬🇧 English", use_container_width=True, type="primary" if st.session_state.curriculum_lang_mode == "en" else "secondary"):
            st.session_state.curriculum_lang_mode = "en"
            st.rerun()
    with col_lang4:
        if st.button("🌐 Song ngữ", use_container_width=True, type="primary" if st.session_state.curriculum_lang_mode == "bilingual" else "secondary"):
            st.session_state.curriculum_lang_mode = "bilingual"
            st.rerun()

    lang_mode = st.session_state.curriculum_lang_mode

    # Module Stepper Tabs (1 to 7)
    mod_tabs = st.tabs([f"{m['icon']} HP {m['number']}: {m['titleVi'][:18]}..." if st.session_state.lang == 'vi' else f"{m['icon']} M{m['number']}: {m['titleEn'][:16]}..." for m in all_modules])
    
    for idx, tab in enumerate(mod_tabs):
        with tab:
            mod_item = all_modules[idx]
            if mod_item["id"] != active_mod_id:
                if st.button(f"👉 {t('Mở', 'Open')} {mod_item['titleVi'] if st.session_state.lang == 'vi' else mod_item['titleEn']}", key=f"btn_switch_mod_{mod_item['id']}"):
                    st.session_state.active_module_id = mod_item["id"]
                    first_les_id = mod_item["lessons"][0]["id"] if mod_item.get("lessons") else None
                    st.session_state.active_lesson_id = first_les_id
                    st.rerun()

    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 12px 0 16px 0;'/>", unsafe_allow_html=True)

    # SPECIAL HANDLING FOR MODULE 7: GLOSSARY & DEFINITIONS
    if active_mod_id == "mod-7":
        render_module_7_glossary(t)
        return

    # FOR MODULES 1 TO 6: SEQUENTIAL LESSON RUNNER
    col_nav_left, col_lesson_content = st.columns([1, 3])

    # LEFT SIDEBAR: LESSON LIST & PROGRESS STATUS
    with col_nav_left:
        st.markdown(f"#### 📑 {t('Danh Sách Bài Học', 'Lesson Directory')}")
        for l_idx, les in enumerate(mod_lessons):
            les_prog = progress.get(les["id"], {"status": "unread", "score": 0, "needs_review": False})
            status = les_prog.get("status", "unread")
            
            status_icon = "⚪"
            if status == "quiz_passed":
                status_icon = "✅"
            elif status == "read":
                status_icon = "📖"
            if les_prog.get("needs_review"):
                status_icon = "🚩"

            is_cur = (les["id"] == active_les["id"]) if active_les else False
            btn_style = "primary" if is_cur else "secondary"
            btn_title = f"{status_icon} {les.get('lessonNumber', l_idx+1)}. {les['titleVi'][:22]}..."
            if st.button(btn_title, key=f"btn_sel_les_{les['id']}", use_container_width=True, type=btn_style):
                st.session_state.active_lesson_id = les["id"]
                st.rerun()

        # Wrap-up review quiz button if available
        if active_mod.get("wrapUpQuiz"):
            st.markdown("---")
            if st.button(f"🏆 {t('Bài Ôn Tập Tổng Hợp', 'Comprehensive Review')}", key=f"btn_wrapup_{active_mod_id}", use_container_width=True):
                st.session_state.active_lesson_id = f"{active_mod_id}-wrapup"
                st.rerun()

    # RIGHT MAIN COLUMN: 10-POINT LESSON RUNNER
    with col_lesson_content:
        # Check if user clicked wrap-up quiz
        if active_les_id == f"{active_mod_id}-wrapup" and active_mod.get("wrapUpQuiz"):
            render_module_wrapup_quiz(active_mod["wrapUpQuiz"], active_mod_id, t)
            return

        if not active_les:
            st.info(t("Chưa có bài học nào được chọn.", "No lesson currently selected."))
            return

        les_id = active_les["id"]
        les_prog = progress.get(les_id, {"status": "unread", "score": 0, "note": "", "needs_review": False})

        # Top Bar: Lesson Title & Quick Actions
        col_t1, col_t2 = st.columns([3, 1])
        with col_t1:
            st.markdown(f"""
            <div style="margin-bottom: 8px;">
                <span class="zen-badge zen-badge-gold">{t('Bài', 'Lesson')} {active_les.get('lessonNumber', 1)}</span>
                <span class="zen-badge zen-badge-blue">⏱️ {active_les.get('estimatedMinutes', 15)} {t('phút tự học sâu', 'mins study')}</span>
                <span class="zen-badge {'zen-badge-primary' if les_prog.get('status') == 'quiz_passed' else 'zen-badge-pink'}">
                    {'✅ ' + t('Đã làm bài kiểm tra', 'Quiz Passed') if les_prog.get('status') == 'quiz_passed' else ('📖 ' + t('Đã đọc lý thuyết', 'Read') if les_prog.get('status') == 'read' else '⚪ ' + t('Chưa học', 'Unread'))}
                </span>
            </div>
            <h3 style="color: #2F3E34; margin: 4px 0 10px 0;">
                {active_les['titleVi'] if lang_mode != 'en' else active_les['titleEn']}
            </h3>
            """, unsafe_allow_html=True)
        with col_t2:
            st.write("")
            is_rev = les_prog.get("needs_review", False)
            flag_btn_label = "🚩 " + t("Cần Ôn Lại", "Flag Review") if not is_rev else "⛳ " + t("Bỏ Đánh Dấu", "Unflag")
            if st.button(flag_btn_label, key=f"btn_flag_{les_id}", use_container_width=True):
                update_lesson_progress(les_id, needs_review=not is_rev)
                st.toast(t("Đã cập nhật trạng thái cần ôn!", "Updated review flag!"))
                st.rerun()

        # SPECIAL HANDLING FOR MODULE 5: 5-STEP CASE STUDY INTERACTIVE WORKFLOW
        if active_mod_id == "mod-5" and active_les.get("caseWorkflow"):
            render_module_5_case_study_step_by_step(active_les, les_id, les_prog, lang_mode, t)
            render_bottom_navigation(all_modules, active_mod_id, les_id, t)
            return

        # SPECIAL HANDLING FOR MODULE 6: FAQS DIRECTORY
        if active_mod_id == "mod-6" and active_les.get("faqs"):
            render_module_6_faqs(active_les, les_id, lang_mode, t)
            render_bottom_navigation(all_modules, active_mod_id, les_id, t)
            return

        # STANDARD 10-POINT LESSON RENDERING (MODULES 1, 2, 3, 4)
        # 1. MỤC TIÊU HỌC
        st.markdown(f"""
        <div class="zen-card" style="padding: 14px 18px; margin-bottom: 14px; border-left: 4px solid #8BA888;">
            <h4 style="margin: 0 0 6px 0; color: #2F3E34;">🎯 {t('Mục Tiêu Bài Học', 'Learning Objectives')}</h4>
            <ul style="margin: 4px 0 0 20px; font-size: 0.9rem; color: #333; line-height: 1.55;">
                {"".join([f"<li>{obj}</li>" for obj in (active_les.get('objectivesVi', []) if lang_mode != 'en' else active_les.get('objectivesEn', []))])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # 2. TÀI LIỆU NGUỒN VÀ PHIÊN BẢN
        st.markdown(f"""
        <div style="font-size: 0.85rem; color: #7A5C43; background: #FAF7F2; padding: 8px 12px; border-radius: 6px; margin-bottom: 14px; border: 1px dashed #D8C7B5;">
            <b>📜 {t('Căn cứ nguồn & Phiên bản:', 'Source & Version:')}</b> {active_les.get('sourceDocument', '')} | <i>{active_les.get('sourceVersion', '')}</i> | 
            <a href="{active_les.get('sourceLink', '#')}" target="_blank" style="color: #1E4E79; text-decoration: underline;">{t('Đọc tài liệu gốc tại ICF ↗', 'View Original at ICF ↗')}</a>
        </div>
        """, unsafe_allow_html=True)

        # 3 & 4. NỘI DUNG GỐC & BẢN DỊCH TIẾNG VIỆT TRUNG THÀNH
        if lang_mode in ["en", "bilingual"] and active_les.get("originalExcerptEn"):
            st.markdown(f"""
            <div class="zen-card" style="background: #FFFFFF; border-left: 3px solid #1E4E79; margin-bottom: 12px;">
                <span class="zen-badge zen-badge-blue">🇬🇧 Original ICF Language (Authoritative Reference)</span>
                <div style="font-size: 0.92rem; line-height: 1.65; color: #1E3A5F; margin-top: 6px; font-family: Georgia, serif;">
                    {active_les['originalExcerptEn']}
                </div>
            </div>
            """, unsafe_allow_html=True)

        if lang_mode in ["vi", "bilingual"] and active_les.get("translationVi"):
            st.markdown(f"""
            <div class="zen-card" style="background: #FFFFFF; border-left: 3px solid #8BA888; margin-bottom: 14px;">
                <span class="zen-badge zen-badge-primary">🇻🇳 {t('Bản Dịch / Tóm Tắt Tiếng Việt Phục Vụ Học Tập', 'Faithful Vietnamese Translation')}</span>
                <div style="font-size: 0.95rem; line-height: 1.7; color: #2C3E50; margin-top: 6px;">
                    {active_les['translationVi']}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # 5. GIẢI THÍCH DỄ HIỂU (CÓ NHÃN RIÊNG)
        if active_les.get("commentaryVi") or active_les.get("commentaryEn"):
            com_text = active_les.get("commentaryVi") if lang_mode != "en" else active_les.get("commentaryEn")
            st.markdown(f"""
            <div class="zen-card" style="background: #FAFDF9; border-left: 4px solid #8BA888; margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span class="zen-badge zen-badge-gold">💡 {t('Giải Thích Sư Phạm (Diễn Giải Học Tập Của App)', 'Pedagogical Commentary (App Study Notes)')}</span>
                    <span style="font-size: 0.75rem; color: #888;">{t('Không phải văn bản gốc của ICF', 'App Commentary, Not ICF Text')}</span>
                </div>
                <div style="font-size: 0.92rem; line-height: 1.65; color: #3F4F44;">
                    {com_text}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # 6. VÍ DỤ ỨNG DỤNG THỰC TẾ
        if active_les.get("exampleContentVi") or active_les.get("exampleContentEn"):
            ex_text = active_les.get("exampleContentVi") if lang_mode != "en" else active_les.get("exampleContentEn")
            st.markdown(f"""
            <div class="zen-card" style="background: #FAF7F2; border-left: 3px solid #9C4158; margin-bottom: 14px;">
                <span class="zen-badge zen-badge-pink">🎭 {active_les.get('exampleType', 'Ví dụ tự soạn')}</span>
                <div style="font-size: 0.92rem; line-height: 1.6; color: #4A3E3D; margin-top: 6px;">
                    {ex_text}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # 7 & 8. CÂU HỎI TỰ KIỂM TRA & PHÂN TÍCH ĐÁP ÁN SAU KHI NỘP
        if active_les.get("quiz"):
            quiz = active_les["quiz"]
            q_text = quiz["questionVi"] if lang_mode != "en" else quiz["questionEn"]
            opts = quiz.get("options", [])
            opt_dict = {o["key"]: f"[{o['key']}] {o['textVi'] if lang_mode != 'en' else o['textEn']}" for o in opts}

            st.markdown(f"""
            <div class="zen-card" style="margin-top: 18px; border: 1px solid #D8C7B5;">
                <span class="zen-badge zen-badge-primary">📝 {t('Câu Hỏi Tự Kiểm Tra Hiểu Chuẩn', 'Self-Check Mastery Question')}</span>
                <div style="font-size: 0.98rem; font-weight: 600; color: #2F3E34; margin: 8px 0 12px 0;">
                    {q_text}
                </div>
            </div>
            """, unsafe_allow_html=True)

            radio_key = f"quiz_radio_{les_id}"
            user_choice = st.radio(
                t("Chọn đáp án của bạn:", "Select your answer:"),
                options=list(opt_dict.keys()),
                format_func=lambda k: opt_dict[k],
                key=radio_key,
                index=None
            )

            col_sub, col_reset = st.columns([1, 3])
            with col_sub:
                if st.button("📤 " + t("Nộp Bài", "Submit Answer"), key=f"btn_sub_{les_id}", type="primary"):
                    if not user_choice:
                        st.warning(t("Vui lòng chọn một đáp án trước khi nộp!", "Please choose an answer before submitting!"))
                    else:
                        is_corr = (user_choice == quiz.get("correctAnswer"))
                        if is_corr:
                            update_lesson_progress(les_id, status="quiz_passed", score=100)
                            st.balloons()
                            st.success(f"🎉 {t('CHÍNH XÁC 100%!', 'CORRECT!')} {t('Bạn đã nắm vững chuẩn mực bài học này và nở thêm 1 đóa sen chánh niệm!', 'You mastered this standard and bloomed a lotus!')}")
                        else:
                            update_lesson_progress(les_id, status="read", score=0)
                            st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án chuẩn xác là:', 'Correct answer is:')} **{quiz.get('correctAnswer')}**.")
                        
                        st.markdown(f"""
                        <div style="background: #FAF7F2; padding: 14px; border-radius: 8px; border-left: 3px solid #8BA888; margin-top: 8px;">
                            <b>💡 {t('Phân tích đáp án chuẩn mực:', 'Answer Rationale:')}</b><br/>
                            {quiz.get('explanationVi') if lang_mode != 'en' else quiz.get('explanationEn')}
                        </div>
                        """, unsafe_allow_html=True)

        # 9. GHI CHÚ CÁ NHÂN
        st.markdown(f"#### 📓 {t('Sổ Tay Ghi Chú Cá Nhân Cho Bài Học Này', 'Personal Study Notes')}")
        current_note = les_prog.get("note", "")
        updated_note = st.text_area(
            t("Ghi chú của bạn (tự động lưu khi bấm nút bên dưới):", "Your reflections:"),
            value=current_note,
            height=100,
            key=f"note_area_{les_id}"
        )
        if st.button("💾 " + t("Lưu Ghi Chú", "Save Note"), key=f"btn_save_note_{les_id}"):
            update_lesson_progress(les_id, note=updated_note)
            st.toast(t("Đã lưu ghi chú thành công!", "Note saved successfully!"))

        # 10. NÚT HOÀN THÀNH & CHUYỂN BÀI TIẾP THEO
        render_bottom_navigation(all_modules, active_mod_id, les_id, t)

def render_bottom_navigation(all_modules, cur_mod_id, cur_les_id, t_func):
    """Handles strict sequential progression across modules 1 to 7"""
    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 20px 0;'/>", unsafe_allow_html=True)
    
    # Flatten all lessons across all modules
    flat_lessons = []
    for mod in all_modules:
        for les in mod.get("lessons", []):
            flat_lessons.append((mod["id"], les["id"]))

    cur_tuple = (cur_mod_id, cur_les_id)
    cur_idx = -1
    for idx, item in enumerate(flat_lessons):
        if item == cur_tuple:
            cur_idx = idx
            break

    c_b1, c_b2, c_b3 = st.columns(3)
    with c_b1:
        if cur_idx > 0:
            prev_mod, prev_les = flat_lessons[cur_idx - 1]
            if st.button("⬅️ " + t("Bài Trước", "Previous Lesson"), key=f"btn_prev_{cur_les_id}", use_container_width=True):
                set_page("curriculum", module_id=prev_mod, lesson_id=prev_les)
                st.rerun()

    with c_b2:
        if st.button("✅ " + t("Đánh Dấu Đã Đọc Xong", "Mark as Read"), key=f"btn_mark_read_{cur_les_id}", use_container_width=True):
            update_lesson_progress(cur_les_id, status="read")
            st.toast(t("Đã ghi nhận hoàn thành việc đọc bài!", "Recorded reading completion!"))
            st.rerun()

    with c_b3:
        if cur_idx >= 0 and cur_idx < len(flat_lessons) - 1:
            next_mod, next_les = flat_lessons[cur_idx + 1]
            if st.button("➡️ " + t("Bài Tiếp Theo", "Next Lesson"), key=f"btn_next_{cur_les_id}", type="primary", use_container_width=True):
                # Mark current as read if unread
                prog = st.session_state.curriculum_progress.get(cur_les_id, {})
                if prog.get("status") == "unread":
                    update_lesson_progress(cur_les_id, status="read")
                set_page("curriculum", module_id=next_mod, lesson_id=next_les)
                st.rerun()
        else:
            if st.button("🏆 " + t("Hoàn Thành Lộ Trình", "Finish Pathway"), key=f"btn_finish_{cur_les_id}", type="primary", use_container_width=True):
                st.balloons()
                st.success(t("Chúc mừng bạn đã hoàn thành trọn vẹn toàn bộ các học phần chuẩn mực ICF!",
                             "Congratulations on completing the entire official ICF curriculum!"))

def render_module_wrapup_quiz(wrapup_data, mod_id, t_func):
    """Renders comprehensive end-of-module assessment quiz"""
    st.markdown(f"""
    <div class="zen-card" style="border-left: 4px solid #8BA888; margin-bottom: 16px;">
        <span class="zen-badge zen-badge-gold">🏆 {t('Bài Kiểm Tra Ôn Tập Tổng Hợp Học Phần', 'Comprehensive Module Review')}</span>
        <h3 style="color: #2F3E34; margin: 8px 0 4px 0;">{wrapup_data['titleVi'] if st.session_state.lang == 'vi' else wrapup_data['titleEn']}</h3>
        <p style="font-size: 0.9rem; color: #666;">
            {t('Bài kiểm tra tổng hợp kiểm tra năng lực phán đoán và sự kết nối giữa các bài học trong học phần.',
               'Integrated assessment evaluating judgment and cross-lesson competency synthesis.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    for q_idx, q in enumerate(wrapup_data.get("questions", [])):
        st.markdown(f"""
        <div class="zen-card" style="padding: 16px; margin-bottom: 12px;">
            <b>{q_idx + 1}. {q['questionVi'] if st.session_state.lang == 'vi' else q['questionEn']}</b>
        </div>
        """, unsafe_allow_html=True)
        opts = q.get("options", [])
        opt_dict = {o["key"]: f"[{o['key']}] {o['textVi'] if st.session_state.lang == 'vi' else o['textEn']}" for o in opts}
        chosen = st.radio(f"Đáp án câu {q_idx+1}:", options=list(opt_dict.keys()), format_func=lambda k: opt_dict[k], key=f"wrapup_{mod_id}_{q['id']}", index=None)
        if chosen:
            if chosen == q["correctAnswer"]:
                st.success(f"✅ {t('Chính xác!', 'Correct!')} {q.get('explanationVi', '')}")
            else:
                st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer:')} **{q['correctAnswer']}**.\n\n{q.get('explanationVi', '')}")

def render_module_5_case_study_step_by_step(active_les, les_id, les_prog, lang_mode, t_func):
    """Renders authentic 5-step ICF Ethics Case Study with hidden source analysis until revealed"""
    cw = active_les["caseWorkflow"]

    st.markdown(f"""
    <div class="zen-card" style="border-left: 4px solid #9C4158; margin-bottom: 16px;">
        <span class="zen-badge zen-badge-pink">🎭 {t('Quy Trình Học 5 Bước Chuẩn ICF Ethics', 'ICF 5-Step Ethics Case Study Process')}</span>
        <h3 style="color: #2F3E34; margin: 8px 0;">{active_les['titleVi'] if lang_mode != 'en' else active_les['titleEn']}</h3>
        <p style="font-size: 0.85rem; color: #7A5C43; margin-bottom: 0;">
            📜 <b>Nguồn gốc:</b> {active_les.get('sourceDocument')} ({active_les.get('sourceVersion')})
        </p>
    </div>
    """, unsafe_allow_html=True)

    # BƯỚC 1: ĐỌC TÌNH HUỐNG
    st.markdown(f"""
    <div class="zen-card" style="border-left: 3px solid #8BA888; margin-bottom: 14px;">
        <h4 style="color: #2F3E34; margin-top: 0;">📍 Bước 1: Đọc Kịch Bản Tình Huống Tiến Thoái Lưỡng Nan</h4>
        <div style="font-size: 0.95rem; line-height: 1.7; color: #2C3E50;">
            {cw['step1_scenarioVi'] if lang_mode != 'en' else cw['step1_scenarioEn']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # BƯỚC 2: TỰ NHẬN DIỆN VẤN ĐỀ VÀ CÁC BÊN LIÊN QUAN
    with st.expander("🔍 Bước 2: Nhận diện các bên liên quan và ranh giới quyền lợi", expanded=True):
        st.markdown(f"""
        <div style="font-size: 0.92rem; line-height: 1.6; color: #444;">
            {cw['step2_stakeholdersVi'] if lang_mode != 'en' else cw['step2_stakeholdersEn']}
        </div>
        """, unsafe_allow_html=True)

    # BƯỚC 3: GHI CÁCH CÂN NHẮC VÀ PHƯƠNG ÁN XỬ LÝ
    st.markdown(f"#### ✍️ Bước 3: Ghi Nhận Cách Bạn Sẽ Cân Nhắc / Xử Lý Tình Huống Này")
    user_handling = st.text_area(
        cw['step3_selfReflectionPromptVi'] if lang_mode != 'en' else cw['step3_selfReflectionPromptEn'],
        height=120,
        key=f"case_input_{les_id}",
        placeholder=t("Hãy viết ra cách xử lý của riêng bạn trước khi mở phân tích của nguồn...",
                      "Draft your own ethical solution before opening the source analysis...")
    )

    # BƯỚC 4: MỞ PHẦN PHÂN TÍCH CỦA NGUỒN (CHỈ HIỆN KHI NGƯỜI HỌC CHỌN MỞ)
    st.markdown("#### 🔓 Bước 4: Khám Phá Phân Tích Chuẩn Mực Từ ICF")
    show_analysis = st.checkbox("👉 " + t("Mở phần phân tích đạo đức chính thức từ nguồn ICF", "Reveal official ICF ethical analysis"), key=f"chk_reveal_{les_id}")
    
    if show_analysis:
        st.markdown(f"""
        <div class="zen-card" style="background: #FAFDF9; border: 2px solid #8BA888; padding: 18px; margin: 12px 0;">
            <span class="zen-badge zen-badge-primary">🏛️ {t('Phân Tích Đạo Đức Chính Thức', 'Official Ethical Analysis')}</span>
            <div style="font-size: 0.95rem; line-height: 1.7; color: #2C3E50; margin-top: 8px; white-space: pre-line;">
                {cw['step4_sourceAnalysisVi'] if lang_mode != 'en' else cw['step4_sourceAnalysisEn']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # BƯỚC 5: SO SÁNH VÀ ĐÚC KẾT ĐIỀU HỌC ĐƯỢC
        st.markdown(f"""
        <div class="zen-quote-box" style="margin-top: 14px;">
            <b>💡 Bước 5: Điểm Cốt Lõi Cần Nhớ (Key Takeaway):</b><br/>
            {cw['step5_takeawaysVi']}
        </div>
        """, unsafe_allow_html=True)

    # Case study quiz
    if active_les.get("quiz"):
        quiz = active_les["quiz"]
        st.markdown("---")
        st.markdown(f"**📝 {t('Câu hỏi phán đoán tình huống:', 'Judgment Question:')}** {quiz['questionVi'] if lang_mode != 'en' else quiz['questionEn']}")
        opts = quiz.get("options", [])
        opt_dict = {o["key"]: f"[{o['key']}] {o['textVi'] if lang_mode != 'en' else o['textEn']}" for o in opts}
        chosen = st.radio(t("Chọn phương án:", "Choose option:"), options=list(opt_dict.keys()), format_func=lambda k: opt_dict[k], key=f"case_qz_{les_id}", index=None)
        if chosen:
            if chosen == quiz["correctAnswer"]:
                update_lesson_progress(les_id, status="quiz_passed", score=100)
                st.success(f"✅ {t('Chính xác!', 'Correct!')} {quiz.get('explanationVi', '')}")
            else:
                st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer:')} **{quiz['correctAnswer']}**.\n\n{quiz.get('explanationVi', '')}")

def render_module_6_faqs(active_les, les_id, lang_mode, t_func):
    """Renders categorized ICF FAQs with explicit official vs synthesized tags and verified dates"""
    st.markdown(f"""
    <div class="zen-card" style="border-left: 4px solid #1E4E79; margin-bottom: 16px;">
        <span class="zen-badge zen-badge-blue">❓ {t('Hỏi Đáp Chuẩn Mực ICF', 'Official ICF FAQs Hub')}</span>
        <h3 style="color: #2F3E34; margin: 8px 0;">{active_les['titleVi'] if lang_mode != 'en' else active_les['titleEn']}</h3>
        <p style="font-size: 0.85rem; color: #555; margin-bottom: 0;">
            📜 <b>{t('Nguồn gốc:', 'Source:')}</b> {active_les.get('sourceDocument')} ({active_les.get('sourceVersion')}) | 
            <a href="{active_les.get('sourceLink')}" target="_blank" style="color: #1E4E79; text-decoration: underline;">{t('Đọc bài viết gốc trên ICF Blog ↗', 'Read Original on ICF Blog ↗')}</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    faqs = active_les.get("faqs", [])
    for faq in faqs:
        badge_cls = "zen-badge-primary" if faq["tag"] == "Official ICF FAQ" else "zen-badge-gold"
        with st.expander(f"📌 [{faq['tag']}] {faq['questionVi'] if lang_mode != 'en' else faq['questionEn']}", expanded=True):
            st.markdown(f"""
            <div style="margin-bottom: 6px;">
                <span class="zen-badge {badge_cls}">{faq['tag']}</span>
                <span class="zen-badge zen-badge-blue">Tiêu chuẩn: {faq.get('relatedStandard', '')}</span>
                <span class="zen-badge zen-badge-gold">Xác minh: {faq.get('verifiedDate', '06/11/2026')}</span>
            </div>
            <div style="font-size: 0.95rem; line-height: 1.7; color: #2C3E50; margin-top: 8px;">
                <b>{t('Câu trả lời chuẩn mực:', 'Answer:')}</b><br/>
                {faq['answerVi'] if lang_mode != 'en' else faq['answerEn']}
            </div>
            """, unsafe_allow_html=True)

    # Self check quiz for FAQ
    if active_les.get("quiz"):
        quiz = active_les["quiz"]
        st.markdown("---")
        st.markdown(f"**📝 {t('Câu hỏi tự kiểm tra:', 'Self-Check Question:')}** {quiz['questionVi'] if lang_mode != 'en' else quiz['questionEn']}")
        opts = quiz.get("options", [])
        opt_dict = {o["key"]: f"[{o['key']}] {o['textVi'] if lang_mode != 'en' else o['textEn']}" for o in opts}
        chosen = st.radio(t("Chọn phương án:", "Choose option:"), options=list(opt_dict.keys()), format_func=lambda k: opt_dict[k], key=f"faq_qz_{les_id}", index=None)
        if chosen:
            if chosen == quiz["correctAnswer"]:
                update_lesson_progress(les_id, status="quiz_passed", score=100)
                st.success(f"✅ {t('Chính xác!', 'Correct!')} {quiz.get('explanationVi', '')}")
            else:
                st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer:')} **{quiz['correctAnswer']}**.\n\n{quiz.get('explanationVi', '')}")

def render_module_7_glossary(t_func):
    """Renders comprehensive Glossary with accent-insensitive search, EN/VI lookup, flashcards, and near-synonym exercises"""
    st.markdown(f"""
    <div class="zen-card" style="border-left: 4px solid #8BA888; margin-bottom: 18px;">
        <span class="zen-badge zen-badge-primary">📖 {t('Từ Điển Thuật Ngữ & Định Nghĩa Chuẩn ICF', 'Official ICF Glossary & Lexicon')}</span>
        <h3 style="color: #2F3E34; margin: 8px 0;">{t('Tra Cứu Thuật Ngữ & Bài Tập Phân Biệt Từ Gần Nghĩa', 'Terminology Search & Disambiguation Drills')}</h3>
        <p style="font-size: 0.9rem; color: #5F6F65; line-height: 1.6;">
            {t('Tập hợp các định nghĩa chính thức từ Code of Ethics, 8 Năng lực Cốt lõi và White Paper Chuyển gửi. Hỗ trợ tìm kiếm tiếng Việt không dấu, tìm bằng tiếng Anh hoặc tiếng Việt, lật thẻ flashcard và làm bài tập phân biệt các cặp từ dễ nhầm lẫn.',
               'Authoritative glossary from ICF Code of Ethics, Core Competencies and Referral White Paper. Features accent-folding search, EN/VI lookup, Leitner flashcards and near-synonym exercises.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_search, tab_fc, tab_ex = st.tabs([
        "🔍 " + t("Tra Cứu Thuật Ngữ", "Search Terms"),
        "🗂️ " + t("Luyện Flashcard Từ Vựng", "Vocabulary Flashcards"),
        "⚖️ " + t("Bài Tập Phân Biệt Từ Gần Nghĩa", "Disambiguation Drills")
    ])

    # SUB-TAB 1: SEARCH
    with tab_search:
        search_kw = st.text_input(
            "🔍 " + t("Tìm kiếm thuật ngữ (hỗ trợ gõ không dấu, tiếng Anh hoặc tiếng Việt):", "Search terms (accent-insensitive, EN or VI):"),
            placeholder=t("Ví dụ: khach hang, client, sponsor, xung dot loi ich, holding space, imminent harm...",
                          "e.g., client, sponsor, conflict of interest, autonomy, holding space...")
        )
        
        results = search_glossary(search_kw)
        st.markdown(f"<div style='font-size: 0.85rem; color: #8C6D53; margin-bottom: 10px;'>{t('Tìm thấy', 'Found')} {len(results)} {t('thuật ngữ phù hợp', 'matching terms')}</div>", unsafe_allow_html=True)

        for term in results:
            tag_cls = "zen-badge-primary" if term["isOfficial"] else "zen-badge-gold"
            tag_name = "Định nghĩa chính thức ICF" if term["isOfficial"] else "Thuật ngữ hỗ trợ (Diễn giải học tập)"
            
            st.markdown(f"""
            <div class="zen-card" style="padding: 14px 18px; margin-bottom: 12px; border-left: 3px solid {'#8BA888' if term['isOfficial'] else '#C4785A'};">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <h4 style="margin: 0; color: #2F3E34;">
                        {term['termVi']} <span style="font-size: 0.9rem; color: #8C6D53;">({term['termEn']})</span>
                    </h4>
                    <span class="zen-badge {tag_cls}" style="font-size: 0.72rem;">{tag_name}</span>
                </div>
                <div style="font-size: 0.92rem; color: #2C3E50; margin: 8px 0 4px 0; line-height: 1.55;">
                    <b>{t('Định nghĩa tiếng Việt:', 'Vietnamese Definition:')}</b> {term['definitionVi']}
                </div>
                <div style="font-size: 0.88rem; color: #1E3A5F; font-family: Georgia, serif; line-height: 1.5;">
                    <b>English:</b> {term['definitionEn']}
                </div>
                <div style="font-size: 0.8rem; color: #777; margin-top: 6px;">
                    📜 <b>Nguồn:</b> {term['source']} ({term['version']}) | <b>Từ gần nghĩa dễ nhầm:</b> {", ".join(term.get('nearSynonyms', []))}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # SUB-TAB 2: FLASHCARDS FOR GLOSSARY
    with tab_fc:
        all_terms = get_glossary_terms()
        fc_idx = st.session_state.get("fc_glossary_idx", 0) % len(all_terms)
        cur_t = all_terms[fc_idx]
        is_flip = st.session_state.get("fc_glossary_flip", False)

        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span class="zen-badge zen-badge-primary">Thẻ {fc_idx + 1} / {len(all_terms)}</span>
            <span class="zen-badge {'zen-badge-primary' if cur_t['isOfficial'] else 'zen-badge-gold'}">
                {'Chính thức ICF' if cur_t['isOfficial'] else 'Thuật ngữ hỗ trợ'}
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="flashcard-box" style="background: {'#FAFDF9' if is_flip else '#FFFFFF'}; border-color: {'#8BA888' if is_flip else '#D8C7B5'};">
            <div style="font-size: 0.82rem; color: #8C6D53; font-weight: 600; margin-bottom: 8px;">
                {'🔄 MẶT SAU: ĐỊNH NGHĨA CHUẨN MỰC' if is_flip else '❓ MẶT TRƯỚC: THUẬT NGỮ'}
            </div>
            <div style="font-size: 1.3rem; color: #2F3E34; font-weight: 600;">
                {cur_t['termVi'] + ' (' + cur_t['termEn'] + ')' if not is_flip else cur_t['definitionVi']}
            </div>
            {f'<div style="font-size: 0.9rem; color: #1E3A5F; margin-top: 8px; font-family: Georgia, serif;">{cur_t["definitionEn"]}</div>' if is_flip else ''}
        </div>
        """, unsafe_allow_html=True)

        c_fl1, c_fl2, c_fl3 = st.columns([1, 2, 1])
        with c_fl2:
            flip_lbl = "🔄 " + t("Lật Thẻ Xem Định Nghĩa", "Flip Card") if not is_flip else "↩️ " + t("Lật Lại", "Flip Back")
            if st.button(flip_lbl, use_container_width=True, type="primary", key="btn_flip_gl"):
                st.session_state.fc_glossary_flip = not is_flip
                st.rerun()

        c_n1, c_n2 = st.columns(2)
        with c_n1:
            if st.button("⬅️ " + t("Thẻ Trước", "Previous"), use_container_width=True, key="btn_prev_gl"):
                st.session_state.fc_glossary_idx = (fc_idx - 1) % len(all_terms)
                st.session_state.fc_glossary_flip = False
                st.rerun()
        with c_n2:
            if st.button("➡️ " + t("Thẻ Kế Tiếp", "Next"), use_container_width=True, key="btn_next_gl"):
                st.session_state.fc_glossary_idx = (fc_idx + 1) % len(all_terms)
                st.session_state.fc_glossary_flip = False
                st.rerun()

    # SUB-TAB 3: DISAMBIGUATION DRILLS
    with tab_ex:
        from scripts.icf_curriculum_data import GLOSSARY_EXERCISES
        st.markdown(f"#### ⚖️ {t('Bài Tập Phân Biệt Các Cặp Từ Gần Nghĩa / Dễ Nhầm Lẫn', 'Near-Synonym Disambiguation Drills')}")
        for ex_idx, ex in enumerate(GLOSSARY_EXERCISES):
            st.markdown(f"""
            <div class="zen-card" style="padding: 14px 18px; margin-bottom: 12px; border-left: 3px solid #8BA888;">
                <span class="zen-badge zen-badge-pink">Cặp từ: {ex['termPair']}</span>
                <div style="font-weight: 600; color: #2F3E34; margin: 8px 0;">
                    {ex_idx + 1}. {ex['questionVi'] if st.session_state.lang == 'vi' else ex['questionEn']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            opts = ex.get("options", [])
            opt_d = {o["key"]: f"[{o['key']}] {o['textVi'] if st.session_state.lang == 'vi' else o['textEn']}" for o in opts}
            chosen = st.radio(f"Đáp án bài {ex_idx+1}:", options=list(opt_d.keys()), format_func=lambda k: opt_d[k], key=f"gl_ex_{ex['id']}", index=None)
            if chosen:
                if chosen == ex["correctAnswer"]:
                    st.success(f"✅ {t('Chính xác!', 'Correct!')} {ex.get('explanationVi')}")
                else:
                    st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer:')} **{ex['correctAnswer']}**.\n\n{ex.get('explanationVi')}")
