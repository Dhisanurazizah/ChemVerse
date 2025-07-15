import streamlit as st
import math

# ------------------ Styling CSS ------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                          url("https://i.ibb.co/ZSHwBCr/lab-bg.jpg"); /* Ganti dengan direct link gambarmu */
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }

    .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
        color: #ffffff;
    }

    [data-testid="stSidebar"] {
        background-image: linear-gradient(120deg, #d4fc79 0%, #96e6a1 100%);
        color: black;
    }

    .stNumberInput > div > div {
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    ul {
        margin-left: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Judul Aplikasi ------------------
st.title("🧪 ChemVerse (Kalkulator Kimia Digital)")

# ------------------ Sidebar Navigasi ------------------
menu = st.sidebar.selectbox(
    "📘 Menu Navigasi",
    [
        "Beranda",
        "Hitung Mol",
        "Hitung pH",
        "Pengenceran Larutan",
        "Persentase Konsentrasi",
        "Tentang Kami",
        "Tentang Aplikasi"
    ]
)

# ------------------ Halaman Beranda ------------------
if menu == "Beranda":
    st.header("Selamat datang di ChemVerse - Aplikasi Kimia Pintar 🎉")
    st.markdown("""
    Bersama aplikasi ini, mari wujudkan perhitungan kimia yang cepat, cerdas, dan praktis.  
    Saatnya mahasiswa bergerak lebih digital di era Revolusi 4.0!  
    **ChemVerse** menggabungkan teknologi dan pendidikan untuk membawamu ke level baru dalam memahami dunia kimia.  
    """)

# ------------------ Hitung Mol ------------------
elif menu == "Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("Rumus: `mol = massa / Mr`")
    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0)
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.0)
    if massa > 0 and mr > 0:
        mol = massa / mr
        st.success(f"Jumlah mol = {mol:.4f} mol")

# ------------------ Hitung pH ------------------
elif menu == "Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("Rumus: `pH = -log[H⁺]`")
    h_concentration = st.number_input("Masukkan konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f")
    if h_concentration > 0:
        ph = -math.log10(h_concentration)
        st.success(f"pH = {ph:.2f}")
        if ph < 7:
            st.info("Larutan bersifat Asam")
        elif ph == 7:
            st.info("Larutan bersifat Netral")
        else:
            st.info("Larutan bersifat Basa")

# ------------------ Pengenceran Larutan ------------------
elif menu == "Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("Rumus: `M₁V₁ = M₂V₂`")
    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0)
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0)
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.0)
    if m1 > 0 and m2 > 0:
        v2 = (m1 * v1) / m2
        st.success(f"Volume akhir (V₂) = {v2:.2f} mL")

# ------------------ Persentase Konsentrasi ------------------
elif menu == "Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    st.markdown("Rumus: `(massa zat / massa larutan) × 100%`")
    massa_zat = st.number_input("Massa zat terlarut (gram)", min_value=0.0)
    massa_larutan = st.number_input("Massa larutan total (gram)", min_value=0.0)
    if massa_zat > 0 and massa_larutan > 0:
        if massa_zat <= massa_larutan:
            persen = (massa_zat / massa_larutan) * 100
            st.success(f"Persentase Konsentrasi = {persen:.2f}%")
        else:
            st.error("❌ Massa zat tidak boleh lebih besar dari massa larutan.")

# ------------------ Tentang Kami ------------------
elif menu == "Tentang Kami":
    st.subheader("👥 Tentang Kami")
    st.markdown("""
    **TIM PENYUSUN**  
    *Kelompok 3 - 1 D*  
    1. Andrian Prayugo (2460324)  
    2. Dhisa Nur Azizah (2460358)  
    3. Marcelino David Mangatur (2460411)  
    4. Nabil Syafiq Suhendar (2460446)  
    5. Sefina Zahra Pangestika (2460515)
    """)

# ------------------ Tentang Aplikasi ------------------
elif menu == "Tentang Aplikasi":
    st.subheader("📘 Tentang Aplikasi")
    st.markdown("""
    ChemVerse adalah aplikasi kalkulator kimia digital yang interaktif, inovatif, dan cerdas.  
    Dirancang untuk mempermudah perhitungan kimia dan eksplorasi konsep kimia secara praktis.  
    """)

# ------------------ Footer ------------------
st.markdown("<hr style='border-top: 1px solid white;'>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: white;'>© 2025 ChemVerse | Dibuat untuk Pembelajaran</div>",
    unsafe_allow_html=True
)
