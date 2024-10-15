import pandas as pd


data = {'Öğrenci Adı': ['ayhan', 'beyhan', 'ceyhan', 'deyhan'],
        'Soyadı': ['acar', 'kapar', 'sayar', 'sozel'],
        'Sınav Notu': [70, 10, 89, 60]}

# DataFrame oluşturma
df = pd.DataFrame(data)

# Başarılı öğrencileri filtreleme
basarili_ogrenciler = df[df['Sınav Notu'] > 60][['Öğrenci Adı', 'Soyadı']]

print("Başarılı Öğrenciler:")
print(basarili_ogrenciler)

# Okul numarası verilerini oluşturma
okul_numaralari = [101, 102, 103, 104]

# Okul numarası sütununu DataFrame'e ekleme
df['Okul Numarası'] = okul_numaralari

okul_no = df[df['Okul Numarası'] < 103][['Öğrenci Adı']]
print("Okul numarası 103'ten küçük olan öğrencilerin adları:\n", okul_no)



