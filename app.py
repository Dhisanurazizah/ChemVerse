import streamlit as st
import math

# ------------------ Styling CSS ------------------
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
                          url("https://i.imgur.com/BSBUvyu.jpeg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
        font-family: 'Arial', sans-serif;
    }
    header[data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding-top: 1rem !important; }
    .stApp h1, h2, h3, h4, h5 { color: white !important; }
    label, .stMarkdown { color: white !important; }
    input[type="number"], input[type="text"] {
        color: black !important;
        background-color: rgba(255,255,255,0.9) !important;
        border-radius: 8px !important;
        padding: 6px !important;
        border: 1px solid #00ccff !important;
    }
    .custom-output {
        background-color: rgba(255, 255, 255, 0.9);
        color: #003366;
        font-weight: bold;
        padding: 12px;
        border-radius: 12px;
        border: 2px solid #00ccff;
        text-align: center;
        margin-top: 12px;
    }
    .reset-btn {
        background-color: #ff6666 !important;
        color: white !important;
        border-radius: 8px !important;
        margin-top: 10px;
    }
    [data-testid="stSidebar"] {
        background-image: linear-gradient(135deg, #cceeff 0%, #99ccff 100%);
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Judul ------------------
st.title("🧪 ChemVerse (Kalkulator Kimia Digital)")

# ------------------ Navigasi Sidebar ------------------
menu = st.sidebar.selectbox("📘 Menu Navigasi", [
    "🏠 Beranda",
    "👥 Tentang Kami",
    "ℹ️ Tentang Aplikasi",
    "🧪 Hitung Mol",
    "🧫 Hitung pH",
    "💧 Pengenceran Larutan",
    "📊 Persentase Konsentrasi"
])

# ------------------ Halaman Beranda ------------------
if menu == "🏠 Beranda":
    st.header("Selamat datang di ChemVerse - Aplikasi Kimia Pintar 🎉")
    st.markdown("""
    Bersama aplikasi ini, mari wujudkan perhitungan kimia yang cepat, cerdas, dan praktis.  
    Aplikasi ini dirancang untuk mendukung aktivitas perkuliahan, praktikum, dan penelitian kimiamu.  
    Yuk, manfaatkan ChemVerse sebagai sahabat belajar dan praktikum kamu!
    """)

# ------------------ Tentang Kami ------------------
elif menu == "👥 Tentang Kami":
    st.subheader("👥 Tentang Kami")
    st.markdown("""
    **Kelompok 3 - 1D**  
    1. Andrian Prayugo (2460324)  
    2. Dhisa Nur Azizah (2460358)  
    3. Marcelino David Mangatur (2460411)  
    4. Nabil Syafiq Suhendar (2460446)  
    5. Sefina Zahra Pangestika (2460515)
    """)

# ------------------ Tentang Aplikasi ------------------
elif menu == "ℹ️ Tentang Aplikasi":
    st.subheader("📘 Tentang Aplikasi - ChemVerse")
    tab = st.tabs(["🧪 Deskripsi", "🔍 Latar Belakang", "🎯 Tujuan", "⚙️ Fitur", "🌟 Manfaat"])

    with tab[0]:
        st.markdown("""
        ChemVerse adalah aplikasi kalkulator kimia digital yang interaktif, inovatif, dan cerdas.  
        Dirancang untuk membantu perhitungan mol, pH, pengenceran larutan, dan persentase konsentrasi secara cepat dan akurat.
        """)

    with tab[1]:
        st.markdown("""
        Di era Revolusi Industri 4.0, integrasi teknologi ke dalam pendidikan dan laboratorium sangat penting.  
        ChemVerse hadir sebagai solusi untuk mempercepat perhitungan kimia dasar secara digital.
        """)

    with tab[2]:
        st.markdown("""
        - Mempermudah perhitungan kimia dasar  
        - Meningkatkan pemahaman konsep mol, pH, pengenceran, dan konsentrasi  
        - Menghemat waktu dalam kegiatan laboratorium  
        - Menyediakan alat bantu praktis dan responsif untuk pelajar dan mahasiswa  
        """)

    with tab[3]:
        st.markdown("""
        1. Perhitungan Molaritas  
        2. Perhitungan pH  
        3. Pengenceran Larutan  
        4. Perhitungan Persentase Konsentrasi  
        """)

    with tab[4]:
        st.markdown("""
        - Membantu proses belajar dan praktikum mandiri maupun kelompok  
        - Menurunkan tingkat kesalahan hitung manual  
        - Menghemat waktu dalam analisis kimia  
        - Mendorong adaptasi teknologi digital di pendidikan dan industri  
        """)

# ------------------ Hitung Mol ------------------
elif menu == "🧪 Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("*Rumus:* mol = massa / Mr")
    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0, format="%.4f")
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.01, format="%.4f")
    if st.button("Hitung"):
        if massa == 0 or mr == 0:
            st.warning("⚠️ Massa dan Mr harus lebih besar dari 0.")
        else:
            mol = massa / mr
            st.markdown(f"<div class='custom-output'>Mol = {mol:.4f} mol</div>", unsafe_allow_html=True)
    st.button("Reset", type="primary", key="reset_mol")

# ------------------ Hitung pH ------------------
elif menu == "🧫 Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("*Rumus:* pH = -log[H⁺]")
    h_conc = st.number_input("Konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f")
    if st.button("Hitung"):
        if h_conc <= 0:
            st.warning("⚠️ Konsentrasi H⁺ harus lebih besar dari 0.")
        else:
            ph = -math.log10(h_conc)
            st.markdown(f"<div class='custom-output'>pH = {ph:.2f}</div>", unsafe_allow_html=True)
    st.button("Reset", type="primary", key="reset_ph")

# ------------------ Pengenceran ------------------
elif menu == "💧 Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("*Rumus:* M₁V₁ = M₂V₂")
    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0, format="%.4f")
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0, format="%.4f")
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.01, format="%.4f")
    if st.button("Hitung"):
        if m1 == 0 or v1 == 0 or m2 == 0:
            st.warning("⚠️ Semua input harus lebih besar dari 0.")
        else:
            v2 = (m1 * v1) / m2
            st.markdown(f"<div class='custom-output'>Volume akhir (V₂) = {v2:.2f} mL</div>", unsafe_allow_html=True)
    st.button("Reset", type="primary", key="reset_pengenceran")

# ------------------ Persentase Konsentrasi ------------------
elif menu == "📊 Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    st.markdown("*Rumus:* (massa zat / massa larutan) × 100%")
    massa_zat = st.number_input("Massa zat (gram)", min_value=0.0, format="%.4f")
    massa_larutan = st.number_input("Massa larutan total (gram)", min_value=0.01, format="%.4f")
    if st.button("Hitung"):
        if massa_zat == 0 or massa_larutan == 0:
            st.warning("⚠️ Massa zat dan larutan harus lebih besar dari 0.")
        elif massa_zat > massa_larutan:
            st.error("❌ Massa zat tidak boleh lebih besar dari massa larutan.")
        else:
            persen = (massa_zat / massa_larutan) * 100
            st.markdown(f"<div class='custom-output'>Persentase Konsentrasi = {persen:.2f}%</div>", unsafe_allow_html=True)
    st.button("Reset", type="primary", key="reset_persen")

# ------------------ Footer ------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: white;'>© 2025 ChemVerse | Dibuat oleh Kelompok 3</div>",
    unsafe_allow_html=True
)
