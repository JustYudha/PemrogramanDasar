#Soal 1
jumlah_lokasi = int(input("Masukkan jumlah lokasi pengumpulan sampah: "))

#Soal 3
daftar_nama = []
daftar_plastik = []
daftar_organik = []
daftar_logam = []

#Soal 2
for i in range(jumlah_lokasi):
    print(f"\nMasukkan data untuk lokasi {i + 1}:")
    nama = input("Nama lokasi: ")
    plastik = float(input("Jumlah sampah plastik (kg): "))
    organik = float(input("Jumlah sampah organik (kg): "))
    logam = float(input("Jumlah sampah logam (kg): "))

    #Soal 3
    daftar_nama.append(nama)
    daftar_plastik.append(plastik)
    daftar_organik.append(organik)
    daftar_logam.append(logam)

#Soal 4
rata_rata_plastik = sum(daftar_plastik) / jumlah_lokasi
rata_rata_organik = sum(daftar_organik) / jumlah_lokasi
rata_rata_logam = sum(daftar_logam) / jumlah_lokasi

#Soal 4
print("\nRata-rata sampah yang terkumpul:")
print(f"Plastik: {rata_rata_plastik:.2f} kg")
print(f"Organik: {rata_rata_organik:.2f} kg")
print(f"Logam: {rata_rata_logam:.2f} kg")

#Soal 5
lokasi_berlebih = []
lokasi_aman = []

for i in range(jumlah_lokasi):
    if daftar_plastik[i] > 500 or daftar_organik[i] > 300:
        lokasi_berlebih.append(daftar_nama[i])
    else:
        lokasi_aman.append(daftar_nama[i])

#Soal 5
print("\nLokasi dengan sampah berlebih:")
if lokasi_berlebih:
    for lokasi in lokasi_berlebih:
        print(f"- {lokasi}")
else:
    print("Tidak ada lokasi dengan sampah berlebih.")

print("\nLokasi dalam kisaran aman:")
if lokasi_aman:
    for lokasi in lokasi_aman:
        print(f"- {lokasi}")
else:
    print("Tidak ada lokasi dalam kisaran aman.")
