print("="*40)
print(" PROGRAM MENGHITUNG JARAK ANTAR TITIK ")
print("="*40)

n = int(input("\nmasukkan jumlah titik: "))
titik = []
for i in range (n):
    print(f"\nkoordinat titik ke-{i+1}: ")
    x = float(input(" titik x: "))
    y = float(input(" titik y: "))
    titik.append([x, y])
    
print("\nKumpulan titik:", titik)
print("\nJarak Antar titik:")
for i in range(n):
    for j in range(i + 1, n):
        dx = titik[j][0] - titik[i][0]
        dy = titik[j][1] - titik[i][1]
        jarak = (dx**2 + dy**2) ** 0.5

        print(f"jarak antara {titik[i]} dan {titik[j]} : {jarak:.3f}")