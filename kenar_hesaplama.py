import math
# Kullanıcıdan kenarları alan fonksiyon
def kenarlari_al():
    kenarlar = input("Kenarları girin (virgülle ayrılmış, bilinmeyen kenar için '?' girin): ")
    kenar_listesi = kenarlar.split(',')
    # '?' işareti bilinmeyen kenarı belirlemek için kullanılıyor
    return kenar_listesi

# Kısa kenar hesaplayan fonksiyon (Hipotenüs ve bir kısa kenar biliniyorsa)
def kisa_kenar_hesapla(hipotenus, kisa_kenar):
    return math.sqrt(abs(hipotenus**2 - kisa_kenar**2))

# Hipotenüs hesaplayan fonksiyon (iki kısa kenar biliniyorsa)
def hipotenus_hesapla(kisa_kenar1, kisa_kenar2):
    return math.sqrt(kisa_kenar1**2 + kisa_kenar2**2)

# Ana işlem fonksiyonu
def dik_ucgen_hesapla():
    kenarlar = kenarlari_al()
    kenarlar = [float(k) if k != '?' else '?' for k in kenarlar]

    if kenarlar.count('?') != 1:
        return "Lütfen sadece bir bilinmeyen kenar girin."

    if kenarlar[2] == '?':  # Hipotenüs bilinmiyorsa
        return hipotenus_hesapla(kenarlar[0], kenarlar[1])
    elif kenarlar[0] == '?':  # İlk kısa kenar bilinmiyorsa
        return kisa_kenar_hesapla(kenarlar[2], kenarlar[1])
    elif kenarlar[1] == '?':  # İkinci kısa kenar bilinmiyorsa
        return kisa_kenar_hesapla(kenarlar[2], kenarlar[0])

# Örnek kullanım
sonuc = dik_ucgen_hesapla()

print("Sonuç:", sonuc)
