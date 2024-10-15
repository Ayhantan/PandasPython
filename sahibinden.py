import pandas as pd

# Verilen veriler
veriler = {
    'Kategori': ['Emlak', 'Araç', ....],
    'Yoğun İlgi': ['En yoğun ilgiyi görmüştür', 'En çok karşılaştırılan ',.....],
    'İlan Sayısı': ['357,133,407 m² emlak ilanı', ....]
    'araç markası': ['Volkswagen Passat, Ford Focus, Toyota Corolla, Opel Astra, Renault Megane ve Renault Clio,..........']
    "Karşılaştırma Sayısı": [100, 90, 80, 70, 60, 50, 30]
}

df = pd.DataFrame(veriler)

cevap_1 = df[df["Yoğun İlgi"] == "En yoğun ilgiyi görmüştür"]
print("Soru 1: Sahibinden.com'da", cevap_1["Kategori"].values[0], cevap_1["Yoğun İlgi"].values[0], "ve bu kategoride toplam", cevap_1["İlan Sayısı"].values[0], "verilmiştir.")

# En çok karşılaştırılan araçları ve karşılaştırma sayılarını bulma
en_cok_karsilastirilan = df.sort_values(by="Karşılaştırma Sayısı", ascending=False).head(5)

# Cevabı yazdırma
print("Soru 2: 2021 yılında sahibinden.com'da en çok", ", ".join(en_cok_karsilastirilan["Araçlar"].values), "karşılaştırılmıştır.")
print("Bu araçlar en popüler karşılaştırmalar arasında yer almaktadır.")