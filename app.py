import streamlit as st  # Baris ini SANGAT PENTING agar 'st' dikenali
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

logo = Image.open("LogoMFoke.png")

#Konfigurasi Halaman (Favicon tetap pakai logo kecil)
st.set_page_config(page_title="MoodFood AI", page_icon=logo)

# --- 2. LETAKKAN CUSTOM CSS DI SINI (Tepat setelah set_page_config) ---
st.markdown("""
    <style>
    /* Mengubah warna background aplikasi agar lebih bersih */
    .stApp {
        background-color: #f9fbf9;
    }
    
    /* Mempercantik tombol 'Dapatkan Rekomendasi Menu' */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #2E7D32; /* Hijau Tua yang elegan */
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.6rem;
        transition: 0.3s;
    }
    
    /* Efek saat tombol disentuh kursor */
    .stButton>button:hover {
        background-color: #1B5E20;
        color: white;
        transform: scale(1.01);
    }

    /* Mempercantik Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }

    /* Mengatur style teks judul agar lebih profesional */
    h1 {
        color: #1B5E20 !important;
        font-family: 'Trebuchet MS', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 5])
with col1:
    st.image(logo, width=200) 

with col2:
    st.title("MoodFood AI")
st.markdown("---")

# Bagian Input User
st.subheader("Bagaimana perasaanmu saat ini?")
mood_pilihan = st.selectbox("Pilih Mood:", ["Sedih", "Stres", "Lelah", "Cemas", "Senang"])
tanya_tambahan = st.text_input("Ada Pertanyaan/keluhan lain? (Opsional)", placeholder="Misal: Saya kurang tidur...")

if st.button("Dapatkan Rekomendasi Menu"):
    model = genai.GenerativeModel('gemini-2.5-flash') # Menggunakan model terbaru
    
    prompt = f"Saya sedang merasa {mood_pilihan}. {tanya_tambahan}. Berikan 2 rekomendasi makanan dan minuman yang sehat secara ilmiah untuk mood ini, sertakan resep singkat dan fun fact nutrisinya."
    
    with st.spinner('AI sedang memikirkan menu terbaik...'):
        response = model.generate_content(prompt)
        st.success("Rekomendasi untukmu:")
        st.write(response.text)
        
        # Sisi Backend Sederhana: Menyimpan riwayat ke session
        if 'history' not in st.session_state:
            st.session_state['history'] = []
        st.session_state['history'].append(f"Mood: {mood_pilihan}")

# Sidebar untuk "Backend Data"
st.sidebar.header("Riwayat Konsultasi (Database)")
if 'history' in st.session_state:
    for h in st.session_state['history']:
        st.sidebar.info(h)























