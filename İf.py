print("Sistemimize Hoş Geldiniz! Lütfen gerekli bilgileri giriniz.")

name = input("isim :")
age = int(input("yaş: "))
degree = input("Eğitim seviyesi: ")

if (age > 18) and (degree == "Üniversite" or degree == "Lise"):
    print("Uygunsunuz")
else:
    print("Uygun değilsiniz")
    