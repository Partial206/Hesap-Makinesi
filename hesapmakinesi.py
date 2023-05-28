Sayi1 = int(input("İşlem yapmak için 1'nci sayini seç:"))
print(Sayi1)
Sayi2 = int(input("İşlem yapmak için 2'nci sayini  seç:"))
print(Sayi2)
işlem = int(input("İşlem yapmak bir işlem seç 1 sayisi toplamayi ifade eder 2 sayisi çarpmayi 3 sayisi bolmeyi 4 sayisi çikarmayi:"))
if işlem == 1:
    print(int(Sayi1+Sayi2))
if işlem == 2:
    print(int(Sayi1*Sayi2))
if işlem == 3:
    print(int(Sayi1/Sayi2))
if işlem == 4:
    print(int(Sayi1-Sayi2))
if işlem > 4:
    print("Böyle bir işlem bulunamadı")
if işlem < 1:
    print("Böyle bir işlem bulunamadı")
if işlem == str:
    print("İşlem bir harf olamaz")
    
