nama_file = "data_keuangan.txt"

def baca_data():
    data = []
    f = open(nama_file, "r")
    for baris in f:
        bagian = []
        kata = ""
        i = 0
        while i < len(baris):
            huruf = baris[i]
            if huruf == "|":
                bagian.append(kata)
                kata = ""
            elif huruf == "\n":
                bagian.append(kata)
            else:
                kata = kata + huruf
            i = i + 1
        if len(bagian) == 4:
            data.append(bagian)
    f.close()
    return data

def simpan_data(data):
    f = open(nama_file, "w")
    for baris in data:
        teks = baris[0] + "|" + baris[1] + "|" + baris[2] + "|" + baris[3] + "\n"
        f.write(teks)
    f.close()

def tambah_data():
    tanggal = input("Masukan Tanggal (YYYY-MM-DD) : ")
    keterangan = input("Masukan Keterangan : ")
    jumlah = input("Masukan Jumlah nominal uang : ")
    tipe = input("Tipe (pemasukan/pengeluaran): ")
    f = open(nama_file, "a")
    f.write(tanggal + "|" + keterangan + "|" + jumlah + "|" + tipe + "\n")
    f.close()
    print("!!Data berhasil ditambahkan!!")

def tampilkan_data():
    data = baca_data()
    if len(data) == 0:
        print("Tidak ada data.")
    else:
        print("Tanggal | Keterangan | Jumlah | Tipe")
        for baris in data:
            print(baris[0] + " | " + baris[1] + " | " + baris[2] + " | " + baris[3])


def hapus_data():
    tanggal_hapus = input("Masukkan tanggal yang ingin dihapus: ")
    data = baca_data()
    data_baru = []
    ketemu = False
    for baris in data:
        if baris[0] != tanggal_hapus:
            data_baru.append(baris)
        else:
            ketemu = True
    if ketemu:
        simpan_data(data_baru)
        print("!!Data berhasil dihapus!!")
    else:
        print("!!Data tidak ditemukan!!")

def menu():
    while True:
        print("\n=== MENU KEUANGAN ===")
        print("1. Menambahkan data")
        print("2. Menampilkan data")
        print("3. Menghapus data")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            hapus_data()
        elif pilihan == "4":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

menu()