# -*- coding: utf-8 -*-
"""
Learning Journal & Real Exam History for PCC Learning & Practice
Tracks real exam attempts, bookmarked review questions, and personal notes across all units.
Strictly authentic data tracking without fabricated progress.
"""
import streamlit as st

def render_journal_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t, set_page):
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-primary">📓 {t('Nhật Ký Tỉnh Thức', 'Reflective Journal')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Sổ Học Tập & Lịch Sử Làm Bài (Learning Journal)', 'Learning Journal & Practice History')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Nơi ghi dấu từng bước chân tiến bộ thực chất của bạn trên hành trình chinh phục kỳ thi PCC. Toàn bộ lịch sử điểm số, câu hỏi cần ôn lại và ghi chú đúc kết được lưu trữ nguyên vẹn.',
               'A dedicated space recording your genuine progress towards PCC mastery. Tracks authentic test attempts, bookmarked items for spaced repetition, and personal reflections.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_hist, tab_bm, tab_notes = st.tabs([
        f"📊 {t('Lịch Sử Thi & Điểm Số', 'Exam History')} ({len(st.session_state.exam_history)})",
        f"★ {t('Câu Hỏi Đã Đánh Dấu', 'Bookmarked Items')} ({len(st.session_state.bookmarked_qids)})",
        f"📝 {t('Ghi Chú Năng Lực', 'Competency Notes')} ({len([k for k, v in st.session_state.notes.items() if v.strip()])})"
    ])

    # TAB 1: REAL EXAM HISTORY
    with tab_hist:
        history = st.session_state.exam_history
        if not history:
            st.info(t("Bạn chưa hoàn thành phiên làm bài nào. Hãy bắt đầu một lượt Luyện 10 Câu hoặc Thi Thử Mô Phỏng để ghi lại tiến trình thực tế!",
                      "No exam attempts recorded yet. Complete a Daily Drill or Mock Simulator to track genuine progress!"))
            col1, col2 = st.columns(2)
            with col1:
                if st.button("⚡ " + t("Luyện 10 Câu Ngay", "Start Daily Drill"), use_container_width=True):
                    set_page("daily_practice")
                    st.rerun()
            with col2:
                if st.button("⚖️ " + t("Vào Thi Thử Mô Phỏng", "Enter Mock Simulator"), use_container_width=True):
                    set_page("sjt")
                    st.rerun()
        else:
            # Summary Metrics
            scores = [h.get("scaledScore", 0) for h in history if "scaledScore" in h]
            avg_score = int(sum(scores) / len(scores)) if scores else 0
            best_score = max(scores) if scores else 0
            pass_count = sum(1 for h in history if "Đạt" in h.get("status", "") or "Pass" in h.get("status", ""))

            c1, c2, c3, c4 = st.columns(4)
            with c1: st.metric(label=t("Tổng Lượt Thi", "Total Attempts"), value=f"{len(history)} {t('lượt', 'runs')}")
            with c2: st.metric(label=t("Điểm Trung Bình", "Average Scaled Score"), value=f"{avg_score} / 600")
            with c3: st.metric(label=t("Điểm Cao Nhất", "Best Scaled Score"), value=f"{best_score} / 600")
            with c4: st.metric(label=t("Tỷ Lệ Đạt (>=460)", "Pass Rate (>=460)"), value=f"{int(pass_count / len(history) * 100)}%")

            st.markdown("<br/>", unsafe_allow_html=True)
            st.markdown(f"#### 📋 {t('Bảng Nhật Ký Các Lượt Thi Đã Lưu:', 'Recorded Exam Attempts:')}")

            for h in history:
                is_pass = ("Đạt" in h.get("status", "") or "Pass" in h.get("status", ""))
                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 12px; border-left: 4px solid {'#8BA888' if is_pass else '#D4A373'};">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                        <div>
                            <span class="zen-badge {'zen-badge-primary' if is_pass else 'zen-badge-gold'}">{h.get('status', 'Hoàn thành')}</span>
                            <span class="zen-badge zen-badge-gray">📅 {h.get('date', '')}</span>
                            <span class="zen-badge zen-badge-blue">{h.get('type', 'Thi Thử')}</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 700; color: #2F3E34;">
                            {h.get('scaledScore', '--')} <span style="font-size: 0.85rem; font-weight: normal; color: #777;">/ 600</span>
                        </div>
                    </div>
                    <div style="font-size: 0.88rem; color: #555; margin-top: 8px;">
                        <b>{t('Cấu hình:', 'Profile:')}</b> {h.get('profile', '')} | 
                        <b>{t('Điểm thô:', 'Raw:')}</b> {h.get('rawScore', '')} ({h.get('totalQuestions', 0)} {t('câu hỏi', 'items')})
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # TAB 2: BOOKMARKED ITEMS
    with tab_bm:
        bm_ids = st.session_state.bookmarked_qids
        all_q_map = {q["id"]: q for q in (PRACTICE_QUESTIONS + KNOWLEDGE_QUESTIONS + OFFICIAL_SAMPLES)}

        if not bm_ids:
            st.info(t("Chưa có câu hỏi nào được đánh dấu. Hãy bấm '☆ Đánh dấu' khi làm bài hoặc khảo sát đề mẫu để lưu vào đây!",
                      "No bookmarked questions yet. Click '☆ Bookmark' during practice to review questions here!"))
        else:
            st.markdown(f"#### ★ {t('Danh Sách Câu Hỏi Cần Ôn Tập Lại:', 'Questions Marked for Review:')}")
            for qid in list(bm_ids):
                q = all_q_map.get(qid)
                if not q: continue

                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 14px; border-left: 3px solid #D4A373;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="zen-badge zen-badge-gold">ID: {qid}</span>
                        <span class="zen-badge zen-badge-primary">{q.get('primaryCompetency', q.get('domain', 'ICF Standard'))}</span>
                    </div>
                    <h4 style="margin: 8px 0; color: #2F3E34; font-size: 1rem; line-height: 1.5;">
                        {q['questionVi'] if st.session_state.lang == 'vi' else q['questionEn']}
                    </h4>
                    <div style="font-size: 0.85rem; color: #666; margin-top: 4px;">
                        <b>{t('Đáp án chuẩn:', 'Official Key:')}</b> {'BEST: ' + str(q.get('bestAnswer')) + ' | WORST: ' + str(q.get('worstAnswer')) if 'bestAnswer' in q else 'ĐÁP ÁN: ' + str(q.get('correctAnswer'))}<br/>
                        <b>{t('Lý giải:', 'Rationale:')}</b> {q.get('explanationVi', '') if st.session_state.lang == 'vi' else q.get('explanationEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("🗑️ " + t("Bỏ Đánh Dấu Câu Này", "Remove Bookmark"), key=f"btn_unbm_{qid}"):
                    st.session_state.bookmarked_qids.remove(qid)
                    st.rerun()

    # TAB 3: PERSONAL NOTES
    with tab_notes:
        saved_notes = {k: v for k, v in st.session_state.notes.items() if v.strip()}
        if not saved_notes:
            st.info(t("Bạn chưa lưu ghi chú nào trong các bài học lý thuyết. Hãy vào mục 'Lộ Trình Học' -> Tab 'Sổ Tay Ghi Chú' để ghi lại bài học của mình!",
                      "No personal notes recorded yet. Head over to Curriculum -> Study Notes tab to document your insights!"))
        else:
            st.markdown(f"#### 📝 {t('Các Ghi Chú Đã Lưu Theo Bài Học:', 'Saved Reflections by Unit:')}")
            for sec_id, note_content in saved_notes.items():
                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 14px; border-left: 3px solid #8BA888;">
                    <span class="zen-badge zen-badge-primary">{sec_id}</span>
                    <div style="margin-top: 8px; font-size: 0.95rem; line-height: 1.6; color: #2C3E50; white-space: pre-wrap;">
                        {note_content}
                    </div>
                </div>
                """, unsafe_allow_html=True)
