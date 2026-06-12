import streamlit as st
import google.generativeai as genai
import pandas as pd
import datetime
import re

# ──────────────────────────────────────────────────────────
# Page Config
# ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OvercomeAI — Teman Sehat Mentalmu",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────
# Custom CSS — pastel, calming, premium feel
# ──────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700&display=swap');

/* ── Root Variables ── */
:root {
    --pastel-lavender: #E8E0F0;
    --pastel-mint: #D4EDDA;
    --pastel-peach: #FDDCB5;
    --pastel-sky: #D6EAF8;
    --pastel-rose: #FADBD8;
    --pastel-cream: #FDF6F0;
    --text-primary: #4A4A6A;
    --text-secondary: #7B7B9E;
    --accent-purple: #9B8EC4;
    --accent-blue: #7C9CBF;
    --accent-green: #82C9A1;
    --gradient-1: linear-gradient(135deg, #E8E0F0 0%, #D6EAF8 50%, #D4EDDA 100%);
    --gradient-2: linear-gradient(135deg, #9B8EC4 0%, #7C9CBF 100%);
    --shadow-soft: 0 4px 20px rgba(155, 142, 196, 0.15);
    --shadow-hover: 0 8px 30px rgba(155, 142, 196, 0.25);
    --radius: 16px;
}

html, body, .stApp {
    font-family: 'Inter', sans-serif !important;
}

[data-testid="collapsedControl"] span,
[data-testid="collapsedControl"] div,
[data-testid="collapsedControl"] svg,
.material-symbols-rounded,
.stIcon {
    font-family: "Material Symbols Rounded", "Material Icons" !important;
}      

h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif !important;
    color: var(--text-primary) !important;
}

/* ── Hero Header ── */
.hero-header {
    background: var(--gradient-1);
    border-radius: var(--radius);
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow-soft);
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(155,142,196,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-header h1 {
    font-size: 2.2rem;
    margin: 0;
    background: var(--gradient-2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-header p {
    color: var(--text-secondary);
    font-size: 1rem;
    margin-top: 0.3rem;
}

/* ── Glass Card ── */
.glass-card {
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(232, 224, 240, 0.6);
    border-radius: var(--radius);
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-soft);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.glass-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-hover);
}

/* ── Metric Card ── */
.metric-card {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    border-radius: var(--radius);
    padding: 1.2rem 1.5rem;
    text-align: center;
    border: 1px solid rgba(232,224,240,0.5);
    box-shadow: var(--shadow-soft);
    transition: transform 0.2s ease;
}
.metric-card:hover {
    transform: translateY(-2px);
}
.metric-card .metric-icon {
    font-size: 2rem;
    margin-bottom: 0.3rem;
}
.metric-card .metric-value {
    font-family: 'Outfit', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-primary);
}
.metric-card .metric-label {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-top: 0.2rem;
}

/* ── Status Badge ── */
.status-badge {
    display: inline-block;
    padding: 0.4rem 1.2rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.95rem;
    margin: 0.5rem 0;
}
.status-green  { background: #D4EDDA; color: #2D6A4F; }
.status-yellow { background: #FFF3CD; color: #856404; }
.status-orange { background: #FDDCB5; color: #8B5E3C; }
.status-red    { background: #FADBD8; color: #922B21; }

/* ── Chat Bubbles ── */
.chat-container {
    max-height: 480px;
    overflow-y: auto;
    padding: 1rem;
    border-radius: var(--radius);
    background: rgba(255,255,255,0.4);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(232,224,240,0.4);
    margin-bottom: 1rem;
}
.chat-bubble {
    padding: 0.85rem 1.15rem;
    border-radius: 18px;
    margin-bottom: 0.7rem;
    max-width: 80%;
    line-height: 1.55;
    font-size: 0.92rem;
    animation: fadeSlideIn 0.3s ease;
}
@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
.chat-user {
    background: var(--gradient-2);
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}
.chat-ai {
    background: rgba(232, 224, 240, 0.55);
    color: var(--text-primary);
    border-bottom-left-radius: 6px;
}

/* ── Coping Card ── */
.coping-card {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    border-radius: var(--radius);
    padding: 1.5rem;
    border: 1px solid rgba(232,224,240,0.5);
    box-shadow: var(--shadow-soft);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    height: 100%;
}
.coping-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-hover);
}
.coping-card .card-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}
.coping-card h3 {
    font-size: 1.15rem;
    margin: 0.3rem 0;
}
.coping-card p {
    font-size: 0.88rem;
    color: var(--text-secondary);
    line-height: 1.6;
}
.coping-card .steps {
    background: rgba(232,224,240,0.3);
    border-radius: 12px;
    padding: 0.8rem 1rem;
    margin-top: 0.7rem;
    font-size: 0.85rem;
    line-height: 1.7;
}

/* ── Tab styling ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(255,255,255,0.5);
    border-radius: 12px;
    padding: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 10px 24px;
    font-weight: 500;
    font-family: 'Inter', sans-serif;
}
.stTabs [aria-selected="true"] {
    background: var(--gradient-2) !important;
    color: white !important;
    border-radius: 10px;
}

/* ── Slider label ── */
.slider-label {
    font-weight: 500;
    color: var(--text-primary);
    margin-bottom: 0.2rem;
    font-size: 0.92rem;
}

/* ── Scrollbar ── */
.chat-container::-webkit-scrollbar { width: 6px; }
.chat-container::-webkit-scrollbar-track { background: transparent; }
.chat-container::-webkit-scrollbar-thumb {
    background: var(--accent-purple);
    border-radius: 10px;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 1.5rem;
    color: var(--text-secondary);
    font-size: 0.8rem;
    margin-top: 2rem;
    border-top: 1px solid rgba(232,224,240,0.5);
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────
# Gemini Configuration
# ──────────────────────────────────────────────────────────
SYSTEM_INSTRUCTION = """
Kamu adalah "OvercomeAI", seorang konselor sebaya (peer counselor) yang empatik, hangat, dan suportif. 
Kamu berfokus membantu mahasiswa yang mengalami burnout akademik, kelelahan emosional, dan tekanan perkuliahan.

Panduan perilaku:
1. Selalu gunakan bahasa Indonesia yang ramah, santai tapi tetap sopan — seperti teman dekat yang bisa diajak curhat.
2. Validasi perasaan pengguna terlebih dahulu sebelum memberikan saran. Contoh: "Wajar banget kalau kamu ngerasa capek..."
3. Berikan saran yang praktis dan konkret, seperti teknik manajemen waktu, istirahat, atau olahraga ringan.
4. Jangan pernah mendiagnosis kondisi medis atau psikologis. Jika pengguna menunjukkan tanda-tanda serius, sarankan untuk menemui profesional.
5. Gunakan emoji secukupnya untuk membuat percakapan terasa hangat 🌱
6. Jawaban harus ringkas (maksimal 3-4 paragraf) kecuali diminta menjelaskan lebih detail.
7. Jika pengguna menyebutkan pikiran untuk menyakiti diri sendiri atau bunuh diri, SEGERA tanggapi dengan empati dan arahkan ke layanan darurat.
8. Ingat konteks percakapan sebelumnya untuk memberikan respons yang koheren.
"""

SELF_HARM_KEYWORDS = [
    "bunuh diri", "suicide", "mau mati", "ingin mati", "pengen mati",
    "self harm", "self-harm", "menyakiti diri", "nyakitin diri",
    "gak mau hidup", "tidak mau hidup", "nggak mau hidup",
    "potong nadi", "gantung diri", "overdosis", "kill myself",
    "end my life", "want to die", "hurt myself", "cutting",
    "tidak berguna", "lebih baik mati", "mending mati",
]


def check_self_harm(text: str) -> bool:
    """Check if the user's message contains self-harm related keywords."""
    text_lower = text.lower()
    return any(kw in text_lower for kw in SELF_HARM_KEYWORDS)


def show_emergency_contacts():
    """Display emergency mental health contacts."""
    st.error(
        "🚨 **Kami mendeteksi bahwa kamu mungkin sedang dalam kesulitan berat.**\n\n"
        "Kamu tidak sendirian. Tolong hubungi bantuan profesional sekarang:\n\n"
        "📞 **Into The Light Indonesia** — 119 ext. 8\n\n"
        "📞 **LSM Jangan Bunuh Diri** — 021-9696 9293 / 0858-9155-0802\n\n"
        "📞 **Yayasan Pulih** — 021-788-42580 / 081-184-36633\n\n"
        "📞 **Sejiwa (Kemenkes)** — 119 ext. 8\n\n"
        "💬 **Crisis Text Line** — Kirim SMS ke 119\n\n"
        "---\n"
        "💛 *Kamu berharga. Perasaanmu valid. Bantuan profesional tersedia 24/7.*"
    )


def get_gemini_response(user_message: str, chat_history: list) -> str:
    """Get response from Gemini API with conversation history."""
    # Mengambil API Key dari Streamlit Secrets
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except KeyError:
        return "⚠️ API Key belum dikonfigurasi oleh developer."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=SYSTEM_INSTRUCTION,
        )

        # Build history for Gemini
        gemini_history = []
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model"
            gemini_history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=gemini_history)
        response = chat.send_message(user_message)
        return response.text

    except Exception as e:
        return f"❌ Maaf, terjadi kesalahan: {str(e)}"


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
# Sidebar — API Key Input
# ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        "#### 🌿 Tentang OvercomeAI\n"
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
        <h1>🌿 OvercomeAI</h1>
        <p>Teman digitalmu untuk melewati masa-masa sulit perkuliahan</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────
# Tabs
# ──────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🎯 Dashboard Stres", "💬 AI Venting Buddy", "🧭 Coping Navigator"])

# ══════════════════════════════════════════════════════════
# TAB 1 — Dashboard Stres
# ══════════════════════════════════════════════════════════
with tab1:
    st.markdown("## 📊 Cek Kondisi Mentalmu Hari Ini")
    st.markdown(
        '<p style="color:#7B7B9E;">Jawab 3 pertanyaan singkat berikut untuk mengetahui level stresmu saat ini.</p>',
        unsafe_allow_html=True,
    )

    with st.form("stress_form", clear_on_submit=False):
        st.markdown('<p class="slider-label">1️⃣ Seberapa lelah kamu secara emosional hari ini?</p>', unsafe_allow_html=True)
        q1 = st.slider(
            "Kelelahan emosional",
            1, 5, 3,
            help="1 = Sangat segar, 5 = Sangat kelelahan",
            label_visibility="collapsed",
        )

        st.markdown('<p class="slider-label">2️⃣ Seberapa sulit kamu berkonsentrasi pada tugas kuliah?</p>', unsafe_allow_html=True)
        q2 = st.slider(
            "Kesulitan konsentrasi",
            1, 5, 3,
            help="1 = Sangat fokus, 5 = Sangat sulit fokus",
            label_visibility="collapsed",
        )

        st.markdown('<p class="slider-label">3️⃣ Seberapa besar tekanan akademik yang kamu rasakan?</p>', unsafe_allow_html=True)
        q3 = st.slider(
            "Tekanan akademik",
            1, 5, 3,
            help="1 = Sangat ringan, 5 = Sangat berat",
            label_visibility="collapsed",
        )

        submitted = st.form_submit_button("📝 Lihat Hasil", use_container_width=True)

    if submitted:
        avg_score = round((q1 + q2 + q3) / 3, 1)
        st.session_state.stress_scores.append(avg_score)
        st.session_state.questionnaire_submitted = True

    if st.session_state.questionnaire_submitted and st.session_state.stress_scores:
        latest = st.session_state.stress_scores[-1]

        # Determine status
        if latest <= 2.0:
            status = "🟢 Baik"
            badge_class = "status-green"
            message = "Kondisi mentalmu terlihat baik! Tetap jaga keseimbangan ya 🌟"
            emoji = "😊"
        elif latest <= 3.0:
            status = "🟡 Perlu Perhatian"
            badge_class = "status-yellow"
            message = "Kamu mungkin mulai merasa tekanan. Yuk coba teknik relaksasi di tab Coping Navigator 🌱"
            emoji = "😐"
        elif latest <= 4.0:
            status = "🟠 Stres Sedang"
            badge_class = "status-orange"
            message = "Level stresmu cukup tinggi. Pertimbangkan untuk istirahat dan curhat di AI Venting Buddy 💛"
            emoji = "😟"
        else:
            status = "🔴 Stres Tinggi"
            badge_class = "status-red"
            message = "Kamu sedang dalam tekanan besar. Tolong jangan ragu untuk mencari bantuan profesional 🤝"
            emoji = "😰"

        # Result Display
        st.markdown("---")
        col_r1, col_r2, col_r3 = st.columns(3)

        with col_r1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-icon">{emoji}</div>
                    <div class="metric-value">{latest}/5</div>
                    <div class="metric-label">Skor Stres Rata-rata</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_r2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-icon">📋</div>
                    <div class="metric-value">{len(st.session_state.stress_scores)}</div>
                    <div class="metric-label">Total Check-in</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_r3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-icon">📈</div>
                    <div class="metric-value">{round(sum(st.session_state.stress_scores)/len(st.session_state.stress_scores),1)}</div>
                    <div class="metric-label">Rata-rata Keseluruhan</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(f'<div class="status-badge {badge_class}">{status}</div>', unsafe_allow_html=True)
        st.info(message)

    # ── Weekly Stress Trend Chart (Mock Data) ──
    st.markdown("---")
    st.markdown("### 📈 Tren Stres Mingguan")
    st.markdown(
        '<p style="color:#7B7B9E;font-size:0.88rem;">Data simulasi untuk menggambarkan pola stres selama seminggu terakhir.</p>',
        unsafe_allow_html=True,
    )

    mock_data = pd.DataFrame(
        {
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"],
            "Stres Emosional": [2.5, 3.0, 3.8, 4.2, 3.5, 2.0, 1.8],
            "Tekanan Akademik": [3.0, 3.5, 4.0, 4.5, 3.8, 2.5, 2.0],
            "Kelelahan": [2.0, 2.8, 3.5, 4.0, 3.2, 1.8, 1.5],
        }
    )
    mock_data = mock_data.set_index("Hari")

    st.line_chart(mock_data, use_container_width=True)

    st.markdown(
        """
        <div class="glass-card" style="text-align:center;">
            <p style="margin:0;font-size:0.88rem;color:#7B7B9E;">
                💡 <strong>Insight:</strong> Stres cenderung memuncak di pertengahan minggu (Rabu-Kamis) 
                dan menurun di akhir pekan. Pastikan kamu punya waktu istirahat di tengah minggu!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════
# TAB 2 — AI Venting Buddy
# ══════════════════════════════════════════════════════════
with tab2:
    st.markdown("## 💬 Curhat Sama AI Buddy")
    st.markdown(
        '<p style="color:#7B7B9E;">Ceritakan apa yang kamu rasakan. Aku di sini untuk mendengarkan tanpa menghakimi 🌱</p>',
        unsafe_allow_html=True,
    )

    # Chat history display
    chat_container = st.container()
    with chat_container:
        if not st.session_state.chat_history:
            st.markdown(
                """
                <div class="glass-card" style="text-align:center;padding:2.5rem;">
                    <p style="font-size:2.5rem;margin-bottom:0.5rem;">🌿</p>
                    <p style="font-size:1.05rem;color:#4A4A6A;font-weight:500;">
                        Hai! Aku OvercomeAI, teman curhatmu.
                    </p>
                    <p style="font-size:0.88rem;color:#7B7B9E;">
                        Ceritakan apa pun yang mengganjal di hatimu.<br>
                        Aku akan mendengarkan dengan penuh perhatian. 💛
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    with st.chat_message("user", avatar="🧑‍🎓"):
                        st.markdown(msg["content"])
                else:
                    with st.chat_message("assistant", avatar="🌿"):
                        st.markdown(msg["content"])

    # Chat input
    user_input = st.chat_input("Tulis curhatanmu di sini...", key="chat_input")

    if user_input:
        # Check for self-harm content
        if check_self_harm(user_input):
            # Still add to history but with a safety note
            st.session_state.chat_history.append(
                {"role": "user", "content": user_input}
            )
            safety_response = (
                "Aku sangat khawatir dengan apa yang kamu ceritakan. "
                "Perasaanmu valid, dan kamu tidak sendirian. "
                "Tolong hubungi layanan bantuan darurat di bawah ini. "
                "Mereka terlatih untuk membantu dan tersedia 24/7. 💛"
            )
            st.session_state.chat_history.append(
                {"role": "assistant", "content": safety_response}
            )
            show_emergency_contacts()
            st.rerun()
        else:
            # Add user message to history
            st.session_state.chat_history.append(
                {"role": "user", "content": user_input}
            )

            # Get AI response
            with st.spinner("🌿 OvercomeAI sedang mengetik..."):
                ai_response = get_gemini_response(
                    user_input, st.session_state.chat_history[:-1]
                )

            # Check AI response for self-harm trigger
            if check_self_harm(ai_response):
                show_emergency_contacts()

            st.session_state.chat_history.append(
                {"role": "assistant", "content": ai_response}
            )
            st.rerun()

    # Clear chat button
    if st.session_state.chat_history:
        col_clear, _ = st.columns([1, 3])
        with col_clear:
            if st.button("🗑️ Hapus Riwayat Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()

# ══════════════════════════════════════════════════════════
# TAB 3 — Coping Navigator
# ══════════════════════════════════════════════════════════
with tab3:
    st.markdown("## 🧭 Panduan Coping & Self-Care")
    st.markdown(
        '<p style="color:#7B7B9E;">Temukan teknik-teknik yang terbukti efektif untuk mengelola stres dan burnout.</p>',
        unsafe_allow_html=True,
    )

    # ── Row 1: Breathing & Pomodoro ──
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="coping-card">
                <div class="card-icon">🫁</div>
                <h3>Pernapasan Kotak (Box Breathing)</h3>
                <p>Teknik pernapasan yang digunakan oleh Navy SEALs untuk mengatasi stres dan meningkatkan fokus.</p>
                <div class="steps">
                    <strong>Cara Melakukan:</strong><br>
                    1️⃣ <strong>Tarik napas</strong> selama 4 detik 🌬️<br>
                    2️⃣ <strong>Tahan napas</strong> selama 4 detik ⏸️<br>
                    3️⃣ <strong>Buang napas</strong> selama 4 detik 🌊<br>
                    4️⃣ <strong>Tahan kosong</strong> selama 4 detik ⏸️<br>
                    🔄 Ulangi 4-6 siklus
                </div>
                <p style="margin-top:0.7rem;font-size:0.82rem;color:#82C9A1;">
                    ✅ Menurunkan detak jantung & hormon kortisol
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="coping-card">
                <div class="card-icon">🍅</div>
                <h3>Teknik Pomodoro</h3>
                <p>Metode manajemen waktu yang membagi kerja menjadi interval fokus dengan jeda istirahat teratur.</p>
                <div class="steps">
                    <strong>Cara Melakukan:</strong><br>
                    1️⃣ Pilih satu tugas untuk dikerjakan 📝<br>
                    2️⃣ Pasang timer <strong>25 menit</strong> — fokus penuh! ⏱️<br>
                    3️⃣ Istirahat <strong>5 menit</strong> (peregangan/air) 💧<br>
                    4️⃣ Setelah 4 siklus, istirahat <strong>15-30 menit</strong> 🛋️<br>
                    🔄 Ulangi hingga tugas selesai
                </div>
                <p style="margin-top:0.7rem;font-size:0.82rem;color:#82C9A1;">
                    ✅ Mengurangi prokrastinasi & meningkatkan produktivitas
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Row 2: Journaling & Grounding ──
    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            """
            <div class="coping-card">
                <div class="card-icon">📓</div>
                <h3>Journaling Ekspresif</h3>
                <p>Menulis perasaan dan pikiran secara bebas untuk melepaskan beban emosional dan mendapatkan kejelasan.</p>
                <div class="steps">
                    <strong>Prompt Journaling:</strong><br>
                    🌅 <strong>Pagi:</strong> "3 hal yang kusyukuri hari ini..."<br>
                    📝 <strong>Siang:</strong> "Satu hal yang membuatku bangga..."<br>
                    🌙 <strong>Malam:</strong> "Yang kurasakan hari ini adalah..."<br>
                    💭 <strong>Bebas:</strong> Tulis apa pun selama 10 menit non-stop
                </div>
                <p style="margin-top:0.7rem;font-size:0.82rem;color:#82C9A1;">
                    ✅ Memproses emosi & meningkatkan self-awareness
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="coping-card">
                <div class="card-icon">🌍</div>
                <h3>Teknik Grounding 5-4-3-2-1</h3>
                <p>Teknik mindfulness yang membawamu kembali ke saat ini saat merasa cemas atau overwhelmed.</p>
                <div class="steps">
                    <strong>Cara Melakukan:</strong><br>
                    👀 Sebutkan <strong>5 hal</strong> yang bisa kamu lihat<br>
                    ✋ Sentuh <strong>4 hal</strong> yang bisa kamu rasakan<br>
                    👂 Dengarkan <strong>3 suara</strong> di sekitarmu<br>
                    👃 Cium <strong>2 aroma</strong> di sekitarmu<br>
                    👅 Rasakan <strong>1 rasa</strong> di mulutmu
                </div>
                <p style="margin-top:0.7rem;font-size:0.82rem;color:#82C9A1;">
                    ✅ Efektif untuk meredakan serangan panik & kecemasan
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Row 3: Movement & Digital Detox ──
    col5, col6 = st.columns(2)

    with col5:
        st.markdown(
            """
            <div class="coping-card">
                <div class="card-icon">🏃</div>
                <h3>Gerakan Aktif Ringan</h3>
                <p>Aktivitas fisik ringan yang bisa dilakukan di mana saja untuk melepas ketegangan otot dan pikiran.</p>
                <div class="steps">
                    <strong>Pilihan Aktivitas (10-15 menit):</strong><br>
                    🚶 Jalan kaki di sekitar kampus/kos<br>
                    🧘 Yoga ringan atau peregangan<br>
                    💃 Menari bebas dengan musik favorit<br>
                    🤸 Jumping jacks & peregangan leher<br>
                    🌳 Berjemur pagi 10 menit
                </div>
                <p style="margin-top:0.7rem;font-size:0.82rem;color:#82C9A1;">
                    ✅ Melepaskan endorfin & meningkatkan mood
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col6:
        st.markdown(
            """
            <div class="coping-card">
                <div class="card-icon">📵</div>
                <h3>Digital Detox Mini</h3>
                <p>Istirahat dari layar dan notifikasi untuk memulihkan energi mental dan mengurangi overstimulation.</p>
                <div class="steps">
                    <strong>Panduan Detox:</strong><br>
                    ⏰ Pilih waktu 30-60 menit tanpa gadget<br>
                    🔕 Matikan semua notifikasi<br>
                    📖 Ganti scrolling dengan baca buku/corat-coret<br>
                    🌿 Habiskan waktu di luar ruangan<br>
                    ☕ Nikmati secangkir teh tanpa distraksi
                </div>
                <p style="margin-top:0.7rem;font-size:0.82rem;color:#82C9A1;">
                    ✅ Mengurangi kecemasan digital & information overload
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Motivational Quote ──
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card" style="text-align:center;padding:2rem;">
            <p style="font-size:1.5rem;margin-bottom:0.5rem;">🌸</p>
            <p style="font-size:1.05rem;font-style:italic;color:#4A4A6A;margin:0;">
                "You don't have to be positive all the time. It's perfectly okay to feel sad, 
                angry, annoyed, frustrated, scared, or anxious. Having feelings doesn't make 
                you a negative person. It makes you human."
            </p>
            <p style="font-size:0.85rem;color:#7B7B9E;margin-top:0.8rem;">— Lori Deschene</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="footer">
        🌿 <strong>OvercomeAI</strong> v1.0 — Dibuat dengan 💛 untuk kesehatan mental mahasiswa Indonesia<br>
        <span style="font-size:0.75rem;">⚠️ Aplikasi ini bukan pengganti konseling profesional. 
        Jika kamu membutuhkan bantuan segera, hubungi 119 ext. 8</span>
    </div>
    """,
    unsafe_allow_html=True,
)
