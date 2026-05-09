from gtts import gTTS
import streamlit as st

# contoh penggunaan gtts
text = "Youkoso, selamat datang di kelas struktur data!"
tts = gtts(text, lang='en')
tts.save("welcome.mp3")

# contoh play
st.audio("welcome.mp3")