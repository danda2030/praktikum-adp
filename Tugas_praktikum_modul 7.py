def input_data():
    data = []
    n = int(input("\nMasukkan jumlah praktikan: "))
    for i in range(n):
        print(f"\nPraktikan ke-{i+1}")
        nama = input(" Masukkan Nama praktikan: ")
        nim = input(" Masukkan NIM praktikan: ")
        pretest = int(input(" Masukkan nilai Pretest: "))
        postest = int(input(" Masukkan nilai Postest: "))
        tugas = int(input(" Masukkan nilai Tugas: "))
        bonus = int(input(" Masukkan nilai Bonus: "))
        data.append([nama, nim, pretest, postest, tugas, bonus, 0, 0])
    return data

def hitung(data):
    for p in data:
        akhir = 0.25 * p[2] + 0.25 * p[3] + 0.5 * p[4] + p[5]
        p[6] = akhir  
    return data

def rata_rata(data, indeks):
    total = 0
    for p in data:
        total += p[indeks]
    return total / len(data)

def urutkan(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j][6] < data[j+1][6]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        data[i][7] = i + 1 
    return data

def tampil(data):
    garis = "+" + "-"*10 + "+" + "-"*17 + "+" + "-"*14 + "+" + "-"*9*6 + "+"
    print("\n+ Data Praktikan +")
    print(garis)
    print("|{:^10}|{:^17}|{:^14}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
        "Ranking", "Nama", "NIM", "Pretest", "Postest", "Tugas", "Bonus", "Akhir"))
    print(garis)
    for p in data:
        print("|{:^10}|{:17}|{:14}|{:10.2f}|{:10.2f}|{:10.2f}|{:10.2f}|{:10.2f}|".format(
            p[7], p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
        print(garis)

    
    print("|{:^10}|{:17}|{:14}|{:10.2f}|{:10.2f}|{:10.2f}|{:10}|{:10.2f}|".format(
        "", "Rata-rata", "",
        rata_rata(data, 2),  
        rata_rata(data, 3), 
        rata_rata(data, 4),  
        "",
        rata_rata(data, 6)))  
    print(garis)

praktikan = input_data()
praktikan = hitung(praktikan)
praktikan = urutkan(praktikan)
tampil(praktikan)