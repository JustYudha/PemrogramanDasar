def hitung_IMT(weight, height):
    hasil = weight / (height**2)
    print("Bentar Ya Di Hitung")
    return hasil

while True:
    Nama = input("Masukan Nama: ")
    berat = float(input("Masukan Berat badan: "))
    tinggi = float(input("Masukan Tinggi Anda dalam meter: "))
    Penghitung = hitung_IMT(berat,tinggi)
    print("Halo  {Nama}")
    if Penghitung < 18.5:
        print("Anda Masuk Kategori Underweight")
    elif 18.5 <= Penghitung < 25:
        print("Anda Masuk Kategori Normal weight ")
    elif 25 <= Penghitung < 30:
        print("Anda Masuk Kategori Over weight ")
    elif Penghitung >= 30:
        print("Anda Masuk Kategori Obesity! ")
    ulang = input("apakah ingin menlanjutkan? (y/n): ").lower()
    if ulang != "y" :
        print("Selesai.")
        break