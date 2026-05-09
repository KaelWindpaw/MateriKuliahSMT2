# VIsualisasi Konsep Stack dengan Streamlit

import streamlit as st
import stack

st.title("Visualisasi Stack")

# Inisialisasi Stacak
if 'stack' not in st.session_state:
