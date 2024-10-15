import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını yükle
df = pd.read_csv('kitaplar.csv')
# Veri setini göster
print(df.head())
#cvs oku ve verisetine dönüştür
# Özet istatistikleri hesapla
summary_statistics = df.describe()
print(summary_statistics)
# Histogram çiz
plt.hist(df['Published Date'], bins=40, color='skyblue', edgecolor='black')
plt.title('Kitapların Yayınlanma Tarihlerine Göre Dağılımı')
plt.xlabel('Yayınlanma Tarihi')
plt.ylabel('Kitap Sayısı')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()