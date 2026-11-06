# -*- coding: utf-8 -*-
"""
Zen Theme & Audio/Visual Components for PCC Learning & Practice
Plum Village (Làng Mai) Aesthetic
"""
import streamlit as st

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,400&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        color: #2C3E50;
    }

    .stApp {
        background-color: #F7F3EA;
    }

    h1, h2, h3, .zen-serif {
        font-family: 'Playfair Display', Georgia, serif !important;
        color: #2F3E34 !important;
        font-weight: 600;
    }

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

    .zen-disclaimer {
        background: #FFF9E6;
        border-left: 4px solid #D4A373;
        border-radius: 8px;
        padding: 12px 16px;
        font-size: 0.85rem;
        color: #6B5B4D;
        line-height: 1.5;
        margin: 16px 0;
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
    .zen-badge-blue { background-color: #E6F0FA; color: #1E4E79; }
    .zen-badge-gray { background-color: #F0EDE8; color: #5F6F65; }

    .stButton > button {
        background-color: #3F4F44;
        color: #FFFFFF !important;
        border-radius: 12px;
        padding: 9px 20px;
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
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""

def render_bell_button(t):
    btn_text = t("Thỉnh một tiếng chuông thiền", "Ring a Mindful Bell")
    bell_html = f"""
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
            width: 100%;
            justify-content: center;
        ">
            🔔 <span>{btn_text}</span>
        </button>
    </div>
    <script>
    function playZenBell() {{
        try {{
            const ctx = new (window.AudioContext || window.webkitAudioContext)();
            const now = ctx.currentTime;
            const freqs = [180, 360, 540, 720];
            const gains = [0.4, 0.25, 0.15, 0.08];

            freqs.forEach((freq, i) => {{
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
            }});
        }} catch (e) {{
            console.log(e);
        }}
    }}
    </script>
    """
    st.components.v1.html(bell_html, height=55)

def render_breathing_widget(t):
    title = t("Khoảng Lặng Thở 4-7-8 Cùng Sen", "Mindful 4-7-8 Breathing Pause")
    desc = t("Hít vào (4s) qua mũi — Giữ hơi (7s) an trú — Thở ra (8s) buông thư qua miệng.",
             "Inhale (4s) deeply — Hold gently (7s) — Exhale slowly (8s) releasing all tension.")
    quote = t("Thở vào, tâm tĩnh lặng... Thở ra, miệng mỉm cười.", "Breathing in, I calm my body... Breathing out, I smile.")
    breathing_html = f"""
    <div style="background: #FAF7F2; border: 1px solid #D8C7B5; border-radius: 16px; padding: 24px; text-align: center; margin: 20px 0;">
        <h4 style="font-family: Georgia, serif; color: #2F3E34; margin: 0 0 8px 0;">🌿 {title}</h4>
        <p style="font-size: 0.88rem; color: #666; margin-bottom: 20px;">{desc}</p>
        <div style="display: flex; justify-content: center; align-items: center; margin: 16px 0;">
            <div id="zenBreathCircle" style="
                width: 120px;
                height: 120px;
                border-radius: 50%;
                background: radial-gradient(circle, #E2ECE1 0%, #8BA888 100%);
                box-shadow: 0 0 25px rgba(139, 168, 136, 0.4);
                display: flex;
                align-items: center;
                justify-content: center;
                color: #2F3E34;
                font-weight: 600;
                font-size: 0.95rem;
                animation: breathAnim 19s infinite ease-in-out;
            ">
                🪷
            </div>
        </div>
        <div style="font-size: 0.9rem; font-weight: 500; color: #3F4F44; min-height: 24px;">{quote}</div>
    </div>
    <style>
    @keyframes breathAnim {{
        0% {{ transform: scale(0.85); opacity: 0.8; }}
        21% {{ transform: scale(1.35); opacity: 1; }}
        58% {{ transform: scale(1.35); opacity: 1; }}
        100% {{ transform: scale(0.85); opacity: 0.8; }}
    }}
    </style>
    """
    st.components.v1.html(breathing_html, height=270)

def render_disclaimer_banner(t):
    disc_title = t("Tuyên Bố Miễn Trừ Trách Nhiệm Độc Lập:", "Independent Study Disclaimer:")
    disc_text = t("Ứng dụng độc lập phục vụ học tập; không tự nhận được ICF bảo trợ, chứng nhận hoặc phê duyệt. Không sử dụng logo ICF nếu chưa được phép.",
                  "This application is an independent educational tool for self-study and practice; it does not claim to be sponsored, accredited, or approved by the International Coaching Federation (ICF). Official ICF logos are not used without permission.")
    st.markdown(f"""
    <div class="zen-disclaimer">
        <b>⚖️ {disc_title}</b><br/>
        {disc_text}
    </div>
    """, unsafe_allow_html=True)
