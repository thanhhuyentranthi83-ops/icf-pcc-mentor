"""
Ứng dụng: Mentor thi ICF PCC (ICF PCC Exam Prep Mentor)
Triết lý thiết kế: Thiền Làng Mai (Plum Village Zen) — Tĩnh tại, mộc mạc, không hối thúc.
Triển khai: Streamlit Community Cloud (share.streamlit.io) & GitHub Ready.
"""

import os
import json
import random
import streamlit as st

# ==========================================
# 1. CẤU HÌNH TRANG STREAMLIT & GIAO DIỆN ZEN
# ==========================================
st.set_page_config(
    page_title="Mentor thi ICF PCC 🪷",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Zen CSS (Làng Mai Theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,400&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        color: #2C3E50;
    }

    .stApp {
        background-color: #F7F3EA;
    }

    /* Tiêu đề & Font chữ */
    h1, h2, h3, .zen-serif {
        font-family: 'Playfair Display', Georgia, serif !important;
        color: #2F3E34 !important;
        font-weight: 600;
    }

    /* Thẻ bo tròn kiểu Zen (Zen Cards) */
    .zen-card {
        background: #FFFFFF;
        border: 1px solid #EADBCC;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(63, 79, 68, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .zen-card:hover {
        box-shadow: 0 6px 20px rgba(63, 79, 68, 0.08);
    }

    .zen-quote-box {
        background: #FAF7F2;
        border-left: 4px solid #8BA888;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 16px 0;
        font-style: italic;
    }

    .zen-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-right: 8px;
    }
    .zen-badge-primary { background-color: #E2ECE1; color: #3F4F44; }
    .zen-badge-pink { background-color: #FCE8ED; color: #9C4158; }
    .zen-badge-gold { background-color: #FEF3D6; color: #8A6112; }

    /* Nút bấm Zen */
    .stButton > button {
        background-color: #3F4F44;
        color: #FFFFFF !important;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #2F3E34;
        color: #F7F3EA !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(63, 79, 68, 0.2);
    }

    /* Flashcard Leitner */
    .flashcard-box {
        background: #FFFFFF;
        border: 2px solid #D8C7B5;
        border-radius: 18px;
        padding: 36px 24px;
        text-align: center;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 6px 20px rgba(140, 109, 83, 0.08);
        cursor: pointer;
    }

    /* Vườn Sen */
    .lotus-garden-banner {
        background: linear-gradient(135deg, #FAF7F2 0%, #F2EBE1 100%);
        border: 1px solid #D8C7B5;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 24px;
    }

    /* Top Nav Buttons */
    .top-nav-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        background: #FAF7F2;
        padding: 10px;
        border-radius: 16px;
        border: 1px solid #EADBCC;
        margin-bottom: 20px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. TẢI DỮ LIỆU ĐỘC LẬP (SELF-CONTAINED DATA)
# ==========================================
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "mentor_data.json")

@st.cache_data
def load_mentor_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

DATA = load_mentor_data()
SECTIONS = DATA.get("sections", [])
COMPETENCIES = DATA.get("competencies", [])
THEORIES = {th["sectionId"]: th for th in DATA.get("theories", [])}
KEYWORDS = DATA.get("keywords", [])
FLASHCARDS = DATA.get("flashcards", [])
CASE_STUDIES = {cs["sectionId"]: cs for cs in DATA.get("caseStudies", [])}
QUIZZES = DATA.get("quizzes", [])
PRACTICE_QUESTIONS = DATA.get("practiceQuestions", [])
MINDFULNESS_MESSAGES = DATA.get("mindfulnessMessages", [])
STICKERS = DATA.get("stickers", [])
SYSTEM_SETTINGS = DATA.get("systemSettings", {})
DISCOUNT_CODES = DATA.get("discountCodes", [])

# Chỉ lọc các bài học có nội dung đầy đủ (9 bài học chính có bài giảng, flashcard, quiz)
STUDY_SECTIONS = [s for s in SECTIONS if s["id"] in THEORIES]
if not STUDY_SECTIONS:
    STUDY_SECTIONS = [s for s in SECTIONS if s.get("parentId")]

# ==========================================
# 3. QUẢN LÝ TRẠNG THÁI (SESSION STATE)
# ==========================================
if "lang" not in st.session_state:
    st.session_state.lang = "vi"

if "page" not in st.session_state:
    st.session_state.page = "home"  # "home", "curriculum", "sjt", "pricing", "admin"

if "lotus_bloomed" not in st.session_state:
    st.session_state.lotus_bloomed = 5

if "current_section" not in st.session_state or st.session_state.current_section not in THEORIES:
    st.session_state.current_section = "sec-a1-1"

if "fc_index" not in st.session_state:
    st.session_state.fc_index = 0

if "fc_flipped" not in st.session_state:
    st.session_state.fc_flipped = False

if "notes" not in st.session_state:
    st.session_state.notes = {}

if "sjt_answers" not in st.session_state:
    st.session_state.sjt_answers = {}

if "sjt_submitted" not in st.session_state:
    st.session_state.sjt_submitted = False

if "orders" not in st.session_state:
    st.session_state.orders = [
        {"code": "PCC-1001-A89", "name": "Thu Hương", "tier": "1 Tháng", "amount": 299000, "status": "Đã duyệt"},
        {"code": "PCC-1002-B72", "name": "Bảo Nam", "tier": "6 Tháng", "amount": 1190000, "status": "Đã duyệt"},
        {"code": "PCC-1003-C34", "name": "Minh Đức", "tier": "6 Tháng", "amount": 1190000, "status": "Chờ duyệt"}
    ]

# Helper đa ngôn ngữ
def t(vi_text, en_text):
    return vi_text if st.session_state.lang == "vi" else en_text

# Helper chuyển trang
def set_page(page_name, section_id=None):
    st.session_state.page = page_name
    if section_id:
        st.session_state.current_section = section_id

# Helper phát chuông thiền Web Audio
def render_bell_button():
    bell_html = """
    <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
        <button onclick="playZenBell()" style="
            background: #FAF7F2;
            border: 1px solid #8BA888;
            color: #3F4F44;
            padding: 8px 18px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        ">
            🔔 <span>""" + t("Thỉnh một tiếng chuông thiền", "Ring a Mindful Bell") + """</span>
        </button>
    </div>
    <script>
    function playZenBell() {
        try {
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const now = ctx.currentTime;
            const freqs = [180, 360, 540, 720];
            const gains = [0.4, 0.25, 0.15, 0.08];

            freqs.forEach((freq, i) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, now);
                gain.gain.setValueAtTime(gains[i], now);
                gain.gain.exponentialRampToValueAtTime(0.0001, now + 4.5);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 4.5);
            });
        } catch (e) {
            console.log(e);
        }
    }
    </script>
    """
    st.components.v1.html(bell_html, height=55)

# ==========================================
# 4. THANH ĐIỀU HƯỚNG TRÊN CÙNG (TOP NAVIGATION)
# (Đảm bảo người dùng điện thoại / máy tính luôn nhìn thấy và chuyển trang tức thì)
# ==========================================
top_col1, top_col2, top_col3, top_col4, top_col5 = st.columns(5)
with top_col1:
    if st.button("🏠 " + t("Trang Chủ", "Home"), use_container_width=True, type="primary" if st.session_state.page == "home" else "secondary"):
        st.session_state.page = "home"
        st.rerun()
with top_col2:
    if st.button("📚 " + t("Lộ Trình Học", "Curriculum"), use_container_width=True, type="primary" if st.session_state.page == "curriculum" else "secondary"):
        st.session_state.page = "curriculum"
        st.rerun()
with top_col3:
    if st.button("⚖️ " + t("Thi Thử SJT", "SJT Exam"), use_container_width=True, type="primary" if st.session_state.page == "sjt" else "secondary"):
        st.session_state.page = "sjt"
        st.rerun()
with top_col4:
    if st.button("💳 " + t("Gói Hội Viên", "Pricing"), use_container_width=True, type="primary" if st.session_state.page == "pricing" else "secondary"):
        st.session_state.page = "pricing"
        st.rerun()
with top_col5:
    if st.button("🛡️ " + t("Quản Trị", "Admin"), use_container_width=True, type="primary" if st.session_state.page == "admin" else "secondary"):
        st.session_state.page = "admin"
        st.rerun()

st.markdown("<hr style='margin: 8px 0 20px 0; border: none; border-top: 1px solid #EADBCC;'/>", unsafe_allow_html=True)

# ==========================================
# 5. THANH BÊN (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 2px;'>🪷 Mentor thi ICF PCC</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #8C6D53; font-size: 0.9rem; margin-top: 0;'>{t('Vì ước mơ đưa Coaching thành lối sống', 'Making Coaching a Way of Life')}</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Ngôn ngữ
    col_lang1, col_lang2 = st.columns(2)
    with col_lang1:
        if st.button("🇻🇳 Tiếng Việt", use_container_width=True, type="primary" if st.session_state.lang == "vi" else "secondary"):
            st.session_state.lang = "vi"
            st.rerun()
    with col_lang2:
        if st.button("🇬🇧 English", use_container_width=True, type="primary" if st.session_state.lang == "en" else "secondary"):
            st.session_state.lang = "en"
            st.rerun()

    st.markdown("---")
    render_bell_button()

    # Trích dẫn chánh niệm
    if MINDFULNESS_MESSAGES:
        quote = MINDFULNESS_MESSAGES[hash(str(os.getpid())) % len(MINDFULNESS_MESSAGES)]
        st.markdown(f"""
        <div class="zen-quote-box">
            <div style="font-size: 0.85rem; color: #3F4F44; font-weight: 600; margin-bottom: 4px;">🌿 {t('Lời nhắn chánh niệm', 'Mindfulness Whisper')}</div>
            <div style="font-size: 0.88rem; color: #555;">"{quote['textVi'] if st.session_state.lang == 'vi' else quote['textEn']}"</div>
            <div style="font-size: 0.78rem; color: #8C6D53; margin-top: 4px; text-align: right;">— {quote['author']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Thống kê Vườn sen
    st.markdown(f"""
    <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 12px; padding: 12px; text-align: center; font-size: 0.85rem;">
        <div>🪷 <b>{t('Vườn sen hiện tại', 'Your Lotus Garden')}</b></div>
        <div style="font-size: 1.4rem; color: #9C4158; margin: 4px 0;">{'🪷 ' * min(st.session_state.lotus_bloomed, 7)}</div>
        <div style="color: #666;">{st.session_state.lotus_bloomed} {t('đóa sen đã nở', 'lotuses in full bloom')}</div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# 6. TRANG CHỦ & VƯỜN SEN (HOME PAGE)
# ==========================================
if st.session_state.page == "home":
    st.markdown(f"""
    <div style="text-align: center; max-width: 800px; margin: 0 auto 20px auto;">
        <span class="zen-badge zen-badge-primary">🌱 {t('Học Tỉnh Thức — Đạt Chuẩn PCC', 'Mindful Mastery — PCC Standard')}</span>
        <h1 style="font-size: 2.4rem; margin: 12px 0;">{t('Mentor Ôn Thi ICF PCC', 'ICF PCC Credentialing Mentor')}</h1>
        <p style="font-size: 1.05rem; color: #5F6F65; line-height: 1.6;">
            {t('Không gian học tập tĩnh lặng và sâu sắc, đồng hành cùng bạn bồi đắp 8 Năng lực cốt lõi và chinh phục bài thi phán đoán tình huống (SJT) với phong thái an nhiên, tự tại.',
               'A tranquil and profound learning sanctuary, empowering you to master the 8 Core Competencies and excel in the Situational Judgment Test (SJT) with grounded confidence.')}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 2 NÚT HÀNH ĐỘNG NỔI BẬT NHẤT (CALL TO ACTION)
    col_cta1, col_cta2 = st.columns(2)
    with col_cta1:
        if st.button("🚀 " + t("BẮT ĐẦU HỌC NGAY (8 NĂNG LỰC)", "START LEARNING (8 COMPETENCIES)"), use_container_width=True, type="primary"):
            st.session_state.page = "curriculum"
            st.session_state.current_section = "sec-a1-1"
            st.rerun()
    with col_cta2:
        if st.button("⚖️ " + t("VÀO THI THỬ SJT (16 TÌNH HUỐNG THỰC TẾ)", "ATTEMPT SJT EXAM (16 REAL SCENARIOS)"), use_container_width=True):
            st.session_state.page = "sjt"
            st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # Vườn Sen Chánh Niệm Banner
    st.markdown(f"""
    <div class="lotus-garden-banner">
        <h3 style="margin-bottom: 6px;">🪷 {t('Vườn Sen Tỉnh Thức (Lotus Garden)', 'Mindful Lotus Garden')}</h3>
        <p style="color: #6B7C72; font-size: 0.95rem; margin-bottom: 12px;">
            {t('Mỗi bài học bạn hoàn thành, mỗi câu hỏi SJT bạn chiêm nghiệm là một giọt nước mát lành nuôi dưỡng đóa sen tỉnh thức.',
               'Every lesson completed and every SJT scenario reflected upon is a gentle drop of water nurturing your lotus.')}
        </p>
        <div style="font-size: 2.2rem; letter-spacing: 12px; margin: 10px 0;">
            {'🪷 ' * min(st.session_state.lotus_bloomed, 10)} 🦋 🐉
        </div>
        <span class="zen-badge zen-badge-gold">✨ {st.session_state.lotus_bloomed} {t('Đóa sen nở rộ', 'Bloomed Lotuses')}</span>
        <span class="zen-badge zen-badge-primary">🍃 7 {t('Ngày tinh tấn liên tục', 'Day Diligence Streak')}</span>
    </div>
    """, unsafe_allow_html=True)

    # Bài tập 3 hơi thở
    with st.expander(f"🧘 {t('Thực hành 3 Hơi Thở Chánh Niệm Trước Khi Học', 'Practice 3 Mindful Breaths Before Studying')}", expanded=False):
        st.markdown(f"""
        <div style="text-align: center; padding: 15px;">
            <p style="font-size: 1.1rem; color: #3F4F44; font-style: italic;">
                "{t('Thở vào, tâm tĩnh lặng — Thở ra, miệng mỉm cười — An trú trong hiện tại — Giờ phút đẹp tuyệt vời.',
                   'Breathing in, I calm my body and mind — Breathing out, I smile — Dwelling in the present moment — I know this is the only moment.')}"
            </p>
            <div style="display: flex; justify-content: center; gap: 20px; margin-top: 15px;">
                <div style="background: #EAE3D2; padding: 12px 20px; border-radius: 12px;">1️⃣ {t('Hít vào sâu (4 giây)', 'Inhale Deeply (4s)')}</div>
                <div style="background: #EAE3D2; padding: 12px 20px; border-radius: 12px;">2️⃣ {t('Giữ tâm an (4 giây)', 'Hold Still (4s)')}</div>
                <div style="background: #EAE3D2; padding: 12px 20px; border-radius: 12px;">3️⃣ {t('Thở ra nhẹ (6 giây)', 'Exhale Gently (6s)')}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(t("Đã hoàn thành 3 hơi thở — Tưới hoa sen 🪷", "Completed 3 Breaths — Water Lotus 🪷"), key="btn_breathe"):
            st.session_state.lotus_bloomed += 1
            st.toast(t("Tâm đã an định! Bạn vừa tưới thêm 1 đóa sen nở rộ.", "Mind calmed! 1 lotus added to your garden."))
            st.rerun()

    # 5 Nhánh Lớn Của Khung Năng Lực kèm nút học trực tiếp
    st.markdown(f"<h3 style='margin-top: 30px;'>🌿 {t('5 Nhánh Trọng Tâm Của Chương Trình Ôn Luyện', '5 Core Pillars of the PCC Curriculum')}</h3>", unsafe_allow_html=True)
    
    pillars = [
        {"code": "A", "targetSec": "sec-a1-1", "titleVi": "Phần A: Nền Tảng (Foundation)", "titleEn": "Part A: Foundation", "descVi": "Năng lực 1 (Đạo đức 2025) & Năng lực 2 (Tư duy Khai vấn). Giữ gìn chính trực và tôn trọng bản sắc.", "descEn": "Competency 1 (Ethics 2025) & Competency 2 (Coaching Mindset). Integrity and identity sensitivity.", "icon": "🌱", "btnVi": "Học Năng Lực 1 & 2", "btnEn": "Study Competencies 1 & 2"},
        {"code": "B", "targetSec": "sec-b1", "titleVi": "Phần B: Cùng Tạo Dựng Mối Quan Hệ", "titleEn": "Part B: Co-creating Relationship", "descVi": "Năng lực 3 (Thiết lập Thỏa thuận) & Năng lực 4 (Nuôi dưỡng Niềm tin & An toàn tâm lý).", "descEn": "Competency 3 (Agreements) & Competency 4 (Trust & Psychological Safety).", "icon": "🌿", "btnVi": "Học Năng Lực 3 & 4", "btnEn": "Study Competencies 3 & 4"},
        {"code": "C", "targetSec": "sec-c1", "titleVi": "Phần C: Giao Tiếp Hiệu Quả", "titleEn": "Part C: Communicating Effectively", "descVi": "Năng lực 5 (Hiện diện Tĩnh lặng) & Năng lực 6 (Lắng nghe Chủ động Cấp độ 3).", "descEn": "Competency 5 (Presence) & Competency 6 (Level 3 Active Listening).", "icon": "🎋", "btnVi": "Học Năng Lực 5 & 6", "btnEn": "Study Competencies 5 & 6"},
        {"code": "D", "targetSec": "sec-d1", "titleVi": "Phần D: Nuôi Dưỡng Học Tập & Phát Triển", "titleEn": "Part D: Cultivating Growth", "descVi": "Năng lực 7 (Khơi mở Nhận thức Who/What) & Năng lực 8 (Thúc đẩy Sự Phát triển Tự chủ).", "descEn": "Competency 7 (Evoking Awareness) & Competency 8 (Facilitating Growth & Autonomy).", "icon": "🪷", "btnVi": "Học Năng Lực 7 & 8", "btnEn": "Study Competencies 7 & 8"},
        {"code": "SJT", "targetPage": "sjt", "titleVi": "Chiến Lược Phòng Thi SJT Thực Tế", "titleEn": "SJT Exam Strategy & Simulation", "descVi": "16 Tình huống phán đoán thực tế chọn đồng thời 1 BEST và 1 WORST kèm phân tích bẫy thi.", "descEn": "16 Authentic Situational Judgment scenarios with dual BEST/WORST scoring and trap analysis.", "icon": "⚖️", "btnVi": "Vào Phòng Thi Thử SJT", "btnEn": "Enter SJT Exam"}
    ]

    for p in pillars:
        col_p_text, col_p_btn = st.columns([3, 1])
        with col_p_text:
            st.markdown(f"""
            <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 12px; padding: 16px; margin-bottom: 12px;">
                <div style="font-size: 1.4rem; float: left; margin-right: 12px;">{p['icon']}</div>
                <div>
                    <b>{p['titleVi'] if st.session_state.lang == 'vi' else p['titleEn']}</b>
                    <p style="color: #666; font-size: 0.9rem; margin: 4px 0 0 0;">{p['descVi'] if st.session_state.lang == 'vi' else p['descEn']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_p_btn:
            st.write("")
            if p.get("targetPage"):
                if st.button("👉 " + (p['btnVi'] if st.session_state.lang == 'vi' else p['btnEn']), key=f"btn_p_{p['code']}", use_container_width=True):
                    st.session_state.page = "sjt"
                    st.rerun()
            else:
                if st.button("👉 " + (p['btnVi'] if st.session_state.lang == 'vi' else p['btnEn']), key=f"btn_p_{p['code']}", use_container_width=True):
                    st.session_state.page = "curriculum"
                    st.session_state.current_section = p["targetSec"]
                    st.rerun()


# ==========================================
# 7. LỘ TRÌNH 8 NĂNG LỰC & 6 TAB (CURRICULUM)
# ==========================================
elif st.session_state.page == "curriculum":
    st.markdown(f"<h2>📚 {t('Lộ Trình Học Tập Chuyên Sâu 8 Năng Lực', '8 Core Competencies In-Depth Curriculum')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #666;'>{t('Mỗi bài học được thiết kế trọn vẹn gồm 6 thành phần: Lý thuyết, Từ khóa, Thẻ Leitner, Case Study, Quiz và Ghi chú phản tư.', 'Each lesson features 6 interactive components: Theory, Keywords, Leitner Cards, Case Study, Quiz, and Personal Reflection Notes.')}</p>", unsafe_allow_html=True)

    # Tạo danh sách bài học có nội dung chuẩn xác
    sec_dict = {
        s["id"]: f"[{s.get('code', '')}] {s['titleVi'] if st.session_state.lang == 'vi' else s['titleEn']}" 
        for s in STUDY_SECTIONS
    }
    
    # Đảm bảo bài học hiện tại hợp lệ
    if st.session_state.current_section not in sec_dict:
        st.session_state.current_section = list(sec_dict.keys())[0]

    current_sec_id = st.selectbox(
        t("📖 Chọn bài học để bắt đầu học:", "📖 Select lesson to study:"),
        options=list(sec_dict.keys()),
        format_func=lambda x: sec_dict[x],
        index=list(sec_dict.keys()).index(st.session_state.current_section)
    )
    st.session_state.current_section = current_sec_id

    # 6 Tab Chi Tiết
    tab_titles = [
        t("📖 1. Lý Thuyết Chắt Lọc", "📖 1. Distilled Theory"),
        t("🔑 2. Thuật Ngữ Song Ngữ", "🔑 2. Bilingual Terms"),
        t("🎴 3. Flashcards Leitner", "🎴 3. Leitner Flashcards"),
        t("🎙️ 4. Case Study Khai Vấn", "🎙️ 4. Coaching Dialogue"),
        t("❓ 5. Mini Quiz Tức Thì", "❓ 5. Diagnostic Quiz"),
        t("📝 6. Ghi Chú Cá Nhân", "📝 6. Personal Notes")
    ]
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tab_titles)

    # TAB 1: LÝ THUYẾT
    with tab1:
        th = THEORIES.get(current_sec_id)
        if th:
            st.markdown(f"### {th['titleVi'] if st.session_state.lang == 'vi' else th['titleEn']}")
            st.markdown(th['contentVi'] if st.session_state.lang == 'vi' else th['contentEn'])
        else:
            st.info(t("Nội dung bài giảng đang được đồng bộ.", "Lecture content is syncing."))

    # TAB 2: TỪ KHÓA
    with tab2:
        sec_keywords = [k for k in KEYWORDS if k.get("sectionId") == current_sec_id]
        if not sec_keywords:
            sec_keywords = KEYWORDS[:2]

        for kw in sec_keywords:
            st.markdown(f"""
            <div class="zen-card">
                <span class="zen-badge zen-badge-primary">{kw.get('category', 'term').upper()}</span>
                <h4 style="margin: 8px 0 4px 0; color: #2F3E34;">{kw['termVi']} <span style="color: #8C6D53; font-weight: normal; font-size: 0.95rem;">({kw['termEn']})</span></h4>
                <p style="color: #444; font-size: 0.95rem; margin-bottom: 8px;"><b>{t('Định nghĩa:', 'Definition:')}</b> {kw['definitionVi'] if st.session_state.lang == 'vi' else kw['definitionEn']}</p>
                <div style="background: #FAF7F2; padding: 8px 12px; border-radius: 8px; font-size: 0.88rem; color: #3F4F44;">
                    💡 <b>{t('Mẹo ghi nhớ:', 'Memory Cue:')}</b> {kw['memoryCueVi'] if st.session_state.lang == 'vi' else kw['memoryCueEn']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # TAB 3: FLASHCARDS
    with tab3:
        sec_fcs = [f for f in FLASHCARDS if f.get("sectionId") == current_sec_id]
        if not sec_fcs:
            sec_fcs = FLASHCARDS[:2]

        fc_idx = st.session_state.fc_index % len(sec_fcs)
        fc = sec_fcs[fc_idx]

        st.markdown(f"<div style='text-align: right; color: #8C6D53; font-size: 0.9rem;'>{t('Thẻ', 'Card')} {fc_idx + 1} / {len(sec_fcs)}</div>", unsafe_allow_html=True)
        
        # Thẻ hiển thị
        if not st.session_state.fc_flipped:
            st.markdown(f"""
            <div class="flashcard-box">
                <div style="font-size: 0.85rem; color: #8BA888; font-weight: 600; margin-bottom: 12px;">QUESTION / MẶT TRƯỚC</div>
                <h3 style="color: #2F3E34; font-size: 1.25rem;">{fc['frontVi'] if st.session_state.lang == 'vi' else fc['frontEn']}</h3>
                <div style="margin-top: 16px; color: #888; font-size: 0.88rem;">💡 {t('Gợi ý:', 'Hint:')} {fc.get('hintVi', '') if st.session_state.lang == 'vi' else fc.get('hintEn', '')}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="flashcard-box" style="background: #F4EFE6; border-color: #8BA888;">
                <div style="font-size: 0.85rem; color: #3F4F44; font-weight: 600; margin-bottom: 12px;">ANSWER / MẶT SAU</div>
                <h4 style="color: #2F3E34; font-size: 1.15rem; line-height: 1.6;">{fc['backVi'] if st.session_state.lang == 'vi' else fc['backEn']}</h4>
            </div>
            """, unsafe_allow_html=True)

        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
        with col_btn1:
            if st.button(t("🔄 Lật Thẻ", "🔄 Flip Card"), use_container_width=True):
                st.session_state.fc_flipped = not st.session_state.fc_flipped
                st.rerun()
        with col_btn2:
            if st.button(t("➡️ Thẻ Kế Tiếp", "➡️ Next Card"), use_container_width=True):
                st.session_state.fc_index += 1
                st.session_state.fc_flipped = False
                st.rerun()
        with col_btn3:
            if st.button(t("🌟 Đã Thành Thạo (+1 Sen)", "🌟 Mastered (+1 Lotus)"), use_container_width=True):
                st.session_state.lotus_bloomed += 1
                st.session_state.fc_index += 1
                st.session_state.fc_flipped = False
                st.toast(t("Đã ghi nhớ! Vườn sen vừa nở thêm 1 hoa.", "Mastered! Lotus bloomed in your garden."))
                st.rerun()

    # TAB 4: CASE STUDY
    with tab4:
        cs = CASE_STUDIES.get(current_sec_id)
        if cs:
            st.markdown(f"### {cs['titleVi'] if st.session_state.lang == 'vi' else cs['titleEn']}")
            st.markdown(f"**{t('Bối cảnh:', 'Scenario:')}** {cs['scenarioVi'] if st.session_state.lang == 'vi' else cs['scenarioEn']}")
            
            st.markdown(f"#### 🎙️ {t('Trích đoạn hội thoại phiên khai vấn:', 'Session Transcript:')}")
            for d in cs.get("dialogue", []):
                speaker_badge = "zen-badge-primary" if d["speaker"] == "Coach" else "zen-badge-pink"
                marker_html = f"<span class='zen-badge zen-badge-gold' style='margin-left: 8px;'>🎯 {d['markerTag']}</span>" if d.get("markerTag") else ""
                text = d['textVi'] if st.session_state.lang == 'vi' else d['textEn']
                st.markdown(f"""
                <div style="margin-bottom: 12px; padding: 10px 14px; background: {'#FFFFFF' if d['speaker'] == 'Coach' else '#FAF7F2'}; border-radius: 10px; border-left: 3px solid {'#3F4F44' if d['speaker'] == 'Coach' else '#D8A7B1'};">
                    <b><span class="zen-badge {speaker_badge}">{d['speaker']}</span></b> {marker_html}
                    <div style="margin-top: 6px; color: #333;">{text}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"#### 💡 {t('Câu hỏi phản tư dành cho Coach:', 'Coach Reflection Prompts:')}")
            prompts = cs.get("reflectionQuestionsVi", []) if st.session_state.lang == 'vi' else cs.get("reflectionQuestionsEn", [])
            for p in prompts:
                st.markdown(f"- *{p}*")
        else:
            st.info(t("Chưa có case study cho bài học này.", "No case study for this lesson."))

    # TAB 5: QUIZ
    with tab5:
        sec_quizzes = [q for q in QUIZZES if q.get("sectionId") == current_sec_id]
        if not sec_quizzes:
            sec_quizzes = QUIZZES[:1]

        for q_idx, q in enumerate(sec_quizzes):
            st.markdown(f"**Câu {q_idx + 1}: {q['questionVi'] if st.session_state.lang == 'vi' else q['questionEn']}**")
            opts = {opt["key"]: f"{opt['key']}. {opt['textVi'] if st.session_state.lang == 'vi' else opt['textEn']}" for opt in q["options"]}
            
            user_choice = st.radio(
                t("Chọn câu trả lời:", "Select option:"),
                options=list(opts.keys()),
                format_func=lambda k: opts[k],
                key=f"quiz_opt_{q['id']}",
                index=None
            )

            if user_choice:
                if user_choice == q["correctAnswer"]:
                    st.success(f"✅ {t('Chính xác!', 'Correct!')} {q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}")
                else:
                    st.error(f"❌ {t('Chưa chính xác.', 'Incorrect.')} {t('Đáp án đúng là:', 'Correct answer is:')} **{q['correctAnswer']}**.\n\n{q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}")

    # TAB 6: GHI CHÚ CÁ NHÂN
    with tab6:
        st.markdown(f"#### 📝 {t('Ghi chú phản tư cá nhân cho bài học này', 'Personal Study Notes')}")
        current_note = st.session_state.notes.get(current_sec_id, "")
        user_input = st.text_area(
            t("Ghi lại bài học đọng lại trong bạn hôm nay:", "Note down key insights from this lesson:"),
            value=current_note,
            height=180
        )
        if st.button(t("💾 Lưu Ghi Chú", "💾 Save Notes")):
            st.session_state.notes[current_sec_id] = user_input
            st.toast(t("Ghi chú đã được lưu an toàn!", "Notes saved successfully!"))


# ==========================================
# 8. PHÒNG THI THỬ SJT CHUẨN ICF (SJT EXAM)
# ==========================================
elif st.session_state.page == "sjt":
    st.markdown(f"<h2>⚖️ {t('Phòng Thi Thử Situational Judgment Test (SJT)', 'ICF PCC SJT Exam Simulator')}</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 12px; padding: 16px; margin-bottom: 20px;">
        <b>📌 {t('Quy chế thi phán đoán tình huống ICF:', 'ICF Credentialing Exam Rules:')}</b>
        <ul style="margin: 8px 0 0 0; padding-left: 20px; font-size: 0.95rem; color: #555;">
            <li>{t('Mỗi tình huống yêu cầu chọn đồng thời <b>1 phương án TỐT NHẤT (BEST)</b> và <b>1 phương án TỆ NHẤT (WORST)</b>.', 'Each scenario requires choosing exactly <b>1 BEST option</b> and <b>1 WORST option</b>.')}</li>
            <li>{t('Thang điểm: +1 điểm cho mỗi lựa chọn đúng (Tối đa 2 điểm/câu).', 'Scoring: +1 point for correct BEST, +1 point for correct WORST (Max 2 pts/question).')}</li>
            <li>{t('Không được chọn trùng 1 phương án cho cả Best và Worst.', 'You cannot select the same option for both Best and Worst.')}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    total_questions = len(PRACTICE_QUESTIONS)
    
    for idx, q in enumerate(PRACTICE_QUESTIONS):
        qid = q["id"]
        q_ans = st.session_state.sjt_answers.get(qid, {"best": None, "worst": None})

        st.markdown(f"""
        <div class="zen-card">
            <span class="zen-badge zen-badge-primary">Câu {idx + 1} / {total_questions}</span>
            <span class="zen-badge zen-badge-gold">{q.get('primaryCompetency', 'ICF Competency')}</span>
            <h4 style="margin: 12px 0; color: #2F3E34; font-size: 1.1rem; line-height: 1.6;">
                {q['questionVi'] if st.session_state.lang == 'vi' else q['questionEn']}
            </h4>
        </div>
        """, unsafe_allow_html=True)

        options = q["options"]
        opt_dict = {opt["key"]: f"[{opt['key']}] {opt['textVi'] if st.session_state.lang == 'vi' else opt['textEn']}" for opt in options}

        col_b, col_w = st.columns(2)
        with col_b:
            best_choice = st.selectbox(
                f"🌟 {t('Chọn phương án TỐT NHẤT (BEST)', 'Select BEST option')} ({qid}):",
                options=["-- Chưa chọn --"] + list(opt_dict.keys()),
                format_func=lambda k: opt_dict.get(k, k),
                key=f"best_{qid}",
                index=0 if not q_ans.get("best") else (list(opt_dict.keys()).index(q_ans["best"]) + 1)
            )
        with col_w:
            worst_choice = st.selectbox(
                f"⚠️ {t('Chọn phương án TỆ NHẤT (WORST)', 'Select WORST option')} ({qid}):",
                options=["-- Chưa chọn --"] + list(opt_dict.keys()),
                format_func=lambda k: opt_dict.get(k, k),
                key=f"worst_{qid}",
                index=0 if not q_ans.get("worst") else (list(opt_dict.keys()).index(q_ans["worst"]) + 1)
            )

        st.session_state.sjt_answers[qid] = {
            "best": None if best_choice == "-- Chưa chọn --" else best_choice,
            "worst": None if worst_choice == "-- Chưa chọn --" else worst_choice
        }

        if best_choice != "-- Chưa chọn --" and best_choice == worst_choice:
            st.warning(t("⚠️ Bạn đang chọn cùng một phương án cho cả Best và Worst. Vui lòng chọn 2 phương án khác nhau!", "⚠️ Best and Worst cannot be the same option!"))

        if st.session_state.sjt_submitted:
            b_correct = (best_choice == q["bestAnswer"])
            w_correct = (worst_choice == q["worstAnswer"])
            
            st.markdown(f"""
            <div style="background: #F2EBE1; border-radius: 10px; padding: 14px; margin-top: 12px; font-size: 0.92rem;">
                <div><b>🎯 {t('Đáp án chính thức:', 'Official Key:')}</b> BEST = <b style="color: green;">{q['bestAnswer']}</b> | WORST = <b style="color: red;">{q['worstAnswer']}</b></div>
                <div style="margin-top: 6px;"><b>Kết quả của bạn:</b> BEST ({'✅ Đúng' if b_correct else '❌ Sai'}) | WORST ({'✅ Đúng' if w_correct else '❌ Sai'})</div>
                <div style="margin-top: 8px; color: #333;"><b>📖 {t('Phân tích lăng kính ICF:', 'ICF Rationale:')}</b> {q['explanationVi'] if st.session_state.lang == 'vi' else q['explanationEn']}</div>
                <div style="margin-top: 4px; color: #8C6D53;"><b>💡 {t('Từ khóa trọng tâm:', 'Key Exam Clue:')}</b> {q.get('keyClueVi', '') if st.session_state.lang == 'vi' else q.get('keyClueEn', '')}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<hr style='border: none; border-top: 1px dashed #D8C7B5; margin: 24px 0;'/>", unsafe_allow_html=True)

    col_sub1, col_sub2 = st.columns([2, 1])
    with col_sub1:
        if st.button(t("📝 Nộp Bài Thi Thử & Chấm Điểm Ngay", "📝 Submit Mock Exam & View Scores"), use_container_width=True, type="primary"):
            st.session_state.sjt_submitted = True
            score = 0
            for q in PRACTICE_QUESTIONS:
                qid = q["id"]
                ans = st.session_state.sjt_answers.get(qid, {})
                if ans.get("best") == q["bestAnswer"]:
                    score += 1
                if ans.get("worst") == q["worstAnswer"]:
                    score += 1
            st.session_state.sjt_score = score
            st.rerun()

    if st.session_state.sjt_submitted and "sjt_score" in st.session_state:
        score = st.session_state.sjt_score
        max_score = total_questions * 2
        pct = int(score / max_score * 100)
        
        st.markdown(f"""
        <div class="zen-card" style="text-align: center; background: #FAF7F2; border: 2px solid #8BA888; margin-top: 20px;">
            <h2>🎉 {t('Kết Quả Bài Thi Thử SJT', 'Mock Exam Results')}</h2>
            <div style="font-size: 2.8rem; color: {'#3F4F44' if pct >= 75 else '#9C4158'}; font-weight: bold; margin: 8px 0;">
                {score} / {max_score} <span style="font-size: 1.4rem;">({pct}%)</span>
            </div>
            <p style="font-size: 1.1rem; color: #444;">
                {t('Chuẩn đỗ ICF PCC: ≥ 75% tổng điểm.', 'ICF PCC Passing Standard: ≥ 75% total points.')}
            </p>
            <div style="margin-top: 10px;">
                {'🌟 Chúc mừng bạn đã vượt qua chuẩn năng lực PCC xuất sắc!' if pct >= 75 else '🌿 Hãy tiếp tục chiêm nghiệm các giải thích bẫy thi ở trên để bồi đắp phản xạ nhé!'}
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 9. BẢNG GIÁ HỘI VIÊN & VIETQR (PRICING)
# ==========================================
elif st.session_state.page == "pricing":
    st.markdown(f"<h2>💳 {t('Gói Hội Viên Ôn Thi & Kích Hoạt VietQR', 'Membership Tiers & VietQR Activation')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #666;'>{t('Lựa chọn lộ trình đồng hành phù hợp với thời gian dự thi của bạn. Hỗ trợ thanh toán tự động qua mã VietQR chuẩn ngân hàng Việt Nam.', 'Select the study roadmap aligned with your exam schedule. Automated VietQR bank transfer supported.')}</p>", unsafe_allow_html=True)

    # Nhập mã giảm giá
    st.markdown(f"#### 🎁 {t('Mã Ưu Đãi Giảm Giá', 'Promo & Discount Code')}")
    col_code1, col_code2 = st.columns([3, 1])
    with col_code1:
        entered_code = st.text_input(t("Nhập mã giảm giá (VD: PCC2026, ZENCOACH, LANGMAI):", "Enter promo code:"), key="promo_input").strip().upper()
    with col_code2:
        st.write("")
        st.write("")
        discount_rate = 0
        if entered_code == "PCC2026":
            discount_rate = 0.20
            st.success(t("Giảm 20% (PCC 2026)", "20% Off applied!"))
        elif entered_code == "ZENCOACH":
            discount_rate = 0.15
            st.success(t("Giảm 15% (Zen Coach)", "15% Off applied!"))
        elif entered_code == "LANGMAI":
            discount_rate = 0.10
            st.success(t("Giảm 10% (Làng Mai)", "10% Off applied!"))
        elif entered_code:
            st.error(t("Mã không hợp lệ", "Invalid code"))

    pricing_data = SYSTEM_SETTINGS.get("pricing", {})
    tiers = ["free", "1_month", "6_months", "12_months"]
    
    cols = st.columns(4)
    for i, tier_key in enumerate(tiers):
        t_info = pricing_data.get(tier_key, {})
        base_price = t_info.get("price", 0)
        final_price = int(base_price * (1 - discount_rate)) if base_price > 0 else 0

        with cols[i]:
            st.markdown(f"""
            <div class="zen-card" style="height: 100%; border-top: 4px solid {'#8BA888' if tier_key == '6_months' else '#D8C7B5'};">
                <span class="zen-badge {'zen-badge-gold' if tier_key == '6_months' else 'zen-badge-primary'}">{t_info.get('nameVi' if st.session_state.lang == 'vi' else 'nameEn', tier_key)}</span>
                <div style="font-size: 1.6rem; font-weight: bold; color: #2F3E34; margin: 12px 0 6px 0;">
                    {f"{final_price:,} đ" if final_price > 0 else t("Miễn Phí", "Free")}
                </div>
                {f'<div style="text-decoration: line-through; color: #999; font-size: 0.85rem;">{base_price:,} đ</div>' if discount_rate > 0 and base_price > 0 else ''}
                <hr style="margin: 12px 0;"/>
                <ul style="padding-left: 16px; font-size: 0.85rem; color: #555; line-height: 1.5;">
                    {''.join([f'<li>{f}</li>' for f in t_info.get('featuresVi' if st.session_state.lang == 'vi' else 'featuresEn', [])])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(f"### 📲 {t('Thanh Toán Nhanh Qua Mã VietQR Chuẩn NAPAS', 'Instant VietQR Bank Transfer')}")
    chosen_tier = st.selectbox(
        t("Chọn gói bạn muốn đăng ký:", "Choose tier to activate:"),
        options=["1_month", "6_months", "12_months"],
        format_func=lambda k: f"{pricing_data.get(k, {}).get('nameVi' if st.session_state.lang == 'vi' else 'nameEn', k)} — {int(pricing_data.get(k, {}).get('price', 0) * (1 - discount_rate)):,} đ"
    )

    chosen_info = pricing_data.get(chosen_tier, {})
    amount_to_pay = int(chosen_info.get("price", 0) * (1 - discount_rate))
    order_code = f"PCC-{chosen_tier[:2].upper()}-{random.randint(100, 999)}"
    
    bank_bin = SYSTEM_SETTINGS.get("bankBin", "970436")
    acc_num = SYSTEM_SETTINGS.get("accountNumber", "9988776655")
    acc_holder = SYSTEM_SETTINGS.get("accountHolder", "VI VIEN KHAI VAN ZEN PCC")
    
    vietqr_url = f"https://img.vietqr.io/image/{bank_bin}-{acc_num}-compact2.png?amount={amount_to_pay}&addInfo={order_code}&accountName={acc_holder.replace(' ', '%20')}"

    col_qr, col_info = st.columns([1, 1])
    with col_qr:
        st.image(vietqr_url, caption=f"{t('Mã VietQR tự động điền số tiền', 'VietQR pre-filled')} {amount_to_pay:,} đ", use_column_width=True)
    with col_info:
        st.markdown(f"""
        <div class="zen-card">
            <h4>{t('Thông Tin Chuyển Khoản:', 'Bank Transfer Details:')}</h4>
            <p>🏦 <b>{t('Ngân hàng:', 'Bank:')}</b> {SYSTEM_SETTINGS.get('bankName', 'Vietcombank')}</p>
            <p>🔢 <b>{t('Số tài khoản:', 'Account Number:')}</b> <code style="font-size: 1.1rem; color: #3F4F44;">{acc_num}</code></p>
            <p>👤 <b>{t('Chủ tài khoản:', 'Account Holder:')}</b> {acc_holder}</p>
            <p>💰 <b>{t('Số tiền:', 'Amount:')}</b> <b style="color: #9C4158; font-size: 1.2rem;">{amount_to_pay:,} đ</b></p>
            <p>📝 <b>{t('Nội dung chuyển khoản:', 'Reference Note:')}</b> <code style="background: #FEF3D6; padding: 2px 8px; border-radius: 4px; font-weight: bold;">{order_code}</code></p>
            <hr style="margin: 12px 0;"/>
            <p style="font-size: 0.85rem; color: #666;">
                <i>{t('Tài khoản sẽ được mở khóa tự động trong vòng 5-15 phút sau khi hệ thống nhận được giao dịch.',
                      'Your account will be activated within 5-15 minutes once payment is verified.')}</i>
            </p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 10. CỔNG QUẢN TRỊ ADMIN (ADMIN)
# ==========================================
elif st.session_state.page == "admin":
    st.markdown(f"<h2>🛡️ {t('Cổng Quản Trị Hệ Thống & Quản Lý Đơn Hàng', 'Admin Portal & Order Management')}</h2>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(t("Tổng Học Viên", "Total Students"), "128", "+12 tuần này")
    with c2:
        st.metric(t("Doanh Thu Tháng", "Monthly Revenue"), "34.500.000 đ", "+18%")
    with c3:
        st.metric(t("Đơn Chờ Duyệt", "Pending Orders"), str(len([o for o in st.session_state.orders if o['status'] == 'Chờ duyệt'])))
    with c4:
        st.metric(t("Ngân Hàng Đề SJT", "SJT Bank"), str(len(PRACTICE_QUESTIONS)) + " câu")

    st.markdown("---")
    st.markdown(f"### 📋 {t('Danh Sách Đơn Hàng Gần Đây', 'Recent VietQR Orders')}")
    
    for o in st.session_state.orders:
        col_o1, col_o2, col_o3, col_o4, col_o5 = st.columns([2, 2, 2, 2, 2])
        with col_o1:
            st.write(f"**{o['code']}**")
        with col_o2:
            st.write(o['name'])
        with col_o3:
            st.write(o['tier'])
        with col_o4:
            st.write(f"{o['amount']:,} đ")
        with col_o5:
            if o['status'] == "Chờ duyệt":
                if st.button(t("Duyệt đơn", "Approve"), key=f"app_{o['code']}"):
                    o['status'] = "Đã duyệt"
                    st.toast(t(f"Đã duyệt đơn {o['code']} thành công!", f"Order {o['code']} approved!"))
                    st.rerun()
            else:
                st.markdown(f"<span style='color: green;'>✅ {o['status']}</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"### 🪷 {t('Bộ Sưu Tập 12 Huy Hiệu Chánh Niệm (Stickers)', '12 Mindfulness Stickers Collection')}")
    
    sticker_cols = st.columns(4)
    for idx, s in enumerate(STICKERS):
        with sticker_cols[idx % 4]:
            st.markdown(f"""
            <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 12px; padding: 12px; text-align: center; margin-bottom: 12px;">
                <div style="font-size: 1.8rem;">🏵️</div>
                <b>{s['nameVi'] if st.session_state.lang == 'vi' else s['nameEn']}</b>
                <div style="font-size: 0.78rem; color: #888;">{s['code']}</div>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# 11. CHÂN TRANG (FOOTER & DISCLAIMER)
# ==========================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #7F8C8D; font-size: 0.85rem; padding: 20px 0;">
    <p>🪷 <b>Mentor thi ICF PCC</b> — {t('Vì ước mơ đưa Coaching thành lối sống', 'Making Coaching a Way of Life')}</p>
    <p style="font-size: 0.78rem; max-width: 800px; margin: 0 auto; color: #95A5A6; line-height: 1.5;">
        {t('Tuyên bố miễn trừ: Giao diện và trải nghiệm được lấy cảm hứng từ triết lý Thiền Làng Mai. Ứng dụng này là một nền tảng giáo dục độc lập nhằm hỗ trợ học viên ôn luyện theo Khung Năng lực ICF PCC, không phải là sản phẩm chính thức hoặc có liên kết pháp lý trực tiếp với International Coaching Federation (ICF).',
           'Disclaimer: UI/UX inspired by Plum Village Zen philosophy. This is an independent educational platform built to mentor candidates following the ICF PCC Core Competencies, and is not an official product of or affiliated with the International Coaching Federation (ICF).')}
    </p>
</div>
""", unsafe_allow_html=True)
