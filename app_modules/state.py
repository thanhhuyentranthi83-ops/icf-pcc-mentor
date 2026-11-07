# -*- coding: utf-8 -*-
"""
Session State Management & Multi-language helpers
Includes verified real tracking of curriculum progress, tea-cup micro lessons, and genuine lotus blossoms.
"""
import streamlit as st

def t(vi_text, en_text):
    return vi_text if st.session_state.get("lang", "vi") == "vi" else en_text

def set_page(page_name, section_id=None, module_id=None, lesson_id=None):
    st.session_state.page = page_name
    if section_id:
        st.session_state.current_section = section_id
    if module_id:
        st.session_state.active_module_id = module_id
    if lesson_id:
        st.session_state.active_lesson_id = lesson_id

def compute_real_lotus_bloomed(progress_dict=None):
    """Computes genuine lotus bloom count: 1 completed lesson = 1 lotus (awarded once per lesson, never duplicate)."""
    if progress_dict is None:
        progress_dict = st.session_state.get("curriculum_progress", {})
    # Each lesson marked completed ('read' or 'quiz_passed') counts as 1 lotus flower
    completed = sum(1 for p in progress_dict.values() if p.get("status") in ["read", "quiz_passed"])
    return completed

def update_lesson_progress(lesson_id, status=None, score=None, note=None, needs_review=None):
    if "curriculum_progress" not in st.session_state:
        st.session_state.curriculum_progress = {}
    
    current = st.session_state.curriculum_progress.get(lesson_id, {
        "status": "unread",
        "score": 0,
        "note": "",
        "needs_review": False
    })
    
    if status is not None:
        # Don't downgrade quiz_passed to read
        if not (current.get("status") == "quiz_passed" and status == "read"):
            current["status"] = status
    if score is not None:
        current["score"] = score
    if note is not None:
        current["note"] = note
        # Sync to global notes dictionary as well
        if "notes" not in st.session_state:
            st.session_state.notes = {}
        st.session_state.notes[lesson_id] = note
    if needs_review is not None:
        current["needs_review"] = needs_review

    st.session_state.curriculum_progress[lesson_id] = current
    st.session_state.lotus_bloomed = compute_real_lotus_bloomed()

def init_session_state(DATA):
    if "lang" not in st.session_state:
        st.session_state.lang = "vi"

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if "exam_profile_id" not in st.session_state:
        st.session_state.exam_profile_id = "legacy_78_sjt"

    # Real Curriculum Pathway state
    if "active_module_id" not in st.session_state:
        st.session_state.active_module_id = "mod-1"

    if "active_lesson_id" not in st.session_state:
        st.session_state.active_lesson_id = "mod1-les1"

    if "active_tea_lesson_id" not in st.session_state:
        st.session_state.active_tea_lesson_id = "tea-01"

    if "curriculum_progress" not in st.session_state:
        # Real progress dictionary: {lesson_id: {"status": "unread"|"read"|"quiz_passed", "score": 0, "note": "", "needs_review": False}}
        st.session_state.curriculum_progress = {}

    if "curriculum_lang_mode" not in st.session_state:
        st.session_state.curriculum_lang_mode = "bilingual" # "vi", "en", "bilingual"

    if "lotus_bloomed" not in st.session_state:
        st.session_state.lotus_bloomed = compute_real_lotus_bloomed()

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
        st.session_state.content_status = {}

    if "orders" not in st.session_state:
        st.session_state.orders = [
            {"code": "PCC-1001-A89", "name": "Thu Hương", "tier": "1 Tháng", "amount": 299000, "status": "Đã duyệt"},
            {"code": "PCC-1002-B72", "name": "Bảo Nam", "tier": "6 Tháng", "amount": 1190000, "status": "Đã duyệt"},
            {"code": "PCC-1003-C34", "name": "Minh Đức", "tier": "6 Tháng", "amount": 1190000, "status": "Chờ duyệt"}
        ]
