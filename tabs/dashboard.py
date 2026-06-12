import streamlit as st
import pandas as pd

def render_dashboard():
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