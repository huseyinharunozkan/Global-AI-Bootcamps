class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def __del__(self):
        self.file.close()

    def kitaplari_listele(self):
        self.file.seek(0)
        kitaplar = self.file.read().splitlines()
        for kitap in kitaplar:
            isim, yazar, tarih, sayfa_sayisi = kitap.split(',')
            print(f"Kitap ismi: {isim}, Yazar: {yazar}")

    def kitap_ekle(self):
        isim = input("Kitabın ismini girin: ")
        yazar = input("Kitabın yazarını girin: ")
        tarih = input("Tarihini girin: ")
        sayfa_sayisi = input("Sayfa sayısını girin: ")

        kitap_bilgisi = f"{isim},{yazar},{tarih},{sayfa_sayisi}\n"
        self.file.write(kitap_bilgisi)
        print("Kitap başarılı bir şekilde eklendi.")

    def kitap_kaldir(self):
        isim = input("Kaldırmak istediğiniz kitabın ismini girin: ")
        self.file.seek(0)
        kitaplar = self.file.readlines()
        güncel_kitaplar = []
        for kitap in kitaplar:
            if isim not in kitap:
                güncel_kitaplar.append(kitap)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(güncel_kitaplar)
        print(f"Kitap '{isim}' başarılı bir şekilde kaldırıldı..")

lib = Library()

while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldır")
    print("4) ÇIKIŞ")

    secim = input("Seçiminizi giriniz(1-4): ")

    if secim == '1':
        lib.kitaplari_listele()
    elif secim == '2':
        lib.kitap_ekle()
    elif secim == '3':
        lib.kitap_kaldir()
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı bir seçim yaptınız!")

