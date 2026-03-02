import numpy as np

dizi = np.array([10,20,30,40,50,65,78,83,97])

boolean_mask = dizi > 50 
# boolean dizisi, orijinal dizideki her bir elemanın belirli bir koşulu sağlayıp sağlamadığını gösteren bir dizi oluşturur.
# Örneğin, dizi > 50 ifadesi, dizi içindeki her bir elemanın 50'den büyük olup olmadığını kontrol eder ve sonuç olarak True veya False değerlerinden oluşan bir boolean dizisi oluşturur. 
print(boolean_mask)

# Boolean mask ile dizideki elemanları seçme
secilen_elemanlar = dizi[boolean_mask]
print("50'den büyük olan elemanlar:", secilen_elemanlar)

# Boolean mask ile dizideki elemanları seçmenin kısa yolu
secilen_elemanlar_kisa = dizi[dizi > 50]   
print("50'den büyük olan elemanlar (kısa yol):", secilen_elemanlar_kisa)

# çoklu eleme
#& ve operatörüdür. | veya operatörüdür.
boolean_mask_coklu = (dizi > 30) & (dizi < 80) # iki koşulu kıyaslarken () kullanmak önemlidir. 
print("30 ile 80 arasında olan elemanlar:", dizi[boolean_mask_coklu])

boolean_coklu = (dizi < 20) | (dizi > 80)
print("20'den küçük veya 80'den büyük olan elemanlar:", dizi[boolean_coklu])
