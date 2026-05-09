from gtts import gTTS
import streamlit as st
import queue
# membuat visualisasi antrian dengan gtts
st.title("Antrian Klinik")
st.write("Visualisasi Queue kasus Antrian klinik")
#inisiasi state
if 'antrian' not in st.session_state:
    st.session_state.antrian = queue.Queue()

#membuat tombol input antrian
input_antrian = st.text_input("Masukkan nama pasien:")
if st.button("Tambah Antrian"):
    st.session_state.antrian.put(input_antrian)
    st.write("Antrian berhasil ditambahkan")

# menampilkan seluruh antrian
st.write("seluruh antrian")
nomor = 1
for i in st.session_state.antrian.queue:
    st.write(f"Antrian ke {nomor}: {i}")
    nomor += 1

# membuat tombol panggilan antrian
if st.button("Panggil Antrian"):
    if not st.session_state.antrian.empty():
        pasien = st.session_state.antrian.get()
        print(pasien)
        st.write(f"Antrian yang dipanggil: {pasien}")
        tts = gTTS(f"Antrian yang dipanggil: {pasien}", lang='id')
        tts.save("panggilan_antrian.mp3")
        st.audio("panggilan_antrian.mp3, autoplay=True")

    else:
        tts = gTTS("Antrian kosong", lang='id')
        tts.save("antrian_kosong.mp3")
        st.audio("antrian_kosong.mp3, autoplay=True")