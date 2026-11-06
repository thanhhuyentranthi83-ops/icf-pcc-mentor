# -*- coding: utf-8 -*-
"""
Daily 10-Question Targeted Practice for PCC Learning & Practice
Supports 10 Situational Judgment questions, 10 Knowledge MCQs, or 10 Bookmarked questions
Features immediate feedback mode, dual Best/Worst validation, bookmarking, and dispute reporting.
"""
import streamlit as st
import datetime

def render_daily_practice_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, t):
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-gold">⚡ {t('Rèn Phán Đoán Hàng Ngày', 'Daily Discipline')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Luyện Tập 10 Câu / Ngày (Targeted Drill)', 'Daily 10-Question Targeted Drill')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Rèn luyện kỷ luật phán đoán tình huống: Mỗi ngày thực hành 10 câu hỏi để củng cố tư duy chánh niệm, nhận diện hành vi đạo đức và giữ trọn sự tự chủ của khách hàng.',
               'Hone your situational judgment daily: Practice 10 curated questions to reinforce mindful coaching presence, ethical boundaries, and client autonomy.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_ctrl1, col_ctrl2 = st.columns(2)
    with col_ctrl1:
        pool_options = [
            t("10 Tình huống phán đoán (SJT)", "10 Situational Judgment Items (SJT)"),
            t("10 Câu kiến thức chuẩn mực (Knowledge)", "10 Knowledge MCQs"),
            t("10 Câu đã đánh dấu xem lại", "10 Bookmarked Review Items")
        ]
        selected_pool = st.selectbox(
            "🎯 " + t("Chọn tập câu hỏi rèn luyện:", "Select question pool:"),
            options=pool_options,
            index=0
        )
    with col_ctrl2:
        drill_mode_options = [
            t("Chế độ Học tập (Xem giải thích tức thì)", "Study Mode (Instant Feedback)"),
            t("Chế độ Thi tính giờ (Nộp bài xem tổng kết)", "Exam Mode (Submit for Report)")
        ]
        selected_mode = st.radio(
            "⚙️ " + t("Phương thức làm bài:", "Practice mode:"),
            options=drill_mode_options,
            horizontal=True,
            index=0
        )

    is_study_mode = ("Học tập" in selected_mode or "Study" in selected_mode)

    # Determine question pool
    if "đánh dấu" in selected_pool.lower() or "bookmarked" in selected_pool.lower():
        bm_ids = set(st.session_state.bookmarked_qids)
        all_pool = [q for q in (PRACTICE_QUESTIONS + KNOWLEDGE_QUESTIONS) if q["id"] in bm_ids]
        if not all_pool:
            st.info(t("Bạn chưa có câu hỏi nào trong danh sách Đánh dấu. Hãy bấm '☆ Đánh dấu' ở các câu hỏi để đưa vào đây!",
                      "No bookmarked questions yet. Click '☆ Bookmark' on any question to add it here!"))
            target_questions = PRACTICE_QUESTIONS[:10]
        else:
            target_questions = all_pool[:10]
    elif "kiến thức" in selected_pool.lower() or "knowledge" in selected_pool.lower():
        target_questions = KNOWLEDGE_QUESTIONS[:10]
    else:
        target_questions = PRACTICE_QUESTIONS[:10]

    st.markdown(f"**{t('Đang làm bài:', 'Practicing:')}** {len(target_questions)} {t('câu hỏi', 'items')}")
    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 12px 0 20px 0;'/>", unsafe_allow_html=True)

    # Question list
    for idx, q in enumerate(target_questions):
        qid = q["id"]
        is_knowledge = (q.get("type") != "icf_sjt" and "correctAnswer" in q)
        is_bm = qid in st.session_state.bookmarked_qids

        st.markdown(f"""
        <div class="zen-card" style="border-left: 4px solid #8BA888; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap;">
                <span class="zen-badge zen-badge-primary">Câu {idx + 1} / {len(target_questions)} ({qid})</span>
                <span class="zen-badge zen-badge-gold">{q.get('primaryCompetency', q.get('domain', 'ICF Standard'))}</span>
            </div>
            <div style="font-size: 1.02rem; font-weight: 600; color: #2F3E34; line-height: 1.6; margin: 10px 0;">
                {q['questionVi'] if st.session_state.lang == 'vi' else q['questionEn']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        options = q["options"]
        opt_dict = {opt["key"]: f"[{opt['key']}] {opt['textVi'] if st.session_state.lang == 'vi' else opt['textEn']}" for opt in options}

        # Knowledge Question Single Select
        if is_knowledge:
            user_k = st.radio(
                t(f"Chọn 1 đáp án đúng ({qid}):", f"Select single correct answer ({qid}):"),
                options=list(opt_dict.keys()),
                format_func=lambda k: opt_dict[k],
                key=f"daily_k_{qid}",
                index=None
            )
            st.session_state.daily_answers[qid] = {"pick": user_k}

            if is_study_mode and user_k:
                if user_k == q["correctAnswer"]:
                    st.success(f"✅ {t('Chính xác!', 'Correct!')} {q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}")
                else:
                    st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer is:')} **{q['correctAnswer']}**.\n\n{q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}")
        else:
            # Situational Judgment Question (Best and Worst)
            col_b, col_w = st.columns(2)
            with col_b:
                user_best = st.selectbox(
                    f"🌟 {t('Chọn BEST (TỐT NHẤT)', 'Select BEST')} ({qid}):",
                    options=["-- Chưa chọn --"] + list(opt_dict.keys()),
                    format_func=lambda k: opt_dict.get(k, k),
                    key=f"daily_best_{qid}"
                )
            with col_w:
                user_worst = st.selectbox(
                    f"⚠️ {t('Chọn WORST (TỆ NHẤT)', 'Select WORST')} ({qid}):",
                    options=["-- Chưa chọn --"] + list(opt_dict.keys()),
                    format_func=lambda k: opt_dict.get(k, k),
                    key=f"daily_worst_{qid}"
                )

            chosen_b = None if user_best == "-- Chưa chọn --" else user_best
            chosen_w = None if user_worst == "-- Chưa chọn --" else user_worst
            st.session_state.daily_answers[qid] = {"best": chosen_b, "worst": chosen_w}

            if chosen_b and chosen_w and chosen_b == chosen_w:
                st.warning(t("⚠️ Cảnh báo: Best và Worst không được trùng nhau! Vui lòng chọn 2 phương án khác nhau.",
                             "⚠️ Warning: Best and Worst cannot be identical! Please pick two distinct options."))

            if is_study_mode and chosen_b and chosen_w and chosen_b != chosen_w:
                b_correct = (chosen_b == q["bestAnswer"])
                w_correct = (chosen_w == q["worstAnswer"])
                pts = (1 if b_correct else 0) + (1 if w_correct else 0)
                tier_badge = "zen-badge-primary" if pts == 2 else ("zen-badge-gold" if pts == 1 else "zen-badge-pink")

                st.markdown(f"""
                <div style="background: #FAF7F2; padding: 14px; border-radius: 10px; margin-top: 10px; border: 1px solid #EADBCC;">
                    <div style="margin-bottom: 6px;">
                        <span class="zen-badge {tier_badge}">Điểm: {pts}/2</span>
                        <b>🎯 Đáp án chuẩn:</b> BEST = <b style="color: green;">{q['bestAnswer']}</b> ({'✅ Đúng' if b_correct else '❌ Sai'}) | WORST = <b style="color: red;">{q['worstAnswer']}</b> ({'✅ Đúng' if w_correct else '❌ Sai'})
                    </div>
                    <div style="font-size: 0.9rem; line-height: 1.5; margin-top: 6px;">
                        <b>📖 {t('Lý giải:', 'Rationale:')}</b> {q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}
                    </div>
                    <div style="font-size: 0.85rem; color: #8C6D53; margin-top: 4px;">
                        <b>💡 {t('Dấu hiệu nhận diện:', 'Key Clue:')}</b> {q.get('keyClueVi', '') if st.session_state.lang == 'vi' else q.get('keyClueEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Action bar for each question: Bookmark & Dispute
        col_act1, col_act2 = st.columns([4, 1])
        with col_act2:
            bm_label = "★ " + t("Đã Lưu", "Saved") if is_bm else "☆ " + t("Đánh Dấu", "Bookmark")
            if st.button(bm_label, key=f"btn_daily_bm_{qid}", use_container_width=True):
                if is_bm:
                    st.session_state.bookmarked_qids.remove(qid)
                else:
                    st.session_state.bookmarked_qids.append(qid)
                st.rerun()

        # Dispute / Feedback Expander
        with st.expander("🚩 " + t("Phản ánh / Góp ý về câu hỏi này", "Flag / Dispute this question")):
            dispute_text = st.text_input(
                t("Nội dung phản ánh (Ví dụ: dịch chưa sát, phân vân giữa 2 đáp án...):",
                  "Feedback / Dispute reason:"),
                key=f"disp_in_{qid}"
            )
            if st.button("📨 " + t("Gửi Phản Hồi", "Submit Feedback"), key=f"btn_disp_sub_{qid}"):
                if dispute_text.strip():
                    log_entry = {
                        "id": f"DISP-{len(st.session_state.dispute_logs) + 1:04d}",
                        "questionId": qid,
                        "questionType": "Knowledge" if is_knowledge else "SJT",
                        "note": dispute_text.strip(),
                        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "status": "Đang xem xét"
                    }
                    st.session_state.dispute_logs.append(log_entry)
                    st.success(t("Cảm ơn bạn! Phản hồi đã được ghi nhận vào nhật ký quản trị.",
                                 "Thank you! Your feedback has been recorded in the review log."))
                else:
                    st.warning(t("Vui lòng nhập nội dung trước khi gửi.", "Please enter your comments."))

        st.markdown("<hr style='border: none; border-top: 1px dashed #E0D5C7; margin: 16px 0;'/>", unsafe_allow_html=True)

    # Submission & Save
    if st.button("📝 " + t("Hoàn Thành Lượt Luyện & Lưu Kết Quả", "Complete Drill & Save to Journal"), type="primary", use_container_width=True):
        total_pts = 0
        max_pts = 0
        for q in target_questions:
            qid = q["id"]
            ans = st.session_state.daily_answers.get(qid, {})
            if q.get("type") != "icf_sjt" and "correctAnswer" in q:
                max_pts += 1
                if ans.get("pick") == q["correctAnswer"]:
                    total_pts += 1
            else:
                max_pts += 2
                b = ans.get("best")
                w = ans.get("worst")
                if b == q.get("bestAnswer"): total_pts += 1
                if w == q.get("worstAnswer"): total_pts += 1

        pct = int(round((total_pts / max_pts) * 100)) if max_pts > 0 else 0
        scaled_score = int(round(200 + (pct / 100.0) * 400))

        # Real record
        history_entry = {
            "id": f"HIST-{len(st.session_state.exam_history) + 1:04d}",
            "type": "Luyện Tập 10 Câu",
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "profile": selected_pool,
            "rawScore": f"{total_pts}/{max_pts} ({pct}%)",
            "scaledScore": scaled_score,
            "status": "Đạt" if scaled_score >= 460 else "Cần rèn thêm",
            "totalQuestions": len(target_questions)
        }
        st.session_state.exam_history.insert(0, history_entry)
        st.session_state.lotus_bloomed += 1

        st.toast(f"🎉 Hoàn thành lượt luyện! Điểm ước tính: {scaled_score}/600. Đã lưu vào Sổ Học Tập (+1 Đóa sen)!")
        st.success(f"""
        ### 🎉 {t('Kết Quả Lượt Luyện Tập:', 'Drill Completed:')}
        - **{t('Điểm thô:', 'Raw Score:')}** {total_pts} / {max_pts} ({pct}%)
        - **{t('Điểm quy đổi ước tính (200-600):', 'Estimated Scaled Score:')}** {scaled_score} / 600 ({'ĐẠT CHUẨN 460' if scaled_score >= 460 else 'CẦN BỒI ĐẮP THÊM'})
        - {t('Kết quả đã được ghi vào **Sổ Học Tập & Lịch Sử**.', 'Attempt logged to **Learning Journal & History**.')}
        """)
