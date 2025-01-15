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


print("Seluruh Data Panen:")
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    for tanaman, jumlah in data['hasil_panen'].items():
        print(f"  {tanaman.capitalize()}: {jumlah}")
    print()


jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung dari lokasi2 (Kebun B): {jumlah_jagung_lokasi2}\n")


nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}\n")


hasil_padi = {}
hasil_kedelai = {}

for lokasi, data in data_panen.items():
    hasil_padi[data['nama_lokasi']] = data['hasil_panen']['padi']
    hasil_kedelai[data['nama_lokasi']] = data['hasil_panen']['kedelai']

print("Hasil Panen Padi:")
print(hasil_padi)
print("\nHasil Panen Kedelai:")
print(hasil_kedelai)
print()


print("Status Lokasi:")
for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {nama_lokasi} dalam kondisi baik.")
