import time
import os
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich.panel import Panel
from rich import print

console = Console()
# fungsi append kata kata berwarna
def add(text_obj, content="",  style=None, newline=False, blank_line=False):
    text_obj.append(content, style)
    if newline:
        text_obj.append("\n")
    if blank_line:
        text_obj.append("\n")

# Fungsi animasi loading
def loading(teks="Memproses"):
    for i in range(3):
        print(f"{teks}{'.' * (i+1)}", end='\r')
        time.sleep(0.5)
    print(" " * 20, end='\r')

# Fungsi saran kesehatan
def saran_kesehatan(jenis, hasil):
    if jenis == "BMI":
        if hasil < 16:
            text = Text()
            add(text,"KEKURUSAN PARAH","underline bold red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"Segera konsultasikan ke ")
            add(text,"dokter","yellow")
            add(text," atau ")
            add(text,"ahli gizi","yellow")
            add(text,". Risiko ")
            add(text,"malnutrisi serius","red")
            add(text," dan fungsi tubuh terganggu (lihat opsi 3 kalkulator ")
            add(text,"BMI", "bold cyan")
            add(text,").")
            return console.print(text, width=80)
        elif 16 <= hasil < 18.5:
            text = Text()
            add(text,"KEKURUSAN RINGAN-SEDANG","underline red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"tingkatkan ")
            add(text,"asupan nutrisi seimbang","green")
            add(text," dan  ")
            add(text,"tambahkan kalori","green")
            add(text," harian Anda untuk mencapai berat badan ")
            add(text,"ideal","bold green")
            add(text,".")
            return console.print(text, width=80)
        elif 18.5 <= hasil <= 25:
            text = Text()
            add(text,"IDEAL","underline bold green", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"BAGUS!","green")
            add(text," Terus pertahankan ")
            add(text,"pola makan seimbang","green")
            add(text," dan ")
            add(text,"olahraga teratur","green")
            add(text," untuk menjaga kesehatan tubuh.")
            return console.print(text, width=80)
        elif 25 < hasil <= 30:
            text = Text()
            add(text,"KEGEMUKAN","underline bold yellow", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"Perhatikan ")
            add(text,"pola makan","green")
            add(text," dan tingkatkan ")
            add(text,"aktivitas fisik","green")
            add(text," untuk menghindari kelebihan berat badan yang lebih serius.")
            return console.print(text, width=80)
        elif 30 < hasil <= 40:
            text = Text()
            add(text,"OBESITAS KELAS I & II","underline red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"Risiko kesehatan meningkat","red")
            add(text,". Disarakankan menurunkan berat badan secara bertahap dengan ")
            add(text,"pola makan seimbang","green")
            add(text," dan ")
            add(text,"olahraga teratur","green")
            add(text,".")
            return console.print(text, width=80)
        elif hasil > 40:
            text = Text()
            add(text,"OBESITAS KELAS III","underline bold red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"TERMASUK OBESITAS MORBID","red")
            add(text,". ")
            add(text,"Bahaya penyakit mengintai","red")
            add(text," (baca opsi 2 kalkulator ")
            add(text,"BMI", "bold cyan")
            add(text,"). Sangat disarankan untuk segera berkonsultasi dengan ")
            add(text,"dokter spesialis","yellow")
            add(text," untuk penanganan intensif.")
            return console.print(text, width=80)

# Fungsi menyimpan ke file .txt
def simpan_riwayat_kalori(data):
    with open("riwayat.txt", "a") as file:
        file.write(data + "\n")
def simpan_riwayat_bmi(jenis, hasil):
    with open("Riwayat_BMI.txt", "a") as file:
        file.write(f"{jenis}: {hasil:.2f}\n")
##### KALKULATOR BMI ✅
def pengenalan_bmi():
    console.rule("[bold cyan]📘 Pengenalan Tentang BMI")

    # Pengantar dalam panel
    wal = Text()
    wal.append("BMI", style="bold cyan")
    wal.append(" adalah pengukuran ")
    wal.append("KELANGSINGAN", style="green")
    wal.append(" atau ")
    wal.append("KEGEMUKAN", style="red")
    wal.append(" seseorang berdasarkan berat badan dan tinggi badan.\n")
    wal.append("Ini digunakan secara luas sebagai indikator umum untuk menentukan apakah seseorang memiliki berat badan yang sehat.\n")

    console.print(Panel(wal, title="📏 Apa itu BMI", expand=False, border_style="cyan"))

    # Penjelasan tambahan
    kir = Text()
    kir.append("Rentang ", style="")
    kir.append("BMI", style="bold cyan")
    kir.append(" bisa berbeda tergantung usia, wilayah, dan kondisi individu.\n")
    kir.append("Kadang dibagi lagi menjadi subkategori seperti ")
    kir.append("SANGAT KEKURANGAN BERAT BADAN", style="red")
    kir.append(" dan ")
    kir.append("SANGAT OBESITAS", style="red")
    kir.append(".\n")

    console.print(Panel(kir, title="📊 Variasi Rentang BMI", expand=False, border_style="bright_cyan"))

    # Tabel klasifikasi
    console.print("\n[bold]Berikut adalah klasifikasi [cyan]BMI[/cyan] berdasarkan [italic blue]World Health Organization (WHO)[/italic blue]:\n")
    table = Table(title="Klasifikasi BMI", header_style="bold magenta")
    table.add_column("Klasifikasi", style="yellow")
    table.add_column("Kisaran BMI - kg/m²", style="green")

    data = [
        ["Kekurusan Parah", "< 16"],
        ["Kekurusan Sedang", "16 - 17"],
        ["Kekurusan Ringan", "17 - 18.5"],
        ["Ideal", "18.5 - 25"],
        ["Kegemukan", "25 - 30"],
        ["Obesitas Kelas I", "30 - 35"],
        ["Obesitas Kelas II", "35 - 40"],
        ["Obesitas Kelas III", "> 40"]
    ]

    for row in data:
        table.add_row(*row)

    console.print(table)
    console.rule("[bold green]Selesai")
def hitung_bmi():
    berat = FloatPrompt.ask("⚖️  Masukkan berat badan Anda (kg)")
    hei = FloatPrompt.ask("📏 Masukkan tinggi badan Anda (cm)")
    tinggi = hei / 100
    bmi = berat / (tinggi ** 2)

    loading("Menghitung BMI...")

    # Tentukan kategori + warna
    if bmi < 16:
        kategori = "Kekurusan Parah"
        warna = "red"
    elif 16 <= bmi < 17:
        kategori = "Kekurusan Sedang"
        warna = "red"
    elif 17 <= bmi < 18.5:
        kategori = "Kekurusan Ringan"
        warna = "yellow"
    elif 18.5 <= bmi < 25:
        kategori = "Ideal"
        warna = "green"
    elif 25 <= bmi < 30:
        kategori = "Kegemukan"
        warna = "yellow"
    elif 30 <= bmi < 35:
        kategori = "Obesitas Kelas I"
        warna = "red"
    elif 35 <= bmi < 40:
        kategori = "Obesitas Kelas II"
        warna = "red"
    else:
        kategori = "Obesitas Kelas III"
        warna = "bold red"

    # Tampilkan hasil dengan rich table
    console.print("\n[bold cyan]✅ Hasil BMI Anda:[/bold cyan]\n")
    table = Table(show_header=False)
    table.add_row("Berat Badan", f"{berat:.1f} kg")
    table.add_row("Tinggi Badan", f"{hei:.1f} cm")
    table.add_row("Nilai BMI", f"[bold]{bmi:.2f}[/bold]")
    table.add_row("Kategori", f"[{warna}]{kategori}[/{warna}]")
    console.print(table)

    # Tampilkan saran kesehatan
    print("💡", end=" ")
    saran_kesehatan("BMI", bmi)

    # Simpan riwayat
    simpan_riwayat_bmi("BMI", bmi)
def risiko_kelebihan_berat_badan():
    console.rule("[bold red]⚠️ Risiko Kelebihan Berat Badan")

    # Paragraf pengantar
    wal = Text()
    wal.append("KELEBIHAN BERAT BADAN", style="bold red")
    wal.append(" dapat meningkatkan risiko berbagai penyakit dan masalah kesehatan serius.\n")
    wal.append("Berikut ini adalah daftar risiko tersebut, menurut ")
    wal.append("Centers for Disease Control and Prevention (CDC)", style="italic blue")
    wal.append(":\n")
    console.print(Panel(wal, title="📌 Pengantar", expand=False, border_style="red"))

    # Daftar risiko sebagai tabel
    table = Table(title="Risiko Kesehatan Akibat Kelebihan Berat Badan", header_style="bold magenta")
    table.add_column("No.", justify="center", style="cyan", width=5)
    table.add_column("Risiko", style="red")

    risiko_list = [
        "Tekanan darah tinggi",
        "Kolesterol tidak seimbang (LDL naik, HDL turun)",
        "Diabetes tipe II",
        "Penyakit jantung koroner",
        "Stroke",
        "Penyakit kandung empedu",
        "Osteoartritis (kerusakan sendi)",
        "Apnea tidur dan gangguan pernapasan",
        "Kanker (endometrium, payudara, ginjal, hati, kantong empedu)",
        "Kualitas hidup menurun",
        "Penyakit mental seperti depresi dan kecemasan",
        "Nyeri tubuh dan keterbatasan gerak",
        "Risiko kematian meningkat"
    ]

    for i, risiko in enumerate(risiko_list, 1):
        table.add_row(str(i), risiko)

    console.print(table)

    # Penutup
    kir = Text()
    kir.append("Kelebihan berat badan dapat menimbulkan ")
    kir.append("dampak negatif", style="red")
    kir.append(", bahkan dalam beberapa kasus bisa ")
    kir.append("berakibat fatal", style="red")
    kir.append(".\n")
    kir.append("Menjaga ")
    kir.append("BMI", style="bold cyan")
    kir.append(" di bawah 25 kg/m² dan berkonsultasi dengan ")
    kir.append("dokter", style="yellow")
    kir.append(" dapat membantu mempertahankan hidup yang lebih ")
    kir.append("sehat", style="green")
    kir.append(".\n")

    console.print(Panel(kir, title="🩺 Kesimpulan & Anjuran", expand=False, border_style="bright_red"))
    console.rule("[bold green]Selesai")
def risiko_kekurangan_berat_badan():
    console.rule("[bold red]⚠️ Risiko Kekurangan Berat Badan")

    # Paragraf pengantar
    wal = Text()
    wal.append("KEKURANGAN BERAT BADAN", style="bold red")
    wal.append(" dapat menimbulkan sejumlah risiko kesehatan yang serius, tidak kalah berbahaya dibandingkan kegemukan.\n")
    wal.append("Berikut ini adalah beberapa risiko yang perlu diketahui:\n")
    console.print(Panel(wal, title="📌 Pengantar", expand=False, border_style="red"))

    # Tampilkan risiko sebagai tabel berwarna
    table = Table(title="Risiko Kesehatan Akibat Kekurangan Berat Badan", header_style="bold magenta")
    table.add_column("No.", justify="center", style="cyan", width=5)
    table.add_column("Risiko", style="red")

    risiko_list = [
        "Malnutrisi, kekurangan vitamin, anemia",
        "Osteoporosis, tulang rapuh & mudah patah",
        "Penurunan daya tahan tubuh",
        "Masalah pertumbuhan anak & remaja",
        "Gangguan reproduksi pada wanita",
        "Risiko keguguran lebih tinggi",
        "Komplikasi pasca operasi",
        "Risiko kematian lebih tinggi secara umum"
    ]

    for i, risiko in enumerate(risiko_list, 1):
        table.add_row(str(i), risiko)

    console.print(table)

    # Paragraf penutup
    kir = Text()
    kir.append("Dalam beberapa kasus, ", style="")
    kir.append("kekurangan berat badan", style="bold red")
    kir.append(" bisa menjadi gejala dari kondisi serius seperti ")
    kir.append("anoreksia nervosa", style="red")
    kir.append(". Jika Anda atau orang terdekat mengalami tanda-tanda ini, sangat disarankan untuk berkonsultasi dengan ")
    kir.append("dokter", style="yellow")
    kir.append(" sesegera mungkin.\n")

    console.print(Panel(kir, title="🩺 Kesimpulan & Anjuran", expand=False, border_style="bright_red"))
    console.rule("[bold green]Selesai")

def kalkulator_bmi():
    while True:
        os.system("cls")

        # Header Panel
        console.print(Panel.fit(
            "[bold cyan]🧮 KALKULATOR BMI[/bold cyan]",
            subtitle="Pilih salah satu opsi di bawah ini",
            border_style="bright_blue"
        ))

        # Menu dengan warna
        console.print("[bold yellow]1.[/bold yellow] Pengenalan [cyan]BMI[/cyan]")
        console.print("[bold yellow]2.[/bold yellow] Risiko [red]kelebihan berat badan[/red]")
        console.print("[bold yellow]3.[/bold yellow] Risiko [red]kekurangan berat badan[/red]")
        console.print("[bold yellow]4.[/bold yellow] Hitung [cyan]BMI[/cyan]")
        console.print("[bold yellow]0.[/bold yellow] Kembali ke menu utama")

        pilihan = console.input("\n[bold]📥 Pilih opsi [0-4]: [/bold]")

        os.system("cls")

        if pilihan == '1':
            pengenalan_bmi()
        elif pilihan == '2':
            risiko_kelebihan_berat_badan()
        elif pilihan == '3':
            risiko_kekurangan_berat_badan()
        elif pilihan == '4':
            hitung_bmi()
        elif pilihan == '0':
            break
        else:
            console.print("[red]❌ Pilihan tidak valid. Coba lagi.[/red]")

        console.input("\n[bold cyan]Tekan Enter untuk kembali ke menu Kalkulator BMI...[/bold cyan]")

##### KALKULATOR KALORI
def input_data():
    console.rule("[bold cyan]🔢 Masukkan Data Anda")

    age = IntPrompt.ask("Umur")
    gender = Prompt.ask("Jenis kelamin", choices=["male", "female"])
    tinggi = FloatPrompt.ask("Tinggi badan (cm)", default=170)
    berat = FloatPrompt.ask("Berat badan (kg)", default=65)

    # Tabel aktivitas
    console.print("\n[bold cyan]Pilih tingkat aktivitas harian kamu:[/bold cyan]\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Kode", justify="center")
    table.add_column("Aktivitas")
    table.add_column("Keterangan")

    aktivitas_dict = {
        "1": {"nama": "BMR", "ket": "Tidak aktif sama sekali"},
        "2": {"nama": "Sedentary", "ket": "Sedikit atau tidak latihan"},
        "3": {"nama": "Light", "ket": "Latihan 1–3x/minggu"},
        "4": {"nama": "Moderate", "ket": "Latihan 4–5x/minggu"},
        "5": {"nama": "Active", "ket": "Latihan intens 3-4x/minggu"},
        "6": {"nama": "Very Active", "ket": "Latihan intens 6–7x/minggu"},
        "7": {"nama": "Extra Active", "ket": "Pekerjaan fisik atau Latihan sangat intens setiap hari"},
    }

    for kode, detail in aktivitas_dict.items():
        row = []
        for key in ["nama", "ket"]:
            row.append(detail[key])
        table.add_row(kode, *row)

    console.print(table)

    # Penjelasan tambahan
    console.print("\n[bold]Catatan:[/bold]")
    console.print("• [cyan]Latihan[/cyan]: 15–30 menit aktivitas dengan detak jantung meningkat.")
    console.print("• [cyan]Latihan intens[/cyan]: 45–120 menit aktivitas dengan detak jantung meningkat.")
    console.print("• [cyan]Latihan sangat[/cyan]: lebih dari 2 jam aktivitas dengan detak jantung meningkat.\n")

    activity_code = Prompt.ask("Masukkan kode aktivitas (1–7)", choices=[str(i) for i in range(1, 8)])
    return age, gender, tinggi, berat, int(activity_code)
def hitung_bmr(age, gender, tinggi, berat):
    if gender == "male":
        return 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * age)
    else:
        return 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * age)
def faktor_aktivitas(kode):
    return {
        1: 1.0,
        2: 1.2,
        3: 1.375,
        4: 1.465,
        5: 1.55,
        6: 1.725,
        7: 1.9
    }.get(kode, 1.2)
def tampilkan_hasil(bmr, tdee):
    console.rule("[bold green]📊 Hasil Perhitungan")
    table = Table(show_header=False)
    table.add_row("Basal Metabolic Rate (BMR)", f"[cyan]{round(bmr, 2)}[/cyan] kcal/hari")
    table.add_row("Total Daily Energy Expenditure (TDEE)", f"[green]{round(tdee, 2)}[/green] kcal/hari")
    console.print(table)

def hitung_kalori():
    age, gender, tinggi, berat, activity_code = input_data()
    bmr = hitung_bmr(age, gender, tinggi, berat)
    tdee = bmr * faktor_aktivitas(activity_code)
    tampilkan_hasil(bmr, tdee)
    simpan_riwayat_kalori(f"Kalkulator Kalori - BMR: {round(bmr, 2)} kalori, TDEE: {round(tdee, 2)} kalori")
    # Langsung tampilkan simulasi
    console.print("\n[bold cyan]🎯 Simulasi Tujuan[/bold cyan]")
    kalori_cutting_500 = tdee - 550
    kalori_cutting_250 = tdee - 275
    kalori_bulking_250 = tdee + 275
    kalori_bulking_500 = tdee + 550

    console.print(f"• [red]Cutting (-0,5 kg/minggu)[/red]: [bold]{round(kalori_cutting_500, 2)}[/bold] kcal/hari")
    console.print(f"• [red]Cutting (-0,25 kg/minggu)[/red]: [bold]{round(kalori_cutting_250, 2)}[/bold] kcal/hari")
    console.print(f"• [yellow]Maintenance[/yellow]: [bold]{round(tdee, 2)}[/bold] kcal/hari")
    console.print(f"• [green]Bulking (+0,25 kg/minggu)[/green]: [bold]{round(kalori_bulking_250, 2)}[/bold] kcal/hari")
    console.print(f"• [green]Bulking (+0,5 kg/minggu)[/green]: [bold]{round(kalori_bulking_500, 2)}[/bold] kcal/hari")
def penjelasan_kalori():
    console.rule("[bold cyan]📘 Penjelasan Kalori, BMR, dan TDEE")

    # Penjelasan Kalori
    kalori = Text()
    kalori.append("Kalori", style="bold yellow")
    kalori.append(" adalah satuan energi yang digunakan tubuh untuk berfungsi. Semua aktivitas, mulai dari bernapas hingga berolahraga, membutuhkan kalori.\n", style="")
    console.print(Panel(kalori, title="🔥 Apa itu Kalori", expand=False))

    # Penjelasan BMR
    bmr = Text()
    bmr.append("BMR (Basal Metabolic Rate)", style="bold cyan")
    bmr.append(" adalah jumlah kalori yang dibutuhkan tubuh untuk menjalankan fungsi dasar dalam keadaan istirahat total (seperti bernapas, detak jantung, fungsi organ).\n")
    console.print(Panel(bmr, title="💤 Apa itu BMR", expand=False))

    # Penjelasan TDEE
    tdee = Text()
    tdee.append("TDEE (Total Daily Energy Expenditure)", style="bold green")
    tdee.append(" adalah total kalori yang dibakar tubuh dalam sehari, termasuk BMR dan semua aktivitas fisik.\n")
    console.print(Panel(tdee, title="🏃‍♂️ Apa itu TDEE", expand=False))

    # Tabel Perbandingan
    table = Table(title="Perbandingan BMR vs TDEE", header_style="bold magenta")
    table.add_column("Komponen", style="cyan", justify="center")
    table.add_column("BMR", justify="center")
    table.add_column("TDEE", justify="center")

    table.add_row("Aktivitas Fisik", "❌ Tidak dihitung", "✅ Dihitung")
    table.add_row("Digunakan saat", "Tubuh istirahat total", "Sepanjang hari")
    table.add_row("Dipakai untuk", "Hitung dasar kalori", "Target kalori harian")
    table.add_row("Contoh Angka", "1500 kcal", "2000–2500 kcal")

    console.print(table)

    # Catatan Akhir
    console.print(Panel.fit(
        "[bold]Kesimpulan:[/bold]\n"
        "• Gunakan [cyan]BMR[/cyan] untuk tahu kebutuhan dasar tubuh.\n"
        "• Gunakan [green]TDEE[/green] untuk tahu berapa banyak kalori yang harus kamu konsumsi setiap hari, tergantung aktivitas.\n"
        "• Untuk [red]cutting[/red] → konsumsi di bawah TDEE.\n"
        "• Untuk [green]bulking[/green] → konsumsi di atas TDEE.",
        title="📌 Ringkasan", border_style="bright_blue"
    ))

    console.rule("[bold green]Selesai")
def kalkulator_kalori():
    while True:
        os.system("cls")

        # Header Panel
        console.print(Panel.fit(
            "[bold cyan]🔥 KALKULATOR KALORI[/bold cyan]",
            subtitle="Pilih salah satu",
            border_style="bright_blue"
        ))

        # Menu Pilihan
        console.print("[bold yellow]1.[/bold yellow] Hitung [green]kalori harian[/green]")
        console.print("[bold yellow]2.[/bold yellow] Penjelasan [cyan]Kalori, BMR, dan TDEE[/cyan]")
        console.print("[bold yellow]0.[/bold yellow] Kembali ke menu utama")

        pilihan = console.input("\n[bold]📥 Pilih opsi [0-2]: [/bold]")

        os.system("cls")

        if pilihan == '1':
            hitung_kalori()
        elif pilihan == '2':
            penjelasan_kalori()
        elif pilihan == '0':
            break
        else:
            console.print("[red]❌ Pilihan tidak valid. Silakan coba lagi.[/red]")

        console.input("\n[bold cyan]Tekan Enter untuk kembali ke menu Kalkulator Kalori...[/bold cyan]")

##### LIHAT RIWAYAT
def tampilkan_riwayat():
    console.rule("[bold blue]📂 Riwayat Perhitungan")
    
    # BMI
    if os.path.exists("Riwayat_BMI.txt"):
        console.print("[bold cyan]📘 Riwayat BMI:[/bold cyan]")
        with open("Riwayat_BMI.txt", "r") as f:
            for i, line in enumerate(f, 1):
                console.print(f"{i}. {line.strip()}")
    else:
        console.print("[red]Tidak ada riwayat BMI tersimpan.[/red]")

    # Kalori
    if os.path.exists("riwayat.txt"):
        console.print("\n[bold green]🔥 Riwayat Kalori:[/bold green]")
        with open("riwayat.txt", "r") as f:
            for i, line in enumerate(f, 1):
                console.print(f"{i}. {line.strip()}")
    else:
        console.print("[red]Tidak ada riwayat Kalori tersimpan.[/red]")

# Menu utama
def main():
    while True:
        os.system("cls")

        # Header Menu Utama
        console.print(Panel.fit(
            "[bold magenta]🧮 KALKULATOR KESEHATAN[/bold magenta]",
            subtitle="Pilih jenis kalkulator",
            border_style="bright_magenta"
        ))

        # Daftar Menu
        console.print("[bold yellow]1.[/bold yellow] Kalkulator [cyan]BMI[/cyan] (Indeks Massa Tubuh)")
        console.print("[bold yellow]2.[/bold yellow] Kalkulator [green]Kalori[/green] (BMR & TDEE)")
        console.print("[bold yellow]3.[/bold yellow] 📂 Lihat [blue]Riwayat[/blue] Penggunaan")
        console.print("[bold yellow]0.[/bold yellow] ❌ Keluar dari program")

        pilihan = console.input("\n[bold]📥 Pilih kalkulator [0-3]: [/bold]")

        os.system("cls")

        if pilihan == '1':
            kalkulator_bmi()
        elif pilihan == '2':
            kalkulator_kalori()
        elif pilihan == '3':
            tampilkan_riwayat()
            console.input("\n[bold cyan]Tekan Enter untuk kembali ke menu utama...[/bold cyan]")
        elif pilihan == '0':
            console.print("\n[bold green]👋 Terima kasih telah menggunakan Kalkulator Kesehatan! Jaga tubuhmu, jaga semangatmu![/bold green]")
            break
        else:
            console.print("[red]❌ Pilihan tidak valid. Silakan coba lagi.[/red]")
            console.input("\n[bold cyan]Tekan Enter untuk kembali ke menu utama...[/bold cyan]")

if __name__ == "__main__":
    main()