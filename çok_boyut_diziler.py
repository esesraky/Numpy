import numpy as np

dizi = np.array([["Pazartesi","Salı","Çarşamba","Perşembe","Cuma"],[6, 7, 8, 9, 10]]) # iki boyutlu bir dizi oluşturduk.

dizi_2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]) # üç boyutlu bir dizi oluşturduk.

print(dizi.shape) # shape özelliği, bir dizinin boyutlarını gösterir. 
print(dizi_2)
print(dizi_2.shape) # üç boyutlu bir dizi oluşturduk, bu yüzden shape çıktısı (1, 4, 3) olur. Bu, dizinin 1 adet 4x3'lük alt dizisi olduğunu gösterir.
