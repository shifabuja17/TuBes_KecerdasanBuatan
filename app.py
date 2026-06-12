import streamlit as st

# Import komponen yang sudah kita pisah
from styles import apply_custom_css
from tabs.dashboard import render_dashboard
from tabs.chat import render_chat
from tabs.coping import render_coping

# ──────────────────────────────────────────────────────────
# Page Config & Styles
# ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AmigoAI — Teman Sehat Mentalmu",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)
apply_custom_css()

# ──────────────────────────────────────────────────────────
# Session State Initialization
# ──────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "stress_scores" not in st.session_state:
    st.session_state.stress_scores = []
if "questionnaire_submitted" not in st.session_state:
    st.session_state.questionnaire_submitted = False

# ──────────────────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        "#### 🌿 Tentang AmigoAI\n"
        "Teman digital untuk membantu mahasiswa "
        "mengatasi burnout akademik dengan empati dan dukungan."
    )
    st.markdown(
        '<p style="font-size:0.78rem;color:#7B7B9E;">'
        "⚠️ Aplikasi ini bukan pengganti konseling profesional.</p>",
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────────────────
# Hero Header
# ──────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero-header">
        <h1>🌿 AmigoAI</h1>
        <p>Teman digitalmu untuk melewati masa-masa sulit perkuliahan</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────
# Tabs Router
# ──────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🎯 Dashboard Stres", "💬 AI Venting Buddy", "🧭 Coping Navigator"])

with tab1:
    render_dashboard()

with tab2:
    render_chat()

with tab3:
    render_coping()

# ──────────────────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="footer">
        🌿 <strong>AmigoAI</strong> v1.0 — Dibuat dengan 💛 untuk kesehatan mental mahasiswa Indonesia<br>
        <span style="font-size:0.75rem;">⚠️ Aplikasi ini bukan pengganti konseling profesional. 
        Jika kamu membutuhkan bantuan segera, hubungi 119 ext. 8</span>
    </div>
    """,
    unsafe_allow_html=True,
)