import random
# 4 renkten oluşan okey taşlarını oluşturuyoruz
renkler = ['turuncu', 'kırmızı', 'mavi', 'siyah']
taslar = [(renk, numara) for renk in renkler for numara in range(1, 14)] * 2  # Her taşın iki kopyası
def tasCek():
    while taslar:
        secilen_tas=random.choice(taslar) #rastgale tas sec
        taslar.remove(secilen_tas) #secilen ttası siliyor
        yield secilen_tas #secilen taşı dönürüyor
        #taş çekme işlemi ve sonuçları yazdırma
for tas in tasCek():
        print(f"{tas[0]} {tas[1]}", end=" ")
print("\nYerde çekilecek taş kalmadı.")
