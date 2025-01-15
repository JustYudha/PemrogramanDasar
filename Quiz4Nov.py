jumlah_pasien = int(input("Masukkan Jumlah pasiennya : "))

nama_pasien = []
tekanan_sistolik = []
tekanan_diastolik = []

for i in range(jumlah_pasien):
    print(f"\nMasukkan Informasi pasien ke-{i+1}:")
    nama = input("Nama: ")
    sistolik = int(input("Tekanan darah sistolik: "))
    diastolik = int(input("Tekanan darah diastolik: "))

    nama_pasien.append(nama)
    tekanan_sistolik.append(sistolik)
    tekanan_diastolik.append(diastolik)

rata_sistolik = sum(tekanan_sistolik) / jumlah_pasien
rata_diastolik = sum(tekanan_diastolik) / jumlah_pasien

print("\nRata-rata tekanan darah:")
print(f"Sistolik: {rata_sistolik:.2f}")
print(f"Diastolik: {rata_diastolik:.2f}")
print("\nPasien dengan tekanan darah tinggi (sistolik > 140 atau diastolik > 90):")
hipertensi_ditemukan = False
for i in range(jumlah_pasien):
    if tekanan_sistolik[i] > 140 or tekanan_diastolik[i] > 90:
        print(f"{nama_pasien[i]}")
        hipertensi_ditemukan = True

if not hipertensi_ditemukan:
    print("Tidak ada pasien dengan hipertensi.")