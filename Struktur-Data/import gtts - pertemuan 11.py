import gtts
import playsound
# Contoh Penggunaaan GTTS
text = "Hello, selamat datang di kelas Informatika2A"
tts = gtts.gTTS(text, lang="id")
tts.save("output.mp3")

# Contoh Play
playsound.playsound("output.mp3")