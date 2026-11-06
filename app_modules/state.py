# -*- coding: utf-8 -*-
"""
Session State Management & Multi-language helpers
"""
import streamlit as st

def t(vi_text, en_text):
    return vi_text if st.session_state.get("lang", "vi") == "vi" else en_text

def set_page(page_name, section_id=None):
    st.session_state.page = page_name
    if section_id:
        st.session_state.current_section = section_id

def init_session_state(DATA):
    if "lang" not in st.session_state:
        st.session_state.lang = "vi"

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if "exam_profile_id" not in st.session_state:
        st.session_state.exam_profile_id = "legacy_78_sjt"

    if "lotus_bloomed" not in st.session_state:
        st.session_state.lotus_bloomed = 5

    theories = {th["sectionId"]: th for th in DATA.get("theories", [])}
    if "current_section" not in st.session_state or st.session_state.current_section not in theories:
        st.session_state.current_section = "sec-a1-1"

    if "fc_index" not in st.session_state:
        st.session_state.fc_index = 0

    if "fc_flipped" not in st.session_state:
        st.session_state.fc_flipped = False

    if "notes" not in st.session_state:
        st.session_state.notes = {}

    if "bookmarked_qids" not in st.session_state:
        st.session_state.bookmarked_qids = []

    if "daily_answers" not in st.session_state:
        st.session_state.daily_answers = {}

    if "daily_submitted" not in st.session_state:
        st.session_state.daily_submitted = False

    if "daily_mode" not in st.session_state:
        st.session_state.daily_mode = "sjt_10"

    if "official_answers" not in st.session_state:
        st.session_state.official_answers = {}

    if "dispute_logs" not in st.session_state:
        st.session_state.dispute_logs = []

    if "exam_history" not in st.session_state:
        # Strictly empty real history (no fabricated progress)
        st.session_state.exam_history = []

    if "sjt_pool_mode" not in st.session_state:
        st.session_state.sjt_pool_mode = "profile_full"

    if "sjt_answers" not in st.session_state:
        st.session_state.sjt_answers = {}

    if "sjt_flagged" not in st.session_state:
        st.session_state.sjt_flagged = []

    if "sjt_submitted" not in st.session_state:
        st.session_state.sjt_submitted = False

    if "sjt_last_result" not in st.session_state:
        st.session_state.sjt_last_result = None

    if "content_status" not in st.session_state:
        # Default all questions to Approved
        st.session_state.content_status = {}

    if "orders" not in st.session_state:
        st.session_state.orders = [
            {"code": "PCC-1001-A89", "name": "Thu Hương", "tier": "1 Tháng", "amount": 299000, "status": "Đã duyệt"},
            {"code": "PCC-1002-B72", "name": "Bảo Nam", "tier": "6 Tháng", "amount": 1190000, "status": "Đã duyệt"},
            {"code": "PCC-1003-C34", "name": "Minh Đức", "tier": "6 Tháng", "amount": 1190000, "status": "Chờ duyệt"}
        ]
