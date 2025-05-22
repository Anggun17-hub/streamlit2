import streamlit as st

st.write(HELLO ANGGUN)
import streamlit as st

st.title("Aplikasi Hello World Interaktif")

# Tampilkan teks sederhana
st.write("Selamat datang di aplikasi Streamlit pertamamu!")

# Input teks dari pengguna
name = st.text_input("Siapa nama kamu?", "")

# Tombol interaksi
if st.button("Sapa Saya"):
    if name:
        st.success(f"Halo, {ANGGUN}! Semoga harimu menyenangkan 😊")
    else:
        st.warning("ANGGUN!")

