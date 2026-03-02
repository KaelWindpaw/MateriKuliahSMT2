import sys
# tuple lebih efisien dalam penggunaan memori dibandingkan dengan list
logAppsList = ["User1 Login"]
print(logAppsList)
print(sys.getsizeof(logAppsList))

# membuat struktur tuple
logApps = ("User1 Login")
print(logApps)
print(sys.getsizeof(logApps))

# pembuktian Tuple tidak bisa diubah
# tambah data baru ke dalam tuple
# logApps.append("User4 Login") # akan error karena tuple tidak bisa diubah
# ubah data di dalam tuple
# logApps[0] = "User1 Logout" # akan error karena tuple tidak bisa diubah

# hapus
# del logApps[1]
# pembuktian tuple bisa diakses dengan index
print(logApps[0]) # akan menampilkan "User1 Login"
print(logApps[1]) # akan menampilkan "User2 Login"  
print(logApps[2]) # akan menampilkan "User3 Login"

# menduplikat Tuple 
logAppsBackup = logApps
print("ini isi backup logApps: ", logAppsBackup)
print("ini isi logApps: ", logApps)