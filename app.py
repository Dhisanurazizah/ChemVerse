import streamlit as st
import math

# ------------------ Styling CSS ------------------
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)),
                          url("https://i.imgur.com/BSBUvyu.jpeg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: black;
    }
    header[data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding-top: 1rem !important; }

    .stApp h1, h2, h3, h4, h5 { color: black !important; }
    .stMarkdown, label { color: black !important; }

    section[data-testid="stSidebar"] label {
        color: black !important;
        font-weight: bold;
    }

    input[type="number"], input[type="text"] {
        color: black !important;
        background-color: rgba(255,255,255,0.85) !important;
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
    </style>
""", unsafe_allow_html=True)

# ------------------ Judul Aplikasi ------------------
st.title("🧪 ChemVerse (Kalkulator Kimia Digital)")

# ------------------ Menu Navigasi ------------------
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
    st.header("Selamat datang di ChemVerse 🎉")
    st.markdown("""
    Bersama aplikasi ini, mari wujudkan perhitungan kimia yang cepat, cerdas, dan praktis.  
    Aplikasi ini dirancang untuk mendukung aktivitas perkuliahan, praktikum, dan penelitian kimiamu.  
    Yuk, manfaatkan ChemVerse sebagai sahabat belajar dan praktikummu!
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
    tab = st.selectbox("Pilih Penjelasan", [
        "🧪 Deskripsi",
        "🔍 Latar Belakang",
        "🎯 Tujuan",
        "⚙️ Fitur",
        "🌟 Manfaat"
    ])

    if tab == "🧪 Deskripsi":
        st.markdown("""
        ChemVerse adalah aplikasi kalkulator kimia digital yang interaktif, inovatif, dan cerdas.  
        Aplikasi ini dirancang untuk membantu dalam perhitungan mol, pH, pengenceran larutan, dan persentase konsentrasi secara cepat dan akurat.
        """)

    elif tab == "🔍 Latar Belakang":
        st.markdown("""
        Di era Revolusi Industri 4.0, integrasi teknologi ke dalam dunia pendidikan dan laboratorium sangat penting.  
        ChemVerse hadir sebagai solusi untuk mempermudah dan mempercepat proses perhitungan kimia dasar secara digital.
        """)

    elif tab == "🎯 Tujuan":
        st.markdown("""
        - Mempermudah perhitungan kimia dasar  
        - Meningkatkan pemahaman konsep mol, pH, pengenceran, dan konsentrasi  
        - Menghemat waktu dalam kegiatan laboratorium  
        - Menyediakan alat bantu praktis dan responsif untuk pelajar dan mahasiswa  
        - Mendukung pelajar, dosen, dan profesional industri memahami dan menerapkan konsep kimia secara efisien dan intuitif
        """)

    elif tab == "⚙️ Fitur":
        st.markdown("""
        1. Perhitungan Molaritas  
        2. Perhitungan pH  
        3. Pengenceran Larutan  
        4. Persentase Konsentrasi  
        """)

    elif tab == "🌟 Manfaat":
        st.markdown("""
        - Membantu proses belajar dan praktikum secara mandiri maupun kelompok  
        - Mengurangi kesalahan hitung manual  
        - Menghemat waktu dalam analisis kimia  
        - Mendorong penggunaan teknologi digital di bidang pendidikan dan industri kimia  
        """)

# ------------------ Hitung Mol ------------------
elif menu == "🧪 Hitung Mol":
    st.header("🔹 Hitung Mol")
    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.01)
    if massa > 0 and mr > 0:
        mol = massa / mr
        st.markdown(f"<div class='custom-output'>Mol = {mol:.4f} mol</div>", unsafe_allow_html=True)

# ------------------ Hitung pH ------------------
elif menu == "🧫 Hitung pH":
    st.header("🔹 Hitung pH")
    h_conc = st.number_input("Konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f")
    if h_conc > 0:
        ph = -math.log10(h_conc)
        st.markdown(f"<div class='custom-output'>pH = {ph:.2f}</div>", unsafe_allow_html=True)

# ------------------ Pengenceran Larutan ------------------
elif menu == "💧 Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0)
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0)
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.01)
    if m1 > 0 and v1 > 0 and m2 > 0:
        v2 = (m1 * v1) / m2
        st.markdown(f"<div class='custom-output'>Volume akhir (V₂) = {v2:.2f} mL</div>", unsafe_allow_html=True)

# ------------------ Persentase Konsentrasi ------------------
elif menu == "📊 Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    massa_zat = st.number_input("Massa zat (gram)", min_value=0.0)
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
    "<div style='text-align: center; color: black;'>© 2025 ChemVerse | Dibuat oleh Kelompok 3</div>",
    unsafe_allow_html=True
)
