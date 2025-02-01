#yöntem1

cevap = input("pizza ister misiniz")
while cevap == "evet" :
    print("buyrun pizzanız")
    cevap = input("pizza ister misin")

#yöntem2

cevap = bool(input("pizza ister misiniz"))
while cevap == True:
    print("buyrun pizzanız")
    cevap = bool(input("pizza ister misiniz"))