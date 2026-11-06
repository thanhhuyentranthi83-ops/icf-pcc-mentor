# -*- coding: utf-8 -*-
"""
Mentor Thi — PCC Learning & Practice
Phụ đề: Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching.
Vì ước mơ đưa Coaching thành lối sống.
Ứng dụng độc lập phục vụ học tập; không tự nhận được ICF bảo trợ, chứng nhận hoặc phê duyệt. Không sử dụng logo ICF nếu chưa được phép.
Triết lý thiết kế: Thiền Làng Mai (Plum Village Zen) — Tĩnh tại, mộc mạc, không hối thúc.
Triển khai: Streamlit Community Cloud (share.streamlit.io) & GitHub Ready.
"""

import os
import sys

# Ensure base directory and scripts directory are in sys.path for Streamlit Cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

import json
import streamlit as st

# Import app modules
from app_modules.styles import CUSTOM_CSS, render_bell_button
from app_modules.state import init_session_state, t, set_page
from app_modules.page_home import render_home_page
from app_modules.page_library import render_library_page
from app_modules.page_official_samples import render_official_samples_page
from app_modules.page_curriculum import render_curriculum_page
from app_modules.page_daily_practice import render_daily_practice_page
from app_modules.page_sjt import render_sjt_page
from app_modules.page_assistant import render_assistant_page
from app_modules.page_journal import render_journal_page
from app_modules.page_admin import render_admin_page
from app_modules.page_pricing import render_pricing_page

