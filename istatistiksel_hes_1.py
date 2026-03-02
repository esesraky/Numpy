import numpy as np

dizi = np.array([1,2,3,4,5,6])

maks = np.max(dizi)
min = np.min(dizi)
print("Dizinin maksimum değeri:", maks)
print("Dizinin minimum değeri:", min)

toplam = np.sum(dizi)
kume_toplam = np.cumsum(dizi) # cumsum() fonksiyonu, dizinin kümülatif toplamını hesaplar.
print("Dizinin toplamı:", toplam)
print("Dizinin kümülatif toplamı:", kume_toplam)

# kümülatif toplam dizisi, her bir elemanın kendisinden önceki elemanların toplamını içerir. 

