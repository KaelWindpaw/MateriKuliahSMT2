# 🚀 PANDUAN INSTALASI SISTEM ANTRIAN TIKET KEREN

## 📋 TABLE OF CONTENTS
1. [Prasyarat](#prasyarat)
2. [Langkah-Langkah Instalasi](#langkah-langkah-instalasi)
3. [Verifikasi Instalasi](#verifikasi-instalasi)
4. [Menjalankan Aplikasi](#menjalankan-aplikasi)
5. [Troubleshooting](#troubleshooting)

---

## ✅ PRASYARAT

Sebelum mulai, pastikan Anda memiliki:

### 1. Python
- **Versi:** Python 3.8 atau lebih tinggi
- **Download:** https://www.python.org/downloads/
- **Verifikasi:**
  ```bash
  python --version
  # Harus menampilkan: Python 3.8.x atau lebih tinggi
  ```

### 2. pip (Python Package Manager)
- Biasanya sudah included dengan Python
- **Verifikasi:**
  ```bash
  pip --version
  # Harus menampilkan: pip x.x.x from ...
  ```

### 3. Terminal/Command Prompt
- **Windows:** Command Prompt, PowerShell, atau Git Bash
- **Mac/Linux:** Terminal

### 4. Internet Connection
- Diperlukan untuk download dependencies dari PyPI

---

## 🔧 LANGKAH-LANGKAH INSTALASI

### STEP 1: Download/Clone Project

**Option A: Download ZIP**
```
1. Buka: GitHub repository atau file manager
2. Download project sebagai ZIP
3. Extract ke folder pilihan Anda
```

**Option B: Git Clone**
```bash
git clone <repository-url>
cd Semester-2/Strukturdata/pertemuan14
```

**Option C: Sudah ada di folder**
```bash
cd "c:\Users\HYPE AMD\OneDrive\Dokumen\GitHub\Semester-2\Strukturdata\pertemuan14"
```

### STEP 2: Buka Terminal di Project Folder

**Windows (Command Prompt):**
```
1. Tekan Windows + R
2. Ketik: cmd
3. Tekan Enter
4. Copy-paste path folder dan tekan Enter
```

**Windows (PowerShell):**
```
1. Tekan Windows + X
2. Pilih: Windows PowerShell
3. Ketik: cd path/to/folder
```

**Windows (File Explorer):**
```
1. Buka File Explorer
2. Navigasi ke project folder
3. Shift + Right-click di kosong area
4. Pilih: Open PowerShell window here
```

### STEP 3: Buat Virtual Environment (Opsional tapi Disarankan)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Expected Output:**
```
(venv) C:\path\to\project>
```

### STEP 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected Output:**
```
Collecting streamlit==1.28.1
  Downloading streamlit-1.28.1-py2.py3-none-any.whl (xxx KB)
Collecting plotly==5.17.0
  Downloading plotly-5.17.0-py2.py3-none-any.whl (xxx KB)
...
Successfully installed streamlit-1.28.1 plotly-5.17.0
```

### STEP 5: Verifikasi Instalasi

```bash
python test_sistem.py
```

**Expected Output:**
```
╔════════════════════════════════════════════════╗
║       🎪 TEST SISTEM ANTRIAN TIKET KEREN 🎪       ║
╚════════════════════════════════════════════════╝

✅ All Queue tests passed!
✅ All Graph tests passed!
✅ All Sistem Antrian tests passed!

🎉 ALL TESTS PASSED! 🎉
```

---

## ✨ VERIFIKASI INSTALASI

### Cek Python Version
```bash
python --version
```
✅ Harus: Python 3.8+

### Cek pip Version
```bash
pip --version
```
✅ Harus: pip versi terbaru

### Cek Installed Packages
```bash
pip list
```
✅ Harus terlihat:
- streamlit (1.28.1 atau lebih tinggi)
- plotly (5.17.0 atau lebih tinggi)

### Cek Import Modules
```bash
python -c "import streamlit; import plotly; print('✅ All modules imported successfully!')"
```
✅ Harus: "✅ All modules imported successfully!"

### Run Unit Tests
```bash
python test_sistem.py
```
✅ Harus: "ALL TESTS PASSED!"

---

## ▶️ MENJALANKAN APLIKASI

### Option 1: Jalankan Streamlit UI (RECOMMENDED)

```bash
streamlit run app.py
```

**Expected Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**Langkah selanjutnya:**
1. Browser akan otomatis membuka
2. Jika tidak, buka URL `http://localhost:8501` secara manual
3. Aplikasi akan loaded dengan interface Streamlit
4. Mulai tambahkan pembeli dan explore fitur-fitur!

### Option 2: Jalankan Simulasi CLI

```bash
python simulasi.py
```

**Output:**
Akan menampilkan simulasi sistem antrian dengan output text-based
Berguna untuk melihat bagaimana sistem bekerja tanpa UI

### Option 3: Jalankan Unit Tests

```bash
python test_sistem.py
```

**Output:**
Akan menampilkan hasil test untuk semua modul
Berguna untuk verifikasi semua komponen berfungsi

---

## 🎮 FIRST RUN CHECKLIST

Setelah menjalankan `streamlit run app.py`, cek:

- [ ] Browser membuka dengan URL `localhost:8501`
- [ ] Sidebar menampilkan menu dengan emoji
- [ ] Dashboard menampilkan 4 metric cards
- [ ] Dapat klik button "DAFTARKAN PEMBELI"
- [ ] Dapat switch antar menu di sidebar
- [ ] Chart dan visualisasi ter-render dengan baik
- [ ] Tidak ada error messages di terminal

---

## ❓ TROUBLESHOOTING

### ❌ Error: "Python is not recognized"

**Solusi:**
```
1. Python belum diinstall atau tidak di PATH
2. Download Python dari: https://www.python.org/downloads/
3. PENTING: Centang "Add Python to PATH" saat install
4. Restart terminal/command prompt
5. Verifikasi: python --version
```

### ❌ Error: "No module named 'streamlit'"

**Solusi:**
```bash
# Install streamlit
pip install streamlit

# Atau reinstall dari requirements
pip install -r requirements.txt

# Verifikasi
pip list | grep streamlit
```

### ❌ Error: "Port 8501 already in use"

**Solusi:**
```bash
# Option 1: Gunakan port lain
streamlit run app.py --server.port 8502

# Option 2: Kill process yang menggunakan port
# Windows (PowerShell):
Get-Process | Where-Object {$_.Handles -like "*8501*"} | Stop-Process

# Mac/Linux:
lsof -ti:8501 | xargs kill -9

# Option 3: Restart computer
```

### ❌ Error: "ModuleNotFoundError" saat run app.py

**Solusi:**
```bash
# Pastikan di folder yang benar
cd "c:\Users\HYPE AMD\OneDrive\Dokumen\GitHub\Semester-2\Strukturdata\pertemuan14"

# Reinstall dependencies
pip install -r requirements.txt

# Check file ada
ls -la  # atau: dir (Windows)

# Harus terlihat: app.py, queue_ticket.py, graph_position.py, ticket_system.py
```

### ❌ Error: "AttributeError: module 'plotly' has no attribute..."

**Solusi:**
```bash
# Update plotly ke versi terbaru
pip install --upgrade plotly

# Verifikasi version
pip show plotly
```

### ❌ Aplikasi tidak responsif / loading lama

**Solusi:**
1. Check CPU/Memory usage - close aplikasi lain
2. Reduce jumlah pembeli di sistem
3. Clear browser cache: Ctrl+Shift+Delete
4. Restart aplikasi: Stop (Ctrl+C) dan jalankan lagi

### ❌ Dashboard blank / tidak muncul apa-apa

**Solusi:**
1. Refresh browser: F5 atau Ctrl+R
2. Check console untuk error: F12 (Developer Tools)
3. Check terminal untuk error messages
4. Restart aplikasi

### ❌ Data hilang setelah refresh browser

**This is normal!** 
Streamlit re-run script setiap ada perubahan, data session tidak persisten.
Jika ingin persisten, integrate dengan database (SQLite, PostgreSQL).

---

## 🆘 SUPPORT & HELP

### Jika masih ada masalah:

1. **Baca dokumentasi:**
   - README.md - Dokumentasi lengkap
   - QUICK_START.md - Panduan cepat
   - INDEX.md - Referensi lengkap

2. **Cek code:**
   - ticket_system.py - Main logic
   - app.py - UI implementation
   - Cari comments dan docstrings

3. **Run tests:**
   ```bash
   python test_sistem.py
   ```

4. **Check environment:**
   ```bash
   python -c "import sys; print(sys.executable)"  # Python path
   pip list  # Installed packages
   ```

---

## 📦 REQUIREMENTS DETAILED

File `requirements.txt` berisi:

```
streamlit==1.28.1
plotly==5.17.0
```

**Explanation:**
- `streamlit` - Web framework untuk UI
- `plotly` - Interactive visualization library

**Alternative install:**
```bash
pip install streamlit==1.28.1 plotly==5.17.0
```

---

## 🎓 SETUP VERIFICATION CHECKLIST

```
✅ Python 3.8+ installed
✅ pip working
✅ Virtual environment created (opsional)
✅ Dependencies installed via requirements.txt
✅ test_sistem.py passes all tests
✅ simulasi.py runs successfully
✅ streamlit run app.py starts without error
✅ Browser opens at localhost:8501
✅ Dashboard displays correctly
✅ Can add pembeli and interact with UI
```

---

## 🎯 NEXT STEPS AFTER INSTALLATION

1. **Explore Dashboard:**
   - Lihat statistik dan metrics
   - Pahami struktur UI

2. **Add Sample Data:**
   - Menu "Tambah Pembeli"
   - Tambahkan 10-15 pembeli

3. **View Visualizations:**
   - Menu "Visualisasi Lokasi"
   - Interact dengan peta

4. **Process Queue:**
   - Menu "Proses Tiket"
   - Lihat statistik update

5. **Read Code:**
   - Pahami implementasi Queue dan Graph
   - Review test_sistem.py untuk examples

---

## 🎉 READY TO GO!

Jika semua langkah berhasil, Anda sekarang siap menggunakan:

```bash
streamlit run app.py
```

**Enjoy your awesome ticket queue system!** 🎪✨

---

## 📝 QUICK COMMAND REFERENCE

```bash
# Setup
cd "c:\Users\HYPE AMD\OneDrive\Dokumen\GitHub\Semester-2\Strukturdata\pertemuan14"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Verify
python test_sistem.py

# Run applications
streamlit run app.py      # UI
python simulasi.py         # CLI simulation
python test_sistem.py      # Unit tests

# Deactivate virtual environment
deactivate
```

---

*Last Updated: 2026-05-22*
*Installation Guide for Sistem Antrian Tiket Keren*
*Status: ✅ COMPLETE*
