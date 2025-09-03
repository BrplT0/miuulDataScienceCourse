def kume_kontrol():
    # Setleri tanımla
    kume1 = set(["data", "python"])
    kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

    if kume2.issubset(kume1):  # Eğer kume2, kume1'in alt kümesi ise
        print("kume1, kume2'yi kapsıyor!")
        ortak_elemanlar = kume1.intersection(kume2)
        return ortak_elemanlar

    else:  # Eğer kapsamıyor ise
        print("kume1, kume2'yi kapsamıyor!")
        fark = kume2.difference(kume1)
        return fark

sonuc = kume_kontrol()
print("Sonuç:", sonuc)

