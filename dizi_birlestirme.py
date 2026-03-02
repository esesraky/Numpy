import numpy as np

dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])

birlesik_dizi = np.concatenate((dizi1, dizi2)) # concatenate fonksiyonu ile iki diziyi birleştiriyoruz
print(birlesik_dizi)

# İki boyutlu dizileri birleştirme
dizi3 = np.array([[1, 2], [3, 4]])
dizi4 = np.array([[5, 6], [7, 8]])

birlesik_dizi = np.hstack((dizi3, dizi4)) # hstack fonksiyonu ile sütun bazında birleştirme 
print(birlesik_dizi)
birlesik_dizi_v= np.vstack((dizi3, dizi4)) # vstack fonksiyonu ile satır bazında birleştirme
print(birlesik_dizi_v)
# bunları axis parametresi ile de yapabiliriz
birlesik_dizi_2d = np.concatenate((dizi3, dizi4), axis=0) # axis=0 ile satır bazında birleştirme
print(birlesik_dizi_2d)
birlesik_dizi_2d_axis1 = np.concatenate((dizi3, dizi4), axis=1) # axis=1 ile sütun bazında birleştirme
print(birlesik_dizi_2d_axis1)

# dizi ayırma
dizi = np.array([1, 2, 3, 4, 5, 6])
ayrilmis_dizi = np.split(dizi, 3) # split fonksiyonu ile diziyi 3 parçaya bölüyoruz
print(ayrilmis_dizi)

# İki boyutlu diziyi ayırma
dizi2d = np.array([[1,2,3,4],[5,6,7,8]])
ayrilmis_dizi2d = np.hsplit(dizi2d, 2) # hsplit fonksiyonu ile sütun bazında ayırma yapılır
print(ayrilmis_dizi2d)
ayrilmis_dizi2d_v = np.vsplit(dizi2d, 2) # vsplit fonksiyonu ile satır bazında ayırma yapılır
print(ayrilmis_dizi2d_v)
