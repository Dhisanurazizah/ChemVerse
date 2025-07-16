import streamlit as st
import math

# ------------------ Styling CSS ------------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.ibb.co/9v4CWbz/chemistry-border-bg.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: black !important;
    }

    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp li, .stApp span, .stApp label, .stApp div {
        color: black !important;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #cceeff, #b3e0ff, #99ccff);
        color: #003366;
    }

    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stSelectbox span {
        color: #003366 !important;
        font-weight: bold;
    }

    [data-testid="stSidebar"] .stSelectbox div[role="combobox"] {
        background-color: #e6f7ff;
        color: #003366;
        border-radius: 5px;
        border: 1px solid #66b3ff;
    }

    .stNumberInput > div > div {
        border: 1px solid #99ccff;
        border-radius: 5px;
        color: black !important;
    }

    ul {
        margin-left: 20px;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
