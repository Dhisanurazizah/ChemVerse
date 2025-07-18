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
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    .block-container {
        padding-top: 1rem !important;
    }

    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: white !important;
    }

    label, .stTextInput label, .stNumberInput label, .stMarkdown {
        color: white !important;
    }

    input[type="number"], input[type="text"] {
        color: black !important;
        background-color: rgba(255, 255, 255, 0.85) !important;
        border: 1px solid #ccc !important;
        border-radius: 5px !important;
    }

    .custom-output {
        background-color: rgba(255, 255, 255, 0.85);
        color: black;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #00ccff;
        text-align: center;
        margin-top: 10px;
    }

    [data-testid="stSidebar"] {
        background-image: linear-gradient(135deg, #cceeff 0%, #99ccff 100%);
        color: black;
    }

    section[data-testid="stSidebar"] label {
        color: black !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Judul Aplikasi ------------------
st.title("🧪 ChemVerse (Kalkulator Kimia Digital)")

# ------------------ Sidebar Navigasi ------------------
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
    Yuk, manfaatkan ChemVerse sebagai sahabat belajar dan praktikummu!
    """)

# ------------------ Tentang Kami ------------------
elif menu == "👥 Tentang Kami":
    st.subheader("👥 Tentang Kami")
    st.markdown("""
    **Kelompok 3 - 1 D**  
    1. Andrian Prayugo (2460324)  
    2. Dhisa Nur Azizah (2460358)  
    3. Marcelino David Mangatur (2460411)  
    4. Nabil Syafiq Suhendar (2460446)  
    5. Sefina Zahra Pangestika (2460515)
    """)

# ------------------ Tentang Aplikasi ------------------
elif menu == "ℹ️ Tentang Aplikasi":
    st.subheader("📘 Tentang Aplikasi")
    st.markdown("""
    **ChemVerse** adalah aplikasi kalkulator kimia digital interaktif.  
    Dirancang untuk membantu pelajar dan mahasiswa dalam menghitung:
    - Mol
    - pH
    - Pengenceran larutan
    - Persentase konsentrasi  

    Dengan antarmuka sederhana dan dukungan teknologi digital, ChemVerse mempermudah pekerjaan laboratorium dan tugas kuliah kimia.
    """)

    # Tambahan versi lengkap
    st.markdown("""
    ---
    ### 🧪 ChemVerse  
    *“Your Chemistry Universe in One App”*

    ### 📌 Deskripsi
    ChemVerse adalah aplikasi kalkulator kimia digital yang interaktif, inovatif, dan cerdas.  
    Dirancang untuk mempermudah perhitungan kimia sekaligus menjadi ruang eksplorasi konsep kimia dalam satu ekosistem terintegrasi.

    ### 🔍 Latar Belakang
    Di era Revolusi Industri 4.0, integrasi teknologi dalam pendidikan dan industri kimia menjadi sebuah keharusan.  
    ChemVerse hadir untuk menjawab tantangan tersebut dengan menghadirkan solusi perhitungan kimia yang cepat, akurat, dan berbasis teknologi digital. 

    ### 🎯 Tujuan Aplikasi
    Aplikasi ini dibuat untuk:
    1. Mempermudah proses perhitungan kimia dasar.
    2. Meningkatkan pemahaman konsep mol, pH, pengenceran, dan konsentrasi.
    3. Menghemat waktu dalam kegiatan laboratorium.
    4. Menyediakan alat bantu praktis dan responsif untuk pelajar dan mahasiswa.
    5. Mendukung pelajar, mahasiswa, dosen, dan profesional industri dalam memahami dan mengaplikasikan konsep kimia secara efisien dan intuitif.

    ### ⚙️ Fitur Unggulan ChemVerse
    1. Perhitungan Molaritas
    2. Perhitungan pH
    3. Pengenceran Larutan
    4. Perhitungan Persentase Konsentrasi

    ### 🎯 Manfaat Aplikasi
    1. Membantu proses belajar dan praktikum secara mandiri maupun kelompok.
    2. Menurunkan tingkat kesalahan hitung manual, sehingga hasil perhitungan yang didapat akurat.
    3. Menghemat waktu dalam analisis kimia.
    4. Mendorong adaptasi teknologi digital di dunia pendidikan dan industri kimia.
    """)

# ------------------ Hitung Mol ------------------
elif menu == "🧪 Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("**Rumus:** `mol = massa / Mr`")

    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.01)

    if massa > 0 and mr > 0:
        mol = massa / mr
        st.markdown(f"<div class='custom-output'>Jumlah mol = {mol:.4f} mol</div>", unsafe_allow_html=True)

# ------------------ Hitung pH ------------------
elif menu == "🧫 Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("**Rumus:** `pH = -log[H⁺]`")

    h_conc = st.number_input("Masukkan konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f")

    if h_conc > 0:
        ph = -math.log10(h_conc)
        st.markdown(f"<div class='custom-output'>pH = {ph:.2f}</div>", unsafe_allow_html=True)

# ------------------ Pengenceran ------------------
elif menu == "💧 Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("**Rumus:** `M₁V₁ = M₂V₂`")

    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0)
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0)
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.01)

    if m1 > 0 and v1 > 0 and m2 > 0:
        v2 = (m1 * v1) / m2
        st.markdown(f"<div class='custom-output'>Volume akhir (V₂) = {v2:.2f} mL</div>", unsafe_allow_html=True)

# ------------------ Persentase Konsentrasi ------------------
elif menu == "📊 Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    st.markdown("**Rumus:** `(massa zat / massa larutan) × 100%`")

    massa_zat = st.number_input("Massa zat terlarut (gram)", min_value=0.0)
    massa_larutan = st.number_input("Massa larutan total (gram)", min_value=0.01)

    if massa_zat > 0 and massa_larutan > 0:
        if massa_zat <= massa_larutan:
            persen = (massa_zat / massa_larutan) * 100
            st.markdown(f"<div class='custom-output'>Persentase Konsentrasi = {persen:.2f}%</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='custom-output' style='border-color: red;'>❌ Massa zat tidak boleh lebih besar dari massa larutan.</div>", unsafe_allow_html=True)

# ------------------ Footer ------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: white;'>© 2025 ChemVerse | Dibuat untuk Pembelajaran</div>",
    unsafe_allow_html=True
)
