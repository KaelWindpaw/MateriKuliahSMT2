# 🎪 Sistem Antrian Tiket Keren dengan Queue dan Graph

Aplikasi sistem antrian tiket yang menggunakan **Queue** untuk manajemen antrian dan **Graph** untuk menghitung prioritas berdasarkan posisi pembeli terdekat dari pusat penjualan tiket. Dilengkapi dengan front-end Streamlit yang unik dan lucu! 🎟️✨

## 📋 Daftar Isi
1. [Fitur Utama](#fitur-utama)
2. [Struktur Program](#struktur-program)
3. [Instalasi](#instalasi)
4. [Cara Menjalankan](#cara-menjalankan)
5. [Penjelasan Komponen](#penjelasan-komponen)
6. [Contoh Penggunaan](#contoh-penggunaan)
7. [Konsep Data Structure](#konsep-data-structure)

## ✨ Fitur Utama

### 1. **Queue untuk Manajemen Antrian** 📊
- Implementasi Queue menggunakan Linked List
- Operasi FIFO (First In First Out)
- Fitur enqueue, dequeue, peek, dan clear
- Support untuk melihat seluruh antrian

### 2. **Graph untuk Prioritas Lokasi** 🗺️
- Representasi posisi pembeli dalam koordinat 2D
- Perhitungan jarak Euclidean dari pusat penjualan
- Sorting pembeli berdasarkan prioritas jarak
- Implementasi algoritma Dijkstra untuk rute terpendek

### 3. **Sistem Antrian Tiket Terintegrasi** 🎫
- Manajemen pembeli dengan nomor tiket otomatis
- Tracking status pembeli (Menunggu, Selesai)
- Integrasi Queue dan Graph
- Riwayat pembeli yang lengkap

### 4. **Antarmuka Streamlit yang Menarik** 🎨
- Dashboard real-time dengan statistik
- Visualisasi peta lokasi pembeli dengan Plotly
- 7 menu berbeda untuk berbagai fungsi
- UI yang colorful dan interaktif

## 📁 Struktur Program

```
📦 Struktur Antrian Tiket
├── 📄 queue_ticket.py          # Implementasi Queue
├── 📄 graph_position.py        # Implementasi Graph
├── 📄 ticket_system.py         # Logika sistem antrian
├── 📄 app.py                   # Aplikasi Streamlit
├── 📄 requirements.txt         # Dependencies
└── 📄 README.md               # Dokumentasi (file ini)
```

## 🚀 Instalasi

### Prerequisites
- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. **Navigasi ke folder project:**
```bash
cd path/to/Strukturdata/pertemuan14
```

2. **Buat virtual environment (opsional tapi disarankan):**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## ▶️ Cara Menjalankan

Jalankan aplikasi Streamlit dengan perintah:

```bash
streamlit run app.py
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## 📖 Penjelasan Komponen

### 1. **Queue Implementation** (queue_ticket.py)

```python
class Queue:
    def enqueue(data)      # Tambah pembeli ke belakang antrian
    def dequeue()          # Ambil pembeli dari depan antrian
    def peek()             # Lihat pembeli depan tanpa mengeluarkan
    def is_empty()         # Cek apakah antrian kosong
    def get_size()         # Dapatkan jumlah pembeli
    def get_all_queue()    # Dapatkan semua pembeli dalam antrian
```

**Karakteristik:**
- Menggunakan Linked List untuk efisiensi
- Time Complexity: O(1) untuk enqueue dan dequeue
- Space Complexity: O(n) dimana n = jumlah pembeli

### 2. **Graph Implementation** (graph_position.py)

```python
class Graph:
    def add_node()                          # Tambah pembeli ke graph
    def set_center()                        # Set pusat penjualan
    def add_edge()                          # Tambah hubungan antar node
    def calculate_distance()                # Hitung jarak Euclidean
    def get_distance_from_center()          # Jarak dari pusat
    def get_nearest_nodes()                 # Dapatkan node terdekat
    def get_priority_queue()                # Dapatkan antrian prioritas
    def dijkstra()                          # Rute terpendek (Dijkstra)
```

**Karakteristik:**
- Menggunakan adjacency list representation
- Mendukung weighted edges
- Perhitungan jarak real-time

### 3. **Sistem Antrian** (ticket_system.py)

Kelas `SistemAntrian` mengintegrasikan Queue dan Graph:

```python
class SistemAntrian:
    def tambah_pembeli()                    # Tambah pembeli baru
    def lanjutkan_pembeli()                 # Proses pembeli berikutnya
    def lihat_antrian()                     # Lihat antrian saat ini
    def get_prioritas_berdasarkan_lokasi()  # Prioritas dari jarak
    def get_pembeli_terdekat()              # Top N pembeli terdekat
    def get_statistik()                     # Statistik sistem
```

## 💻 Contoh Penggunaan

### Scenario: Sistem Antrian Tiket Bioskop

```python
from ticket_system import SistemAntrian

# Inisialisasi sistem dengan pusat di (50, 50)
sistem = SistemAntrian(pusat_x=50, pusat_y=50)

# Tambah pembeli
pembeli1 = sistem.tambah_pembeli("Budi", 30, 40)
pembeli2 = sistem.tambah_pembeli("Ani", 60, 60)
pembeli3 = sistem.tambah_pembeli("Citra", 45, 45)

# Lihat antrian
print(sistem.lihat_antrian())
# Output: [Pembeli(Budi, 1000), Pembeli(Ani, 1001), Pembeli(Citra, 1002)]

# Lihat pembeli terdekat
terdekat = sistem.get_pembeli_terdekat(2)
# Output: Citra (jarak 7.07m), Budi (jarak 22.36m)

# Proses pembeli
pembeli = sistem.lanjutkan_pembeli()
print(f"Melayani: {pembeli.nama}")

# Lihat statistik
stat = sistem.get_statistik()
print(f"Menunggu: {stat['menunggu']}, Selesai: {stat['selesai']}")
```

## 🎯 Menu-Menu di Streamlit

### 1. 🏠 Dashboard
- Menampilkan statistik real-time
- Pembeli yang sedang diproses
- 5 pembeli terdekat dari pusat

### 2. 👥 Tambah Pembeli
- Input manual atau random lokasi
- Automatic ticket number generation
- Visualisasi pembeli yang baru ditambahkan

### 3. 🎫 Proses Tiket
- Button untuk proses pembeli berikutnya
- Info detail pembeli yang sedang dilayani

### 4. 📊 Statistik
- Metrik pembeli menunggu vs selesai
- Grafik progress menggunakan Plotly

### 5. 🗺️ Visualisasi Lokasi
- Interactive map dengan Plotly
- Scatter plot dengan color gradient berdasarkan jarak
- Tabel urutan prioritas pembeli

### 6. 📋 Riwayat
- Daftar semua pembeli yang sudah dilayani
- Sort berdasarkan Waktu, Nama, atau Tiket

### 7. 🔄 Reset Sistem
- Reset semua data sistem antrian

## 🧮 Konsep Data Structure

### Queue (Antrian) 🔄
**Karakteristik FIFO:**
```
Enqueue:  [1] -> [2] -> [3] ->
Dequeue:  [1]   [2] -> [3]
```

**Aplikasi dalam Sistem:**
- Pembeli pertama yang datang akan dilayani pertama
- Pembeli baru ditambahkan ke belakang antrian
- Pembeli yang sudah dilayani dikeluarkan dari depan

### Graph (Graf) 🕸️
**Representasi Posisi:**
```
Koordinat 2D dengan:
- Node: Pembeli dan Pusat Penjualan
- Edge: Hubungan/jarak antar node
- Weight: Jarak Euclidean
```

**Perhitungan Jarak:**
```
Jarak = √[(x₂-x₁)² + (y₂-y₁)²]
```

## 📊 Contoh Output

```
Dashboard Statistik:
👥 Total Pembeli: 10
⏳ Menunggu: 7
✅ Selesai: 3
📈 Progress: 30%

Pembeli Terdekat:
1. Citra (Tiket: 1002) - Jarak: 7.07m
2. Budi (Tiket: 1000) - Jarak: 22.36m
3. Ani (Tiket: 1001) - Jarak: 14.14m
```

## 🎨 Fitur UI Streamlit

- **Gradient Background:** Purple to Pink gradient
- **Interactive Buttons:** Dengan hover effects
- **Color-coded Status:** 🟠 Menunggu, 🟢 Selesai
- **Emoji Integration:** UI yang fun dan memorable
- **Responsive Layout:** Columns dan containers
- **Dark Theme Plotly:** Charts yang aesthetic

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Port 8501 sudah digunakan
```bash
streamlit run app.py --server.port 8502
```

### Performance lambat dengan banyak pembeli
- Gunakan GPU plotting dengan Plotly
- Batasi visualisasi maksimal pembeli

## 📝 Catatan Implementasi

1. **Queue Efficiency:**
   - Linked List implementation: O(1) for enqueue/dequeue
   - Array implementation: O(n) untuk dequeue

2. **Graph Complexity:**
   - Dijkstra: O((V + E) log V)
   - Distance calculation: O(1)

3. **UI Performance:**
   - Streamlit caching untuk data besar
   - Plotly untuk interaktif visualization

## 👨‍💻 Developer Notes

Dibuat dengan:
- **Python 3.8+**
- **Streamlit** untuk UI
- **Plotly** untuk visualisasi
- **OOP** untuk struktur yang clean

## 📄 Lisensi

Program ini dibuat untuk tujuan pendidikan (Semester 2 - Data Structure).

---

🎪 **Selamat Menikmati Sistem Antrian Tiket Keren Anda!** 🎪

Jika ada pertanyaan atau saran, feel free untuk improve! 🚀✨
