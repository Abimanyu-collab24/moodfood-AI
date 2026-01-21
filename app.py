import streamlit as st  # Baris ini SANGAT PENTING agar 'st' dikenali
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

logo = Image.open("LogoMFoke.png")

#Konfigurasi Halaman (Favicon tetap pakai logo kecil)
st.set_page_config(page_title="MoodFood AI", page_icon=logo)

st.markdown("""
    <style>
    /* 1. Mengganti Background Utama dengan gradasi lembut */
    .stApp {
        background: linear-gradient(to right, #f8f9fa, #e8f5e9);
    }

    /* 2. Mempercantik Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #4CAF50;
    }

    /* 3. Judul Utama yang Berwarna */
    h1 {
        color: #2E7D32;
        font-family: 'Poppins', sans-serif;
        text-shadow: 1px 1px 2px #bdbdbd;
        text-align: center;
    }

    /* 4. Membuat Tombol 'Dapatkan Rekomendasi' lebih mencolok */
    .stButton>button {
        width: 100%;
        border-radius: 30px;
        background: linear-gradient(45deg, #4CAF50, #8BC34A);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        padding: 10px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.15);
        color: #ffffff;
    }

    /* 5. Memberikan warna pada kartu hasil rekomendasi */
    .stAlert {
        border-radius: 15px;
        border-left: 5px solid #4CAF50;
        background-color: #ffffff;
    }

    /* 6. Mempercantik Input Label */
    .stSelectbox label, .stTextInput label {
        color: #1B5E20 !important;
        font-weight: bold;
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

if st.button("Klik Dapatkan Rekomendasi Menu"):
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


























