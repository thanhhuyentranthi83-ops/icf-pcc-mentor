# Học Coaching — Cùng Coach Thanh Huyền 🪷
*Từ nền tảng khai vấn đến luyện thi ICF Credentialing*

Ứng dụng học tập và luyện thi chứng chỉ quốc tế **ICF Credentialing (ACC / PCC)** song ngữ Anh – Việt, thiết kế Mobile-First dạng Progressive Web App (PWA) theo phong cách thẩm mỹ **Zen chánh niệm**.

---

## 1. Tính Năng Nổi Bật

1. **Lộ trình 8 Năng lực cốt lõi ICF & Đạo đức 2025**:
   - Cây nội dung động nhiều cấp (Phần A, A.1, A1.1, A1.2, A.2, B, C, D).
   - Mỗi mục lá gồm trọn vẹn **6 tab chuyên sâu**:
     1. **Lý thuyết**: Bài giảng phân đoạn rõ ràng, sơ đồ tư duy đính kèm.
     2. **Keyword**: Mẹo ghi nhớ (Mnemonics) & Tổng quát (Glossary) + phát âm tiếng Anh.
     3. **Flashcard**: Thẻ lật 2 mặt kèm hệ thống lặp lại ngắt quãng (Leitner 3 cấp độ: Biết / Chưa chắc / Chưa biết) và đánh dấu yêu thích.
     4. **Case Study**: Hội thoại thực tế giữa Coach và Khách hàng, đối chiếu trực tiếp với PCC Markers.
     5. **Quiz**: Trắc nghiệm bài học, giải thích chi tiết tức thì.
     6. **Thi thử theo phần (Chuẩn ICF)**: Câu hỏi phán đoán tình huống (SJT) chọn 1 BEST và 1 WORST, đồng hồ đếm ngược, phân tích bẫy tư duy.
2. **Thi thử tổng PCC (Full PCC Mock Exam)**:
   - 16 tình huống SJT chuẩn ICF trích xuất trực tiếp từ bộ đề luyện thi chính thức.
   - Tính năng **"Ba hơi thở trước khi thi"**: Vòng tròn Enso co giãn cùng tiếng chuông chánh niệm để an định tâm trí trước khi làm bài.
3. **Thanh toán VietQR động**:
   - Sinh mã QR tự động theo chuẩn VietQR với cú pháp chuyển khoản duy nhất `PCC-XXXX`.
   - Nút sao chép số tài khoản & nội dung một chạm.
   - Tải lên ảnh biên lai đối chiếu. Kế toán bấm "Duyệt" -> Tự kích hoạt gói và tính ngày hết hạn.
4. **Vườn sen của tôi & Gamification dịu dàng**:
   - Tiến độ học hiển thị như một khu vườn sinh thái (Hạt giống -> Chồi non -> Đóa sen nở -> Bướm & chuồn chuồn).
   - Chuông chánh niệm (Sound of Mindfulness) Web Audio API chân thực.
   - Kho 12 Sticker SVG độc quyền và 30 Lời nhắn chánh niệm song ngữ.
5. **Cổng Quản Trị Hệ Thống (Admin Portal)**:
   - Dashboard thống kê học viên, doanh thu, đơn hàng chờ duyệt.
   - Quản lý cây nội dung động: kéo thả, sắp xếp, soạn thảo cả 6 tab.
   - Quản lý đơn hàng & phê duyệt thanh toán.
   - Cấu hình tài khoản ngân hàng thụ hưởng (BANK_NAME, ACCOUNT_NUMBER, ACCOUNT_HOLDER, BANK_BIN) và giá gói học phí.

---

## 2. Hướng Dẫn Triển Khai Streamlit Cloud (`share.streamlit.io`)

Ứng dụng đã được đóng gói hoàn chỉnh bằng Python và cấu hình sẵn sàng cho **Streamlit Cloud**:

### 2.1. Đẩy lên GitHub & Deploy 1-Click
Xem hướng dẫn chi tiết tại [DEPLOY_STREAMLIT.md](file:///Users/admin/Downloads/Ôn%20thi%20PCC%20-%20Vì%20ước%20mơ%20500%20PCC%20tại%20Việt%20Nam%20_3/icf-pcc-mentor/DEPLOY_STREAMLIT.md).
1. Đẩy thư mục này lên một repository GitHub mới:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<USERNAME>/icf-pcc-mentor.git
   git push -u origin main
   ```
2. Đăng nhập [share.streamlit.io](https://share.streamlit.io) -> Bấm **New App** -> Chọn Repo, Branch `main`, Main file `streamlit_app.py` -> Bấm **Deploy**!

### 2.2. Chạy Thử Streamlit Cục Bộ (Local Python)
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
Ứng dụng Streamlit sẽ mở tại: **http://localhost:8501**

---

## 3. Hướng Dẫn Chạy Next.js Web PWA (Local)

Codebase nằm tại thư mục:  
`/Users/admin/Downloads/Ôn thi PCC - Vì ước mơ 500 PCC tại Việt Nam _3/icf-pcc-mentor`

### Bước 1: Mở Terminal tại thư mục dự án
```bash
cd "icf-pcc-mentor"
```

### Bước 2: Chạy ứng dụng Next.js local
```bash
npm run dev
```
Mở trình duyệt tại: **http://localhost:3000**

---

## 4. Tài Khoản Demo Sẵn Có

Ứng dụng tích hợp thanh chuyển vai trò nhanh (Quick Role Switcher) ở góc trên bên phải header:

- **Super Admin (Tâm An)**: `admin@pcc.vn` — Toàn quyền hệ thống, cấu hình VietQR, xem doanh thu.
- **Biên tập viên (Tuệ Minh)**: `editor@pcc.vn` — Quản lý cây nội dung, soạn bài 6 tab, xuất/nhập JSON.
- **Kế toán (Diệu Thiện)**: `billing@pcc.vn` — Xem biên lai, duyệt / từ chối đơn hàng VietQR.
- **Học viên Gói 1 Tháng**: `student.1m@pcc.vn` — Đang kích hoạt gói Tinh Tấn.
- **Học viên Gói 6 Tháng**: `student.6m@pcc.vn` — Đang kích hoạt gói Đồng Hành.
- **Học viên Gói Miễn Phí**: `student.free@pcc.vn` — Trải nghiệm giới hạn các bài miễn phí.

---

## 4. Triển Khai Lên Vercel & Supabase Production

### 1. Cơ sở dữ liệu Supabase:
- Tạo một dự án mới tại [supabase.com](https://supabase.com).
- Vào **SQL Editor**, chạy toàn bộ nội dung file:
  `supabase/migrations/01_initial_schema.sql`
- Lấy `NEXT_PUBLIC_SUPABASE_URL` và `NEXT_PUBLIC_SUPABASE_ANON_KEY` điền vào file `.env`.

### 2. Triển khai lên Vercel:
- Đẩy source code lên GitHub.
- Import repository vào [Vercel](https://vercel.com).
- Cấu hình Environment Variables:
  - `NEXT_PUBLIC_SUPABASE_URL`
  - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- Bấm **Deploy**. Vercel sẽ tự động build và cung cấp domain HTTPS miễn phí.

---

## 5. Lưu Ý Pháp Lý & Bản Quyền
- Giao diện lấy cảm hứng từ tinh thần Zen, không liên kết chính thức với Làng Mai.
- Ứng dụng ôn thi độc lập, không phải sản phẩm chính thức của ICF (International Coaching Federation).
