ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for kod, kr, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kr} olan {kod} kodlu dersin kontenjanı {kont} kişidir.")