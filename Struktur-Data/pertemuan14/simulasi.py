"""
Simulasi Sistem Antrian Tiket
Menunjukkan penggunaan Queue dan Graph secara programmatic
"""

from ticket_system import SistemAntrian, Pembeli
from datetime import datetime


def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def print_separator():
    """Print separator line"""
    print("-" * 60)


def simulasi_bioskop():
    """Simulasi sistem antrian tiket bioskop"""
    
    print_header("🎬 SIMULASI SISTEM ANTRIAN TIKET BIOSKOP")
    print("\nSkenario: Penjualan tiket bioskop dengan sistem antrian")
    print("Lokasi pusat penjualan tiket: (50, 50)")
    print("\n")
    
    # Inisialisasi sistem
    sistem = SistemAntrian(pusat_x=50, pusat_y=50)
    
    # Tambah pembeli dengan lokasi berbeda
    pembeli_data = [
        ("Budi Santoso", 30, 40),
        ("Ani Wijaya", 60, 60),
        ("Citra Dewi", 45, 45),
        ("Doni Susilo", 70, 30),
        ("Eka Pratama", 25, 75),
        ("Fara Nabil", 80, 80),
        ("Gita Sari", 35, 65),
        ("Haris Gunawan", 55, 25),
    ]
    
    print_header("REGISTRASI PEMBELI")
    print("\nMendaftarkan 8 pembeli dengan lokasi berbeda:")
    print_separator()
    
    for idx, (nama, x, y) in enumerate(pembeli_data, 1):
        pembeli = sistem.tambah_pembeli(nama, x, y)
        print(f"{idx}. {nama:<20} | Lokasi: ({x:2d}, {y:2d}) | Tiket: {pembeli.nomor_tiket}")
    
    # Tampilkan statistik
    print_separator()
    stat = sistem.get_statistik()
    print(f"\nStatistik Sistem:")
    print(f"  Total pembeli    : {stat['total_pembeli']}")
    print(f"  Menunggu         : {stat['menunggu']}")
    print(f"  Selesai          : {stat['selesai']}")
    print(f"  Progress         : {stat['persentase_selesai']:.1f}%")
    
    # Tampilkan antrian saat ini
    print_header("ANTRIAN SAAT INI")
    antrian = sistem.lihat_antrian()
    print(f"\nTotal dalam antrian: {len(antrian)}\n")
    
    for idx, pembeli in enumerate(antrian, 1):
        print(f"[{idx}] {pembeli.nomor_tiket} - {pembeli.nama:<20} ({pembeli.lokasi_x}, {pembeli.lokasi_y})")
    
    # Tampilkan pembeli terdekat
    print_header("PEMBELI TERDEKAT DARI PUSAT")
    print("\nBerdasarkan jarak Euclidean dari pusat (50, 50):\n")
    
    prioritas = sistem.get_prioritas_berdasarkan_lokasi()
    for p in prioritas:
        print(f"  #{p['priority']:<2} | {p['name']:<20} | Tiket: {p['node_id']} | Jarak: {p['distance']:>6} m")
    
    # Simulasi proses pembeli
    print_header("PROSES PEMBELI (SIMULASI)")
    
    pembeli_diproses = []
    total_diproses = 3
    
    print(f"\nProses {total_diproses} pembeli dari antrian:\n")
    print_separator()
    
    for i in range(total_diproses):
        pembeli = sistem.lihat_pembeli_depan()
        
        if pembeli:
            print(f"\n[{i+1}] SEDANG DILAYANI:")
            print(f"    Nomor Tiket : {pembeli.nomor_tiket}")
            print(f"    Nama        : {pembeli.nama}")
            print(f"    Lokasi      : ({pembeli.lokasi_x}, {pembeli.lokasi_y})")
            print(f"    Waktu Tiba  : {pembeli.waktu_datang.strftime('%H:%M:%S')}")
            
            # Simulasi proses
            print(f"    Status      : ⏳ DIPROSES...")
            
            # Keluarkan dari antrian
            selesai = sistem.lanjutkan_pembeli()
            print(f"    Status      : ✅ SELESAI")
            
            pembeli_diproses.append(selesai)
        else:
            print(f"\n[{i+1}] Tidak ada pembeli dalam antrian")
    
    # Statistik setelah proses
    print_separator()
    print(f"\nStatistik Setelah Proses:")
    stat = sistem.get_statistik()
    print(f"  Menunggu         : {stat['menunggu']}")
    print(f"  Selesai          : {stat['selesai']}")
    print(f"  Progress         : {stat['persentase_selesai']:.1f}%")
    
    # Tampilkan antrian sisa
    print_header("ANTRIAN SISA")
    antrian_sisa = sistem.lihat_antrian()
    print(f"\nTotal dalam antrian: {len(antrian_sisa)}\n")
    
    for idx, pembeli in enumerate(antrian_sisa, 1):
        print(f"[{idx}] {pembeli.nomor_tiket} - {pembeli.nama:<20} ({pembeli.lokasi_x}, {pembeli.lokasi_y})")
    
    # Tampilkan riwayat
    print_header("RIWAYAT PEMBELI YANG SUDAH DILAYANI")
    print(f"\nTotal : {len(sistem.riwayat_pembeli)}\n")
    
    for idx, pembeli in enumerate(sistem.riwayat_pembeli, 1):
        print(f"[{idx}] {pembeli.nomor_tiket} - {pembeli.nama:<20} | Selesai: {pembeli.waktu_datang.strftime('%H:%M:%S')}")
    
    print_header("ANALISIS DATA")
    
    # Analisis pembeli terdekat vs terjauh
    prioritas = sistem.get_prioritas_berdasarkan_lokasi()
    
    if prioritas:
        terdekat = prioritas[0]
        terjauh = prioritas[-1]
        
        print(f"\n📍 Pembeli Terdekat:")
        print(f"    Nama      : {terdekat['name']}")
        print(f"    Tiket     : {terdekat['node_id']}")
        print(f"    Jarak     : {terdekat['distance']} m")
        
        print(f"\n📍 Pembeli Terjauh:")
        print(f"    Nama      : {terjauh['name']}")
        print(f"    Tiket     : {terjauh['node_id']}")
        print(f"    Jarak     : {terjauh['distance']} m")
        
        print(f"\n📊 Statistik Jarak:")
        jarak_list = [p['distance'] for p in prioritas]
        rata_rata = sum(jarak_list) / len(jarak_list) if jarak_list else 0
        
        print(f"    Jarak rata-rata : {rata_rata:.2f} m")
        print(f"    Jarak min       : {min(jarak_list):.2f} m")
        print(f"    Jarak max       : {max(jarak_list):.2f} m")
    
    print("\n")


