import numpy as np

kitap_fiyatlari = np.array([24,45,67,59,90,70])

satis_adetleri = np.array([10,5,8,12,3,7])

kategoriler = np.array(['roman', 'bilim', 'tarih', 'roman', 'psikoloji', 'tarih'])

toplam_gelir = kitap_fiyatlari * satis_adetleri
print("Toplam gelir:",kategoriler, '\n', toplam_gelir, )

ortalama_fiyat = np.mean(kitap_fiyatlari)
max_fiyat = np.max(kitap_fiyatlari)
min_fiyat = np.min(kitap_fiyatlari)
print("Ortalama fiyat:", ortalama_fiyat, 'TL')
print("En yüksek fiyat:", max_fiyat, 'TL')
print("En düşük fiyat:", min_fiyat, 'TL')

romanlar = kitap_fiyatlari[kategoriler == 'roman']
print("Roman kitaplarının fiyatları:", romanlar)
roman_satis = satis_adetleri[kategoriler == 'roman']
print("Roman kitaplarının satış adetleri:", roman_satis)
roman_toplam_gelir = romanlar * roman_satis
print("Roman kitaplarının toplam geliri:", roman_toplam_gelir)


tarih_satis = satis_adetleri[kategoriler == 'tarih']
print("Tarih kitaplarının satış adetleri:", tarih_satis)

veri = np.array([kitap_fiyatlari,satis_adetleri])
veri_reshaped = np.reshape(veri, (2,6))
print("Veri reshape edilmiş hali:\n", veri_reshaped)

