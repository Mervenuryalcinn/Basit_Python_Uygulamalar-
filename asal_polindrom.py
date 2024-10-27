#asal_polindrom
def asal_kontrol(sayi):
    prime:True
    if sayi<2:
        prime:False
    else:
        for i in range(2,int(sayi**0.5)+1):
            if sayi % i==0:
                return False
        return True
def polindrom_kontrol(sayi):
    sayi_str=str(sayi)
    if sayi_str==sayi_str[::-1]:
        return True
    else:
        return False
    
alt_sinir=int(input("Bir alt sınır giriniz"))
ust_sinir=int(input("Bir üst sınır giriniz"))
asal_sayilar=[]
asal_ve_polindrom=[]
for sayi in range(alt_sinir,ust_sinir+1):
    if asal_kontrol(sayi):
        asal_sayilar.append(sayi)
        print(asal_sayilar)
for sayi in range(alt_sinir,ust_sinir+1):
    if polindrom_kontrol(sayi) and asal_kontrol(sayi):
        asal_ve_polindrom.append(sayi)
        print(asal_ve_polindrom)
        