def simulasi_advanced():
    """Simulasi lebih kompleks dengan banyak pembeli"""
    
    print_header("🎪 SIMULASI ADVANCED: SISTEM ANTRIAN BESAR")
    
    sistem = SistemAntrian(pusat_x=50, pusat_y=50)
    
    # Tambah banyak pembeli dengan koordinat acak
    import random
    
    print("\nMenambahkan 30 pembeli dengan lokasi random...")
    nama_template = ["Pembeli", "Customer", "Guest", "Visitor", "Buyer"]
    
    for i in range(30):
        nama = f"{random.choice(nama_template)} #{i+1}"
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        sistem.tambah_pembeli(nama, x, y)
    
    print("✅ Selesai!\n")
    
    # Statistik awal
    stat = sistem.get_statistik()
    print(f"Total pembeli dalam antrian: {stat['menunggu']}")
    
    # Proses 15 pembeli
    print(f"\nProses 15 pembeli...")
    for i in range(15):
        sistem.lanjutkan_pembeli()
    
    print("✅ Selesai!\n")
    
    # Statistik akhir
    stat = sistem.get_statistik()
    print(f"Statistik Final:")
    print(f"  Total pembeli    : {stat['total_pembeli']}")
    print(f"  Menunggu         : {stat['menunggu']}")
    print(f"  Selesai          : {stat['selesai']}")
    print(f"  Progress         : {stat['persentase_selesai']:.1f}%")
    
    # Top 5 pembeli terdekat
    print(f"\nTop 5 Pembeli Terdekat:")
    terdekat = sistem.get_pembeli_terdekat(5)
    for idx, pembeli in enumerate(terdekat, 1):
        print(f"  {idx}. {pembeli['nama']} - {pembeli['jarak']} m")
    
    print("\n")


def main():
    """Main function"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "🎪 SIMULASI SISTEM ANTRIAN TIKET KEREN 🎪".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝\n")
    
    # Simulasi 1
    simulasi_bioskop()
    
    # Simulasi 2
    simulasi_advanced()
    
    print("=" * 60)
    print("🎉 SIMULASI SELESAI!")
    print("=" * 60)
    print("\nUntuk menjalankan aplikasi UI Streamlit, ketik:")
    print("  streamlit run app.py")
    print("\n")


if __name__ == "__main__":
    main()
