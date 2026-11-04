# 🚀 Sổ Tay Hướng Dẫn Đưa Lên GitHub & Triển Khai Streamlit Cloud

Sổ tay này hướng dẫn bạn từng bước đưa dự án **"Mentor thi ICF PCC"** lên **GitHub** và triển khai miễn phí, tự động lên **Streamlit Community Cloud (`share.streamlit.io`)** trong vòng chưa đầy 2 phút.

---

## 📌 BƯỚC 1: Đẩy Mã Nguồn Lên GitHub Cá Nhân / Tổ Chức

Kho mã nguồn cục bộ đã được đóng gói và commit sẵn sàng tại:
`Ôn thi PCC - Vì ước mơ 500 PCC tại Việt Nam _3/icf-pcc-mentor`

### 1.1. Tạo một Repository mới trên GitHub
1. Truy cập [github.com/new](https://github.com/new) và đăng nhập vào tài khoản GitHub của bạn.
2. Đặt tên Repository, ví dụ: `icf-pcc-mentor` hoặc `mentor-thi-icf-pcc`.
3. Chọn chế độ **Public** (hoặc **Private** đều được Streamlit Cloud hỗ trợ miễn phí).
4. **Không** tích chọn *"Add a README file"* (vì dự án đã có sẵn README).
5. Nhấn nút xanh **Create repository**.

### 1.2. Đẩy mã nguồn từ máy lên GitHub
Mở Terminal trên máy tính, chuyển vào thư mục dự án và chạy các lệnh sau:

```bash
cd "/Users/admin/Downloads/Ôn thi PCC - Vì ước mơ 500 PCC tại Việt Nam _3/icf-pcc-mentor"

# 1. Đổi tên nhánh mặc định sang main
git branch -M main

# 2. Gắn địa chỉ repository GitHub của bạn (thay <USERNAME> bằng tên tài khoản của bạn)
git remote add origin https://github.com/<USERNAME>/icf-pcc-mentor.git

# 3. Đẩy toàn bộ mã nguồn lên GitHub
git push -u origin main
```

---

## 📌 BƯỚC 2: Triển Khai Ứng Dụng Lên Streamlit Cloud (`share.streamlit.io`)

Streamlit Community Cloud cung cấp máy chủ đám mây miễn phí, tự động cập nhật mỗi khi bạn push code mới lên GitHub.

1. **Đăng nhập Streamlit Cloud**:
   - Truy cập: [share.streamlit.io](https://share.streamlit.io)
   - Chọn **"Continue with GitHub"** để kết nối tài khoản.

2. **Tạo App mới (Deploy an app)**:
   - Nhấn nút xanh **"Create app"** hoặc **"New app"** ở góc trên bên phải.
   - Chọn **"I already have an app"** (nếu có tùy chọn).

3. **Điền thông số triển khai**:
   - **Repository**: Chọn `your-username/icf-pcc-mentor`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
   - **App URL (tùy chọn)**: Bạn có thể chọn subdomain dễ nhớ, ví dụ: `icf-pcc-mentor.streamlit.app`.

4. **Bấm "Deploy!"**:
   - Streamlit Cloud sẽ tự động đọc tệp `requirements.txt`, cài đặt môi trường Python trong ~30 giây và khởi chạy ứng dụng!
   - Giao diện Zen Làng Mai ấm áp, song ngữ Anh - Việt, 16 câu hỏi tình huống SJT, Thẻ Leitner và VietQR sẽ ngay lập tức hoạt động trên toàn cầu!

---

## 📌 BƯỚC 3: Cài Đặt Ứng Dụng Dạng PWA Về Điện Thoại

Ứng dụng trên Streamlit Cloud tương thích 100% với trình duyệt di động:
- **Trên iPhone (iOS - Safari)**: Nhấn nút **Share (Chia sẻ)** ở chân màn hình Safari -> Chọn **"Thêm vào MH chính" (Add to Home Screen)**.
- **Trên Android (Chrome)**: Nhấn biểu tượng dấu **3 chấm** ở góc trên -> Chọn **"Cài đặt ứng dụng"** hoặc **"Thêm vào Màn hình chính"**.

Biểu tượng hoa sen 🪷 sẽ xuất hiện trên màn hình điện thoại của học viên như một ứng dụng Native đích thực.

---

## 📁 Danh Mục Các Tệp Cốt Lõi Phục Vụ Streamlit

| Tệp tin | Vai trò |
| :--- | :--- |
| `streamlit_app.py` | Điểm khởi chạy chính của ứng dụng Streamlit (Native Zen UI, SJT Runner, VietQR) |
| `requirements.txt` | Khai báo thư viện Python (`streamlit`, `pillow`, `requests`) |
| `.streamlit/config.toml` | Cấu hình bảng màu Zen (giấy dó, rêu phong, đất ấm) và cổng server |
| `data/mentor_data.json` | Toàn bộ dữ liệu 8 năng lực, 16 câu hỏi SJT, flashcards, từ vựng tự chứa |
| `.gitignore` | Bỏ qua các file tạm thời, node_modules, cache để repo gọn nhẹ |
| `DEPLOY_STREAMLIT.md` | Bản hướng dẫn triển khai này |
| `README.md` | Giới thiệu tổng quan dự án |
