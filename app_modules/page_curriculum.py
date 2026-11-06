# -*- coding: utf-8 -*-
"""
Curriculum Page for Mentor Thi (PCC Learning & Practice)
10 Leaf Study Units (9 Core Competencies Units + 1 Special Referral Topic Unit)
Features 6 Tabs: Theory (with 7 sub-lessons for special topic), Keywords, 10 Flashcards, Case Study, 10 Quizzes, Notes.
"""
import streamlit as st

def render_curriculum_page(DATA, STUDY_SECTIONS, THEORIES, KEYWORDS, FLASHCARDS, CASE_STUDIES, QUIZZES, t):
    sec_id = st.session_state.current_section
    sec_dict = {s["id"]: s for s in STUDY_SECTIONS}
    if sec_id not in sec_dict and STUDY_SECTIONS:
        sec_id = STUDY_SECTIONS[0]["id"]
        st.session_state.current_section = sec_id

    curr_sec = sec_dict.get(sec_id, STUDY_SECTIONS[0] if STUDY_SECTIONS else {})
    if not curr_sec:
        st.info("Chưa có dữ liệu bài học.")
        return

    st.markdown(f"""
    <div style="margin-bottom: 16px;">
        <span class="zen-badge zen-badge-primary">📚 {t('Lộ Trình Học Tập Tỉnh Thức', 'Mindful Curriculum Path')}</span>
        <h2 style="margin: 6px 0; color: #2F3E34;">{curr_sec['titleVi'] if st.session_state.lang == 'vi' else curr_sec['titleEn']}</h2>
        <div style="font-size: 0.88rem; color: #8C6D53;">
            ⏱️ {curr_sec.get('estimatedMinutes', 25)} {t('phút tự học sâu', 'mins deep study')} | 🗂️ 10 Flashcards | 📝 10 Mini Quizzes
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section Selector
    sec_options = [s["id"] for s in STUDY_SECTIONS]
    def format_sec(sid):
        s = sec_dict[sid]
        prefix = "🌟 [CHUYÊN ĐỀ] " if "referral" in sid else f"[{s['id']}] "
        return f"{prefix}{s['titleVi'] if st.session_state.lang == 'vi' else s['titleEn']}"

    chosen_sec = st.selectbox(
        "🌿 " + t("Chọn bài học năng lực hoặc chuyên đề:", "Select study unit or special topic:"),
        options=sec_options,
        index=sec_options.index(sec_id) if sec_id in sec_options else 0,
        format_func=format_sec
    )
    if chosen_sec != st.session_state.current_section:
        st.session_state.current_section = chosen_sec
        st.session_state.fc_index = 0
        st.session_state.fc_flipped = False
        st.rerun()

    # Filter data for this section
    theory = THEORIES.get(sec_id, {})
    sec_keywords = [kw for kw in KEYWORDS if kw.get("sectionId") == sec_id]
    sec_flashcards = [fc for fc in FLASHCARDS if fc.get("sectionId") == sec_id]
    sec_case = CASE_STUDIES.get(sec_id, {})
    sec_quizzes = [qz for qz in QUIZZES if qz.get("sectionId") == sec_id]

    # If referral section, dynamically harvest terms from the 7 lessons if sec_keywords is empty
    if sec_id == "sec-referral-special" and not sec_keywords and theory.get("lessons"):
        for les in theory.get("lessons", []):
            for tm in les.get("terms", []):
                sec_keywords.append({
                    "sectionId": "sec-referral-special",
                    "termVi": tm["vi"],
                    "termEn": tm["en"],
                    "definitionVi": tm["desc"],
                    "definitionEn": tm["desc"],
                    "contextVi": f"Trích xuất từ {les['titleVi']} ({les.get('pdfLocation', '')})"
                })

    tab_th, tab_kw, tab_fc, tab_cs, tab_qz, tab_note = st.tabs([
        "📖 " + t("Lý Thuyết Chuẩn", "Theory"),
        f"🏷️ {t('Từ Vựng & Khái Niệm', 'Keywords')} ({len(sec_keywords)})",
        f"🗂️ {t('10 Thẻ Flashcard', '10 Flashcards')} ({len(sec_flashcards)})",
        "🎭 " + t("Tình Huống Thực Tế", "Case Study"),
        f"📝 {t('10 Mini Quiz', '10 Mini Quizzes')} ({len(sec_quizzes)})",
        "📓 " + t("Sổ Tay Ghi Chú", "Study Notes")
    ])

    # TAB 1: THEORY
    with tab_th:
        if theory:
            # If the theory has structured lessons (like the 7 referral lessons)
            if theory.get("lessons"):
                st.markdown(f"""
                <div class="zen-card" style="margin-bottom: 14px; border-left: 4px solid #9C4158;">
                    <h3 style="color: #2F3E34; margin: 0 0 6px 0;">{theory.get('titleVi', '') if st.session_state.lang == 'vi' else theory.get('titleEn', '')}</h3>
                    <p style="font-size: 0.85rem; color: #8C6D53; margin: 0;">
                        <i>* Căn cứ nghiên cứu: Hullinger & DiGirolamo (2018). Bản dịch phục vụ học tập, không phải bản dịch chính thức của ICF.</i>
                    </p>
                </div>
                """, unsafe_allow_html=True)

                lesson_titles = [f"{les['titleVi']} ({les.get('pdfLocation', '')})" for les in theory["lessons"]]
                chosen_lesson_idx = st.selectbox(
                    "📑 " + t("Chọn bài học trong chuyên đề (1–7):", "Select lesson in special topic (1–7):"),
                    options=range(len(lesson_titles)),
                    format_func=lambda idx: lesson_titles[idx]
                )
                selected_lesson = theory["lessons"][chosen_lesson_idx]

                st.markdown(f"""
                <div class="zen-card" style="border-left: 3px solid #8BA888;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <span class="zen-badge zen-badge-primary">Bài {selected_lesson.get('lessonNumber', chosen_lesson_idx + 1)} / 7</span>
                        <span class="zen-badge zen-badge-gold">{selected_lesson.get('pdfLocation', '')}</span>
                    </div>
                    <h4 style="color: #2F3E34; margin-top: 0;">
                        {selected_lesson.get('titleVi', '') if st.session_state.lang == 'vi' else selected_lesson.get('titleEn', '')}
                    </h4>
                    <div style="font-size: 0.95rem; line-height: 1.7; color: #2C3E50;">
                        {selected_lesson.get('contentVi', '') if st.session_state.lang == 'vi' else selected_lesson.get('contentEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if selected_lesson.get("terms"):
                    st.markdown(f"##### 🏷️ {t('Thuật ngữ then chốt bài này:', 'Key Terms in this Lesson:')}")
                    for tm in selected_lesson["terms"]:
                        st.markdown(f"- **{tm['vi']}** *({tm['en']})*: {tm['desc']}")

            else:
                st.markdown(f"""
                <div class="zen-card">
                    <h3 style="color: #2F3E34; margin-top: 0;">{theory.get('titleVi', '') if st.session_state.lang == 'vi' else theory.get('titleEn', '')}</h3>
                    <div style="font-size: 0.95rem; line-height: 1.7; color: #2C3E50;">
                        {theory.get('contentVi', '') if st.session_state.lang == 'vi' else theory.get('contentEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            if theory.get("keyPointsVi") or theory.get("keyPointsEn"):
                points = theory.get("keyPointsVi", []) if st.session_state.lang == "vi" else theory.get("keyPointsEn", [])
                st.markdown(f"#### 💡 {t('Các điểm cốt lõi cần nhớ:', 'Essential Key Takeaways:')}")
                for p in points:
                    st.markdown(f"- {p}")
        else:
            st.info(t("Nội dung bài giảng đang được đồng bộ.", "Theory content is being synced."))

    # TAB 2: KEYWORDS
    with tab_kw:
        st.markdown(f"#### 🏷️ {t('Neo Khái Niệm & Từ Khóa Cốt Lõi', 'Conceptual Anchors & Core Terms')}")
        if sec_keywords:
            for kw in sec_keywords:
                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 12px; border-left: 3px solid #8BA888;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin: 0; color: #2F3E34;">{kw['termVi']} <span style="font-size: 0.85rem; color: #8C6D53;">({kw['termEn']})</span></h4>
                    </div>
                    <div style="font-size: 0.9rem; color: #555; margin-top: 6px; line-height: 1.5;">
                        <b>{t('Định nghĩa:', 'Definition:')}</b> {kw['definitionVi'] if st.session_state.lang == 'vi' else kw['definitionEn']}<br/>
                        <b>{t('Ứng dụng trong tình huống:', 'In Situational Context:')}</b> {kw.get('contextVi', '') if st.session_state.lang == 'vi' else kw.get('contextEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info(t("Không có từ khóa riêng cho bài này.", "No specific keywords recorded for this unit."))

    # TAB 3: 10 FLASHCARDS (LEITNER BOX)
    with tab_fc:
        if sec_flashcards:
            fc_idx = st.session_state.fc_index % len(sec_flashcards)
            card = sec_flashcards[fc_idx]

            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span class="zen-badge zen-badge-primary">{t('Thẻ', 'Card')} {fc_idx + 1} / {len(sec_flashcards)}</span>
                <span class="zen-badge zen-badge-gold">{t('Hộp Leitner', 'Leitner Box')}: {card.get('box', 1)}</span>
                {f'<span class="zen-badge zen-badge-blue">Nguồn: {card["source"]}</span>' if card.get("source") else ''}
            </div>
            """, unsafe_allow_html=True)

            is_flipped = st.session_state.fc_flipped
            front_text = card["frontVi"] if st.session_state.lang == "vi" else card["frontEn"]
            back_text = card["backVi"] if st.session_state.lang == "vi" else card["backEn"]

            # Flashcard container
            st.markdown(f"""
            <div class="flashcard-box" style="background: {'#FAF7F2' if is_flipped else '#FFFFFF'}; border-color: {'#8BA888' if is_flipped else '#D8C7B5'};">
                <div style="font-size: 0.82rem; color: #8C6D53; font-weight: 600; margin-bottom: 8px;">
                    {'🔄 ' + t('MẶT SAU (LÝ GIẢI & ĐÁP ÁN)', 'BACK (EXPLANATION & ANSWER)') if is_flipped else '❓ ' + t('MẶT TRƯỚC (CÂU HỎI TƯ DUY)', 'FRONT (PROMPT / QUESTION)')}
                </div>
                <div style="font-size: 1.15rem; color: #2F3E34; line-height: 1.6; max-width: 650px;">
                    {back_text if is_flipped else front_text}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Flip button
            st.write("")
            col_flip1, col_flip2, col_flip3 = st.columns([1, 2, 1])
            with col_flip2:
                flip_btn_label = "🔄 " + t("Lật Thẻ / Xem Mặt Sau", "Flip Card / Reveal Back") if not is_flipped else "↩️ " + t("Lật Lại Mặt Trước", "Flip Back to Front")
                if st.button(flip_btn_label, use_container_width=True, type="primary"):
                    st.session_state.fc_flipped = not st.session_state.fc_flipped
                    st.rerun()

            col_nav1, col_nav2, col_nav3 = st.columns(3)
            with col_nav1:
                if st.button("⬅️ " + t("Thẻ Trước", "Previous Card"), use_container_width=True):
                    st.session_state.fc_index = (fc_idx - 1) % len(sec_flashcards)
                    st.session_state.fc_flipped = False
                    st.rerun()
            with col_nav2:
                if st.button("🌱 " + t("Đã Nắm Vững (+1 Sen)", "Mastered (+1 Lotus)"), use_container_width=True):
                    card["box"] = min(card.get("box", 1) + 1, 3)
                    st.session_state.lotus_bloomed += 1
                    st.toast(t("Đã chuyển thẻ sang Hộp tiếp theo!", "Card moved to next Leitner Box!"))
                    st.session_state.fc_index = (fc_idx + 1) % len(sec_flashcards)
                    st.session_state.fc_flipped = False
                    st.rerun()
            with col_nav3:
                if st.button("➡️ " + t("Thẻ Kế Tiếp", "Next Card"), use_container_width=True):
                    st.session_state.fc_index = (fc_idx + 1) % len(sec_flashcards)
                    st.session_state.fc_flipped = False
                    st.rerun()
        else:
            st.info(t("Chưa có thẻ flashcard cho bài này.", "No flashcards found for this unit."))

    # TAB 4: CASE STUDY
    with tab_cs:
        if sec_case:
            sc_text = sec_case.get('scenarioVi', sec_case.get('contextVi', '')) if st.session_state.lang == 'vi' else sec_case.get('scenarioEn', sec_case.get('contextEn', ''))
            
            st.markdown(f"""
            <div class="zen-card">
                <span class="zen-badge zen-badge-pink">🎭 {t('Tình Huống Thực Tế & Luyện Tư Duy Phán Đoán', 'Real Case Study & Judgment Drill')}</span>
                <h3 style="color: #2F3E34; margin: 10px 0;">{sec_case.get('titleVi', '') if st.session_state.lang == 'vi' else sec_case.get('titleEn', '')}</h3>
                <div style="background: #FAF7F2; padding: 16px; border-radius: 10px; margin-bottom: 14px; border-left: 3px solid #8BA888;">
                    <b>{t('Bối cảnh khách hàng:', 'Client Scenario:')}</b><br/>
                    {sc_text}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # If dialogue exists (interactive conversation format)
            if sec_case.get("dialogue"):
                st.markdown(f"#### 🎙️ {t('Đoạn Hội Thoại Thực Tế Giữa Coach & Khách Hàng:', 'Authentic Dialogue Between Coach & Client:')}")
                for turn in sec_case["dialogue"]:
                    spk = turn.get("speaker", "Coach")
                    is_coach = (spk == "Coach")
                    bg_col = "#EBF3ED" if is_coach else "#FAF7F2"
                    border_col = "#8BA888" if is_coach else "#D8C7B5"
                    txt = turn.get("textVi", "") if st.session_state.lang == "vi" else turn.get("textEn", "")
                    tag = turn.get("markerTag")

                    st.markdown(f"""
                    <div style="background: {bg_col}; border-left: 4px solid {border_col}; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <b>{spk}:</b>
                            {f'<span class="zen-badge zen-badge-primary">{tag}</span>' if tag else ''}
                        </div>
                        <div style="font-size: 0.92rem; color: #2C3E50; line-height: 1.55;">
                            "{txt}"
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # If coach response exists (direct model answer format)
            elif sec_case.get("coachResponseVi"):
                st.markdown(f"""
                <div class="zen-card" style="border-left: 3px solid #8BA888;">
                    <b>{t('Phản hồi mẫu của Coach (Tôn trọng tự chủ, không suy diễn):', 'Exemplary Coach Response (Objective, No Projection):')}</b><br/>
                    <div style="font-size: 0.95rem; line-height: 1.6; color: #2C3E50; margin-top: 6px;">
                        <i>"{sec_case.get('coachResponseVi', '') if st.session_state.lang == 'vi' else sec_case.get('coachResponseEn', '')}"</i>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Reflection questions
            ref_q = sec_case.get("reflectionQuestionsVi", []) if st.session_state.lang == "vi" else sec_case.get("reflectionQuestionsEn", [])
            if ref_q:
                st.markdown(f"""
                <div class="zen-quote-box" style="margin-top: 14px;">
                    <b>💡 {t('Câu hỏi suy ngẫm đạo đức & năng lực:', 'Reflective Questions:')}</b>
                    <ul style="margin: 6px 0 0 20px;">
                        {"".join([f"<li>{q}</li>" for q in ref_q])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.info(t("Tình huống thực tế đang được biên soạn.", "Case study is being compiled."))

    # TAB 5: 10 MINI QUIZZES
    with tab_qz:
        st.markdown(f"#### 📝 {t('10 Câu Hỏi Trắc Nghiệm Củng Cố Nhanh', '10 Mini Assessment Quizzes')}")
        if sec_quizzes:
            for q_idx, q in enumerate(sec_quizzes):
                qid = q.get("id", f"qz_{sec_id}_{q_idx}")
                q_text = q["questionVi"] if st.session_state.lang == "vi" else q["questionEn"]
                options = q.get("options", [])
                opt_dict = {opt["key"]: f"[{opt['key']}] {opt['textVi'] if st.session_state.lang == 'vi' else opt['textEn']}" for opt in options}

                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 14px;">
                    <div style="font-weight: 600; color: #2F3E34; margin-bottom: 8px;">
                        {q_idx + 1}. {q_text}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                chosen_opt = st.radio(
                    f"Chọn đáp án ({qid}):",
                    options=list(opt_dict.keys()),
                    format_func=lambda k: opt_dict[k],
                    key=f"sec_qz_radio_{qid}",
                    index=None
                )

                if chosen_opt:
                    is_correct = (chosen_opt == q.get("correctAnswer"))
                    if is_correct:
                        st.success(f"✅ {t('Chính xác!', 'Correct!')} {q.get('explanationVi', '') if st.session_state.lang == 'vi' else q.get('explanationEn', '')}")
                    else:
                        st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer is:')} **{q.get('correctAnswer')}**.\n\n{q.get('explanationVi', '') if st.session_state.lang == 'vi' else q.get('explanationEn', '')}")
        else:
            st.info(t("Chưa có câu hỏi mini quiz cho bài này.", "No mini quizzes available."))

    # TAB 6: STUDY NOTES
    with tab_note:
        st.markdown(f"#### 📓 {t('Sổ Tay Ghi Chú Cá Nhân Cho Năng Lực Này', 'Personal Study Journal for this Unit')}")
        user_notes = st.session_state.notes.get(sec_id, "")
        updated_note = st.text_area(
            t("Ghi chú của bạn (tự động lưu khi bấm Lưu):", "Your reflections & key reminders:"),
            value=user_notes,
            height=200,
            key=f"note_input_{sec_id}"
        )
        if st.button("💾 " + t("Lưu Ghi Chú Vào Sổ Học Tập", "Save Note to Learning Journal"), key=f"btn_save_note_{sec_id}"):
            st.session_state.notes[sec_id] = updated_note
            st.toast(t("Đã lưu ghi chú thành công!", "Note saved successfully!"))
