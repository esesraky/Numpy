import numpy as  np

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) 

yeni_dizi = dizi.reshape(3,4) # reshape fonksiyonu, bir dizinin şeklini değiştirmek için kullanılır. 
otomatik_dizi = -1 # Burada yer alan -1 ifadesi, NumPy'ye dizinin boyutunu otomatik olarak belirlemesi talimatını verir. Yani, 2 satır ve otomatik olarak belirlenen sütun sayısı ile yeni bir dizi oluşturur.
yeni_dizi2 = dizi.reshape(2,otomatik_dizi) 
print("yeni_dizi2:\n", yeni_dizi2)

matris = np.array([[1,2],[3,4],[5,6]])
tek_boyut = matris.reshape(-1) # reshape(-1) ifadesi, diziyi tek boyutlu hale getirir. -1, NumPy'ye dizinin boyutunu otomatik olarak belirlemesi talimatını verir.
print(matris)
print("tek_boyut:", tek_boyut)

