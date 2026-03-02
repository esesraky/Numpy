import numpy as np

dizi1 = np.array([1,2,3,4,5])
dizi2 = np.array([6,7,8,9,10])

toplam = np.add(dizi1, dizi2) 
çıkarma = np.subtract(dizi1, dizi2) 
carpma = np.multiply(dizi1, dizi2)
bölme = np.divide(dizi1, dizi2)
min = np.minimum(dizi1, dizi2) 
max = np.maximum(dizi1, dizi2) 

üst_alma = np.power(dizi1, 3) # dizinin elemanlarının üssünü alır.
print(üst_alma)

# Varyans değeri, bir veri setindeki değerlerin ortalamadan ne kadar uzaklaştığını ölçen bir istatistiksel ölçüdür. 
# Varyans, genellikle bir veri setinin dağılımını anlamak ve karşılaştırmak için kullanılır. 
# Varyans değeri ne kadar yüksekse, veri setindeki değerler ortalamadan o kadar uzaklaşır ve dağılım daha geniş olur. 
# Varyans değeri ne kadar düşükse, veri setindeki değerler ortalamaya daha yakın olur ve dağılım daha dar olur.
# Varyans, genellikle standart sapma ile birlikte kullanılır, çünkü standart sapma varyansın kareköküdür ve aynı birimde ifade edilir.
varyans = np.var(dizi1) # dizinin elemanlarının varyansını alır.
print("varyans:", varyans)

# Standart sapma, bir veri setindeki değerlerin ortalamadan ne kadar uzaklaştığını ölçen bir istatistiksel ölçüdür.
# Standart sapma değeri ne kadar yüksekse, veri setindeki değerler ortalamadan o kadar uzaklaşır ve dağılım daha geniş olur.
# Standart sapma değeri ne kadar düşükse, veri setindeki değerler ortalamaya daha yakın olur ve dağılım daha dar olur.
standart_sapma = np.std(dizi1) # dizinin elemanlarının standart sapmasını alır.
print("standart sapma:", standart_sapma)
