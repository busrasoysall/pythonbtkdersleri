class Ogrenci():
    bolum = "bilisim"
    kurs = "btk kursu"

    def __init__(self,ad, soyad, tc):
        print("öğrenci oluşturuldu")
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc
        self.tamad = self.ad + self.soyad
        self.ortalama = None

    def tamAd(self):
        self.tamad = self.ad + self.soyad
        return self.tamad



ogr1 = Ogrenci("ali", "can", 123546)
ogr1.tamAd()
print(ogr1.tamad )