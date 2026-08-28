
#!!!!!! NADO DOBAVLAY KLUCH K ELEMENTU
#country = {4: 5}  #4 - kluch, 5 -element
#kluch - chto ugodnu
#country = {True: 5}
#mozno i bool,l i chto ugodno, krome spiska, no cotrez mozno
#print(country[True])
# country = {(5, 6): 3}
# print(country[(5, 6)])
# country = {"code": "RU", "name": "Russia", "population": 144}
# print(country["population"])
#dict - dictionari, slovar`, mozno sozdavat o tak
# country = dict(code="RU", name = "Russia", population = 200 )
# print(country["name"])
# country = dict(code = "RU", name = "Russia", population = 200)
# print(country)
# for i in country:
#     print(i)
#     print(country[i])
# print(country.items()) #raszbivka na cortezi po 2
# for i, value in country.items():
#     print(i, "-", value) !!!!!!!!!! Krasivo i pravilnee
# for i in country:
#     print(i, "-", country[i] )
# print(country["code"])
# print(country.get("name")) ##get = [], prosto znachenie po kluchu
# # country.clear() #ochishaet slovar`
# # print(country)
# country.pop("code") #udalaet po kluchu
# print(country)
# country.popitem() # udalaet posledni element
# print(country)
# print(country.keys()) #Vivodit tolko kluchi
# print(country.values()) #Vivodit tolko znachenia
# print(country.items()) #vivodit pari razbitie na kortezi
# country.update(dict(code = "EU")) #izmenaet element
#MOZNO i TAK
# country["code"] = "US"
# print(country)

person = dict(
     Sasha =dict(name = "Sasha", age = 24,
                 adress = ["Moscow", "Kakayato street", "45"],
                 garedes = dict(math = 5, physics = 3)),
     Vova = dict(name = "Vova", age = 20, hobby = "basketball")
 )
# print(person.items())
# person = {
#     "user 1":{
#         "first_name" : "Sasha",
#         "last_name" : "Sokolov",
#         "age": 24,
#         "adress": ["Moscow", "Kakayoto street", "45"],
#         "grades": {"math": 5, "physics": 3}
#     },
#     "User 2":{
#
#     }
# }
print(person["Sasha"]["adress"][1]) #vivod opredelennogo mesta
print(person["Vova"])