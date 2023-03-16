


#Fonksiyonlar
ogrenciler = []
def ogrenci_ekle(ad, soyad):
    ogrenci = ad + " " + soyad
    ogrenciler.append(ogrenci)
    print(f"{ogrenci} öğrenci listesine eklendi.")

# öğrenci silme 
def ogrenci_sil(ad, soyad):
    ogrenci = ad + " " + soyad
    if ogrenci in ogrenciler:
        ogrenciler.remove(ogrenci)
        print(f"{ogrenci} öğrenci listesinden silindi.")
    else:
        print(f"{ogrenci} öğrenci listesinde bulunamadı.")

# toplu öğrenci ekleme



# öğrenci listeleme 
def ogrenci_listele():
    print("Öğrenci listesi:")
    for i, ogrenci in enumerate(ogrenciler):
        print(f"{i} - {ogrenci}")

# Öğrenci numarası öğrenme 
def ogrenci_no_bul(ad, soyad):
    ogrenci = ad + " " + soyad
    if ogrenci in ogrenciler:
        no = ogrenciler.index(ogrenci)
        print(f"{ogrenci} öğrencisinin numarası: {no}")
    else:
        print(f"{ogrenci} öğrencisi listede bulunamadı.")

# Birden fazla öğrenci silme 


while True:
    print("""
    1 => Öğrenci Ekle <=
    2 => Öğrenci Sil <=
    3 => Birden Fazla Öğrenci Ekle <=
    4 => Öğrencileri Listele <=
    5 => Öğrenci Numarası Bul <=
    6 => Birden Fazla Öğrenci Sil <=
    q => Çıkış <=
    """)

    secim = input("Ne yapmak istiyorsun ?")
    if secim == "1":
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        ogrenci_ekle(ad, soyad)
    elif secim == "2":
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        ogrenci_sil(ad, soyad)
    elif secim == "3":
        continue
    elif secim == "4":
        ogrenci_listele()
    elif secim == "5":
        ad = input("Ögrenci Adi: ")
        soyad = input("Ögrenci soyadi: ")
        ogrenci_no_bul(ad, soyad)
    elif secim == "6":
         continue
    elif secim == "q":
        print("Kapattim")
        break
    else:
        print("1-6 arasında bir secim yapman lazim")