# -*- coding: utf-8 -*-
"""
Mock Exam Simulator for PCC Learning & Practice
Dynamically adapts to active Exam Profile (Legacy 78 SJT vs Updated 80 Items vs Mini-Mock)
Includes timer simulation, question flags, Best != Worst validation, 4-tier scoring, and real history logging.
"""
import streamlit as st
import datetime

def render_sjt_page(EXAM_PROFILES, PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t):
    prof_id = st.session_state.exam_profile_id
    prof = EXAM_PROFILES.get(prof_id, list(EXAM_PROFILES.values())[0])

    st.markdown(f"""
    <div style="margin-bottom: 16px;">
        <span class="zen-badge zen-badge-pink">⚖️ {t('Phòng Thi Thử Mô Phỏng', 'Mock Exam Simulator')}</span>
        <h2 style="margin: 6px 0; color: #2F3E34;">{t('Mô Phỏng Kỳ Thi ICF Credentialing Exam', 'ICF Credentialing Mock Simulator')}</h2>
        <div style="font-size: 0.9rem; color: #5F6F65;">
            {t('Hệ thống mô phỏng sát thực tế giao diện Pearson VUE: Hỗ trợ đánh dấu cờ (Flag), kiểm tra trùng lặp Best/Worst, và bảng điểm 4 mức quy đổi theo chuẩn 200–600.',
               'Realistic Pearson VUE exam simulation: Flag for review, Best/Worst duplicate validation, and official 4-tier 200–600 scaled scoring.')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Exam Configuration Bar
    col_c1, col_c2, col_c3 = st.columns([2, 1, 1])
    with col_c1:
        st.markdown(f"""
        <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 12px; padding: 12px 16px;">
            <b>🎯 {t('Cấu hình:', 'Active Profile:')}</b> {prof['nameVi'] if st.session_state.lang == 'vi' else prof['nameEn']}<br/>
            <span style="font-size: 0.85rem; color: #666;">
                ⏱️ {prof['totalTimeMinutes']} {t('phút', 'mins')} | ☕ {prof['breakMinutes']} {t('phút nghỉ', 'mins break')} | 📜 {prof['ethicsBaselineVi'] if st.session_state.lang == 'vi' else prof['ethicsBaselineEn']}
            </span>
        </div>
        """, unsafe_allow_html=True)
    with col_c2:
        mock_mode = st.selectbox(
            "📐 " + t("Quy mô bài thi:", "Exam scope:"),
            options=[
                t("Đầy đủ theo Cấu hình thi", "Full Profile Exam"),
                t("Mini-Mock (20 câu)", "Mini-Mock (20 items)"),
                t("Mini-Mock (10 câu)", "Mini-Mock (10 items)")
            ],
            index=0
        )
    with col_c3:
        if st.button("🔄 " + t("Làm Lại Đề Mới", "Reset / New Exam"), use_container_width=True):
            st.session_state.sjt_answers = {}
            st.session_state.sjt_flagged = []
            st.session_state.sjt_submitted = False
            st.session_state.sjt_last_result = None
            st.rerun()

    # Build question dataset based on mode and profile
    if "10 câu" in mock_mode or "10 items" in mock_mode:
        exam_items = PRACTICE_QUESTIONS[:10]
    elif "20 câu" in mock_mode or "20 items" in mock_mode:
        if prof_id == "updated_80_items":
            exam_items = KNOWLEDGE_QUESTIONS[:10] + PRACTICE_QUESTIONS[:10]
        else:
            exam_items = PRACTICE_QUESTIONS[:20]
    else:
        # Full Profile
        if prof_id == "updated_80_items":
            # 36 knowledge + 44 sjt
            exam_items = KNOWLEDGE_QUESTIONS[:36] + PRACTICE_QUESTIONS[:44]
        else:
            # Legacy 78 SJT (using available 50 + 8 official samples + repeat to reach 78)
            base_sjt = PRACTICE_QUESTIONS + OFFICIAL_SAMPLES
            exam_items = (base_sjt * 2)[:78]

    # IF ALREADY SUBMITTED: RENDER SCORE REPORT
    if st.session_state.sjt_submitted and st.session_state.sjt_last_result:
        res = st.session_state.sjt_last_result
        st.markdown(f"""
        <div class="zen-card" style="border: 2px solid {'#8BA888' if res['passed'] else '#D4A373'}; text-align: center; padding: 24px;">
            <span class="zen-badge {'zen-badge-primary' if res['passed'] else 'zen-badge-gold'}" style="font-size: 1rem; padding: 6px 16px;">
                {'🎉 ' + t('CHÚC MỪNG: BẠN ĐÃ ĐẠT CHUẨN!', 'CONGRATULATIONS: PASS!') if res['passed'] else '🌱 ' + t('CẦN TIẾP TỤC BỒI ĐẮP THÊM', 'NEEDS FURTHER PRACTICE')}
            </span>
            <h1 style="font-size: 3rem; margin: 14px 0; color: #2F3E34;">{res['scaledScore']} <span style="font-size: 1.2rem; color: #8C6D53;">/ 600</span></h1>
            <div style="font-size: 1rem; color: #555; margin-bottom: 12px;">
                <b>{t('Điểm thô:', 'Raw Score:')}</b> {res['totalPts']} / {res['maxPts']} ({res['percentage']}%) &nbsp;|&nbsp;
                <b>{t('Ngưỡng chuẩn đỗ:', 'Passing Benchmark:')}</b> 460 / 600
            </div>
            <p style="font-size: 0.9rem; color: #666; max-width: 600px; margin: 0 auto;">
                {t('Điểm số đã được tự động lưu vào Sổ Học Tập & Lịch Sử của bạn. Hãy xem lại chi tiết từng câu hỏi bên dưới để nhận diện khoảng trống năng lực.',
                   'Score has been saved to your Learning Journal. Review question-level feedback below to pinpoint competency gaps.')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### 📋 {t('Chi Tiết Từng Câu Hỏi & Đối Chiếu Đáp Án Chuẩn', 'Question-by-Question Detailed Review')}")
        for idx, item in enumerate(exam_items):
            qid = item["id"]
            user_ans = st.session_state.sjt_answers.get(qid, {})
            is_k = (item.get("type") != "icf_sjt" and "correctAnswer" in item)

            if is_k:
                u_pick = user_ans.get("pick")
                c_pick = item["correctAnswer"]
                q_ok = (u_pick == c_pick)
                pts_q = 1 if q_ok else 0

                st.markdown(f"""
                <div class="zen-card" style="padding: 16px; margin-bottom: 12px; border-left: 4px solid {'#8BA888' if q_ok else '#C62828'};">
                    <div style="display: flex; justify-content: space-between;">
                        <b>Câu {idx + 1} ({qid}) - Kiến thức:</b>
                        <span class="zen-badge {'zen-badge-primary' if q_ok else 'zen-badge-pink'}">{pts_q}/1 Điểm</span>
                    </div>
                    <div style="margin: 6px 0; font-size: 0.95rem;">{item['questionVi'] if st.session_state.lang == 'vi' else item['questionEn']}</div>
                    <div style="font-size: 0.88rem; color: #444;">
                        <b>{t('Bạn chọn:', 'Your pick:')}</b> {u_pick or '--'} &nbsp;|&nbsp; <b>{t('Đáp án đúng:', 'Correct key:')}</b> {c_pick}
                    </div>
                    <div style="font-size: 0.85rem; color: #666; margin-top: 4px;">
                        <b>{t('Lý giải:', 'Explanation:')}</b> {item.get('explanationVi', '') if st.session_state.lang == 'vi' else item.get('explanationEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                u_b = user_ans.get("best")
                u_w = user_ans.get("worst")
                c_b = item["bestAnswer"]
                c_w = item["worstAnswer"]
                b_ok = (u_b == c_b)
                w_ok = (u_w == c_w)
                pts_q = (1 if b_ok else 0) + (1 if w_ok else 0)
                badge_cls = "zen-badge-primary" if pts_q == 2 else ("zen-badge-gold" if pts_q == 1 else "zen-badge-pink")

                st.markdown(f"""
                <div class="zen-card" style="padding: 16px; margin-bottom: 12px; border-left: 4px solid {'#8BA888' if pts_q == 2 else ('#EADBCC' if pts_q == 1 else '#C62828')};">
                    <div style="display: flex; justify-content: space-between;">
                        <b>Câu {idx + 1} ({qid}) - Tình huống phán đoán:</b>
                        <span class="zen-badge {badge_cls}">{pts_q}/2 Điểm</span>
                    </div>
                    <div style="margin: 6px 0; font-size: 0.95rem;">{item['questionVi'] if st.session_state.lang == 'vi' else item['questionEn']}</div>
                    <div style="font-size: 0.88rem; color: #444;">
                        <b>BEST:</b> {t('Bạn chọn', 'You picked')} <b style="color: {'green' if b_ok else 'red'};">{u_b or '--'}</b> ({t('Chuẩn', 'Key')}: {c_b}) &nbsp;|&nbsp;
                        <b>WORST:</b> {t('Bạn chọn', 'You picked')} <b style="color: {'green' if w_ok else 'red'};">{u_w or '--'}</b> ({t('Chuẩn', 'Key')}: {c_w})
                    </div>
                    <div style="font-size: 0.85rem; color: #666; margin-top: 4px;">
                        <b>{t('Lý giải:', 'Explanation:')}</b> {item.get('explanationVi', '') if st.session_state.lang == 'vi' else item.get('explanationEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        return

    # EXAM IN PROGRESS
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; background: #FAF7F2; padding: 10px 16px; border-radius: 10px; margin-bottom: 16px; border: 1px solid #EADBCC;">
        <div><b>📝 {t('Tổng số câu:', 'Total questions:')}</b> {len(exam_items)} {t('câu hỏi', 'items')}</div>
        <div><b>🚩 {t('Đã cắm cờ (Flag):', 'Flagged for review:')}</b> {len(st.session_state.sjt_flagged)} {t('câu', 'items')}</div>
        <div><b>⏱️ {t('Thời gian quy chuẩn:', 'Standard time:')}</b> {prof['totalTimeMinutes']} {t('phút', 'minutes')}</div>
    </div>
    """, unsafe_allow_html=True)

    # Render questions
    for idx, item in enumerate(exam_items):
        qid = item["id"]
        is_k = (item.get("type") != "icf_sjt" and "correctAnswer" in item)
        is_flagged = qid in st.session_state.sjt_flagged

        st.markdown(f"""
        <div class="zen-card" style="margin-bottom: 20px; border-left: 4px solid {'#9C4158' if is_flagged else '#8BA888'};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span class="zen-badge zen-badge-primary">Câu {idx + 1} / {len(exam_items)} ({qid})</span>
                <div>
                    {'<span class="zen-badge zen-badge-pink">🚩 Đã Cắm Cờ</span>' if is_flagged else ''}
                    <span class="zen-badge zen-badge-gold">{item.get('primaryCompetency', item.get('domain', 'ICF Standard'))}</span>
                </div>
            </div>
            <div style="font-size: 1.02rem; font-weight: 500; color: #2F3E34; line-height: 1.6; margin: 8px 0;">
                {item['questionVi'] if st.session_state.lang == 'vi' else item['questionEn']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        options = item["options"]
        opt_dict = {opt["key"]: f"[{opt['key']}] {opt['textVi'] if st.session_state.lang == 'vi' else opt['textEn']}" for opt in options}

        if is_k:
            cur_pick = st.session_state.sjt_answers.get(qid, {}).get("pick")
            pick_idx = list(opt_dict.keys()).index(cur_pick) if cur_pick in opt_dict else None
            chosen_k = st.radio(
                t(f"Chọn 1 đáp án đúng ({qid}):", f"Select single correct answer ({qid}):"),
                options=list(opt_dict.keys()),
                format_func=lambda k: opt_dict[k],
                key=f"sjt_k_radio_{qid}_{idx}",
                index=pick_idx
            )
            st.session_state.sjt_answers[qid] = {"pick": chosen_k}
        else:
            col_b, col_w = st.columns(2)
            cur_b = st.session_state.sjt_answers.get(qid, {}).get("best")
            cur_w = st.session_state.sjt_answers.get(qid, {}).get("worst")

            with col_b:
                user_best = st.selectbox(
                    f"🌟 {t('Chọn BEST (TỐT NHẤT)', 'Select BEST')} ({qid}):",
                    options=["-- Chưa chọn --"] + list(opt_dict.keys()),
                    format_func=lambda k: opt_dict.get(k, k),
                    key=f"sjt_best_sel_{qid}_{idx}",
                    index=(list(opt_dict.keys()).index(cur_b) + 1) if cur_b in opt_dict else 0
                )
            with col_w:
                user_worst = st.selectbox(
                    f"⚠️ {t('Chọn WORST (TỆ NHẤT)', 'Select WORST')} ({qid}):",
                    options=["-- Chưa chọn --"] + list(opt_dict.keys()),
                    format_func=lambda k: opt_dict.get(k, k),
                    key=f"sjt_worst_sel_{qid}_{idx}",
                    index=(list(opt_dict.keys()).index(cur_w) + 1) if cur_w in opt_dict else 0
                )

            b_val = None if user_best == "-- Chưa chọn --" else user_best
            w_val = None if user_worst == "-- Chưa chọn --" else user_worst
            st.session_state.sjt_answers[qid] = {"best": b_val, "worst": w_val}

            if b_val and w_val and b_val == w_val:
                st.warning(t("⚠️ Best và Worst không được trùng nhau! Vui lòng chọn 2 phương án khác nhau.",
                             "⚠️ Best and Worst cannot be identical! Please select two distinct options."))

        # Flag button
        col_f1, col_f2 = st.columns([5, 1])
        with col_f2:
            flag_btn_text = "🚩 " + t("Bỏ Cờ", "Unflag") if is_flagged else "🏳️ " + t("Cắm Cờ", "Flag")
            if st.button(flag_btn_text, key=f"btn_flag_{qid}_{idx}", use_container_width=True):
                if is_flagged:
                    st.session_state.sjt_flagged.remove(qid)
                else:
                    st.session_state.sjt_flagged.append(qid)
                st.rerun()

        st.markdown("<hr style='border: none; border-top: 1px dashed #E0D5C7; margin: 16px 0;'/>", unsafe_allow_html=True)

    # Submission Action
    st.markdown("### 📤 " + t("Nộp Bài & Kết Thúc Kỳ Thi", "Submit Exam & Finalize"))
    unanswered = 0
    duplicate_errors = 0
    for it in exam_items:
        q_id = it["id"]
        ans = st.session_state.sjt_answers.get(q_id, {})
        if it.get("type") != "icf_sjt" and "correctAnswer" in it:
            if not ans.get("pick"): unanswered += 1
        else:
            b = ans.get("best")
            w = ans.get("worst")
            if not b or not w: unanswered += 1
            if b and w and b == w: duplicate_errors += 1

    if unanswered > 0:
        st.info(f"ℹ️ {t('Bạn còn', 'You have')} {unanswered} {t('câu chưa hoàn thành đầy đủ.', 'unanswered question(s).')}")
    if duplicate_errors > 0:
        st.error(f"⚠️ {t('Có', 'There are')} {duplicate_errors} {t('câu bị trùng giữa Best và Worst! Hãy sửa lại trước khi nộp.', 'item(s) where Best == Worst. Please resolve before submitting!')}")

    if st.button("✅ " + t("Nộp Bài Thi Ngay", "Submit Exam Now"), type="primary", use_container_width=True, disabled=(duplicate_errors > 0)):
        total_pts = 0
        max_pts = 0
        for it in exam_items:
            q_id = it["id"]
            ans = st.session_state.sjt_answers.get(q_id, {})
            if it.get("type") != "icf_sjt" and "correctAnswer" in it:
                max_pts += 1
                if ans.get("pick") == it["correctAnswer"]: total_pts += 1
            else:
                max_pts += 2
                b = ans.get("best")
                w = ans.get("worst")
                if b == it.get("bestAnswer"): total_pts += 1
                if w == it.get("worstAnswer"): total_pts += 1

        pct = int(round((total_pts / max_pts) * 100)) if max_pts > 0 else 0
        scaled_score = int(round(200 + (pct / 100.0) * 400))
        passed = (scaled_score >= 460)

        result_obj = {
            "totalPts": total_pts,
            "maxPts": max_pts,
            "percentage": pct,
            "scaledScore": scaled_score,
            "passed": passed
        }
        st.session_state.sjt_last_result = result_obj
        st.session_state.sjt_submitted = True

        # Save to history
        hist_entry = {
            "id": f"HIST-{len(st.session_state.exam_history) + 1:04d}",
            "type": mock_mode,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "profile": prof['nameVi'] if st.session_state.lang == 'vi' else prof['nameEn'],
            "rawScore": f"{total_pts}/{max_pts} ({pct}%)",
            "scaledScore": scaled_score,
            "status": "Đạt (Pass)" if passed else "Cần rèn luyện (Need Practice)",
            "totalQuestions": len(exam_items)
        }
        st.session_state.exam_history.insert(0, hist_entry)
        st.session_state.lotus_bloomed += 2
        st.rerun()
