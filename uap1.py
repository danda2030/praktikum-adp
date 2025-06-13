# import os
# import math
# import time
# import tkinter as tk
# from tkinter import messagebox
# from tkinter import simpledialog
# from tkinter import filedialog
# import matplotlib.pyplot as plt
# import pygame

# # Inisialisasi pygame mixer untuk musik
# pygame.mixer.init()
# def putar_musik():
#     try:
#         pygame.mixer.music.load("musik.mp3")  # pastikan file musik.mp3 ada di direktori yang sama
#         pygame.mixer.music.play(-1)  # -1 agar musik berulang terus
#     except Exception as e:
#         print(f"Gagal memutar musik: {e}")

# # Fungsi untuk menghitung BMI
# def hitung_bmi(berat, tinggi):
#     tinggi_meter = tinggi / 100
#     bmi = berat / (tinggi_meter ** 2)
#     return round(bmi, 2)

# # Fungsi untuk menghitung BMR
# def hitung_bmr(jk, berat, tinggi, usia):
#     if jk == 'L':
#         return round(88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia), 2)
#     else:
#         return round(447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia), 2)

# # Fungsi untuk menghitung kebutuhan kalori berdasarkan aktivitas
# def kebutuhan_kalori(bmr, aktivitas):
#     faktor = {
#         '1': 1.2,
#         '2': 1.375,
#         '3': 1.55,
#         '4': 1.725,
#         '5': 1.9
#     }
#     return round(bmr * faktor[aktivitas], 2)

# # Fungsi untuk menghitung Body Fat %
# def hitung_body_fat(jk, tinggi, leher, pinggang, pinggul=None):
#     if jk == 'L':
#         bf = 495 / (1.0324 - 0.19077 * math.log10(pinggang - leher) + 0.15456 * math.log10(tinggi)) - 450
#     else:
#         bf = 495 / (1.29579 - 0.35004 * math.log10(pinggang + pinggul - leher) + 0.22100 * math.log10(tinggi)) - 450
#     return round(bf, 2)

# # Fungsi menampilkan emoji sesuai BMI
# def emoji_bmi(bmi):
#     if bmi < 18.5:
#         return "🦴 Underweight"
#     elif 18.5 <= bmi < 25:
#         return "💪 Normal"
#     elif 25 <= bmi < 30:
#         return "🍔 Overweight"
#     else:
#         return "🏥 Obese"

# # Fungsi untuk menyimpan riwayat ke file
# def simpan_riwayat(data):
#     with open("riwayat.txt", "a") as f:
#         f.write(data + "\n")

# # Fungsi untuk menampilkan grafik berat badan
# def tampilkan_grafik(riwayat):
#     if not riwayat:
#         messagebox.showinfo("Info", "Belum ada data riwayat!")
#         return
#     tanggal = [x[0] for x in riwayat]
#     berat = [x[1] for x in riwayat]
#     plt.plot(tanggal, berat, marker='o')
#     plt.title("Grafik Berat Badan")
#     plt.xlabel("Tanggal")
#     plt.ylabel("Berat (kg)")
#     plt.grid()
#     plt.show()

# # Fungsi utama GUI
# def jalankan_gui():
#     putar_musik()
#     root = tk.Tk()
#     root.title("Kalkulator Kalori - Tugas Akhir Praktikum")
#     root.geometry("500x650")
#     root.configure(bg="#f2f2f2")

#     riwayat_array_2d = []

#     def hitung():
#         try:
#             nama = ent_nama.get()
#             jk = var_jk.get()
#             usia = int(ent_usia.get())
#             berat = float(ent_berat.get())
#             tinggi = float(ent_tinggi.get())
#             aktivitas = var_aktivitas.get()
#             leher = float(ent_leher.get())
#             pinggang = float(ent_pinggang.get())
#             pinggul = float(ent_pinggul.get()) if jk == 'P' else None
#             tujuan = var_tujuan.get()
            
#             bmi = hitung_bmi(berat, tinggi)
#             bmr = hitung_bmr(jk, berat, tinggi, usia)
#             kalori = kebutuhan_kalori(bmr, aktivitas)
#             kalori_tujuan = kalori - 500 if tujuan == '1' else kalori + 500 if tujuan == '3' else kalori
#             label_tujuan = "Menurunkan" if tujuan == '1' else "Menambah" if tujuan == '3' else "Menjaga"
#             body_fat = hitung_body_fat(jk, tinggi, leher, pinggang, pinggul)

#             hasil = f"{nama}: BMI={bmi}, BMR={bmr}, Kalori={kalori}, Tujuan={label_tujuan}, Body Fat={body_fat}%"
#             simpan_riwayat(hasil)
#             riwayat_array_2d.append([time.strftime("%d-%m-%Y"), berat])

#             teks_hasil.set(
#                 f"BMI: {bmi} ({emoji_bmi(bmi)})\n"
#                 f"BMR: {bmr} kal/hari\n"
#                 f"Kalori harian: {kalori} kal/hari\n"
#                 f"Tujuan ({label_tujuan}): {kalori_tujuan} kal/hari\n"
#                 f"Body Fat: {body_fat}%"
#             )
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     # Label dan Entry
#     tk.Label(root, text="Nama:").pack()
#     ent_nama = tk.Entry(root)
#     ent_nama.pack()

#     tk.Label(root, text="Jenis Kelamin (L/P):").pack()
#     var_jk = tk.StringVar(value='L')
#     tk.Entry(root, textvariable=var_jk).pack()

