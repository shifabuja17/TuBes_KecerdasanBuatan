import streamlit as st

def apply_custom_css():
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