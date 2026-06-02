# 🚀 PANDUAN CEPAT MENJALANKAN APLIKASI

## 1. Persiapan Environment

### Instalasi Dependencies
```bash
pip install -r requirements.txt
```

**Output yang diharapkan:**
```
Successfully installed streamlit-1.28.1
Successfully installed plotly-5.17.0
```

### Verifikasi Instalasi
```bash
python test_sistem.py
```

Jika output menampilkan "✅ ALL TESTS PASSED!", maka semua siap!

---

## 2. Menjalankan Aplikasi Streamlit

### Perintah:
```bash
streamlit run app.py
```

### Output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Aplikasi akan otomatis membuka di browser. Jika tidak, buka link tersebut secara manual.

---

## 3. Fitur yang Tersedia

### 🏠 Dashboard
- Statistik real-time sistem
- Pembeli sedang diproses
- 5 pembeli terdekat

### 👥 Tambah Pembeli
- Daftar pembeli baru
- Input manual atau random lokasi
- Auto-generate nomor tiket

### 🎫 Proses Tiket
- Proses pembeli berikutnya dalam antrian
- Lihat info pembeli selanjutnya

### 📊 Statistik
- Metrik pembeli
- Grafik progress dengan Plotly

### 🗺️ Visualisasi Lokasi
- Map interaktif posisi pembeli
- Color gradient berdasarkan jarak
- Urutan prioritas per jarak

### 📋 Riwayat
- Daftar pembeli yang sudah dilayani
- Sort berdasarkan berbagai kriteria

### 🔄 Reset Sistem
- Kosongkan semua data
- Mulai dari awal

---

## 4. Tips Penggunaan

### ✨ Untuk Demo Bagus:

1. **Buka Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Di menu "Tambah Pembeli":**
   - Pilih "Random" untuk lokasi acak
   - Tambahkan 10-15 pembeli

3. **Ke menu "Visualisasi Lokasi":**
   - Lihat peta interaktif dengan color gradient
   - Hover pada titik untuk melihat detail

4. **Ke menu "Proses Tiket":**
   - Klik "PROSES PEMBELI BERIKUTNYA" beberapa kali
   - Lihat statistik berubah di Dashboard

5. **Ke menu "Statistik":**
   - Lihat grafik progress
   - Monitor pembeli yang sudah dilayani

### 🎨 Kustomisasi:

Edit `app.py` untuk customize warna dan desain:

```python
# Ubah warna gradient di CSS
.main {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

# Ubah jumlah pembeli terdekat yang ditampilkan
st.session_state.sistem.get_pembeli_terdekat(5)  # Ubah 5 ke jumlah lain
```

---

## 5. Troubleshooting

### ❌ Error: "No module named 'streamlit'"
```bash
pip install streamlit
```

### ❌ Error: "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### ❌ Performance lambat
- Gunakan browser modern (Chrome, Firefox)
- Close aplikasi lain yang menggunakan resource
- Limit jumlah pembeli di sistem

### ❌ Data hilang setelah refresh
- Ini normal! Streamlit re-run script setiap interaksi
- Data session disimpan dalam `st.session_state`

---

## 6. File Structure

```
pertemuan14/
├── queue_ticket.py          ← Implementasi Queue
├── graph_position.py        ← Implementasi Graph
├── ticket_system.py         ← Logika sistem
├── app.py                   ← Streamlit UI (JALANKAN INI!)
├── test_sistem.py           ← Unit tests
├── requirements.txt         ← Dependencies
├── README.md               ← Dokumentasi lengkap
└── QUICK_START.md          ← File ini
```

---

## 7. Contoh Data Sampel

### Membuat sistem dengan data sampel:

```python
# Di file terpisah (simulasi.py)
from ticket_system import SistemAntrian

sistem = SistemAntrian()

# Tambah pembeli sample
pembeli_names = ["Budi", "Ani", "Citra", "Doni", "Eka", "Fara", "Gita", "Haris"]
for i, nama in enumerate(pembeli_names):
    sistem.tambah_pembeli(nama, i * 12 % 100, (i * 15 + 20) % 100)

# Proses beberapa
for _ in range(3):
    sistem.lanjutkan_pembeli()

print(sistem.get_statistik())
```

---

## 8. Performance Tips

### Untuk sistem dengan banyak pembeli:

1. **Batasi visualisasi:**
   ```python
   # Di app.py, ubah ini:
   terdekat = st.session_state.sistem.get_pembeli_terdekat(10)  # Default 5
   ```

2. **Cache data:**
   ```python
   @st.cache_data
   def get_prioritas():
       return st.session_state.sistem.get_prioritas_berdasarkan_lokasi()
   ```

3. **Gunakan session state:**
   ```python
   if 'cache' not in st.session_state:
       st.session_state.cache = {}
   ```

---

## 🎉 Siap Digunakan!

Aplikasi Anda sekarang sudah siap digunakan. Nikmati sistem antrian tiket yang keren dengan Queue dan Graph! 🎪✨

**Jika ada pertanyaan:**
- Baca `README.md` untuk dokumentasi lengkap
- Cek `test_sistem.py` untuk contoh penggunaan
- Lihat kode di `ticket_system.py`, `queue_ticket.py`, `graph_position.py`

Happy coding! 🚀
