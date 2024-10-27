import random
def loto_olustur():
        kolon_sayisi = int(input("Kaç kolon oluşturmak istiyorsunuz? "))
        istenmeyen = input("İstemediğiniz sayıları (virgülle ayırarak) girin, yoksa boş bırakın: ")
        if istenmeyen:
            istenmeyen = list(map(int, istenmeyen.split(',')))
        else:
            istenmeyen = []
        for i in range(kolon_sayisi):
            # kolonu set atarız çünkü aynı elemanı birden fazla kez tutmaz 
            kolon = set()
            while len(kolon) < 6:
                rastgele_sayi = random.randint(1, 90)
                if rastgele_sayi not in istenmeyen:
                    kolon.add(rastgele_sayi)
            print(f"{i+1}. kolon: {sorted(kolon)}")
loto_olustur()