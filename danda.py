print("===== SELAMAT DATANG DI KONSER CAHAYA MALAM =====")
m = 8
n = 10
total_kursi = m * n
harga_tiket = {
    "VVIP"   : 1000000,
    "VIP"    : 750000,
    "Reguler": 500000,
    "Ekonomi": 250000
}
kategori_kursi = {
    "VVIP"   : total_kursi // 4,
    "VIP"    : total_kursi // 4,
    "Reguler": total_kursi // 4,
    "Ekonomi": total_kursi // 4
}

kursi = [[(i * n + j + 1) for j in range(n)] for i in range(m)]
pemesanan = []
print("\nSelamat datang di reservasi tiket konser!\n")
print(f"kami menyediiakan ukuran kursi {m} x {n}\n")
print("Tampilan Layout Kursi :\n")
for i in range(m):
    for j in range(n):
        print(kursi[i][j], end="\t")
    print()
print("\n===== Harga Tiket =====")
for kategori in harga_tiket:
    print(f"{kategori}: Rp{harga_tiket[kategori]:,}")

jumlah_tiket = int(input("\nMasukkan jumlah tiket yang ingin dipesan : "))

for i in range(jumlah_tiket):
    print(f"\nPemesanan ke-{i+1}:")
    nama = input("Masukkan nama Anda : ")
    nomor_kursi = int(input("Masukkan nomor kursi yang ingin dipesan : "))
    tanggal = input("masukan tanggal pemesanan :")
    metode_pembayaran = input("metode pembayaran anda :")
    password = input("Buat password akses masuk konser : ")

    if 1 <= nomor_kursi <= kategori_kursi["VVIP"]:
        kategori = "VVIP"
    elif kategori_kursi["VVIP"] < nomor_kursi <= kategori_kursi["VVIP"] + kategori_kursi["VIP"]:
        kategori = "VIP"
    elif kategori_kursi["VVIP"] + kategori_kursi["VIP"] < nomor_kursi <= kategori_kursi["VVIP"] + kategori_kursi["VIP"] + kategori_kursi["Reguler"]:
        kategori = "Reguler"
    else:
        kategori = "Ekonomi"

    harga = harga_tiket[kategori]
    pemesanan += [{"nama": nama, "kursi": nomor_kursi, "kategori": kategori, "harga": harga, "password": password}]

    for i in range(m):
        for j in range(n):
            if kursi[i][j] == nomor_kursi:
                kursi[i][j] = 0

    print("\n======= Struk Pemesanan Tiket =======")
    print(f"Nama              : {nama}")
    print(f"Nomor Kursi       : {nomor_kursi}")
    print(f"Kategori          : {kategori}")
    print(f"Harga             : Rp{harga:,}")
    print(f"Tanggal Pemesanan : {tanggal}")
    print(f"Metode Pembayaran : {metode_pembayaran}")
    print(f"Password          : {password}")
    print("-------------------------------------")

sisa_kursi = {"VVIP": kategori_kursi["VVIP"], "VIP": kategori_kursi["VIP"], "Reguler": kategori_kursi["Reguler"], "Ekonomi": kategori_kursi["Ekonomi"]}

for data in pemesanan:
    kategori = data["kategori"]
    sisa_kursi[kategori] -= 1

print("\nSisa kursi per kategori :")
for kategori in sisa_kursi:
    print(f"{kategori}: {sisa_kursi[kategori]}")

print("\nLayout Kursi Setelah Pemesanan :\n")
for i in range(m):
    for j in range(n):
        print(kursi[i][j], end="\t")
    print()

print("\n===== Terima kasih telah melakukan reservasi! =====")