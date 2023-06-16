import school
import random


Ogrenci1=school.Okul.Ogrenci("şevket","Uğurel",111,"12-A",10)
Ogretmen1=school.Okul.Ogretmen("Erdal","erdal",2323)
okul=school.Okul("Vefa Okulu").isim
while True:
    print("""
    Sevgili {} sakinleri Okulumuza Hoşgeldiniz.
    """.format(okul))

    islem=input("Öğrenci İşlemleri için 1'e basın; Öğretmen İşlemleri için 2'ye Basın(Çıkmak için * Basınız:)")
    if islem=="1":
        print("Öğrenci Sistemindesiniz!\n")
        islem2=int(input("Puan görüntülemek için 1'e basınız Öğrenci Bilgilerini Görüntelemek için 2'ye basın:"))
        if islem2==1:
            if Ogrenci1.disiplinPuanı!=None:
                Ogrenci1.puanGoruntule()
            else:
                pass
        elif islem2==2:
            Ogrenci1.goruntule()
        else:
            print("Yanlış Değer Girdiniz.Sistemi Meşgul ettiğiniz için görevli öğretmene Bilgi verildi! ")
            Ogrenci1.hoca_yakalama()
    elif islem== "2":
        print("Öğretmen Bilgi sistemindesiniz.")
        islem3=int(input("""
        Yapabileceğiniz İşlemler:
        [1] Disiplin Cezası
        [2] Ders Notu
        [3] Öğretmen Bilgisi
        """))
        if islem3==1:
            sifre=int(input("Lütfen Öğretmen Şifresini Giriniz:"))
            if sifre==Ogretmen1.sifre:
                Ogrenci1.disiplin()
            else:
                print("Yanlış Şifre girdiniz! Hocaya haber Verildi!")
                Ogrenci1.hoca_yakalama()
        elif islem3==2:
            sifre=int(input("Lütfen Öğretmen Şifresini Giriniz:"))
            if sifre==Ogretmen1.sifre:
                if Ogrenci1.disiplinPuanı==None:
                    pass
                else:
                    Ogrenci1.puanDegis()
            else:  
                print("Yanlış Şifre girdiniz! Hocaya haber Verildi!")
                Ogrenci1.hoca_yakalama()
        elif islem3==3:
            sifre=int(input("Lütfen Öğretmen Şifresini Giriniz:"))
            if sifre==Ogretmen1.sifre:
                Ogretmen1.ogretmen_bilgi()
            else:  
                print("Yanlış Şifre girdiniz! Hocaya haber Verildi!")
                Ogrenci1.hoca_yakalama()
    elif islem=="*":
        break
        
