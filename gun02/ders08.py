#yemek sipariş uygulaması
yemek=input("yemek bilgisi giriniz")
icecek = input("içecek bilgisi giriniz")
if yemek == "pide":
    print(f"{yemek} siparişi geçerli sipariş")
    icecek = input("icecek bilgisi giriniz")
    if icecek == "ayran"  or icecek == "kola":
        print("geçerli içecek")
else:
    print("geçersiz içecek")
    print("içecek iade olacak")
print("afiyet olsun")
else:
print("yemek siparişi doğru sipariş değil")