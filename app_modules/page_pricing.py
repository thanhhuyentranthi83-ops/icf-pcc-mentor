# -*- coding: utf-8 -*-
"""
Pricing & VietQR Activation Page for PCC Learning & Practice
"""
import streamlit as st
import random

def render_pricing_page(t):
    st.markdown(f"""
    <div style="margin-bottom: 20px; text-align: center;">
        <span class="zen-badge zen-badge-gold">💳 {t('Đồng Hành Trọn Vẹn', 'Mindful Investment')}</span>
        <h2 style="margin: 8px 0; color: #2F3E34;">{t('Đăng Ký Gói Học Viên PCC Learning & Practice', 'Membership Plans & Activation')}</h2>
        <p style="font-size: 0.95rem; color: #5F6F65; line-height: 1.6; max-width: 700px; margin: 0 auto;">
            {t('Đầu tư xứng đáng cho sự nghiệp khai vấn chuyên nghiệp. Truy cập không giới hạn toàn bộ kho tình huống chuẩn hóa, phòng thi thử mô phỏng và lộ trình bồi đắp năng lực.',
               'A worthy investment in your professional coaching journey. Unlimited access to standardized SJT scenarios, realistic mock exams, and competency development paths.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    tiers = [
        {"name": "1 Tháng (Cấp Tốc)", "nameEn": "1 Month (Intensive)", "price": 299000, "orig": 499000, "desc": "Phù hợp ôn tập nước rút 30 ngày trước kỳ thi.", "descEn": "Ideal for a focused 30-day sprint before the exam.", "badge": "zen-badge-primary"},
        {"name": "3 Tháng (Toàn Diện)", "nameEn": "3 Months (Standard)", "price": 699000, "orig": 1099000, "desc": "Lựa chọn phổ biến nhất để củng cố vững chắc 8 Năng lực.", "descEn": "Most popular choice to deeply internalize all 8 competencies.", "badge": "zen-badge-gold"},
        {"name": "6 Tháng (Đồng Hành)", "nameEn": "6 Months (Complete)", "price": 1190000, "orig": 1890000, "desc": "Trọn vẹn cho lộ trình thi cả 2 cấu hình (Hiện hành & Cập nhật).", "descEn": "Comprehensive coverage for both Current and Updated exam profiles.", "badge": "zen-badge-pink"}
    ]

    selected_tier = st.session_state.get("selected_pricing_tier", tiers[1]["name"])

    for idx, (c, tr) in enumerate(zip([col1, col2, col3], tiers)):
        with c:
            is_sel = (selected_tier == tr["name"])
            st.markdown(f"""
            <div class="zen-card" style="border: 2px solid {'#8BA888' if is_sel else '#EADBCC'}; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span class="zen-badge {tr['badge']}">{tr['name'] if st.session_state.lang == 'vi' else tr['nameEn']}</span>
                    <h2 style="color: #2F3E34; margin: 12px 0 4px 0;">{tr['price']:,} <span style="font-size: 0.9rem; color: #8C6D53;">VNĐ</span></h2>
                    <div style="font-size: 0.85rem; color: #888; text-decoration: line-through; margin-bottom: 8px;">{tr['orig']:,} VNĐ</div>
                    <p style="font-size: 0.88rem; color: #555; line-height: 1.5;">{tr['desc'] if st.session_state.lang == 'vi' else tr['descEn']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("👉 " + t("Chọn Gói Này", "Select Plan"), key=f"btn_pick_tier_{idx}", use_container_width=True):
                st.session_state["selected_pricing_tier"] = tr["name"]
                st.session_state["selected_pricing_amount"] = tr["price"]
                st.rerun()

    chosen_name = st.session_state.get("selected_pricing_tier", tiers[1]["name"])
    chosen_amount = st.session_state.get("selected_pricing_amount", tiers[1]["price"])

    st.markdown("<hr style='border: none; border-top: 1px solid #EADBCC; margin: 24px 0;'/>", unsafe_allow_html=True)

    # VietQR Payment Section
    st.markdown(f"### 📲 {t('Thanh Toán Kích Hoạt Nhanh Qua VietQR', 'Instant VietQR Transfer & Activation')}")
    q_col1, q_col2 = st.columns([1, 1])

    order_code = f"PCC-{random.randint(1000, 9999)}-{chr(random.randint(65, 90))}{random.randint(10, 99)}"
    if "current_order_code" not in st.session_state:
        st.session_state.current_order_code = order_code
    else:
        order_code = st.session_state.current_order_code

    with q_col1:
        # Dynamic VietQR image
        bank_id = "MB"
        account_no = "0988888888"
        account_name = "TRAN THI THANH HUYEN"
        transfer_desc = f"{order_code} ON THI PCC"
        qr_url = f"https://img.vietqr.io/image/{bank_id}-{account_no}-compact2.png?amount={chosen_amount}&addInfo={transfer_desc}&accountName={account_name}"

        st.markdown(f"""
        <div style="text-align: center; background: #FFFFFF; padding: 16px; border-radius: 16px; border: 1px solid #EADBCC;">
            <img src="{qr_url}" alt="VietQR" style="max-width: 280px; border-radius: 12px; margin-bottom: 10px;"/>
            <div style="font-size: 0.85rem; color: #555;">
                Quét mã QR bằng ứng dụng ngân hàng bất kỳ để chuyển khoản tức thì.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with q_col2:
        st.markdown(f"""
        <div class="zen-card">
            <h4 style="margin-top: 0; color: #2F3E34;">📋 {t('Thông Tin Chuyển Khoản Thủ Công:', 'Manual Bank Transfer Details:')}</h4>
            <div style="font-size: 0.9rem; line-height: 1.8; color: #333;">
                <b>Ngân hàng:</b> MB Bank (Ngân hàng Quân Đội)<br/>
                <b>Số tài khoản:</b> <code style="font-size: 1rem; color: #1E4E79;">0988888888</code><br/>
                <b>Chủ tài khoản:</b> TRAN THI THANH HUYEN<br/>
                <b>Số tiền:</b> <b style="color: #9C4158; font-size: 1.1rem;">{chosen_amount:,} VNĐ</b><br/>
                <b>Nội dung chuyển khoản:</b> <code style="font-size: 1rem; color: #C62828;">{transfer_desc}</code><br/>
                <b>Gói đã chọn:</b> {chosen_name}
            </div>
        </div>
        """, unsafe_allow_html=True)

        user_name = st.text_input(t("Họ và tên của bạn:", "Your Full Name:"), key="reg_name")
        user_phone = st.text_input(t("Số điện thoại / Zalo:", "Phone / Zalo:"), key="reg_phone")

        if st.button("✅ " + t("Tôi Đã Chuyển Khoản — Xác Nhận Kích Hoạt", "I Have Transferred — Confirm Activation"), type="primary", use_container_width=True):
            if user_name.strip() and user_phone.strip():
                new_order = {
                    "code": order_code,
                    "name": user_name.strip(),
                    "tier": chosen_name,
                    "amount": chosen_amount,
                    "status": "Chờ duyệt"
                }
                st.session_state.orders.insert(0, new_order)
                st.session_state.current_order_code = f"PCC-{random.randint(1000, 9999)}-{chr(random.randint(65, 90))}{random.randint(10, 99)}"
                st.success(t(f"Cảm ơn bạn {user_name}! Hệ thống đã tiếp nhận thông tin đơn hàng [{order_code}]. Bạn có thể xem trạng thái ở mục Quản Trị.",
                             f"Thank you {user_name}! Order [{order_code}] recorded. Check status in Admin portal."))
            else:
                st.warning(t("Vui lòng điền họ tên và số điện thoại liên hệ.", "Please enter your name and phone number."))
