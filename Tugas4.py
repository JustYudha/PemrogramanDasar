for i in range(3):

    Nama = input("Masukan Nama: ")
    Angka = int(input("Masukan Angka 1-4: "))

    match Angka:
        case 1 :
            print(Nama)
            # Input suhu tubuh dalam derajat Celsius
            suhu_tubuh = float(input("Masukan Suhu Tubuh: "))

            # Input detak jantung per menit
            detak_jantung = int(input("Masukan Detak Jantung: "))

            # Mengecek apakah suhu tubuh di atas normal
            if suhu_tubuh > 37.5:
                print("Suhu tubuh di atas normal.")
                
                # Mengecek apakah suhu tubuh sangat tinggi
                if (suhu_tubuh > 39) & (suhu_tubuh < 50) :
                    print("Harus Segera di Rawat.")   
                # Mengecek detak jantung jika suhu tubuh tidak terlalu tinggi
                else:
                    print("Cukup Istirahat Saja.")
                    # Mengecek apakah detak jantung terlalu tinggi
                    if detak_jantung > 100:
                        print("Detak jantung terlalu tinggi, butuh pemeriksaan lebih lanjut.")
                    else:
                        print("Detak jantung normal, perbanyak istirahat dan minum cairan.")
            else:
                print("Suhu tubuh normal, tidak ada tindakan khusus yang diperlukan.")
        case 2:
            sistolik = int(input("Masukan Sistolik(mmHG): "))
            diastolik = int(input("Masukan Diastolik(mmHG): "))
            denyut_nadi = float(input("Masukan Denyut Nadi(bpm): "))
            print(Nama )

            if sistolik > 180 or diastolik > 120:
                    print("Segera Cari Bantuan MEdis Anda Krisis Hipertensi")
            elif sistolik > 140 or diastolik > 90:
                    print("Konsultasi Ke Dokter mengenai Hipertensi")
            elif (sistolik > 120 ) & (sistolik < 139) or (diastolik > 80) & (diastolik < 89):
                    print("Anda Sedang Dalam Kondisi Hipertensi")
            elif sistolik < 120 and diastolik < 80:
                print("Tekanan Darah Anda Normal")
                if denyut_nadi > 100:
                        print("Disarankan Periksa Kesehatan Jantung")
                elif denyut_nadi < 60:
                        print("Disarankan Periksa Apakah ada Gejala lain yang mengiringi bradikardia")
                elif denyut_nadi > 60 and denyut_nadi < 100:
                        print("Denyut Nadi Anda Normal")
        case 3:
            print("Masih Kosong hehe. ")
        case _:
            print("Masukan angka yang valid")



