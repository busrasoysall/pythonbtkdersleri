from gun03.ders01 import artis

dogum_yili = int(input ("doğum yılınızı giriniz : "))
yas = 2025 - dogum_yili
if yas >= 18:
    print("ehliyet alacak yaştasınız")
else:
    print("ehliyet almak için yaşınız tutmuyor")
    print(dogum_yili )
el