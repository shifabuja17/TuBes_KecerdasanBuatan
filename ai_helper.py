import streamlit as st
import google.generativeai as genai

SYSTEM_INSTRUCTION = """
Kamu adalah "AmigoAI", seorang konselor sebaya (peer counselor) yang empatik, hangat, dan suportif. 
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

        gemini_history = []
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model"
            gemini_history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=gemini_history)
        response = chat.send_message(user_message)
        return response.text

    except Exception as e:
        return f"❌ Maaf, terjadi kesalahan: {str(e)}"