# ==========================================
# 1. STREAMLIT PAGE CONFIG & ZEN CSS
# ==========================================
st.set_page_config(
    page_title="Mentor Thi 🪷",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ==========================================
# 2. LOAD SELF-CONTAINED DATA
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
KNOWLEDGE_QUESTIONS = DATA.get("knowledgeQuestions", [])
OFFICIAL_SAMPLES = DATA.get("officialSampleQuestions", [])
VERIFIED_SOURCES = DATA.get("verifiedSources", [])
EXAM_PROFILES = {ep["id"]: ep for ep in DATA.get("examProfiles", [])}
MINDFULNESS_MESSAGES = DATA.get("mindfulnessMessages", [])
STICKERS = DATA.get("stickers", [])
SYSTEM_SETTINGS = DATA.get("systemSettings", {})
DISCOUNT_CODES = DATA.get("discountCodes", [])

STUDY_SECTIONS = [s for s in SECTIONS if s["id"] in THEORIES]
if not STUDY_SECTIONS:
    STUDY_SECTIONS = [s for s in SECTIONS if s.get("parentId")]

# ==========================================
# 3. INITIALIZE SESSION STATE
# ==========================================
init_session_state(DATA)

# ==========================================
# 4. SIDEBAR (PLUM VILLAGE ZEN)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 2px;'>🪷 Mentor Thi</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #8C6D53; font-size: 0.85rem; margin-top: 0; font-weight: 500;'>{t('Hiểu chuẩn — Luyện phán đoán — Phát triển năng lực coaching', 'Master Standards — Hone Judgment — Elevate Coaching')}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #5F6F65; font-size: 0.8rem; margin-top: -6px;'>{t('Vì ước mơ đưa Coaching thành lối sống', 'Making Coaching a Way of Life')}</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Language Switcher
    col_lang1, col_lang2 = st.columns(2)
    with col_lang1:
        if st.button("🇻🇳 Tiếng Việt", use_container_width=True, type="primary" if st.session_state.lang == "vi" else "secondary"):
            st.session_state.lang = "vi"
            st.rerun()
    with col_lang2:
        if st.button("🇬🇧 English", use_container_width=True, type="primary" if st.session_state.lang == "en" else "secondary"):
            st.session_state.lang = "en"
            st.rerun()

    # Active Exam Profile Info in Sidebar
    st.markdown("---")
    cur_prof_id = st.session_state.exam_profile_id
    cur_prof = EXAM_PROFILES.get(cur_prof_id, list(EXAM_PROFILES.values())[0]) if EXAM_PROFILES else {}
    st.markdown(f"""
    <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 12px; padding: 12px; margin-bottom: 8px;">
        <div style="font-size: 0.78rem; color: #8C6D53; font-weight: 600;">🎯 {t('CẤU HÌNH THI:', 'EXAM PROFILE:')}</div>
        <div style="font-weight: 600; font-size: 0.88rem; color: #2F3E34; margin: 2px 0;">
            {cur_prof.get('nameVi' if st.session_state.lang == 'vi' else 'nameEn', 'ICF Credentialing Exam')}
        </div>
        <div style="font-size: 0.8rem; color: #666;">
            ⏱️ {cur_prof.get('totalTimeMinutes', 180)}p ({cur_prof.get('totalItems', 78)} câu)
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 " + t("Đổi Cấu Hình Thi", "Switch Exam Profile"), use_container_width=True):
        st.session_state.exam_profile_id = "updated_80_items" if cur_prof_id == "legacy_78_sjt" else "legacy_78_sjt"
        st.rerun()

    st.markdown("---")
    render_bell_button(t)

    # Mindful Quote
    if MINDFULNESS_MESSAGES:
        quote = MINDFULNESS_MESSAGES[hash(str(os.getpid())) % len(MINDFULNESS_MESSAGES)]
        st.markdown(f"""
        <div class="zen-quote-box">
            <div style="font-size: 0.82rem; color: #3F4F44; font-weight: 600; margin-bottom: 4px;">🌿 {t('Lời nhắn chánh niệm', 'Mindfulness Whisper')}</div>
            <div style="font-size: 0.85rem; color: #555;">"{quote['textVi'] if st.session_state.lang == 'vi' else quote['textEn']}"</div>
            <div style="font-size: 0.78rem; color: #8C6D53; margin-top: 4px; text-align: right;">— {quote['author']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Lotus Garden Tracker
    st.markdown(f"""
    <div style="background: #FFFFFF; border: 1px solid #EADBCC; border-radius: 12px; padding: 12px; text-align: center; font-size: 0.85rem;">
        <div>🪷 <b>{t('Vườn sen hiện tại', 'Your Lotus Garden')}</b></div>
        <div style="font-size: 1.3rem; color: #9C4158; margin: 4px 0;">{'🪷 ' * min(st.session_state.lotus_bloomed, 7)}</div>
        <div style="color: #666;">{st.session_state.lotus_bloomed} {t('đóa sen đã nở', 'lotuses in full bloom')}</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 5. TOP NAVIGATION BAR (CLEAR CATEGORIES)
# ==========================================
# Row 1: Core Navigation (Home, Library, Official Samples, Curriculum, Assistant)
r1_c1, r1_c2, r1_c3, r1_c4, r1_c5 = st.columns(5)
with r1_c1:
    if st.button("🏠 " + t("Trang Chủ", "Home"), use_container_width=True, type="primary" if st.session_state.page == "home" else "secondary"):
        set_page("home")
        st.rerun()
with r1_c2:
    if st.button("🏛️ " + t("Thư Viện Chuẩn", "Library"), use_container_width=True, type="primary" if st.session_state.page == "library" else "secondary"):
        set_page("library")
        st.rerun()
with r1_c3:
    if st.button("📑 " + t("8 Câu Mẫu ICF", "8 Samples"), use_container_width=True, type="primary" if st.session_state.page == "official_samples" else "secondary"):
        set_page("official_samples")
        st.rerun()
with r1_c4:
    if st.button("📚 " + t("Lộ Trình Học", "Curriculum"), use_container_width=True, type="primary" if st.session_state.page == "curriculum" else "secondary"):
        set_page("curriculum")
        st.rerun()
with r1_c5:
    if st.button("🤖 " + t("Trợ Lý Học Tập", "AI Assistant"), use_container_width=True, type="primary" if st.session_state.page == "assistant" else "secondary"):
        set_page("assistant")
        st.rerun()

# Row 2: Practice, Mock Simulator, Learning Journal, Admin, Pricing
r2_c1, r2_c2, r2_c3, r2_c4, r2_c5 = st.columns(5)
with r2_c1:
    if st.button("⚡ " + t("Luyện 10 Câu/Ngày", "Daily 10 Drill"), use_container_width=True, type="primary" if st.session_state.page == "daily_practice" else "secondary"):
        set_page("daily_practice")
        st.rerun()
with r2_c2:
    if st.button("⚖️ " + t("Thi Thử Mô Phỏng", "Mock Simulator"), use_container_width=True, type="primary" if st.session_state.page == "sjt" else "secondary"):
        set_page("sjt")
        st.rerun()
with r2_c3:
    if st.button("📓 " + t("Sổ Học Tập", "Learning Journal"), use_container_width=True, type="primary" if st.session_state.page == "journal" else "secondary"):
        set_page("journal")
        st.rerun()
with r2_c4:
    if st.button("🛡️ " + t("Quản Trị", "Admin & Review"), use_container_width=True, type="primary" if st.session_state.page == "admin" else "secondary"):
        set_page("admin")
        st.rerun()
with r2_c5:
    if st.button("💳 " + t("Gói Hội Viên", "Pricing"), use_container_width=True, type="primary" if st.session_state.page == "pricing" else "secondary"):
        set_page("pricing")
        st.rerun()

st.markdown("<hr style='margin: 8px 0 20px 0; border: none; border-top: 1px solid #EADBCC;'/>", unsafe_allow_html=True)

# ==========================================
# 6. PAGE ROUTING
# ==========================================
cur_page = st.session_state.page

if cur_page == "home":
    render_home_page(DATA, EXAM_PROFILES, PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t, set_page)

elif cur_page == "library":
    render_library_page(DATA, VERIFIED_SOURCES, COMPETENCIES, t)

elif cur_page == "official_samples":
    render_official_samples_page(OFFICIAL_SAMPLES, t)

elif cur_page == "curriculum":
    render_curriculum_page(DATA, STUDY_SECTIONS, THEORIES, KEYWORDS, FLASHCARDS, CASE_STUDIES, QUIZZES, t)

elif cur_page == "assistant":
    render_assistant_page(t)

elif cur_page == "daily_practice":
    render_daily_practice_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, t)

elif cur_page == "sjt":
    render_sjt_page(EXAM_PROFILES, PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t)

elif cur_page == "journal":
    render_journal_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t, set_page)

elif cur_page == "admin":
    render_admin_page(PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t)

elif cur_page == "pricing":
    render_pricing_page(t)

else:
    render_home_page(DATA, EXAM_PROFILES, PRACTICE_QUESTIONS, KNOWLEDGE_QUESTIONS, OFFICIAL_SAMPLES, t, set_page)
