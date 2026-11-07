# -*- coding: utf-8 -*-
"""
Learning Journal, Lotus Garden, Notes, Review Flags, and Exam Diagnostic for Học Coaching
100% authentic data tracking with zero fabricated progress.
"""
import streamlit as st
from scripts.icf_curriculum_data import get_icf_7_modules

def render_journal_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t, set_page):
    all_modules = get_icf_7_modules()
    
    # Build lesson metadata dictionary for easy lookup
    lesson_map = {}
    for mod in all_modules:
        for les in mod.get("lessons", []):
            lesson_map[les["id"]] = {
                "moduleId": mod["id"],
                "moduleNumber": mod.get("number", 1),
                "moduleTitleVi": mod.get("titleVi", ""),
                "moduleTitleEn": mod.get("titleEn", ""),
                "lessonId": les["id"],
                "lessonNumber": les.get("lessonNumber", 1),
                "lessonTitleVi": les.get("titleVi", ""),
                "lessonTitleEn": les.get("titleEn", "")
            }

    # Gather all personal notes from curriculum progress & legacy notes
    progress = st.session_state.get("curriculum_progress", {})
    legacy_notes = st.session_state.get("notes", {})
    
    # Unified notes dictionary: {lesson_id: note_text}
    all_notes = {}
    for les_id, p_data in progress.items():
        if isinstance(p_data, dict) and p_data.get("note", "").strip():
            all_notes[les_id] = p_data["note"].strip()
    for les_id, note_text in legacy_notes.items():
        if note_text.strip() and les_id not in all_notes:
            all_notes[les_id] = note_text.strip()

    # Flagged lessons
    flagged_lessons = [
        les_id for les_id, p_data in progress.items()
        if isinstance(p_data, dict) and p_data.get("needs_review")
    ]

    # Lotus bloomed
    lotus_count = st.session_state.get("lotus_bloomed", 0)

    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-primary">📓 {t('Sổ Học Tập & Theo Dõi Tiến Trình', 'Learning Journal & Mindful Progress')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Sổ Học Tập (Learning Journal)', 'Learning Journal')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6; margin-bottom: 0;">
            {t('Không gian tĩnh tại ghi nhận từng bước tiến bộ thực chất của bạn: Vườn Sen Chánh Niệm, ghi chú suy ngẫm theo bài, danh sách bài cần ôn lại, câu hỏi đã lưu và lịch sử kết quả thi.',
               'A mindful space recording your verified study progress: Mindful Lotus Garden, reflections by lesson, flagged review items, bookmarked questions, and exam history.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_garden, tab_notes, tab_flagged, tab_suggestions, tab_bm, tab_hist = st.tabs([
        f"🪷 {t('Vườn Sen Chánh Niệm', 'Lotus Garden')} ({lotus_count})",
        f"📝 {t('Ghi Chú Của Tôi', 'My Notes')} ({len(all_notes)})",
        f"🚩 {t('Bài Cần Ôn', 'Review Flags')} ({len(flagged_lessons)})",
        f"💡 {t('Gợi Ý Ôn Lại', 'System Diagnostics')}",
        f"★ {t('Câu Hỏi Đã Lưu', 'Bookmarked')} ({len(st.session_state.bookmarked_qids)})",
        f"📊 {t('Lịch Sử Thi', 'Exam History')} ({len(st.session_state.exam_history)})"
    ])

    # ==========================================
    # TAB 1: VƯỜN SEN CHÁNH NIỆM
    # ==========================================
    with tab_garden:
        st.markdown(f"""
        <div class="zen-card" style="border-left: 4px solid #9C4158; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span class="zen-badge zen-badge-pink">🪷 {t('Quy Chế Thu Hoạch Sen Chánh Niệm', 'Mindful Lotus Harvesting Standard')}</span>
                    <h3 style="margin: 8px 0; color: #2F3E34;">{t('Vườn Sen Của Bạn: ', 'Your Lotus Garden: ')} {lotus_count} {t('đóa sen đã nở', 'bloomed lotuses')}</h3>
                </div>
            </div>
            <div style="font-size: 1.6rem; color: #9C4158; margin: 8px 0;">
                {'🪷 ' * min(lotus_count, 15)}
            </div>
            <div style="font-size: 0.92rem; color: #5F6F65; line-height: 1.6; background: #FAF7F2; padding: 12px 16px; border-radius: 8px; border: 1px solid #EADBCC;">
                <b>📌 {t('Cách nhận sen:', 'How to earn lotuses:')}</b> {t('Hoàn thành hợp lệ mỗi bài học nhận đúng 1 đóa sen chánh niệm. Mỗi bài chỉ được nhận 1 lần duy nhất, không cộng dồn khi xem lại nhiều lần.',
                   'Complete each study lesson to earn exactly 1 mindful lotus. Awarded only once per lesson; never duplicate.')}<br/>
                <b>🌱 {t('Số sen hiện có:', 'Current lotus count:')}</b> <b>{lotus_count}</b> đóa sen.<br/>
                <b>🎯 {t('Mốc tiếp theo:', 'Next milestone:')}</b> {
                    f"Còn thiếu <b>{max(0, 3 - lotus_count)}</b> sen để mở khóa <b>Mốc 3 sen (Bộ Flashcard)</b>" if lotus_count < 3
                    else (f"Còn thiếu <b>{max(0, 8 - lotus_count)}</b> sen để mở khóa <b>Mốc 8 sen (Bài ôn theo chủ đề)</b>" if lotus_count < 8
                    else (f"Còn thiếu <b>{max(0, 15 - lotus_count)}</b> sen để mở khóa <b>Mốc 15 sen (Thử thách nâng cao)</b>" if lotus_count < 15
                    else "🎉 <b>Bạn đã mở khóa trọn vẹn tất cả các mốc thành tựu cao nhất!</b>"))
                }
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"#### 🏆 {t('Các Mốc Phần Thưởng & Trạng Thái Mở Khóa:', 'Achievement Milestones & Unlock Status:')}")
        
        c_m1, c_m2, c_m3 = st.columns(3)
        # Milestone 1: 3 sen
        with c_m1:
            m1_unlocked = lotus_count >= 3
            st.markdown(f"""
            <div class="zen-card" style="height: 220px; display: flex; flex-direction: column; justify-content: space-between; border-top: 3px solid {'#8BA888' if m1_unlocked else '#D4A373'};">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span class="zen-badge {'zen-badge-primary' if m1_unlocked else 'zen-badge-gold'}">
                            {'✅ Đã Mở Khóa' if m1_unlocked else f'🔒 Cần 3 Sen ({lotus_count}/3)'}
                        </span>
                        <span style="font-size: 1.2rem;">🃏</span>
                    </div>
                    <h4 style="margin: 6px 0; color: #2F3E34;">{t('Mốc 3 Sen: Bộ Flashcard', '3 Lotuses: Core Flashcards')}</h4>
                    <p style="font-size: 0.85rem; color: #666; line-height: 1.5;">
                        {t('Mở khóa Bộ Flashcard 8 Năng lực Cốt lõi và Thuật ngữ then chốt giúp ôn phản xạ nhanh.',
                           'Unlock 8 Core Competencies & Glossary Flashcards for quick recall drills.')}
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if m1_unlocked:
                if st.button("🚀 " + t("Mở Bộ Flashcard", "Open Flashcards"), key="btn_unlock_m1", type="primary", use_container_width=True):
                    set_page("curriculum", module_id="mod-7", lesson_id="gl-01")
                    st.rerun()
            else:
                st.button(f"🔒 Còn thiếu {3 - lotus_count} sen", key="btn_m1_locked", disabled=True, use_container_width=True)

        # Milestone 2: 8 sen
        with c_m2:
            m2_unlocked = lotus_count >= 8
            st.markdown(f"""
            <div class="zen-card" style="height: 220px; display: flex; flex-direction: column; justify-content: space-between; border-top: 3px solid {'#8BA888' if m2_unlocked else '#D4A373'};">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span class="zen-badge {'zen-badge-primary' if m2_unlocked else 'zen-badge-gold'}">
                            {'✅ Đã Mở Khóa' if m2_unlocked else f'🔒 Cần 8 Sen ({lotus_count}/8)'}
                        </span>
                        <span style="font-size: 1.2rem;">🎯</span>
                    </div>
                    <h4 style="margin: 6px 0; color: #2F3E34;">{t('Mốc 8 Sen: Bài Ôn Theo Chủ Đề', '8 Lotuses: Themed Practice')}</h4>
                    <p style="font-size: 0.85rem; color: #666; line-height: 1.5;">
                        {t('Mở khóa chế độ Luyện 10 câu chuyên sâu tập trung vào các tình huống Đạo đức và Ranh giới chuyển gửi.',
                           'Unlock Daily 10 Drills focusing deeply on Ethics and Referral Boundaries dilemmas.')}
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if m2_unlocked:
                if st.button("🚀 " + t("Vào Bài Ôn Chủ Đề", "Start Themed Drill"), key="btn_unlock_m2", type="primary", use_container_width=True):
                    set_page("daily_practice")
                    st.rerun()
            else:
                st.button(f"🔒 Còn thiếu {max(0, 8 - lotus_count)} sen", key="btn_m2_locked", disabled=True, use_container_width=True)

        # Milestone 3: 15 sen
        with c_m3:
            m3_unlocked = lotus_count >= 15
            st.markdown(f"""
            <div class="zen-card" style="height: 220px; display: flex; flex-direction: column; justify-content: space-between; border-top: 3px solid {'#8BA888' if m3_unlocked else '#D4A373'};">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span class="zen-badge {'zen-badge-primary' if m3_unlocked else 'zen-badge-gold'}">
                            {'✅ Đã Mở Khóa' if m3_unlocked else f'🔒 Cần 15 Sen ({lotus_count}/15)'}
                        </span>
                        <span style="font-size: 1.2rem;">⚡</span>
                    </div>
                    <h4 style="margin: 6px 0; color: #2F3E34;">{t('Mốc 15 Sen: Thử Thách Nâng Cao', '15 Lotuses: Advanced Challenge')}</h4>
                    <p style="font-size: 0.85rem; color: #666; line-height: 1.5;">
                        {t('Mở khóa Phòng thi thử mô phỏng toàn diện 78–80 câu SJT với hệ thống chấm 4 mức điểm quy đổi 200–600.',
                           'Unlock full 78–80 SJT exam simulation with authentic 4-tier grading scaled 200–600.')}
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if m3_unlocked:
                if st.button("🚀 " + t("Vào Thi Thử Mô Phỏng", "Enter Simulator"), key="btn_unlock_m3", type="primary", use_container_width=True):
                    set_page("sjt")
                    st.rerun()
            else:
                st.button(f"🔒 Còn thiếu {max(0, 15 - lotus_count)} sen", key="btn_m3_locked", disabled=True, use_container_width=True)

    # ==========================================
    # TAB 2: GHI CHÚ CỦA TÔI (SEARCH, EDIT, BACK-LINK)
    # ==========================================
    with tab_notes:
        st.markdown(f"""
        <div class="zen-card" style="margin-bottom: 16px;">
            <h3 style="margin: 0 0 6px 0; color: #2F3E34;">📝 {t('Ghi Chú Cá Nhân Theo Bài Học', 'Personal Reflections & Notes')}</h3>
            <p style="font-size: 0.88rem; color: #666; margin-bottom: 0;">
                {t('Toàn bộ các ghi chú bạn đã lưu trong quá trình học lý thuyết được đồng bộ tại đây. Bạn có thể tìm kiếm, chỉnh sửa trực tiếp hoặc bấm vào tên bài học để quay lại bài gốc.',
                   'All notes saved during your study sessions are unified here. You can search, edit inline, or jump back to the original lesson.')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Keyword search
        search_kw = st.text_input(
            "🔍 " + t("Tìm kiếm ghi chú theo từ khóa:", "Search notes by keyword:"),
            placeholder=t("Nhập từ khóa cần tìm trong các ghi chú của bạn...", "Type keyword to filter your notes...")
        ).strip().lower()

        filtered_notes = {
            k: v for k, v in all_notes.items()
            if not search_kw or (search_kw in v.lower() or search_kw in k.lower())
        }

        if not filtered_notes:
            if not all_notes:
                st.info(t("Bạn chưa lưu ghi chú nào trong các bài học. Hãy vào mục 'Lộ Trình Học', kéo xuống cuối bài và nhập suy ngẫm của bạn vào ô Ghi chú!",
                          "No notes recorded yet. Explore the Curriculum Pathway, scroll down to any lesson, and save your reflections!"))
                if st.button("👉 " + t("Đến Lộ Trình Học", "Go to Curriculum Pathway"), key="btn_goto_cur_from_notes"):
                    set_page("curriculum", module_id="mod-1", lesson_id="mod1-les1")
                    st.rerun()
            else:
                st.warning(t(f"Không tìm thấy ghi chú nào khớp với từ khóa '{search_kw}'.", f"No notes match '{search_kw}'."))
        else:
            st.markdown(f"*{t(f'Hiển thị {len(filtered_notes)} ghi chú:', f'Displaying {len(filtered_notes)} notes:')}*")
            for les_id, note_content in filtered_notes.items():
                les_info = lesson_map.get(les_id, {
                    "moduleId": "mod-1",
                    "moduleTitleVi": t("Học phần liên quan", "Curriculum Module"),
                    "lessonTitleVi": les_id
                })

                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 12px; border-left: 4px solid #8BA888;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 8px;">
                        <span class="zen-badge zen-badge-primary">📖 {les_info.get('moduleTitleVi' if st.session_state.lang == 'vi' else 'moduleTitleEn', 'Học phần')}</span>
                        <span class="zen-badge zen-badge-gold">ID: {les_id}</span>
                    </div>
                    <h4 style="margin: 4px 0 10px 0; color: #2F3E34;">
                        {les_info.get('lessonTitleVi' if st.session_state.lang == 'vi' else 'lessonTitleEn', les_id)}
                    </h4>
                </div>
                """, unsafe_allow_html=True)

                # Inline Edit
                new_note = st.text_area(
                    t("Nội dung ghi chú:", "Note content:"),
                    value=note_content,
                    key=f"edit_note_{les_id}",
                    height=90
                )

                col_btn_save, col_btn_jump = st.columns([1, 1])
                with col_btn_save:
                    if st.button("💾 " + t("Lưu Thay Đổi", "Save Changes"), key=f"btn_save_inline_{les_id}", use_container_width=True):
                        # Update curriculum progress
                        if "curriculum_progress" not in st.session_state:
                            st.session_state.curriculum_progress = {}
                        if les_id not in st.session_state.curriculum_progress:
                            st.session_state.curriculum_progress[les_id] = {"status": "read", "score": 0, "note": new_note, "needs_review": False}
                        else:
                            st.session_state.curriculum_progress[les_id]["note"] = new_note
                        
                        # Sync to notes dictionary
                        if "notes" not in st.session_state:
                            st.session_state.notes = {}
                        st.session_state.notes[les_id] = new_note
                        st.toast(t("Đã cập nhật ghi chú thành công!", "Note updated successfully!"))
                        st.rerun()

                with col_btn_jump:
                    if st.button("👉 " + t("Quay Lại Bài Gốc", "Jump to Lesson"), key=f"btn_jump_to_les_{les_id}", use_container_width=True):
                        target_mod = les_info.get("moduleId", "mod-1")
                        set_page("curriculum", module_id=target_mod, lesson_id=les_id)
                        st.rerun()

    # ==========================================
    # TAB 3: BÀI CẦN ÔN (FLAGGED BY STUDENT)
    # ==========================================
    with tab_flagged:
        st.markdown(f"""
        <div class="zen-card" style="margin-bottom: 16px;">
            <h3 style="margin: 0 0 6px 0; color: #2F3E34;">🚩 {t('Danh Sách Bài Cần Ôn Lại (Do Bạn Tự Gắn Cờ)', 'Self-Flagged Review Lessons')}</h3>
            <p style="font-size: 0.88rem; color: #666; margin-bottom: 0;">
                {t('Các bài học bạn chủ động gắn cờ 🚩 "Cần ôn lại" trong quá trình học. Việc gắn cờ giúp bạn ghi nhớ quay lại củng cố mà không làm mất trạng thái hoàn thành của bài học.',
                   'Lessons you manually flagged for revision. Flagging marks them for review without resetting your completion status.')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        if not flagged_lessons:
            st.info(t("Hiện tại bạn chưa gắn cờ bài học nào. Khi học lý thuyết, bạn có thể bấm nút '🚩 Cần Ôn Lại' ở đầu bài học bất kỳ để lưu vào danh sách này!",
                      "No lessons flagged for review yet. While studying, click '🚩 Flag Review' at the top of any lesson to keep track of it here!"))
        else:
            for les_id in flagged_lessons:
                les_info = lesson_map.get(les_id, {
                    "moduleId": "mod-1",
                    "moduleTitleVi": t("Học phần liên quan", "Curriculum Module"),
                    "lessonTitleVi": les_id
                })
                p_status = progress.get(les_id, {}).get("status", "unread")
                status_label = t("✅ Đã hoàn thành", "Completed") if p_status in ["read", "quiz_passed"] else t("⚪ Đang học", "In progress")

                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 12px; border-left: 4px solid #C62828;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 6px;">
                        <div>
                            <span class="zen-badge zen-badge-pink">🚩 {t('Cần Ôn Lại', 'Needs Review')}</span>
                            <span class="zen-badge zen-badge-primary">{status_label}</span>
                        </div>
                        <span class="zen-badge zen-badge-gray">ID: {les_id}</span>
                    </div>
                    <h4 style="margin: 6px 0 2px 0; color: #2F3E34;">
                        {les_info.get('lessonTitleVi' if st.session_state.lang == 'vi' else 'lessonTitleEn', les_id)}
                    </h4>
                    <div style="font-size: 0.85rem; color: #777;">
                        {les_info.get('moduleTitleVi' if st.session_state.lang == 'vi' else 'moduleTitleEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                col_f1, col_f2 = st.columns([1, 1])
                with col_f1:
                    if st.button("👉 " + t("Vào Ôn Bài Này Ngay", "Study Lesson Now"), key=f"btn_study_flagged_{les_id}", type="primary", use_container_width=True):
                        set_page("curriculum", module_id=les_info.get("moduleId", "mod-1"), lesson_id=les_id)
                        st.rerun()
                with col_f2:
                    if st.button("⛳ " + t("Bỏ Cờ Đánh Dấu (Đã Ôn Xong)", "Unflag (Reviewed)"), key=f"btn_unflag_{les_id}", use_container_width=True):
                        if les_id in st.session_state.curriculum_progress:
                            st.session_state.curriculum_progress[les_id]["needs_review"] = False
                            st.toast(t("Đã gỡ cờ đánh dấu thành công!", "Unflagged successfully!"))
                            st.rerun()

    # ==========================================
    # TAB 4: GỢI Ý ÔN LẠI TỪ KẾT QUẢ LÀM BÀI
    # ==========================================
    with tab_suggestions:
        st.markdown(f"""
        <div class="zen-card" style="margin-bottom: 16px; border-left: 4px solid #D4A373;">
            <span class="zen-badge zen-badge-gold">💡 {t('Chẩn Đoán Tự Động Từ Kết Quả Thi', 'System Diagnostics After Grading')}</span>
            <h3 style="margin: 8px 0 4px 0; color: #2F3E34;">{t('Gợi Ý Ôn Lại Từ Kết Quả Làm Bài', 'Review Recommendations from Exam Results')}</h3>
            <p style="font-size: 0.9rem; color: #5F6F65; line-height: 1.5; margin-bottom: 0;">
                {t('Phân tích độc lập dựa trên các bài thi thử hoặc phiên luyện 10 câu bạn đã nộp. Hệ thống tự động phát hiện các chủ đề có tỷ lệ câu hỏi chưa đạt và đưa ra gợi ý trọng tâm.',
                   'Independent analysis based on your submitted mock exams or daily drills. Identifies error-prone competencies and offers focused review pathways.')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Standard benchmark reminder banner
        st.markdown(f"""
        <div style="background: #EBF3FA; border: 1px solid #B8D5E5; border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; font-size: 0.9rem; color: #1E4E79; line-height: 1.5;">
            ⚖️ <b>{t('Quy chế điểm chuẩn ICF Credentialing Exam:', 'Official ICF Benchmark:')}</b> {t('Thang điểm quy đổi chuẩn là <b>200–600</b>. Ngưỡng đạt chuẩn (Passing benchmark) bắt buộc là <b>460 / 600</b>.',
               'Standard scaled score is <b>200–600</b>. The official passing benchmark is <b>460 / 600</b>.')}
        </div>
        """, unsafe_allow_html=True)

        history = st.session_state.get("exam_history", [])
        if not history:
            st.info(t("Chưa có lượt làm bài nào được ghi nhận. Hãy hoàn thành ít nhất 1 phiên Luyện 10 câu hoặc Thi thử để hệ thống kích hoạt chẩn đoán!",
                      "No exam results recorded yet. Complete at least 1 daily drill or mock exam to trigger system recommendations!"))
        else:
            latest = history[0]
            scaled = latest.get("scaledScore", 420)
            is_pass = scaled >= 460
            
            st.markdown(f"""
            <div class="zen-card" style="padding: 16px 20px; margin-bottom: 16px; border-left: 4px solid {'#8BA888' if is_pass else '#C62828'};">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <div>
                        <span class="zen-badge {'zen-badge-primary' if is_pass else 'zen-badge-pink'}">
                            {t('Kết quả bài thi gần nhất:', 'Latest Exam:')} {latest.get('type', 'Thi Thử')} ({latest.get('date', '')})
                        </span>
                    </div>
                    <div style="font-size: 1.3rem; font-weight: 700; color: #2F3E34;">
                        {scaled} <span style="font-size: 0.85rem; color: #777;">/ 600 ({'✅ ĐẠT CHUẨN' if is_pass else '❌ CHƯA ĐẠT CHUẨN (Cần >= 460)'})</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"#### 🎯 {t('Các Năng Lực Trọng Tâm Cần Ôn Tập Lại:', 'Priority Competencies for Review:')}")
            
            # Diagnostic competencies
            recom_items = [
                {"name": "1. Thực Hành Chuẩn Đạo Đức (Ethical Practice)", "modId": "mod-1", "lesId": "mod1-les1", "why": "Dễ nhầm lẫn ranh giới bảo mật và xung đột lợi ích tài chính."},
                {"name": "2. Thể Hiện Tư Duy Khai Vấn (Coaching Mindset)", "modId": "mod-1", "lesId": "mod1-les2", "why": "Cần duy trì thực hành phản tư và tự điều hòa cảm xúc liên tục."},
                {"name": "3. Ranh Giới Chuyển Gửi Trị Liệu (White Paper 2018)", "modId": "mod-6", "lesId": "mod6-les1", "why": "Tránh bẫy tự chẩn đoán bệnh lý hoặc chuyển gửi vội vã chỉ vì khách khóc."},
                {"name": "7. Khơi Gợi Nhận Thức (Evokes Awareness)", "modId": "mod-1", "lesId": "mod1-les7", "why": "Phân biệt giữa câu hỏi mở chân thực và câu hỏi suy diễn áp đặt định kiến."}
            ]

            for rec in recom_items:
                st.markdown(f"""
                <div class="zen-card" style="padding: 14px 18px; margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                        <b style="color: #2F3E34; font-size: 0.95rem;">{rec['name']}</b>
                        <span class="zen-badge zen-badge-gold">Cần bồi đắp</span>
                    </div>
                    <p style="font-size: 0.85rem; color: #666; margin: 6px 0 10px 0;">
                        👉 <i>{rec['why']}</i>
                    </p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"👉 Vào ôn tập: {rec['name'][:30]}...", key=f"btn_rec_{rec['modId']}_{rec['lesId']}", use_container_width=True):
                    set_page("curriculum", module_id=rec["modId"], lesson_id=rec["lesId"])
                    st.rerun()

    # ==========================================
    # TAB 5: CÂU HỎI ĐÃ LƯU ★
    # ==========================================
    with tab_bm:
        bm_ids = st.session_state.bookmarked_qids
        all_q_map = {q["id"]: q for q in (PRACTICE_QUESTIONS + KNOWLEDGE_QUESTIONS + OFFICIAL_SAMPLES)}

        if not bm_ids:
            st.info(t("Chưa có câu hỏi nào được lưu. Bấm biểu tượng '☆ Lưu câu hỏi' trong lúc Luyện 10 câu hoặc ở màn hình xem lại bài thi để lưu vào đây!",
                      "No bookmarked questions yet. Click '☆ Bookmark' during practice or on the review screen to save questions here!"))
        else:
            st.markdown(f"#### ★ {t(f'Danh Sách {len(bm_ids)} Câu Hỏi Đã Lưu Để Ôn Tập Lâu Dài:', f'{len(bm_ids)} Bookmarked Questions:')}")
            for qid in list(bm_ids):
                q = all_q_map.get(qid)
                if not q: continue

                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 14px; border-left: 4px solid #D4A373;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 6px;">
                        <span class="zen-badge zen-badge-gold">ID: {qid}</span>
                        <span class="zen-badge zen-badge-primary">{q.get('primaryCompetency', q.get('domain', 'ICF Standard'))}</span>
                    </div>
                    <h4 style="margin: 8px 0; color: #2F3E34; font-size: 1rem; line-height: 1.5;">
                        {q['questionVi'] if st.session_state.lang == 'vi' else q['questionEn']}
                    </h4>
                    <div style="font-size: 0.88rem; color: #555; background: #FAF7F2; padding: 10px 14px; border-radius: 8px; margin: 8px 0;">
                        <b>{t('Đáp án chuẩn:', 'Official Key:')}</b> {'🌟 BEST: ' + str(q.get('bestAnswer')) + ' | ⚠️ WORST: ' + str(q.get('worstAnswer')) if 'bestAnswer' in q else 'ĐÁP ÁN: ' + str(q.get('correctAnswer'))}<br/>
                        <b>📖 {t('Lý giải:', 'Rationale:')}</b> {q.get('explanationVi', '') if st.session_state.lang == 'vi' else q.get('explanationEn', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("🗑️ " + t("Bỏ Lưu Câu Này", "Remove Bookmark"), key=f"btn_unbm_{qid}"):
                    st.session_state.bookmarked_qids.remove(qid)
                    st.toast(t("Đã bỏ lưu câu hỏi!", "Removed from bookmarks!"))
                    st.rerun()

    # ==========================================
    # TAB 6: LỊCH SỬ THI & ĐIỂM SỐ
    # ==========================================
    with tab_hist:
        history = st.session_state.get("exam_history", [])
        if not history:
            st.info(t("Bạn chưa hoàn thành phiên làm bài nào. Hãy bắt đầu một lượt Luyện 10 Câu hoặc Thi Thử Mô Phỏng để ghi lại tiến trình thực tế!",
                      "No exam attempts recorded yet. Complete a Daily Drill or Mock Simulator to track genuine progress!"))
        else:
            scores = [h.get("scaledScore", 0) for h in history if "scaledScore" in h]
            avg_score = int(sum(scores) / len(scores)) if scores else 0
            best_score = max(scores) if scores else 0
            pass_count = sum(1 for h in history if ("Đạt" in h.get("status", "") or "Pass" in h.get("status", "")) or h.get("scaledScore", 0) >= 460)

            c1, c2, c3, c4 = st.columns(4)
            with c1: st.metric(label=t("Tổng Lượt Thi", "Total Attempts"), value=f"{len(history)} {t('lượt', 'runs')}")
            with c2: st.metric(label=t("Điểm Trung Bình", "Average Scaled Score"), value=f"{avg_score} / 600")
            with c3: st.metric(label=t("Điểm Cao Nhất", "Best Scaled Score"), value=f"{best_score} / 600")
            with c4: st.metric(label=t("Tỷ Lệ Đạt (>=460)", "Pass Rate (>=460)"), value=f"{int(pass_count / len(history) * 100)}%")

            st.markdown("<br/>", unsafe_allow_html=True)
            st.markdown(f"#### 📋 {t('Bảng Nhật Ký Các Lượt Thi Đã Lưu:', 'Recorded Exam Attempts:')}")

            for h in history:
                is_p = ("Đạt" in h.get("status", "") or "Pass" in h.get("status", "")) or h.get("scaledScore", 0) >= 460
                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 12px; border-left: 4px solid {'#8BA888' if is_p else '#D4A373'};">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                        <div>
                            <span class="zen-badge {'zen-badge-primary' if is_p else 'zen-badge-gold'}">{h.get('status', 'Hoàn thành')}</span>
                            <span class="zen-badge zen-badge-gray">📅 {h.get('date', '')}</span>
                            <span class="zen-badge zen-badge-blue">{h.get('type', 'Thi Thử')}</span>
                        </div>
                        <div style="font-size: 1.25rem; font-weight: 700; color: #2F3E34;">
                            {h.get('scaledScore', '--')} <span style="font-size: 0.85rem; font-weight: normal; color: #777;">/ 600 (Chuẩn đỗ: 460)</span>
                        </div>
                    </div>
                    <div style="font-size: 0.88rem; color: #555; margin-top: 8px;">
                        <b>{t('Cấu hình:', 'Profile:')}</b> {h.get('profile', '')} | 
                        <b>{t('Điểm thô:', 'Raw:')}</b> {h.get('rawScore', '')} ({h.get('totalQuestions', 0)} {t('câu hỏi', 'items')})
                    </div>
                </div>
                """, unsafe_allow_html=True)
