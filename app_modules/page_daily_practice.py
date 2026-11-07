# -*- coding: utf-8 -*-
"""
Daily 10-Question Targeted Practice for PCC Learning & Practice (Mentor Thi)
Supports 10 Situational Judgment questions, 10 Knowledge MCQs, or 10 Bookmarked questions
Features spaced repetition / de-duplication (hạn chế lặp lại tình huống), full A-D analysis, citations, and dispute reporting.
"""
import streamlit as st
import datetime
from app_modules.question_helpers import format_ad_analysis, get_source_anchor

def render_daily_practice_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, t):
    if "daily_seen_qids" not in st.session_state:
        st.session_state.daily_seen_qids = []

    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-gold">⚡ {t('Rèn Phán Đoán Hàng Ngày', 'Daily Discipline')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Luyện Tập 10 Câu / Ngày (Hạn Chế Lặp Tình Huống)', 'Daily 10-Question Targeted Drill (Non-Repeating)')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Rèn luyện kỷ luật phán đoán tình huống: Hệ thống tự động ưu tiên các tình huống bạn chưa làm để hạn chế lặp lại, cung cấp phân tích đa chiều A–D và trích dẫn chuẩn mực kiểm chứng.',
               'Daily situational judgment practice: The system prioritizes unseen scenarios to avoid repetition, delivering in-depth A-D rationales and verified ICF citations.')}
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

    # Filter candidates based on pool
    if "đánh dấu" in selected_pool.lower() or "bookmarked" in selected_pool.lower():
        bm_ids = set(st.session_state.bookmarked_qids)
        candidate_pool = [q for q in (PRACTICE_QUESTIONS + KNOWLEDGE_QUESTIONS) if q["id"] in bm_ids]
        if not candidate_pool:
            st.info(t("Bạn chưa có câu hỏi nào trong danh sách Đánh dấu. Hãy bấm '☆ Đánh dấu' ở các câu hỏi để đưa vào đây!",
                      "No bookmarked questions yet. Click '☆ Bookmark' on any question to add it here!"))
            candidate_pool = PRACTICE_QUESTIONS
    elif "kiến thức" in selected_pool.lower() or "knowledge" in selected_pool.lower():
        candidate_pool = KNOWLEDGE_QUESTIONS
    else:
        candidate_pool = PRACTICE_QUESTIONS

    # De-duplication logic (hạn chế lặp lại tình huống)
    seen_set = set(st.session_state.daily_seen_qids)
    unseen_candidates = [q for q in candidate_pool if q["id"] not in seen_set]
    if len(unseen_candidates) < 10:
        # Reset cycle if exhausted so user can practice again
        unseen_candidates = candidate_pool
        st.session_state.daily_seen_qids = []

    target_questions = unseen_candidates[:10]

    # De-duplication status banner
    st.markdown(f"""
    <div style="background: #FAF7F2; border: 1px solid #EADBCC; border-radius: 8px; padding: 8px 14px; margin-bottom: 16px; font-size: 0.85rem; color: #5F6F65; display: flex; justify-content: space-between;">
        <span>🔄 <b>{t('Chống lặp câu:', 'Non-repeating drill:')}</b> {t('Đã ưu tiên 10 câu mới nhất trong kho dữ liệu.', 'Selected 10 fresh scenarios from question pool.')}</span>
        <span>📊 {t('Số câu đã rèn luyện:', 'Total practiced:')} {len(st.session_state.daily_seen_qids)} / {len(candidate_pool)}</span>
    </div>
    """, unsafe_allow_html=True)

    # Question list
    for idx, q in enumerate(target_questions):
        qid = q["id"]
        is_knowledge = (q.get("type") != "icf_sjt" and "correctAnswer" in q)
        is_bm = qid in st.session_state.bookmarked_qids
        ad_info = format_ad_analysis(q, lang=st.session_state.lang)

        # Header with Question Number and Star Bookmark Button
        col_q_head1, col_q_head2 = st.columns([4, 1])
        with col_q_head1:
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <span class="zen-badge zen-badge-primary">Câu {idx + 1} / {len(target_questions)} ({qid})</span>
                <span class="zen-badge zen-badge-gold">{q.get('primaryCompetency', q.get('domain', 'ICF Standard'))}</span>
            </div>
            """, unsafe_allow_html=True)
        with col_q_head2:
            bm_label = "★ " + t("Đã lưu", "Saved") if is_bm else "☆ " + t("Lưu câu", "Save")
            if st.button(bm_label, key=f"btn_daily_bm_head_{qid}_{idx}", use_container_width=True):
                if is_bm:
                    st.session_state.bookmarked_qids.remove(qid)
                    st.toast(t("Đã bỏ lưu câu hỏi!", "Removed from bookmarks!"))
                else:
                    st.session_state.bookmarked_qids.append(qid)
                    st.toast(t("Đã lưu vào Sổ Học Tập → Câu hỏi đã lưu!", "Saved to Learning Journal!"))
                st.rerun()

        st.markdown(f"""
        <div class="zen-card" style="border-left: 4px solid #8BA888; margin: 8px 0 16px 0;">
            <div style="font-size: 1.02rem; font-weight: 600; color: #2F3E34; line-height: 1.6;">
                {q['questionVi'] if st.session_state.lang == 'vi' else q['questionEn']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        options = q["options"]

        # 1. RENDER FULL WRAPPED OPTION CARDS (A, B, C, D)
        st.markdown(f"<div style='font-size: 0.88rem; font-weight: 600; color: #5F6F65; margin-bottom: 6px;'>{t('Danh sách các phương án (Options):', 'Available Options:')}</div>", unsafe_allow_html=True)
        for opt in options:
            st.markdown(f"""
            <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; line-height: 1.5; white-space: normal; word-break: break-word;">
                <b style="color: #2F3E34; font-size: 0.95rem;">[{opt['key']}]</b> 
                <span style="font-size: 0.92rem; color: #333;">{opt['textVi'] if st.session_state.lang == 'vi' else opt['textEn']}</span>
                <div style="font-size: 0.82rem; color: #777; margin-top: 4px; font-style: italic;">{opt['textEn'] if st.session_state.lang == 'vi' else opt['textVi']}</div>
            </div>
            """, unsafe_allow_html=True)

        opt_keys = [opt["key"] for opt in options]

        # Knowledge Question Single Select
        if is_knowledge:
            cur_k = st.session_state.daily_answers.get(qid, {}).get("pick")
            k_idx = opt_keys.index(cur_k) if cur_k in opt_keys else None
            user_k = st.radio(
                t(f"Chọn 1 đáp án đúng ({qid}):", f"Select single correct answer ({qid}):"),
                options=opt_keys,
                format_func=lambda k: f"Phương án [{k}]",
                horizontal=True,
                key=f"daily_k_{qid}",
                index=k_idx
            )
            st.session_state.daily_answers[qid] = {"pick": user_k}

            if is_study_mode and user_k:
                if user_k == q["correctAnswer"]:
                    st.success(f"✅ {t('Chính xác!', 'Correct!')} {q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}")
                else:
                    st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer is:')} **{q['correctAnswer']}**.\n\n{q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}")

                st.markdown(f"""
                <div style="font-size: 0.82rem; color: #1E4E79; background: #EBF3FA; padding: 6px 12px; border-radius: 6px; margin-top: 6px;">
                    📌 <b>{t('Dẫn nguồn:', 'Source:')}</b> {ad_info['source']['sourceCode']} — {ad_info['source']['referenceStandard']}
                </div>
                """, unsafe_allow_html=True)
        else:
            # Situational Judgment Question (Best and Worst with identical A-D order)
            col_b, col_w = st.columns(2)
            cur_b = st.session_state.daily_answers.get(qid, {}).get("best")
            cur_w = st.session_state.daily_answers.get(qid, {}).get("worst")
            b_idx = opt_keys.index(cur_b) if cur_b in opt_keys else None
            w_idx = opt_keys.index(cur_w) if cur_w in opt_keys else None

            with col_b:
                st.markdown(f"🌟 <b>{t('Chọn BEST (TỐT NHẤT):', 'Select BEST:')}</b>", unsafe_allow_html=True)
                chosen_b = st.radio(
                    label=f"BEST_{qid}",
                    options=opt_keys,
                    format_func=lambda k: f"Phương án [{k}]",
                    horizontal=True,
                    key=f"daily_best_{qid}",
                    index=b_idx,
                    label_visibility="collapsed"
                )
            with col_w:
                st.markdown(f"⚠️ <b>{t('Chọn WORST (TỆ NHẤT):', 'Select WORST:')}</b>", unsafe_allow_html=True)
                chosen_w = st.radio(
                    label=f"WORST_{qid}",
                    options=opt_keys,
                    format_func=lambda k: f"Phương án [{k}]",
                    horizontal=True,
                    key=f"daily_worst_{qid}",
                    index=w_idx,
                    label_visibility="collapsed"
                )

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
                    <div style="margin-top: 10px; font-size: 0.88rem; font-weight: 600;">
                        🔍 {t('Phân tích A–D:', 'A-D Option Breakdown:')}
                    </div>
                """, unsafe_allow_html=True)

                for opt_block in ad_info["options"]:
                    st.markdown(f"""
                    <div style="margin: 4px 0; padding: 6px 10px; border-radius: 6px; background: #FFFFFF; font-size: 0.85rem;">
                        <b style="color: {opt_block['tagColor']};">{opt_block['tag']} [{opt_block['key']}]:</b> {opt_block['text']}<br/>
                        <span style="color: #666;">👉 {opt_block['why']}</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                    <div style="font-size: 0.82rem; color: #1E4E79; background: #EBF3FA; padding: 6px 10px; border-radius: 6px; margin-top: 8px;">
                        📌 <b>{t('Dẫn nguồn:', 'Citation:')}</b> {ad_info['source']['sourceCode']} — {ad_info['source']['referenceStandard']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Action bar for each question: Bookmark & Dispute
        col_act1, col_act2 = st.columns([4, 1])
        with col_act2:
            bm_label = "★ " + t("Đã Lưu", "Saved") if is_bm else "☆ " + t("Đánh Dấu", "Bookmark")
            if st.button(bm_label, key=f"btn_daily_bm_foot_{qid}_{idx}", use_container_width=True):
                if is_bm:
                    st.session_state.bookmarked_qids.remove(qid)
                else:
                    st.session_state.bookmarked_qids.append(qid)
                st.rerun()

        # Dispute / Feedback Expander
        with st.expander("🚩 " + t("Phản biện đáp án / Báo lỗi câu này", "Dispute Answer / Flag this Question")):
            dispute_text = st.text_input(
                t("Nội dung phản biện hoặc góp ý:", "Your counter-argument or feedback:"),
                key=f"disp_in_{qid}"
            )
            if st.button("📨 " + t("Gửi Phản Biện Cho Ban Quản Trị", "Submit Dispute to Reviewers"), key=f"btn_disp_sub_{qid}"):
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
                    st.success(t("Cảm ơn bạn! Phản biện đã được ghi nhận vào nhật ký kiểm duyệt.",
                                 "Thank you! Your dispute has been recorded in the review log."))
                else:
                    st.warning(t("Vui lòng nhập nội dung trước khi gửi.", "Please enter your comments."))

        st.markdown("<hr style='border: none; border-top: 1px dashed #E0D5C7; margin: 16px 0;'/>", unsafe_allow_html=True)

    # Submission & Save
    if st.button("📝 " + t("Hoàn Thành Lượt Luyện & Lưu Kết Quả", "Complete Drill & Save to Journal"), type="primary", use_container_width=True):
        total_pts = 0
        max_pts = 0
        for q in target_questions:
            qid = q["id"]
            # Add to de-duplication tracker
            if qid not in st.session_state.daily_seen_qids:
                st.session_state.daily_seen_qids.append(qid)

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
            "status": "Đạt (Pass)" if scaled_score >= 460 else "Cần rèn thêm",
            "totalQuestions": len(target_questions)
        }
        st.session_state.exam_history.insert(0, history_entry)
        st.session_state.lotus_bloomed += 1

        st.toast(f"🎉 Hoàn thành lượt luyện! Điểm ước tính: {scaled_score}/600. Đã lưu vào Sổ Học Tập (+1 Đóa sen)!")
        st.success(f"""
        ### 🎉 {t('Kết Quả Lượt Luyện Tập:', 'Drill Completed:')}
        - **{t('Điểm thô:', 'Raw Score:')}** {total_pts} / {max_pts} ({pct}%)
        - **{t('Điểm quy đổi ước tính (200-600):', 'Estimated Scaled Score:')}** {scaled_score} / 600 ({'ĐẠT CHUẨN 460' if scaled_score >= 460 else 'CẦN BỒI ĐẮP THÊM'})
        - {t('Đã tự động cập nhật hệ thống chống lặp để lượt thi sau xuất hiện các câu hỏi mới.', 'Anti-repetition system updated for subsequent practice sessions.')}
        """)
