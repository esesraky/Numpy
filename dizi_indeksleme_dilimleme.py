# Dizi indeksleme ve dilimleme, NumPy dizileri üzerinde belirli elemanlara erişmek veya alt diziler oluşturmak için kullanılan güçlü araçlardır. İndeksleme, tek bir elemanı veya belirli bir konumdaki elemanları seçmek için kullanılırken, dilimleme ise bir dizi içindeki belirli bir aralığı seçmek için kullanılır.
# İndeksleme, köşeli parantezler [] kullanılarak yapılır ve sıfır tabanlıdır, yani ilk eleman 0 indeksine sahiptir. Örneğin, dizi[0] ifadesi dizinin ilk elemanını verir. 
# Dilimleme ise iki nokta üst üste :: kullanılarak yapılır ve başlangıç, bitiş ve adım değerlerini belirterek bir alt dizi oluşturur. 
# Örneğin, dizi[1:4] ifadesi dizinin 1. indeksinden başlayarak 4. indekse kadar olan elemanları seçer (4. indeks dahil değildir).

import numpy as np

# dizi = np.array([10,20,30,40,50])

# eleman = dizi[2] # 2. indeksindeki elemanı seçer (30)
# print("Seçilen eleman:", eleman)
# print ("Son eleman:", dizi[-1]) # Son elemanı seçer (50)
# dilim = dizi[1:4] # 1. indeksinden başlayarak 4. indekse kadar olan elemanları seçer (20, 30, 40)
# print("Seçilen dilim:", dilim)
# dilim_1 = dizi[2:7] # 2. indeksinden başlayarak 7. indekse kadar olan elemanları seçer (30, 40, 50) - 7. indeks dahil değildir, bu nedenle sadece 30, 40 ve 50 seçilir.
# print("Seçilen dilim 1:", dilim_1)



matris = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
## matrisin il satırı 1, 2, 3; ikinci satırı 4, 5, 6; üçüncü satırı 7, 8, 9'dur. Aşağıdaki örneklerde, bu matris üzerinde indeksleme ve dilimleme işlemleri yapılmaktadır.
# eleman_2 = matris[1,2] # 1. satır ve 2. sütundaki elemanı seçer (6)
# print(eleman_2)
# eleman_3 = matris[-1,-3] # Son satır ve ilk sütundaki elemanı seçer (7)
# print("eleman_3:", eleman_3)
# #eleman_4 = matris[-1,-7] # burda hata verir çünkü -7 indeksi matrisin boyutunu aşar. Matrisin boyutu 3x3 olduğu için geçerli indeksler -3, -2, -1'dır. -7 indeksi bu aralıkta olmadığı için hata oluşur.
# eleman_5 = matris[-2,-2] # Son satırdan bir önceki satır ve son sütundan bir önceki sütundaki elemanı seçer (5)
# print("eleman_5:", eleman_5)


# çok boyutlu dizilerde dilimleme
alt_matris = matris[0:2, 1:3] # ilk kısım satırları, ikinci kısım sütunları belirtir. Bu örnekte, 0. ve 1. satırları ve 1. ve 2. sütunları seçer (2, 3, 5, 6)
# matrisi dilimlerken, başlangıç indeksi dahil edilirken, bitiş indeksi dahil edilmez. Bu nedenle, 0:2 ifadesi 0. ve 1. satırları seçerken, 1:3 ifadesi 1. ve 2. sütunları seçer.
alt_matris_2 = matris[0:3, 1:2] # 0. ile 2. satırları ve 1. sütunu seçer (2, 5, 8)
print("Seçilen alt matris:\n", alt_matris)
print("Seçilen alt matris 2:\n", alt_matris_2)




