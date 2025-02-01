import json

x = '{"ad":"Gokhan", "soyad":"ozturk","isyeri":"btk"}'

bilgiler = json.loads(x)

print(bilgiler)
print(type(bilgiler))
for bilgi in bilgiler:
    print(bilgi, bilgiler[bilgi])

bilgiler["sehir"] = "izmir"

z = json.dumps(bilgiler)
print(z, type(z))