import time
import os

# Fungsi animasi loading
def loading(teks="Memproses"):
    for i in range(3):
        print(f"{teks}{'.' * (i+1)}", end='\r')
        time.sleep(0.5)
    print(" " * 20, end='\r')

# Fungsi saran kesehatan
def saran_kesehatan(jenis, hasil):
    if jenis == "BMI":
        if hasil < 18.5:
            return "Berat badan kurang. Cobalah pola makan sehat dan bergizi."
        elif 18.5 <= hasil <= 24.9:
            return "Berat badan ideal. Pertahankan gaya hidup sehat!"
        elif 25 <= hasil <= 29.9:
            return "Berat badan berlebih. Perhatikan asupan kalori dan rutin olahraga."
        else:
            return "Obesitas. Konsultasikan ke ahli gizi untuk penanganan lebih lanjut."
    elif jenis == "Kalori":
        return "Pastikan kebutuhan kalori sesuai aktivitas harian Anda."
    elif jenis == "BMR":
        return "Gunakan BMR untuk mengatur pola makan yang tepat."
    elif jenis == "Body Fat":
        return "Persentase lemak tubuh penting untuk kesehatan jantung dan metabolisme."
    return "Jaga selalu gaya hidup sehat!"

# Fungsi menyimpan ke file .txt
def simpan_riwayat(jenis, hasil):
    with open("riwayat_kalkulator.txt", "a") as file:
        file.write(f"{jenis}: {hasil:.2f}\n")

# Fungsi-fungsi kalkulasi
def hitung_bmi():
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (cm): ")) / 100
    bmi = berat / (tinggi ** 2)
    loading("Menghitung BMI")
    print(f"\n✅ BMI Anda: {bmi:.2f}")
    print("💡", saran_kesehatan("BMI", bmi))
    simpan_riwayat("BMI", bmi)

def hitung_bmr():
    gender = input("Jenis kelamin (L/P): ").lower()
    usia = int(input("Usia (tahun): "))
    berat = float(input("Berat badan (kg): "))
    tinggi = float(input("Tinggi badan (cm): "))
    if gender == 'l':
        bmr = 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia)
    loading("Menghitung BMR")
    print(f"\n✅ BMR Anda: {bmr:.2f} kalori/hari")
    print("💡", saran_kesehatan("BMR", bmr))
    simpan_riwayat("BMR", bmr)

def hitung_kalori():
    gender = input("Jenis kelamin (L/P): ").lower()
    usia = int(input("Usia (tahun): "))
    berat = float(input("Berat badan (kg): "))
    tinggi = float(input("Tinggi badan (cm): "))
    aktivitas = float(input("Tingkat aktivitas (1.2 - 1.9): "))
    if gender == 'l':
        bmr = 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia)
    kalori = bmr * aktivitas
    loading("Menghitung kebutuhan kalori")
    print(f"\n✅ Kebutuhan kalori harian Anda: {kalori:.2f} kalori")
    print("💡", saran_kesehatan("Kalori", kalori))
    simpan_riwayat("Kalori", kalori)

def hitung_body_fat():
    gender = input("Jenis kelamin (L/P): ").lower()
    usia = int(input("Usia: "))
    bmi = float(input("Masukkan nilai BMI: "))
    if gender == 'l':
        body_fat = (1.20 * bmi) + (0.23 * usia) - 16.2
    else:
        body_fat = (1.20 * bmi) + (0.23 * usia) - 5.4
    loading("Menghitung Body Fat")
    print(f"\n✅ Persentase lemak tubuh Anda: {body_fat:.2f}%")
    print("💡", saran_kesehatan("Body Fat", body_fat))
    simpan_riwayat("Body Fat", body_fat)

def tampilkan_riwayat():
    print("\n📜 Riwayat Perhitungan:")
    if os.path.exists("riwayat_kalkulator.txt"):
        with open("riwayat_kalkulator.txt", "r") as file:
            print(file.read())
    else:
        print("Belum ada riwayat tersimpan.")

# Menu utama
def main():
    while True:
        print("""
==============================
🧮 KALKULATOR KESEHATAN TERMINAL
==============================
1. Kalkulator BMI
2. Kalkulator BMR
3. Kalkulator Kalori
4. Kalkulator Body Fat
5. Lihat Riwayat
0. Keluar
""")
        pilihan = input("Pilih kalkulator (0-5): ")
        os.system("cls")
        if pilihan == '1':
            hitung_bmi()
        elif pilihan == '2':
            hitung_bmr()
        elif pilihan == '3':
            hitung_kalori()
        elif pilihan == '4':
            hitung_body_fat()
        elif pilihan == '5':
            tampilkan_riwayat()
        elif pilihan == '0':
            print("👋 Terima kasih telah menggunakan kalkulator kesehatan!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")
        input("\nTekan Enter untuk kembali ke menu utama...")
        os.system("cls")

if __name__ == "__main__":
    main()
