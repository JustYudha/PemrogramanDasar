nilai_murid = {
    'murid1': {
        'nama': 'Alice',
        'usia': 20,
        'nilai': {
            'matematika': 88,
            'sains': 92,
            'bahasa_inggris': 85
        }
    },
    'murid2': {
        'nama': 'Bob',
        'usia': 22,
        'nilai': {
            'matematika': 78,
            'sains': 85,
            'bahasa_inggris': 80
        }
    },
    'murid3': {
        'nama': 'Charlie',
        'usia': 21,
        'nilai': {
            'matematika': 95,
            'sains': 90,
            'bahasa_inggris': 92
        }  
    }  
}

print("Daftar Semua Murid:")
for murid, data in nilai_murid.items():
    print(f"{data['nama']} - Usia: {data['usia']} - Nilai: {data['nilai']}")

print("\nNilai Matematika Murid 2:")
print(nilai_murid['murid2']['nilai']['matematika'])

print("\nNama Murid 3:")
print(nilai_murid['murid3']['nama'])

print("\nMasukkan Nilai Sains dan Bahasa Inggris:")

for murid, data in nilai_murid.items():
    sains = data['nilai']['sains']
    bahasa_inggris = data['nilai']['bahasa_inggris']
    print(f"{data['nama']} - Sains: {sains}, Bahasa Inggris: {bahasa_inggris}")
    
    if sains < 90 or bahasa_inggris < 80:
        print(f"{data['nama']} harus belajar lagi.")
    else:
        print(f"{data['nama']} aman.")