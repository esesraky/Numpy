import numpy as np

data = np.loadtxt('data.txt', delimiter=' ') # bu şekilde data.txt dosyasını okuyarak bir numpy array'ine dönüştürürüz. delimiter parametresi, verilerin hangi karakterle ayrıldığını belirtir. Bu örnekte, veriler boşluk karakteriyle ayrılmıştır.
print(data)

satır_topla = np.sum(data, axis=1) # axis=1 parametresi, satırları toplamak istediğimizi belirtir. Eğer axis=0 olsaydı, sütunları toplardık.
print("Her satırın toplamı:", satır_topla)

np.savetxt('output.txt', satır_topla, fmt='%d') # bu şekilde satırların toplamını output.txt dosyasına kaydederiz. fmt parametresi, verilerin hangi formatta kaydedileceğini belirtir. Bu örnekte, tam sayı formatında kaydediyoruz.

output_data = np.column_stack((data, satır_topla)) # column_stack fonksiyonu, data array'ine satır_topla array'ini sütun olarak ekler. Böylece her satırın toplamını da içeren yeni bir array oluştururuz.
np.savetxt('output_with_sums.txt', output_data, fmt='%d', delimiter=' ') # bu şekilde hem orijinal verileri hem de satırların toplamını içeren yeni array'i output_with_sums.txt dosyasına kaydederiz.
print("Output with sums saved to 'output_with_sums.txt'")