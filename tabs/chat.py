import streamlit as st
from ai_helper import check_self_harm, show_emergency_contacts, get_gemini_response

def render_chat():
    st.markdown("## 💬 Curhat Sama AI Buddy")
    st.markdown(
        '<p style="color:#7B7B9E;">Ceritakan apa yang kamu rasakan. Aku di sini untuk mendengarkan tanpa menghakimi 🌱</p>',
        unsafe_allow_html=True,
    )

    chat_container = st.container()
    with chat_container:
        if not st.session_state.chat_history:
            st.markdown(
                """
                <div class="glass-card" style="text-align:center;padding:2.5rem;">
                    <p style="font-size:2.5rem;margin-bottom:0.5rem;">🌿</p>
                    <p style="font-size:1.05rem;color:#4A4A6A;font-weight:500;">
                        Hai! Aku AmigoAI, teman curhatmu.
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

    user_input = st.chat_input("Tulis curhatanmu di sini...", key="chat_input")

    if user_input:
        if check_self_harm(user_input):
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            safety_response = (
                "Aku sangat khawatir dengan apa yang kamu ceritakan. "
                "Perasaanmu valid, dan kamu tidak sendirian. "
                "Tolong hubungi layanan bantuan darurat di bawah ini. "
                "Mereka terlatih untuk membantu dan tersedia 24/7. 💛"
            )
            st.session_state.chat_history.append({"role": "assistant", "content": safety_response})
            show_emergency_contacts()
            st.rerun()
        else:
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            with st.spinner("🌿 AmigoAI sedang mengetik..."):
                ai_response = get_gemini_response(user_input, st.session_state.chat_history[:-1])

            if check_self_harm(ai_response):
                show_emergency_contacts()

            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            st.rerun()

    if st.session_state.chat_history:
        col_clear, _ = st.columns([1, 3])
        with col_clear:
            if st.button("🗑️ Hapus Riwayat Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()