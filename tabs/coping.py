import streamlit as st
import streamlit.components.v1 as components

def render_coping():
    st.markdown("## 🧭 Panduan Coping & Self-Care")
    st.markdown(
        '<p style="color:#7B7B9E;">Temukan teknik-teknik yang terbukti efektif untuk mengelola stres dan burnout.</p>',
        unsafe_allow_html=True,
    )

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

        with st.expander("🫁 Buka Latihan Pernapasan Kotak"):
            components.html(
                """
                <div style="font-family: 'Inter', sans-serif; text-align: center; padding: 15px; background: #ffffff; border-radius: 12px; border: 1px solid #E8E0F0; min-height: 280px; display: flex; flex-direction: column; align-items: center; justify-content: space-between; overflow: hidden;">
                    <div id="cycle-text" style="font-size: 0.95rem; color: #7B7B9E; font-weight: 500;">Siklus: 0 / 6</div>
                    <div style="height: 160px; display: flex; align-items: center; justify-content: center; position: relative;">
                        <div id="breath-circle" style="width: 100px; height: 100px; background: #E8E0F0; border-radius: 50%; display: flex; flex-direction: column; justify-content: center; align-items: center; transition: all 4s linear; box-shadow: 0 4px 15px rgba(155, 142, 196, 0.3);">
                            <div id="time-sec" style="font-size: 2rem; font-weight: 700; color: #4A4A6A;">4</div>
                        </div>
                    </div>
                    <div id="phase-text" style="font-size: 1.1rem; font-weight: 600; color: #9B8EC4; margin-bottom: 10px;">Siap Latihan</div>
                    <button onclick="toggleBreathing()" id="btn-breath" style="background: #7C9CBF; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 1rem; width: 160px; transition: background 0.3s;">Mulai Latihan</button>
                </div>
                <script>
                    let timerId;
                    let isBreathing = false;
                    let phaseIndex = 0; 
                    let cycleCount = 1;
                    let secondsLeft = 4;
                    const phases = [
                        { name: "Tarik Napas 🌬️", color: "#D4EDDA", scale: "scale(1.5)" }, 
                        { name: "Tahan Napas ⏸️", color: "#FDDCB5", scale: "scale(1.5)" }, 
                        { name: "Buang Napas 🌊", color: "#D6EAF8", scale: "scale(1)" },   
                        { name: "Tahan Kosong ⏸️", color: "#E8E0F0", scale: "scale(1)" }   
                    ];

                    function toggleBreathing() {
                        let btn = document.getElementById('btn-breath');
                        if (isBreathing) {
                            clearInterval(timerId);
                            isBreathing = false;
                            btn.innerText = "Mulai Latihan";
                            btn.style.background = "#7C9CBF";
                            btn.style.color = "white";
                            resetUI();
                        } else {
                            isBreathing = true;
                            btn.innerText = "Berhenti";
                            btn.style.background = "#FADBD8";
                            btn.style.color = "#922B21";
                            cycleCount = 1;
                            phaseIndex = 0;
                            secondsLeft = 4;
                            applyPhaseUI();
                            
                            timerId = setInterval(() => {
                                secondsLeft--;
                                if (secondsLeft <= 0) {
                                    phaseIndex++; 
                                    if (phaseIndex > 3) {
                                        phaseIndex = 0; 
                                        cycleCount++;
                                        if (cycleCount > 6) {
                                            clearInterval(timerId);
                                            isBreathing = false;
                                            btn.innerText = "Mulai Latihan";
                                            btn.style.background = "#7C9CBF";
                                            btn.style.color = "white";
                                            let audio = new Audio('https://actions.google.com/sounds/v1/alarms/beep_short.ogg');
                                            audio.play();
                                            setTimeout(() => {
                                                alert("Bagus sekali! Latihan pernapasan 6 siklus telah selesai 🌱. Semoga kamu merasa lebih tenang.");
                                                resetUI();
                                            }, 500);
                                            return;
                                        }
                                    }
                                    secondsLeft = 4;
                                    applyPhaseUI();
                                }
                                document.getElementById('time-sec').innerText = secondsLeft;
                            }, 1000);
                        }
                    }

                    function applyPhaseUI() {
                        document.getElementById('cycle-text').innerText = `Siklus: ${cycleCount} / 6`;
                        document.getElementById('phase-text').innerText = phases[phaseIndex].name;
                        document.getElementById('time-sec').innerText = secondsLeft;
                        let circle = document.getElementById('breath-circle');
                        circle.style.backgroundColor = phases[phaseIndex].color;
                        circle.style.transform = phases[phaseIndex].scale;
                    }

                    function resetUI() {
                        document.getElementById('cycle-text').innerText = "Siklus: 0 / 6";
                        document.getElementById('phase-text').innerText = "Siap Latihan";
                        document.getElementById('time-sec').innerText = "4";
                        let circle = document.getElementById('breath-circle');
                        circle.style.transform = "scale(1)";
                        circle.style.backgroundColor = "#E8E0F0";
                    }
                </script>
                """,
                height=300,
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
        
        with st.expander("⏱️ Buka Timer Pomodoro"):
            components.html(
                """
                <div style="font-family: 'Inter', sans-serif; text-align: center; padding: 15px; background: #ffffff; border-radius: 12px; border: 1px solid #E8E0F0;">
                    <div id="phase" style="font-size: 1.2rem; font-weight: 700; color: #9B8EC4; margin-bottom: 5px;">🎯 Siap Fokus</div>
                    <div id="cycle" style="font-size: 0.9rem; color: #7B7B9E; margin-bottom: 10px;">Siklus: 0 / 4</div>
                    <h2 id="time" style="font-size: 3.2rem; color: #4A4A6A; margin: 0;">25:00</h2>
                    <div style="margin-top: 15px; display: flex; justify-content: center; gap: 10px;">
                        <button onclick="toggleTimer()" id="btn-toggle" style="background: #9B8EC4; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 1rem; width: 140px;">Mulai Siklus</button>
                        <button onclick="resetTimer()" style="background: #FADBD8; color: #922B21; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 1rem;">Reset</button>
                    </div>
                </div>
                <script>
                    let timer;
                    let timeLeft = 25 * 60; 
                    let isRunning = false;
                    let currentPhase = 'Fokus'; 
                    let cycleCount = 0;

                    function updateDisplay() {
                        let m = Math.floor(timeLeft / 60).toString().padStart(2, '0');
                        let s = (timeLeft % 60).toString().padStart(2, '0');
                        document.getElementById('time').innerText = m + ":" + s;
                        let phaseText = currentPhase === 'Fokus' ? '🎯 Fase Fokus' : (currentPhase === 'Jeda Pendek' ? '☕ Jeda Pendek' : '🛋️ Jeda Panjang');
                        document.getElementById('phase').innerText = phaseText;
                        document.getElementById('cycle').innerText = `Siklus: ${cycleCount} / 4`;
                    }

                    function toggleTimer() {
                        if (isRunning) {
                            clearInterval(timer);
                            isRunning = false;
                            document.getElementById('btn-toggle').innerText = "Lanjut";
                            document.getElementById('btn-toggle').style.background = "#82C9A1"; 
                        } else {
                            isRunning = true;
                            document.getElementById('btn-toggle').innerText = "Jeda (Pause)";
                            document.getElementById('btn-toggle').style.background = "#FDCB6E"; 
                            timer = setInterval(() => {
                                if (timeLeft > 0) {
                                    timeLeft--;
                                    updateDisplay();
                                } else {
                                    handlePhaseSwitch();
                                }
                            }, 1000);
                        }
                    }

                    function handlePhaseSwitch() {
                        let audio = new Audio('https://actions.google.com/sounds/v1/alarms/beep_short.ogg');
                        audio.play();

                        if (currentPhase === 'Fokus') {
                            cycleCount++;
                            if (cycleCount >= 4) {
                                currentPhase = 'Jeda Panjang';
                                timeLeft = 15 * 60; 
                                cycleCount = 0; 
                                alert("Kerja bagus! 4 siklus telah selesai. Nikmati istirahat panjang 15 menit 🌱");
                            } else {
                                currentPhase = 'Jeda Pendek';
                                timeLeft = 5 * 60; 
                                alert("Waktu fokus habis! Silakan istirahat sejenak 5 menit ☕");
                            }
                        } else {
                            currentPhase = 'Fokus';
                            timeLeft = 25 * 60; 
                            alert("Waktu istirahat selesai! Yuk kembali fokus 25 menit 🎯");
                        }
                        updateDisplay();
                    }

                    function resetTimer() {
                        clearInterval(timer);
                        isRunning = false;
                        currentPhase = 'Fokus';
                        cycleCount = 0;
                        timeLeft = 25 * 60;
                        document.getElementById('btn-toggle').innerText = "Mulai Siklus";
                        document.getElementById('btn-toggle').style.background = "#9B8EC4";
                        updateDisplay();
                    }
                    
                    updateDisplay();
                </script>
                """,
                height=260,
            )

    st.markdown("<br>", unsafe_allow_html=True)

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