#     for teks, var in zip(["Usia", "Berat (kg)", "Tinggi (cm)", "Leher (cm)", "Pinggang (cm)", "Pinggul (cm) [perempuan saja]"],
#                          ["usia", "berat", "tinggi", "leher", "pinggang", "pinggul"]):
#         tk.Label(root, text=f"{teks}:").pack()
#         globals()[f"ent_{var}"] = tk.Entry(root)
#         globals()[f"ent_{var}"].pack()

#     tk.Label(root, text="Aktivitas (1-5):").pack()
#     var_aktivitas = tk.StringVar(value='1')
#     tk.Entry(root, textvariable=var_aktivitas).pack()

#     tk.Label(root, text="Tujuan (1=Turun, 2=Jaga, 3=Naik):").pack()
#     var_tujuan = tk.StringVar(value='2')
#     tk.Entry(root, textvariable=var_tujuan).pack()

#     tk.Button(root, text="Hitung", command=hitung, bg="green", fg="white").pack(pady=10)
#     tk.Button(root, text="Lihat Grafik", command=lambda: tampilkan_grafik(riwayat_array_2d)).pack()

#     teks_hasil = tk.StringVar()
#     tk.Label(root, textvariable=teks_hasil, bg="#f2f2f2", fg="blue", font=("Arial", 10), justify="left").pack(pady=10)

#     root.mainloop()

# if __name__ == "_main_":
#     print("Program dimulai...")
#     jalankan_gui()
import math
import time

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    tinggi_meter = tinggi / 100
    bmi = berat / (tinggi_meter ** 2)
    return round(bmi, 2)

# Fungsi untuk menghitung BMR
def hitung_bmr(jk, berat, tinggi, usia):
    if jk.upper() == 'L':
        return round(88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia), 2)
    else:
        return round(447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia), 2)

# Fungsi untuk menghitung kebutuhan kalori berdasarkan aktivitas
def kebutuhan_kalori(bmr, aktivitas):
    faktor = {
        '1': 1.2,
        '2': 1.375,
        '3': 1.55,
        '4': 1.725,
        '5': 1.9
    }
    return round(bmr * faktor.get(aktivitas, 1.2), 2)

# Fungsi untuk menghitung Body Fat %
def hitung_body_fat(jk, tinggi, leher, pinggang, pinggul=None):
    if jk.upper() == 'L':
        bf = 495 / (1.0324 - 0.19077 * math.log10(pinggang - leher) + 0.15456 * math.log10(tinggi)) - 450
    else:
        bf = 495 / (1.29579 - 0.35004 * math.log10(pinggang + pinggul - leher) + 0.22100 * math.log10(tinggi)) - 450
    return round(bf, 2)

# Fungsi menampilkan emoji sesuai BMI
def emoji_bmi(bmi):
    if bmi < 18.5:
        return "🦴 Underweight"
    elif 18.5 <= bmi < 25:
        return "💪 Normal"
    elif 25 <= bmi < 30:
        return "🍔 Overweight"
    else:
        return "🏥 Obese"

# Fungsi untuk menyimpan ke file
def simpan_riwayat(data):
    with open("riwayat_terminal.txt", "a") as f:
        f.write(data + "\n")

# Fungsi utama versi terminal
def jalankan_terminal():
    riwayat_array_2d = []
    while True:
        print("\n=== Kalkulator Kalori (Versi Terminal) ===")
        nama = input("Nama: ")
        jk = input("Jenis Kelamin (L/P): ").strip().upper()
        usia = int(input("Usia: "))
        berat = float(input("Berat (kg): "))
        tinggi = float(input("Tinggi (cm): "))
        leher = float(input("Lingkar leher (cm): "))
        pinggang = float(input("Lingkar pinggang (cm): "))
        pinggul = None
        if jk == 'P':
            pinggul = float(input("Lingkar pinggul (cm): "))

        print("Tingkat Aktivitas: 1=Sangat rendah, 2=Rendah, 3=Sedang, 4=Aktif, 5=Sangat aktif")
        aktivitas = input("Pilih (1-5): ").strip()

        print("Tujuan: 1=Turun BB, 2=Jaga BB, 3=Naik BB")
        tujuan = input("Pilih tujuan (1/2/3): ").strip()

        bmi = hitung_bmi(berat, tinggi)
        bmr = hitung_bmr(jk, berat, tinggi, usia)
        kalori = kebutuhan_kalori(bmr, aktivitas)
        body_fat = hitung_body_fat(jk, tinggi, leher, pinggang, pinggul)

        if tujuan == '1':
            kalori_tujuan = kalori - 500
            label_tujuan = "Menurunkan"
        elif tujuan == '3':
            kalori_tujuan = kalori + 500
            label_tujuan = "Menambah"
        else:
            kalori_tujuan = kalori
            label_tujuan = "Menjaga"

        print("\n--- Hasil Perhitungan ---")
        print(f"BMI: {bmi} ({emoji_bmi(bmi)})")
        print(f"BMR: {bmr} kal/hari")
        print(f"Kebutuhan Kalori Harian: {kalori} kal")
        print(f"Tujuan Anda ({label_tujuan} berat): {kalori_tujuan} kal")
        print(f"Persentase Lemak Tubuh (Body Fat): {body_fat}%")

        tanggal = time.strftime("%d-%m-%Y")
        riwayat_array_2d.append([tanggal, berat])
        hasil = f"{tanggal} - {nama}: BMI={bmi}, BMR={bmr}, Kalori={kalori}, Tujuan={label_tujuan}, Body Fat={body_fat}%"
        simpan_riwayat(hasil)

        lanjut = input("\nHitung lagi? (y/n): ").lower()
        if lanjut != 'y':
            print("Terima kasih telah menggunakan Kalkulator Kalori Terminal 🙂")
            break

if __name__ == "__main__":
    jalankan_terminal()
