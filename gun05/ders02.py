dosya_adi = "deneme.txt"
with open(dosya_adi) as dosya:
    print(dosya.readline())

with open(dosya_adi) as dosya:
    print(dosya.readlines())
