print("=======SELAMAT DATANG========")
print("=====DI WARTEG KELUARGA======")
print("=====DAFTAR MENU MAKANAN=====")
print("--------------------")
print("1. Paket A = Ayam Kecap + Nasi Putih + Es Jeruk")
print(" Harga : Rp 40.000,\n ")
print("2. Paket B = Ayam Bakar + Nasi Putih + Es Jeruk")
print(" Harga : Rp 40.000,\n ")
print("3. Paket C = Mie Goreng + Nasi Putih + Es Jeruk")
print(" Harga : Rp 25.000,\n ")
print("4. Paket D = Soto Ayam  + Nasi Putih + Es Jeruk")
print(" Harga : Rp 30.000,\n ")
print("5. Paket E = Pecel Ayam + Nasi Putih + Es Jeruk")
print(" Harga : Rp 40.000,\n ")

nama = input(" Pembelian Atas Nama : ") 
no_telepon = int(input(" Masukan No Telepon : "))
alamat = input(" Masukan Alamat pengiriman : ")

pilihan_paket = input(" mau pilih paket yang mana (A/B/C/D/E) :").upper()
jumlah_paket = int(input(" jumlah paket yang di inginkan : "))

if pilihan_paket == "A":
    harga_paket =  40000
    isi_paket = "Ayam Kecap + Nasi Putih + Es Jeruk"
elif pilihan_paket == "B":
    harga_paket =  40000
    isi_paket = "Ayam Bakar + Nasi Putih + Es Jeruk"
elif pilihan_paket == "C":
    harga_paket =  25000
    isi_paket = "Mie Goreng + Nasi Putih + Es Jeruk"
elif pilihan_paket == "D":
    harga_paket =  30000
    isi_paket = "Soto Ayam  + Nasi Putih + Es Jeruk"
elif pilihan_paket == "E":
    harga_paket =  40000
    isi_paket = "Pecel Ayam + Nasi Putih + Es Jeruk"
else:
    print("Paket tidak tersedia")
    exit()

total_harga = harga_paket * jumlah_paket
pajak = total_harga * 0.10
biaya_pengantaran = " biaya pengantaran : "
if total_harga < 150000 :
    biaya_pengantaran = 25000
else :
    biaya_pengantaran = 0
total_akhir = total_harga + pajak + biaya_pengantaran


print("\n-----------------------------------------")
print("             STRUK PEMESANAN")
print("-----------------------------------------")
print(f"Nama             : {nama}")
print(f"Nomor Telepon    : {no_telepon}")
print(f"Alamat Pengiriman: {alamat}")
print("-----------------------------------------")
print("           DETAIL PESANAN")
print("-----------------------------------------")
print(f"Paket            : {pilihan_paket}")
print(f"Isi Paket        : {isi_paket}")
print(f"Jumlah           : {jumlah_paket}")
print(f"Total Harga      : Rp {total_harga}")
print(f"Pajak (10%)      : Rp {pajak}")
print(f"Biaya Pengantaran: Rp {biaya_pengantaran}")
print("-----------------------------------------")
print(f"TOTAL AKHIR      : Rp {total_akhir}")
print("-----------------------------------------")
print("Terima kasih telah memesan!")
