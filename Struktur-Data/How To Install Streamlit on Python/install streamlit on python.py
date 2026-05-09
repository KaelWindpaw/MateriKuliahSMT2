import streamlit as st
import sys
# Membuat Struktur Tuple
logApps = ("User1 login", "User2 login", "User3 login")
print(logApps)
print(sys.getsizeof(logApps))

#Pembuktian tuple tidak bisa diubah
#1. Tambah
# LogApps.append("User4 login")
#2. Ubah
# LogApps[0] = "User1 logout"

#3. Hapus
del logApps[1]