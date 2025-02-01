dogum_yili = int(input ("doğum yılınızı giriniz : "))
yas = 2025 - dogum_yili
if yas >= 18:
    print("ehliyet alacak yaştasınız")
else:
    print("ehliyet almak için yaşınız tutmuyor")
    print(f"ehliyet alamazsınız,{yas}yasında oldugunuz için" )
    print(f"ehliyet almak için {18 - yas} yıl beklemelisiniz")