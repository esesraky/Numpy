import numpy as np

dizi1 = np. array([1,2,3,7,12])
dizi2 = np. array([4,5,6,8,9])

toplama = dizi1 + dizi2 # iki dizinin elemanlarını sırayla toplar.
çıkarma = dizi1 - dizi2 # iki dizinin elemanlarını sırayla çıkarır.
carpma = dizi1 * dizi2 # iki dizinin elemanlarını sırayla çarpar.
bölme = dizi1 / dizi2 # iki dizinin elemanlarını sırayla böler.
print("toplama:", toplama)
print("çıkarma:", çıkarma)
print("çarpma:", carpma)
print("bölme:", bölme)

toplam = np.sum(dizi1) # dizinin elemanlarını toplar.
carpim = np.prod(dizi1) # dizinin elemanlarını çarpar.
kare_al = np.square(dizi1) # dizinin elemanlarının karesini alır.
karekok = np.sqrt(dizi1) # dizinin elemanlarının karekökünü alır.
print("toplam:", toplam)
print("çarpım:", carpim)
print("kare_al:", kare_al)  
print("karekok:", karekok)

ortalama = np.mean(dizi1) # dizinin elemanlarının ortalamasını alır.
medyan = np.median(dizi1) # dizinin elemanlarının medyanını alır.
print("ortalama:", ortalama)
print("medyan:", medyan)