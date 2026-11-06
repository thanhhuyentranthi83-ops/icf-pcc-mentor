# -*- coding: utf-8 -*-
"""
Admin & Content Quality Review for PCC Learning & Practice
Enables reviewing question bank items (Approved / Under Review), managing dispute logs, and approving membership orders.
"""
import streamlit as st

def render_admin_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t):
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span class="zen-badge zen-badge-blue">🛡️ {t('Bảo Đảm Chất Lượng Học Thuật', 'Academic Quality Assurance')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Quản Trị Hệ Thống & Nhật Ký Kiểm Duyệt', 'Content Administration & Review')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6;">
            {t('Khu vực dành cho kiểm soát chất lượng: Rà soát trạng thái câu hỏi, tiếp nhận và giải quyết phản hồi / khiếu nại của học viên, và quản lý hội viên.',
               'Dedicated administrative portal: Review question bank approvals, handle learner dispute logs, and manage membership transactions.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab_bank, tab_disp, tab_orders = st.tabs([
        f"📚 {t('Kiểm Duyệt Ngân Hàng Câu Hỏi', 'Question Bank Review')} (94 {t('câu', 'items')})",
        f"🚩 {t('Nhật Ký Khiếu Nại & Góp Ý', 'Dispute & Feedback Logs')} ({len(st.session_state.dispute_logs)})",
        f"💳 {t('Đơn Kích Hoạt Hội Viên', 'Membership Orders')} ({len(st.session_state.orders)})"
    ])

    all_questions = OFFICIAL_SAMPLES + PRACTICE_QUESTIONS + KNOWLEDGE_QUESTIONS

    # TAB 1: QUESTION BANK REVIEW
    with tab_bank:
        st.markdown(f"#### 🔍 {t('Danh Mục Toàn Bộ 94 Câu Hỏi Trong Hệ Thống', 'Full Question Bank Inventory (94 Items)')}")
        c_filter1, c_filter2 = st.columns(2)
        with c_filter1:
            type_filter = st.selectbox(
                t("Lọc theo loại câu hỏi:", "Filter by item type:"),
                options=[
                    t("Tất cả câu hỏi", "All Questions"),
                    t("8 Câu mẫu chính thức ICF", "8 Official ICF Samples"),
                    t("50 Tình huống phán đoán (SJT)", "50 SJT Scenarios"),
                    t("36 Câu hỏi kiến thức chuẩn mực", "36 Knowledge MCQs")
                ]
            )
        with c_filter2:
            status_filter = st.selectbox(
                t("Lọc theo trạng thái kiểm duyệt:", "Filter by review status:"),
                options=[t("Tất cả trạng thái", "All Statuses"), t("Đã duyệt (Approved)", "Approved"), t("Đang xem xét (Under Review)", "Under Review")]
            )

        # Filter logic
        display_pool = all_questions
        if "8 Câu mẫu" in type_filter or "Official" in type_filter:
            display_pool = OFFICIAL_SAMPLES
        elif "50 Tình huống" in type_filter or "SJT" in type_filter:
            display_pool = PRACTICE_QUESTIONS
        elif "36 Câu" in type_filter or "Knowledge" in type_filter:
            display_pool = KNOWLEDGE_QUESTIONS

        if "Đã duyệt" in status_filter or "Approved" in status_filter:
            display_pool = [q for q in display_pool if st.session_state.content_status.get(q["id"], "Approved") == "Approved"]
        elif "Đang xem xét" in status_filter or "Under Review" in status_filter:
            display_pool = [q for q in display_pool if st.session_state.content_status.get(q["id"], "Approved") == "Under Review"]

        st.markdown(f"**{t('Số lượng hiển thị:', 'Displayed items:')}** {len(display_pool)} {t('câu hỏi', 'questions')}")
        st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 8px 0 16px 0;'/>", unsafe_allow_html=True)

        for q in display_pool[:30]:  # Render top 30 for performance with pagination notice
            qid = q["id"]
            cur_status = st.session_state.content_status.get(qid, "Approved")
            is_approved = (cur_status == "Approved")

            st.markdown(f"""
            <div class="zen-card" style="padding: 14px 18px; margin-bottom: 12px; border-left: 4px solid {'#8BA888' if is_approved else '#D4A373'};">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <div>
                        <span class="zen-badge {'zen-badge-primary' if is_approved else 'zen-badge-gold'}">
                            {'✅ Đã Duyệt' if is_approved else '⚠️ Đang Xem Xét'}
                        </span>
                        <span class="zen-badge zen-badge-gray">ID: {qid}</span>
                        <span class="zen-badge zen-badge-blue">{q.get('primaryCompetency', q.get('domain', 'ICF Standard'))}</span>
                    </div>
                </div>
                <div style="margin: 8px 0; font-size: 0.92rem; color: #2F3E34;">
                    <b>VI:</b> {q['questionVi']}<br/>
                    <span style="font-size: 0.85rem; color: #555;"><b>EN:</b> {q.get('questionEn', '')[:100]}...</span>
                </div>
                <div style="font-size: 0.85rem; color: #666;">
                    <b>{t('Đáp án chuẩn:', 'Key:')}</b> {'BEST: ' + str(q.get('bestAnswer')) + ' | WORST: ' + str(q.get('worstAnswer')) if 'bestAnswer' in q else 'ĐÁP ÁN: ' + str(q.get('correctAnswer'))}
                </div>
            </div>
            """, unsafe_allow_html=True)

            col_btn1, col_btn2 = st.columns([4, 1])
            with col_btn2:
                btn_status_label = "Chuyển: Xem xét" if is_approved else "Chuyển: Đã duyệt"
                if st.button(btn_status_label, key=f"btn_stat_{qid}", use_container_width=True):
                    st.session_state.content_status[qid] = "Under Review" if is_approved else "Approved"
                    st.rerun()

        if len(display_pool) > 30:
            st.info(f"ℹ️ {t('Đang hiển thị 30 /', 'Showing 30 of')} {len(display_pool)} {t('câu hỏi. Hãy lọc theo loại để xem chi tiết.', 'items. Use filters above to narrow scope.')}")

    # TAB 2: DISPUTE & FEEDBACK LOGS
    with tab_disp:
        disputes = st.session_state.dispute_logs
        if not disputes:
            st.info(t("Hiện tại chưa có khiếu nại hoặc phản hồi nào từ học viên.", "No learner feedback or dispute reports logged yet."))
        else:
            st.markdown(f"#### 🚩 {t('Nhật Ký Các Phản Hồi Từ Học Viên:', 'Learner Feedback Submissions:')}")
            for d in disputes:
                is_resolved = (d.get("status") == "Đã giải quyết")
                st.markdown(f"""
                <div class="zen-card" style="padding: 16px 20px; margin-bottom: 12px; border-left: 4px solid {'#8BA888' if is_resolved else '#9C4158'};">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span class="zen-badge {'zen-badge-primary' if is_resolved else 'zen-badge-pink'}">{d.get('status')}</span>
                            <span class="zen-badge zen-badge-gray">ID: {d.get('id')}</span>
                            <span class="zen-badge zen-badge-gold">Câu hỏi: {d.get('questionId')} ({d.get('questionType')})</span>
                        </div>
                        <span style="font-size: 0.8rem; color: #888;">{d.get('timestamp')}</span>
                    </div>
                    <div style="margin-top: 10px; font-size: 0.92rem; color: #333; background: #FAF7F2; padding: 10px; border-radius: 8px;">
                        <b>{t('Nội dung phản ánh:', 'Learner Feedback Note:')}</b><br/>
                        "{d.get('note')}"
                    </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("🔄 " + t("Đổi trạng thái Xử lý", "Toggle Resolution Status"), key=f"btn_res_{d['id']}"):
                    d["status"] = "Đang xem xét" if is_resolved else "Đã giải quyết"
                    st.rerun()

    # TAB 3: MEMBERSHIP ORDERS
    with tab_orders:
        st.markdown(f"#### 💳 {t('Quản Lý Đơn Kích Hoạt Hội Viên VietQR', 'VietQR Membership Subscriptions')}")
        orders = st.session_state.orders
        for ord_item in orders:
            is_approved = (ord_item["status"] == "Đã duyệt")
            st.markdown(f"""
            <div class="zen-card" style="padding: 16px 20px; margin-bottom: 12px; border-left: 4px solid {'#8BA888' if is_approved else '#D4A373'};">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span class="zen-badge {'zen-badge-primary' if is_approved else 'zen-badge-gold'}">{ord_item['status']}</span>
                        <span class="zen-badge zen-badge-blue">Mã: {ord_item['code']}</span>
                    </div>
                    <div style="font-size: 1.1rem; font-weight: 700; color: #2F3E34;">
                        {ord_item['amount']:,} VNĐ
                    </div>
                </div>
                <div style="font-size: 0.88rem; color: #555; margin-top: 6px;">
                    <b>Học viên:</b> {ord_item['name']} | <b>Gói:</b> {ord_item['tier']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            if not is_approved:
                if st.button("✅ " + t("Phê Duyệt Kích Hoạt Đơn Này", "Approve & Activate Order"), key=f"btn_app_{ord_item['code']}"):
                    ord_item["status"] = "Đã duyệt"
                    st.toast(f"Đã duyệt kích hoạt tài khoản {ord_item['name']}!")
                    st.rerun()
