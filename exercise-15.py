def üslü_sayi_hesaplama(sayi,üs):

    if (sayi == 0 and üs == 0):
        sonuc = "Tanımsız"
        print("Tanımlı değildir...")
    else:
        sonuc = sayi ** üs

        print(sonuc)

    return sonuc

üslü_sayi_hesaplama(1,0)