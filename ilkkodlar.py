import numpy as np 
# Numpy kütüphanesi, Python'da bilimsel hesaplamalar için kullanılan bir kütüphanedir. Numpy, çok boyutlu diziler ve matrisler üzerinde hızlı ve verimli işlemler yapmamızı sağlar. 
# Ayrıca, matematiksel fonksiyonlar, istatistiksel işlemler ve lineer cebir gibi birçok özellik sunar. 
# Numpy, büyük veri setleriyle çalışmak ve karmaşık hesaplamalar yapmak için yaygın olarak kullanılır.

dizi = np.array([1, 2, 3, 4, 5]) 
print(dizi)

dizi_2 = np.arange(0, 10, 2) # arange fonksiyonu, belirli bir aralıkta düzenli olarak artan sayılar içeren bir dizi oluşturur.
print(dizi_2)

dizi_3 = np.linspace(0, 1, 5) # linspace fonksiyonu, belirli bir aralıkta eşit olarak bölünmüş sayılar içeren bir dizi oluşturur.
print(dizi_3)

boyut = dizi.ndim # ndim özelliği, bir dizinin kaç boyutlu olduğunu gösterir.
print(boyut)

veri__turu = dizi.dtype # dtype özelliği, bir dizinin veri türünü gösterir.
print(veri__turu) # sadece sayılardan oluşursa çıktısı int64 olur, eğer içinde ondalık sayı varsa float64 olur.
# eğer dizi içerisinde string ifadeler varsa, o zaman dtype 'U' (Unicode) olur.




