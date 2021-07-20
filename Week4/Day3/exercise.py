# # problem 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dicti = {}
# for i in zip(keys,values):
#     a,b = i
#     dicti[a] = b
# print(dicti)    

# # problem 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# sum = 0
# for age in family:
#     if family[age] < 3:
#         sum += 0
#         print(age + " pays 0")
#     elif family[age] < 13:
#         sum += 10 
#         print(age + " pays 10")
#     else:
#         sum += 15
#         print(age + " pays 15")
# print(f"the family pays {sum}")    

# # problem 3
# brand = {"name": "Zara",
#  "creation_date": 1975, 
#  "creater_name": "Amancio Ortega Gaona", 
#  "type_of_clothes": ["men","women","children","home"], "international_competitors":["Gap","H&m","Benetton"],"number_stores": 7000,
#   "major_color":
#   {"france": "blue",
#   "Spain": "red",
#   "US":["pink","green"]}}
# # print(brand)
# brand["number_stores"] = 2
# # print(brand)
# print( "Zaras clients are " + brand["type_of_clothes"][0]+","+ brand["type_of_clothes"][1]+","+ brand["type_of_clothes"][2]+" and the "+  brand["type_of_clothes"][3])
# country_creation = brand["major_color"]["Spain"]
# print(country_creation)
# print(brand["international_competitors"])
# brand["international_competitors"].append("Desigual")
# print(brand["international_competitors"])
# del brand["creation_date"]
# print(brand)
# print(brand["international_competitors"][3])
# print(brand["major_color"]['US'])
# total =0
# for i in brand:
#     total += 1
# print(total)   
# print(brand.keys()) 
# more_on_zara ={"creation_date": 1975,"number_stores": 10000 }
# brand.update(more_on_zara)
# print(brand["number_stores"])

# exercise 4
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# a = {}
# for index, name in enumerate(users):
#     a[name] =index
# print(a)
# b = {}
# for index, name in enumerate(users):
#     b[index] =name
# print(b)
# users.sort()
# c = {}
# for index, name in enumerate(users):
#     c[name] =index
# print(c)
d = {}
for index, name in enumerate(users):
    if name.find("i") != -1:
        d[name] =index
print(d)
e = {}
for index, name in enumerate(users):
    if name.startswith("M") or name.startswith("P"):
        e[name] =index
print(e)
