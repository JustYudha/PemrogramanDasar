data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

#no.1 (Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing)
for a, b in data_panen.items():
    print(f"lokasi{a}")
    print(f"nama lokasi: {b['nama_lokasi']}")
    print("hasil panen: ")
    for c,d in b['hasil_panen'].items():
        print(f" > {c}:{d}")
        
#no.2 (Tampilkan jumlah hasil panen jagung dari lokasi2)
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"jumlah hasil panen jagung: {hasil_jagung_lokasi2} kg ")

#no.3 (Tampilkan nama lokasi dari lokasi3)
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"nama lokasi: {nama_lokasi3} ")

#no.4 (Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda)
padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']

padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']

padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']

padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']

padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print("Padi Lokasi 1:", padi_lokasi1, "& Kedelai Lokasi 1:", kedelai_lokasi1)
print("Padi Lokasi 2:", padi_lokasi2, "& Kedelai Lokasi 2:", kedelai_lokasi2)
print("Padi Lokasi 3:", padi_lokasi3, "& Kedelai Lokasi 3:", kedelai_lokasi3)
print("Padi Lokasi 4:", padi_lokasi4, "& Kedelai Lokasi 4:", kedelai_lokasi4)
print("Padi Lokasi 5:", padi_lokasi5, "& Kedelai Lokasi 5:", kedelai_lokasi5)

#no.5 (Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi)

#jumlah hasil panen padi
jumlah_padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
jumlah_padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
jumlah_padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
jumlah_padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
jumlah_padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']

#jumlah hasil panen kedelai
jumlah_kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']
jumlah_kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']
jumlah_kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']
jumlah_kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']
jumlah_kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

print("Jumlah Padi dan Kedelai per Lokasi:")
print(f"Lokasi 1 > Padi: {jumlah_padi_lokasi1} & Kedelai: {jumlah_kedelai_lokasi1}")
print(f"Lokasi 2 > Padi: {jumlah_padi_lokasi2} & Kedelai: {jumlah_kedelai_lokasi2}")
print(f"Lokasi 3 > Padi: {jumlah_padi_lokasi3} & Kedelai: {jumlah_kedelai_lokasi3}")
print(f"Lokasi 4 > Padi: {jumlah_padi_lokasi4} & Kedelai: {jumlah_kedelai_lokasi4}")
print(f"Lokasi 5 > Padi: {jumlah_padi_lokasi5} & Kedelai: {jumlah_kedelai_lokasi5}")

#no.6 (Buat Percabangan)

for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    hasil_panen = data['hasil_panen']
    padi = hasil_panen['padi']
    jagung = hasil_panen['jagung']
    
    if padi > 1300 or jagung > 800:
        kondisi = "memerlukan perhatian khusus"
    else:
        kondisi = "dalam kondisi baik"
    
    print(f"Lokasi: {nama_lokasi} > Kondisi: {kondisi}")