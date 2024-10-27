liste = [('Tekirdağ', 120), ('Bursa', 436), ('Ankara', 664), ('Mersin', 1143), ('Hatay', 1783)]
kullanici_input = float(input("Bir mil değeri giriniz: "))
mil = list(map(lambda x: (x[0], x[1] * 0.62137), liste))  # Şehir ve mesafeyi mil'e çevirme
sehir_uzaklik = list(filter(lambda x: x[1] > kullanici_input, mil))  # Kullanıcıdan gelen değerden büyük olanları filtreleme
print([sehir[0] for sehir in sehir_uzaklik])  # Filtrelenen şehirlerin isimlerini yazdırma
