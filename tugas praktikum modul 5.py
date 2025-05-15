
mahasiswa = []

ulang = True
while ulang == True:
    print("===== MENU UTAMA =====")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")
    
    if pilihan == "1":
        print("\n== Tambah Data ==")
        nim = input("Masukkan NIM Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        nilai = float(input("Masukkan Nilai Mahasiswa: "))
        mahasiswa = mahasiswa + [[nim, nama, nilai]]
        print("Data berhasil ditambahkan!\n")
    
    elif pilihan == "2":
        print("\n== Hapus Data ==")
        nim_hapus = input("Masukkan NIM yang ingin dihapus: ")
        indeks = 0
        ditemukan = 0
        data_baru = []
        while indeks < len(mahasiswa):
            if mahasiswa[indeks][0] != nim_hapus:
                data_baru = data_baru + [mahasiswa[indeks]]
            else:
                ditemukan = 1
            indeks = indeks + 1
        mahasiswa = data_baru
        if ditemukan == 0:
            print("Data tidak ditemukan.\n")
        else:
            print("Data berhasil dihapus!\n")

    elif pilihan == "3":
        print("\n== Tampilkan Data ==")
        if len(mahasiswa) == 0:
            print("Belum ada data.\n")
        else:
            print("Data Mahasiswa (Urut Nilai Tertinggi ke Terendah):")
            i = 0
            while i < len(mahasiswa) - 1:
                j = 0
                while j < len(mahasiswa) - i - 1:
                    if mahasiswa[j][2] < mahasiswa[j+1][2]:
                        sementara = mahasiswa[j]
                        mahasiswa[j] = mahasiswa[j+1]
                        mahasiswa[j+1] = sementara
                    j = j + 1
                i = i + 1
            
            indeks = 0
            while indeks < len(mahasiswa):
                print("NIM:", mahasiswa[indeks][0], "| Nama:", mahasiswa[indeks][1], "| Nilai:", mahasiswa[indeks][2])
                indeks = indeks + 1
        
        indeks = 0
        while indeks < len(mahasiswa):
            print("NIM:", mahasiswa[indeks][0], "| Nama:", mahasiswa[indeks][1], "| Nilai:", mahasiswa[indeks][2])
            indeks = indeks + 1

    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        ulang = False
    elif pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4":
        print("Pilihan tidak valid. Silakan coba lagi.\n")