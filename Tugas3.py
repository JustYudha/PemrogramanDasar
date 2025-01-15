# Program Rekomendasi Asupan Air Harian

# Meminta input usia dan jenis kelamin dari pengguna
usia = int(input("Masukkan usia Anda: "))
jenis_kelamin = input("Masukkan jenis kelamin Anda (Laki-laki/Perempuan): ")

# Memberikan rekomendasi berdasarkan usia dan jenis kelamin
if usia < 2:
    print("Masih diberi ASI.")
elif 3 <= usia <= 18:
    if jenis_kelamin.lower() == "laki-laki":
        print("Rekomendasi asupan air harian: 1.6 liter")
    elif jenis_kelamin.lower() == "perempuan":
        print("Rekomendasi asupan air harian: 1.4 liter")
elif 18 < usia < 64:
    if jenis_kelamin.lower() == "laki-laki":
        print("Rekomendasi asupan air harian: 2.5 liter")
    elif jenis_kelamin.lower() == "perempuan":
        print("Rekomendasi asupan air harian: 2.0 liter")
elif usia >= 65:
    if jenis_kelamin.lower() == "laki-laki":
        print("Rekomendasi asupan air harian: 2.0 liter")
    elif jenis_kelamin.lower() == "perempuan":
        print("Rekomendasi asupan air harian: 1.8 liter")
else:
    print("Jenis kelamin tidak valid.")
