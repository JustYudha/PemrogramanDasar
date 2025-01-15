jumlah_pasien = int(input("Masukan jumlah pasien: "))
nama_pasien = []
tekanan_darah_sistolik = []

for i in range(jumlah_pasien):
    nama = input(f"Masukan nama pasien ke{i+1}: ")
    tekanan = float(input(f"Masukan tekanan darah sistolik untuk {nama}: "))
    nama_pasien.append(nama)
    tekanan_darah_sistolik.append(tekanan)

rata2_tekanan = sum(tekanan_darah_sistolik)/jumlah_pasien

pasien_di_atas_rata = []
for i in range(jumlah_pasien):
    if tekanan_darah_sistolik[i] > rata2_tekanan:
        pasien_di_atas_rata.append(nama_pasien[i])

ambang_batas = 140

print("\nHasil Analisis:")
print(f"Ambang batas tekanan darah: {ambang_batas}")
print(f"Rata-rata tekanan darah sistolik: {rata2_tekanan:.2f}")
print("Pasien dengan tekanan darah di atas rata-rata:")

for nama in pasien_di_atas_rata:
    print(f"-{nama}")
