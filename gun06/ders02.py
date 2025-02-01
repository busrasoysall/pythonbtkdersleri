import json

class Ogrenci():
    def __init__(self, kwargs):
    # def __init__(self,name,city,age):
        self.name = kwargs["name"]
        self.city = kwargs["city"]
        self.age = kwargs["age"]


# ogr1 = Ogrenci("gokhan","izmir","23")
# print(vars(ogr1))

ogr2_bilgi = {"name": "ezgi", "city": "manisa", "age": 21}
ogr2 = Ogrenci(ogr2_bilgi)
print(ogr2.age)

ogr_bilgileri = ('{"1":{"name": "ezgi", "city": "bursa", "age": 16},'
                 '"2":{"name": "ezgieda", "city": "manisa", "age":45}}')

ogrenci_listesi = []
json_data = json.loads(ogr_bilgileri)
print(json_data)
for data in json_data:
    print(data, json_data[data])
    ogrenci = Ogrenci(json_data[data])
    ogrenci_listesi.append(ogrenci)

print(ogrenci_listesi)