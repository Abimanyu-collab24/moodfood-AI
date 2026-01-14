import streamlit as st  # Baris ini SANGAT PENTING agar 'st' dikenali
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

logo = Image.open("LogoMF.png")

#Konfigurasi Halaman (Favicon tetap pakai logo kecil)
st.set_page_config(page_title="MoodFood AI", page_icon=logo)

col1, col2 = st.columns([1, 5])
with col1:
    st.image(logo, width=340) 

with col2:
    st.title("MoodFood AI")
st.markdown("---")

# Bagian Input User
st.subheader("Bagaimana perasaanmu saat ini?")
mood_pilihan = st.selectbox("Pilih Mood:", ["Sedih", "Stres", "Lelah", "Cemas", "Senang"])
tanya_tambahan = st.text_input("Ada Pertanyaan/keluhan lain? (Opsional)", placeholder="Misal: Saya kurang tidur...")

if st.button("Dapatkan Rekomendasi Menu"):
    model = genai.GenerativeModel('gemini-2.5-flash') # Menggunakan model terbaru
    
    prompt = f"Saya sedang merasa {mood_pilihan}. {tanya_tambahan}. Berikan 2 rekomendasi makanan atau minuman yang sehat secara ilmiah untuk mood ini, sertakan resep singkat dan fun fact nutrisinya."
    
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














