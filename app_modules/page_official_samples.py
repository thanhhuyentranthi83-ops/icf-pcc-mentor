# -*- coding: utf-8 -*-
"""
Official ICF Sample Questions Page for PCC Learning & Practice
8 Publicly released ICF Credentialing Exam Sample Questions with official answer keys
"""
import streamlit as st

def render_official_samples_page(OFFICIAL_SAMPLES, t):
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-gold">📑 {t('Nguồn Công Bố Chính Thức', 'Official Public Release')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('8 Câu Mẫu Chuẩn Kỳ Thi ICF (Official Sample Questions)', '8 Official ICF Credentialing Exam Sample Questions')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Đây là 8 câu hỏi tình huống mẫu được International Coaching Federation (ICF) công bố công khai trên trang web chính thức đại diện cho 8 Năng lực Cốt lõi. Toàn bộ kịch bản tiếng Anh được giữ nguyên văn, đi kèm bản dịch tiếng Việt học tập và đáp án chính thức.',
               'These are the 8 official public sample questions published on the ICF website representing each of the 8 Core Competencies. English scenario text is presented verbatim alongside verified learning translations and official answer keys.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Filter by Competency
    comp_list = ["Tất cả 8 câu / All 8 Samples"] + [f"Competency {i}" for i in range(1, 9)]
    selected_comp = st.selectbox(
        "🎯 " + t("Lọc theo Năng lực cốt lõi:", "Filter by Core Competency:"),
        options=comp_list,
        index=0
    )

    filtered_samples = OFFICIAL_SAMPLES
    if "Competency" in selected_comp:
        comp_num = selected_comp.split()[1]
        filtered_samples = [q for q in OFFICIAL_SAMPLES if str(q.get("competencyNumber", "")) == comp_num or f"Competency {comp_num}" in q.get("primaryCompetency", "")]

    st.markdown(f"**{t('Hiển thị:', 'Showing:')}** {len(filtered_samples)} {t('câu hỏi mẫu', 'official sample items')}")
    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 12px 0 20px 0;'/>", unsafe_allow_html=True)

    for idx, q in enumerate(filtered_samples):
        qid = q["id"]
        is_bm = qid in st.session_state.bookmarked_qids
        state_key = f"osq_ans_{qid}"
        reveal_key = f"osq_reveal_{qid}"

        if state_key not in st.session_state.official_answers:
            st.session_state.official_answers[state_key] = {"best": None, "worst": None}
        if reveal_key not in st.session_state:
            st.session_state[reveal_key] = False

        # Header with Question Number and Star Bookmark Button
        col_q_head1, col_q_head2 = st.columns([4, 1])
        with col_q_head1:
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <span class="zen-badge zen-badge-primary">Câu {idx + 1} ({qid})</span>
                <span class="zen-badge zen-badge-gold">{q.get('primaryCompetency', '')}</span>
            </div>
            """, unsafe_allow_html=True)
        with col_q_head2:
            bm_label = "★ " + t("Đã lưu", "Saved") if is_bm else "☆ " + t("Lưu câu", "Save")
            if st.button(bm_label, key=f"btn_official_bm_head_{qid}", use_container_width=True):
                if is_bm:
                    st.session_state.bookmarked_qids.remove(qid)
                    st.toast(t("Đã bỏ lưu câu hỏi!", "Removed from bookmarks!"))
                else:
                    st.session_state.bookmarked_qids.append(qid)
                    st.toast(t("Đã lưu vào Sổ Học Tập → Câu hỏi đã lưu!", "Saved to Learning Journal!"))
                st.rerun()

        st.markdown(f"""
            <div style="background: #FAF7F2; padding: 16px; border-radius: 12px; margin: 10px 0 16px 0; border: 1px solid #EADBCC;">
                <div style="font-size: 0.82rem; color: #8C6D53; font-weight: 600; margin-bottom: 4px;">🇬🇧 ORIGINAL ICF VERBATIM SCENARIO:</div>
                <div style="font-size: 0.96rem; color: #2C3E50; line-height: 1.6; font-style: italic;">
                    "{q['scenarioEn']}"
                </div>
                <div style="margin-top: 10px; font-weight: 600; color: #2F3E34;">
                    👉 {q['questionEn']}
                </div>
            </div>
            <div style="background: #FFFFFF; padding: 14px; border-radius: 10px; margin-bottom: 16px; border: 1px dashed #D8C7B5;">
                <div style="font-size: 0.82rem; color: #3F4F44; font-weight: 600; margin-bottom: 4px;">🇻🇳 BẢN DỊCH HỌC TẬP TIẾNG VIỆT:</div>
                <div style="font-size: 0.94rem; color: #333; line-height: 1.6;">
                    {q['scenarioVi']}
                </div>
                <div style="margin-top: 8px; font-weight: 600; color: #2F3E34;">
                    👉 {q['questionVi']}
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Options Display with complete text wrapping
        st.markdown(f"**{t('Các phương án lựa chọn (Options):', 'Available Options:')}**")
        for opt in q["options"]:
            st.markdown(f"""
            <div style="background: #FAF7F2; border: 1px solid #EADBCC; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; line-height: 1.5; white-space: normal; word-break: break-word;">
                <b style="color: #2F3E34; font-size: 0.95rem;">[{opt['key']}]</b> <b>EN:</b> {opt['textEn']}<br/>
                <span style="color: #555; font-size: 0.9rem;"><b>VI:</b> {opt['textVi']}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        # Separate BEST and WORST Blocks with identical A-D options
        col_b, col_w = st.columns(2)
        opt_keys = [opt["key"] for opt in q["options"]]

        with col_b:
            st.markdown(f"**🌟 {t('CHỌN 1 HÀNH ĐỘNG TỐT NHẤT (BEST)', 'SELECT 1 BEST ACTION')}**")
            cur_best = st.session_state.official_answers[state_key].get("best")
            best_idx = opt_keys.index(cur_best) if cur_best in opt_keys else None
            chosen_best = st.radio(
                t(f"Lựa chọn Best cho {qid}:", f"Best selection for {qid}:"),
                options=opt_keys,
                format_func=lambda k: f"Phương án [{k}]",
                horizontal=True,
                key=f"radio_best_{qid}",
                index=best_idx,
                label_visibility="collapsed"
            )
            st.session_state.official_answers[state_key]["best"] = chosen_best

        with col_w:
            st.markdown(f"**⚠️ {t('CHỌN 1 HÀNH ĐỘNG TỆ NHẤT (WORST)', 'SELECT 1 WORST ACTION')}**")
            cur_worst = st.session_state.official_answers[state_key].get("worst")
            worst_idx = opt_keys.index(cur_worst) if cur_worst in opt_keys else None
            chosen_worst = st.radio(
                t(f"Lựa chọn Worst cho {qid}:", f"Worst selection for {qid}:"),
                options=opt_keys,
                format_func=lambda k: f"Phương án [{k}]",
                horizontal=True,
                key=f"radio_worst_{qid}",
                index=worst_idx,
                label_visibility="collapsed"
            )
            st.session_state.official_answers[state_key]["worst"] = chosen_worst

        # Real-time duplicate check
        if chosen_best and chosen_worst and chosen_best == chosen_worst:
            st.error(t(f"⚠️ Cảnh báo: Bạn đang chọn phương án [{chosen_best}] cho CẢ BEST và WORST. Bài thi ICF yêu cầu 2 phương án hoàn toàn khác nhau!",
                       f"⚠️ Warning: You selected option [{chosen_best}] for BOTH Best and Worst. ICF exams strictly require two distinct options!"))

        st.write("")
        col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 1])
        with col_btn1:
            reveal_label = "👁️ " + t("Ẩn Đáp Án & Phân Tích", "Hide Official Answer") if st.session_state[reveal_key] else "🔍 " + t("Xem Đáp Án Chính Thức", "Reveal Official Answer")
            if st.button(reveal_label, key=f"btn_reveal_{qid}", use_container_width=True):
                st.session_state[reveal_key] = not st.session_state[reveal_key]
                st.rerun()

        with col_btn2:
            bm_btn_text = "★ " + t("Đã Đánh Dấu", "Bookmarked") if is_bm else "☆ " + t("Đánh Dấu Xem Lại", "Bookmark Question")
            if st.button(bm_btn_text, key=f"btn_bm_{qid}", use_container_width=True):
                if is_bm:
                    st.session_state.bookmarked_qids.remove(qid)
                else:
                    st.session_state.bookmarked_qids.append(qid)
                st.rerun()

        # REVEAL BLOCK
        if st.session_state[reveal_key]:
            official_b = q["bestAnswer"]
            official_w = q["worstAnswer"]
            user_b = st.session_state.official_answers[state_key].get("best")
            user_w = st.session_state.official_answers[state_key].get("worst")

            score = 0
            if user_b == official_b: score += 1
            if user_w == official_w: score += 1

            tier_badge = "zen-badge-primary" if score == 2 else ("zen-badge-gold" if score == 1 else "zen-badge-pink")
            tier_text = t("ĐẠT ĐIỂM TỐI ĐA (2/2 Điểm)", "FULL CREDIT (2/2 Points)") if score == 2 else (
                t("ĐẠT ĐIỂM MỘT PHẦN (1/2 Điểm)", "PARTIAL CREDIT (1/2 Point)") if score == 1 else
                t("CHƯA ĐẠT ĐIỂM (0/2 Điểm)", "NO CREDIT (0/2 Points)")
            )

            st.markdown(f"""
            <div style="background: #FAF7F2; border: 2px solid #8BA888; border-radius: 12px; padding: 18px; margin-top: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
                    <span class="zen-badge {tier_badge}" style="font-size: 0.9rem;">🎯 {tier_text}</span>
                    <span style="font-size: 0.85rem; color: #555;">
                        <b>{t('Lựa chọn của bạn:', 'Your selections:')}</b> BEST: <b>{user_b or '--'}</b> | WORST: <b>{user_w or '--'}</b>
                    </span>
                </div>
                <div style="font-size: 1.05rem; margin-bottom: 10px;">
                    🎯 <b>{t('ĐÁP ÁN CHÍNH THỨC TỪ ICF:', 'OFFICIAL ICF ANSWER KEY:')}</b><br/>
                    🌟 <b>BEST = <span style="color: #2E7D32; font-size: 1.2rem;">{official_b}</span></b> ({'✅ Bạn chọn đúng' if user_b == official_b else '❌ Bạn chọn sai'}) &nbsp;|&nbsp; 
                    ⚠️ <b>WORST = <span style="color: #C62828; font-size: 1.2rem;">{official_w}</span></b> ({'✅ Bạn chọn đúng' if user_w == official_w else '❌ Bạn chọn sai'})
                </div>
                <div style="margin-top: 10px; font-size: 0.92rem; line-height: 1.6; color: #2C3E50;">
                    <b>📖 {t('GIẢI THÍCH CHÍNH THỨC TỪ ICF (Official Explanation):', 'OFFICIAL ICF RATIONALE:')}</b><br/>
                    <div style="background: #FFFFFF; padding: 10px 14px; border-radius: 8px; margin: 6px 0; border: 1px solid #EADBCC;">
                        <i>"{q['explanationEn']}"</i>
                    </div>
                    <div style="margin-top: 6px; color: #333;">
                        <b>Bản dịch giải thích:</b> {q['explanationVi']}
                    </div>
                </div>
                <div style="margin-top: 12px; font-size: 0.9rem; line-height: 1.5; color: #8C6D53;">
                    <b>💡 {t('ĐIỂM MẤU CHỐT CỦA NĂNG LỰC:', 'CORE COMPETENCY ANCHOR:')}</b><br/>
                    {q['competencyAnalysisVi']}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
