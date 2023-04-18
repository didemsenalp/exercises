def vergi(gelir):

    if (gelir <= 10000):
        vergi_miktarı = 0
        print("Gelir verginiz bulunmamaktadır...")
    elif (gelir <= 20000):
        vergi_miktarı = (gelir-10000)*10/100
        print("Gelir verginiz: ",vergi_miktarı)
    else:
        vergi_miktarı = (10000 * 0)/100 + (10000 * 10)/100 + ((gelir-20000)*20)/100
        print("Gelir verginiz: ",vergi_miktarı)
    

    return vergi_miktarı

vergi(11000)
