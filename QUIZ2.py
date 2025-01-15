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