import numpy as np

rastgele_sayi = np.random.randint(1,10,size=5) # Bu kod, 1 ile 10 arasında (10 dahil değil) rastgele 5 adet tam sayı üretir.
print(rastgele_sayi)
rastgele_sayi2 = np.random.rand(5) # Burada kullanılan rand fonksiyonu, 0 ile 1 arasında rastgele 5 adet ondalık sayı üretir.
print(rastgele_sayi2)

normal_rakam = np.random.normal(0,1,5) # Burada yapılan işlem, normal dağılımda 0 ortalama ve 1 standart sapma ile 5 adet rastgele sayı üretmektir. 
# Normal dağılım demek, verilerin ortalama etrafında simetrik bir şekilde dağıldığı bir dağılım türüdür. 
# Bu tür dağılımda, verilerin çoğu ortalama değere yakın olurken, daha az sayıda veri uzak değerlere sahip olabilir. 
# Normal dağılım, birçok doğal olayın ve ölçümün dağılımını modellemek için kullanılır.
print("normal_rakam:", normal_rakam)

rastgele_dizi = np.random.rand(3,3)
rastgele_dizi = rastgele_dizi.astype(int) # int yerine float kullanarak ondalık sayılarla doldurulmuş bir dizi oluşturabilirsiniz. 
# astype(int) fonksiyonu, dizideki her bir elemanı tam sayıya dönüştürür.
# Ancak, rand fonksiyonu tarafından üretilen ondalık sayılar 0 ile 1 arasında olduğu için, bu dönüşüm sonucunda tüm elemanlar 0 olacaktır.
# Eğer rastgele_dizi'yi tam sayılarla doldurmak istiyorsanız, randint fonksiyonunu kullanabilirsiniz. Örneğin:
# rastgele_dizi = np.random.randint(0, 10, size=(3, 3)) # Bu kod, 0 ile 10 arasında (10 dahil değil) rastgele tam sayılarla doldurulmuş 3x3 boyutunda bir dizi oluşturur.
# rastgele_dizi = np.random.rand(3,3)*10 # bu şekilde de 0 ile 10 arasında rastgele ondalık syaılarla dizi oluşturarak bi önceki kodun çıktısında 0'ların oluşmasını engelleyebilirsiniz.

print("rastgele_dizi:\n", rastgele_dizi)