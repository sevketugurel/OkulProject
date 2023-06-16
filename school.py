import random

class Okul:
    def __init__(self,_isim):
        self.isim=_isim

    class Ogrenci:
        def __init__(self,isim,soyisim,no,sinif,disiplinPuanı,ders={"Türkçe":0,"Matematik":0}):
            self.isim=isim
            self.soyisim=soyisim
            self.no=no
            self.sinif=sinif
            self.disiplinPuanı=disiplinPuanı
            self.ders=ders

        def disiplin(self):
            disiplin=input("öğrenci displine gitti mi? (Evet ya da Hayır yazınız!):")

            if(disiplin=="Evet"):
                self.disiplinPuanı-=10
                if(self.disiplinPuanı<=0):
                    print("Öğrenci Kaydı Silindi!")
                    self.isim=None
                    self.soyisim=None
                    self.no=None
                    self.sinif=None
                    self.disiplinPuanı=None  
                else:
                    print("Öğrencimizin disiplin puanı 10 puanı düşürüldü! Yeni Puanı:",self.disiplinPuanı)
            elif (disiplin!="Evet" or disiplin=="Hayır"):
                print("Meşgul etme!")


        def goruntule(self):
            print("""
            isim:{}
            Soyisim:{}
            No:{}
            Sınıf:{}
            Disiplin Puanı:{}           
            """.format(self.isim,self.soyisim,self.no,self.sinif,self.disiplinPuanı))   

        def puanDegis(self):
            girdi=input("Lüütfen puanı Değiştirmek istediğniz dersi giriniz('Türkçe' ya da 'Matematik'):")
            if girdi=="Türkçe":
                self.ders["Türkçe"]=int(input("Lütfen Puanı Giriniz:"))
                if 0<=self.ders["Türkçe"]<=100:
                    print("başarlı bir şekilde puan Depişti. Türkçe Puanınız:",self.ders["Türkçe"])
                else:
                    print("Puan değişmedi!")
                    self.ders["Türkçe"]=0
            elif girdi=="Matematik":
                self.ders["Matematik"]=int(input("Lütfen Puanı Giriniz:"))
                if 0<=self.ders["Matematik"]<=100:
                    print("başarlı bir şekilde puan Depişti. Matematik Puanınız:",self.ders["Matematik"])
                else:
                    print("Puan değişmedi!")
                    self.ders["Matematik "]=0
            else:
                print("Böyle Bir Ders Yok. Doğru yazdığınızdan Emin olunuz.")

        def puanGoruntule(self):
            print(""" 
            Matematik Notunuz:{}
            Türkçe Notunuz:{}
            """.format(self.ders["Matematik"],self.ders["Türkçe"]))

        def hoca_yakalama(self):
            sayi=random.randint(1,2)
            if sayi==1:
                print("hocaya yakalandık!")
                self.disiplinPuanı-=2
            elif sayi==2:
                print("Yanlış alarm!")
    class Ogretmen():
        def __init__(self,isim,soyisim,sifre=123456) :
            self.isim=isim
            self.soyisim=soyisim
            self.sifre=sifre

        def ogretmen_bilgi(self):
            print(""" 
            İsim:{}
            Soyisim:{}
            Şifre:{}
            """.format(self.isim,self.soyisim,self.sifre))
            




