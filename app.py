import streamlit as st
import math

# ------------------ Styling CSS ------------------
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                          url("https://i.imgur.com/BSBUvyu.jpeg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }
    header[data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding-top: 1rem !important; }
    h1, h2, h3, h4, h5 { color: white !important; }
    label, .stMarkdown { color: white !important; }
    input[type="number"], input[type="text"] {
        color: black !important;
        background-color: rgba(255,255,255,0.9) !important;
        border-radius: 5px !important;
    }
    .custom-output {
        background-color: rgba(255, 255, 255, 0.9);
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
    .stButton button {
        background-color: #00ccff;
        color: black;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #0099cc;
        color: white;
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
    Yuk, manfaatkan ChemVerse sebagai sahabat belajar dan praktikum.
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
        Aplikasi ini dirancang untuk membantu dalam perhitungan mol, pH, pengenceran larutan, dan persentase konsentrasi dengan cepat dan akurat.
        """)

    elif tab == "🔍 Latar Belakang":
        st.markdown("""
        Di era Revolusi Industri 4.0, integrasi teknologi ke dalam dunia pendidikan dan laboratorium sangat penting.  
        ChemVerse hadir sebagai solusi untuk mempermudah dan mempercepat proses perhitungan kimia dasar secara digital.
        """)

    elif tab == "🎯 Tujuan":
        st.markdown("""
        - Mempermudah perhitungan kimia dasar.  
        - Meningkatkan pemahaman konsep mol, pH, pengenceran, dan konsentrasi.  
        - Menghemat waktu dalam kegiatan laboratorium.
        - Menyediakan alat bantu praktis dan responsif untuk pelajar dan mahasiswa.
        """)

    elif tab == "⚙️ Fitur":
        st.markdown("""
        1. Perhitungan Molaritas  
        2. Perhitungan pH  
        3. Pengenceran Larutan  
        4. Perhitungan Persentase Konsentrasi
        """)

    elif tab == "🌟 Manfaat":
        st.markdown("""
        - Membantu proses belajar dan praktikum secara mandiri maupun kelompok.  
        - Menurunkan tingkat kesalahan hitung manual, sehingga hasil perhitungan yang didapat akurat.  
        - Menghemat waktu dalam analisis kimia.  
        """)

# ------------------ Hitung Mol ------------------
elif menu == "🧪 Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("*Rumus:* mol = massa / Mr")

    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0, step=0.1, key="mol_massa")
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.01, step=0.1, key="mol_mr")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if massa == 0 or mr == 0:
            st.warning("⚠️ Mohon masukkan nilai massa dan Mr yang valid.")
        else:
            mol = massa / mr
            st.markdown(f"<div class='custom-output'>Mol = {mol:.4f} mol</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        for key in ["mol_massa", "mol_mr"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Hitung pH ------------------
elif menu == "🧫 Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("*Rumus:* pH = -log[H⁺]")

    h_conc = st.number_input("Konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f", key="ph_hconc")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if h_conc <= 0:
            st.warning("⚠️ Masukkan konsentrasi ion H⁺ yang lebih besar dari 0.")
        else:
            ph = -math.log10(h_conc)
            st.markdown(f"<div class='custom-output'>pH = {ph:.2f}</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        if "ph_hconc" in st.session_state:
            del st.session_state["ph_hconc"]
        st.rerun()

# ------------------ Pengenceran ------------------
elif menu == "💧 Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("*Rumus:* M₁V₁ = M₂V₂")

    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0, key="peng_m1")
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0, key="peng_v1")
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.01, key="peng_m2")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if m1 == 0 or v1 == 0 or m2 == 0:
            st.warning("⚠️ Semua nilai harus diisi dengan benar.")
        else:
            v2 = (m1 * v1) / m2
            st.markdown(f"<div class='custom-output'>Volume akhir (V₂) = {v2:.2f} mL</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        for key in ["peng_m1", "peng_v1", "peng_m2"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Persentase Konsentrasi ------------------
elif menu == "📊 Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    st.markdown("*Rumus:* (massa zat / massa larutan) × 100%")

    massa_zat = st.number_input("Massa zat (gram)", min_value=0.0, key="persen_mz")
    massa_larutan = st.number_input("Massa larutan total (gram)", min_value=0.01, key="persen_ml")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if massa_zat == 0 or massa_larutan == 0:
            st.warning("⚠️ Masukkan nilai massa zat dan massa larutan yang valid.")
        elif massa_zat > massa_larutan:
            st.warning("❌ Massa zat tidak boleh lebih besar dari massa larutan.")
        else:
            persen = (massa_zat / massa_larutan) * 100
            st.markdown(f"<div class='custom-output'>Persentase Konsentrasi = {persen:.2f}%</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        for key in ["persen_mz", "persen_ml"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Footer ------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: white;'>© 2025 ChemVerse | Dibuat oleh Kelompok 3</div>",
    unsafe_allow_html=True
)
