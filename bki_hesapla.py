# Kullanıcıdan boy ve kilo bilgilerini al
boy_input = input("Boyunuzu giriniz: ")
kilo = float(input("Kilonuzu giriniz: "))

if float(boy_input) > 3:  # Eğer boy 3'ten büyükse cm cinsindedir
    boy = float(boy_input) / 100  # cm'yi m'ye çevir
else:
    boy = float(boy_input)  # Boy zaten metre olarak girildiyse

# BKI hesaplama
bki = kilo / (boy ** 2)

# BKI durumu belirle
if bki < 18.5:
    durum = "Zayıf"
elif 18.5 <= bki < 25:
    durum = "Orta"
elif 25 <= bki < 30:
    durum = "Aşırılı kilolu"
else:
    durum = "Obez"

# Sonuçları yazdır
print(f"Beden kitle indeksiniz: {bki:.2f}")
print(f"Durumunuz: {durum}")

# Eğer sağlıklı kilo aralığında değilse ideal kilo aralığını hesapla
if durum != "Orta":
    min_kilo = 18.5 * (boy ** 2)  
    max_kilo = 24.99 * (boy ** 2)
    print(f"Normal kilo aralığında olmanız için {min_kilo:.2f} kg ile {max_kilo:.2f} kg arasında olmalısınız.")
