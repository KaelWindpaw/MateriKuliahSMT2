#LIST PERTEMUAN 2 (2/16/2024)

print ("1 List adalah struktur data untuk menyimpan banyak nilai dalam satu variabel")
#mobil = ["avanza", "xenia", "civic", 1,2,3]
print("avanza", "xenia", "civic", 1,2,3)
print ("\n")


print ("2 MUTABLE (bisa diubah)")
#Penghitungan list dimulai dari 0
angka = [1, 2, 3]
angka[0] = 10
print(angka)
print ("\n")


mobil = ["avanza", "xenia", "civic"]
print ("3 Slicing (mengambil indeks tertentu dalam list)")
print(mobil[:1])  
print(mobil[1:3])  
print ("\n")


print ("4 Menambahkan Data ke List di posisi tertentu")
mobil.insert(1, "punya Ahmad")
print(mobil)
print ("\n")


print ("5 Menambahkan Data ke list di posisi belakang")
mobil.append("fortuner")
print(mobil)
print ("\n")


print ("6 Menghapus Data dari List")
mobil.remove("xenia")    #bisa juga pop
print(mobil)
print ("\n")


print ("7 Menghapus Data dari List dengan indeks tertentu")
del mobil[0]
print(mobil)
print ("\n")


print ("8 Menghapus Data dari List dengan pop")
mobil.pop(2)  
print(mobil)
print ("\n")


print ("9 Menghitung jumlah data dalam List")
jumlah_mobil = len(mobil)
print("Jumlah mobil:", jumlah_mobil)
print ("\n")


print ("10 Mengurutkan List")
mobil.sort()
print(mobil)
print ("\n")


print ("11 Membalik urutan List")
mobil.reverse()
print(mobil)
print ("\n")


print ("12 Menggabungkan dua List")
mobil_lain = ["pajero", "brio"]
semua_mobil = mobil + mobil_lain
print(semua_mobil)
print ("\n")


print ("13 Menghitung jumlah kemunculan suatu nilai dalam List")
jumlah_avanza = semua_mobil.count("avanza")
print("Jumlah avanza:", jumlah_avanza)
print ("\n")


print ("14 Mencari indeks suatu nilai dalam List")
indeks_civic = semua_mobil.index("civic")
print("Indeks civic:", indeks_civic)
print ("\n")


print ("15 Mengosongkan List")
semua_mobil.clear()
print(semua_mobil)
print ("\n")


print ("16 Membuat List dengan tipe data campuran")
campuran = [1, "dua", 3.0, True]
print(campuran)
print ("\n")