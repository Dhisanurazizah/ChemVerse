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

    .stAlert-success {
        background-color: rgba(0, 128, 0, 0.7) !important;
        color: white !important;
        font-weight: bold;
    }

    .stAlert-danger {
        background-color: rgba(255, 0, 0, 0.6) !important;
        color: white !important;
        font-weight: bold;
    }

    [data-testid="stSidebar"] {
        background-image: linear-gradient(135deg, #cceeff 0%, #99ccff 100%);
        color: black;
    }

    section[data-testid="stSidebar"] label {
        color: black !important;
        font-weight: bold;
    }

    ul {
        margin-left: 20px;
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

# ------------------ Hitung Mol ------------------
elif menu == "🧪 Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("**Rumus:** `mol = massa / Mr`")

    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.01)

    if massa > 0 and mr > 0:
        mol = massa / mr
        st.success(f"Jumlah mol = {mol:.4f} mol")

# ------------------ Hitung pH ------------------
elif menu == "🧫 Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("**Rumus:** `pH = -log[H⁺]`")

    h_concentration = st.number_input("Masukkan konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f")

    if h_concentration > 0:
        ph = -math.log10(h_concentration)
        st.success(f"pH = {ph:.2f}")

# ------------------ Pengenceran Larutan ------------------
elif menu == "💧 Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("**Rumus:** `M₁V₁ = M₂V₂`")

    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0)
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0)
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.01)

    if m1 > 0 and v1 > 0 and m2 > 0:
        v2 = (m1 * v1) / m2
        st.success(f"Volume akhir (V₂) = {v2:.2f} mL")

# ------------------ Persentase Konsentrasi ------------------
elif menu == "📊 Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    st.markdown("**Rumus:** `(massa zat / massa larutan) × 100%`")

    massa_zat = st.number_input("Massa zat terlarut (gram)", min_value=0.0)
    massa_larutan = st.number_input("Massa larutan total (gram)", min_value=0.01)

    if massa_zat > 0 and massa_larutan > 0:
        if massa_zat <= massa_larutan:
            persen = (massa_zat / massa_larutan) * 100
            st.success(f"Persentase Konsentrasi = {persen:.2f}%")
        else:
            st.error("❌ Massa zat tidak boleh lebih besar dari massa larutan.")

# ------------------ Footer ------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: white;'>© 2025 ChemVerse | Dibuat untuk Pembelajaran</div>",
    unsafe_allow_html=True
)
