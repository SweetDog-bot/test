#Robot cherez oop
#Class - chertezh/nachinka
#Object - robot so znach i dannimi
#nasledov - dob opctions k chertezu robot
#polimorfizm - functional
#incapsulatiya - zahita vnutrennih dabnnih
# class Cats:   #sozdanie classa
#     name = None
#     age = None
#     isHappy = None
#
#     def set_data(self, name, age, isHappy): #Metod nazivaetsya, hot po suti i function
#         self.name = name #ustanavlivaem (self.name(v klass name)) parametr ukazanni kak name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(self.name, "age is:", self.age, "Happy is:", self.isHappy)
#     def user_cat(self):
#         self.name = input("Vvedite imya cota: ")
#         self.age = int(input("Vvedite vosrast cota: "))
#         if self.age <= 5:
#             self.isHappy = True
#         else:
#             self.isHappy = False
#
#
# #self - tipo obrashenie k polyam vnutri c
# # lassa/mozno lubie nazvaniya parametrov, ne obyazatelno po klaccy
#
# #znacheniya - lubie
#
# cat1 = Cats()  #sozdanie objecta
# cat1.name = "Barsik"
# cat1.age = 5
# cat1.isHappy = True
#
# cat2 = Cats()
# cat2.name = "Djoepich"
# cat2.age = 1
# cat2.isHappy = False
#
# cat3 = Cats()
# cat3.set_data("Igor`", 3, True)
#
# cat4 = Cats()
# cat4.user_cat()
# cat4.get_data()
# # if cat1.age > cat2.age:
# #     print("Starshe: ", cat1.name)
# # elif cat1.age < cat2.age:
# #     print("Starshe: ", cat2.name)
# # else:
# #     print("Vozrast odinakov")

#KONSTRUCTORS

class Cats:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy): #konstructor
        # self.name = name
        # self.age = age
        # self.isHappy = isHappy

        self.set_data(name, age, isHappy)
        self.get_data()
#Mozno srazu visvat v nem drugoi metod
#Tipo srazu vipolnyaetsya funct
#oblegchaet ustanovku, pozvalayet ne zozdavat` bespoleznye mtodi
    def set_data(self, name = None, age = None, isHappy = None):
# Metod nazivaetsya, hot po suti i function
#esli ukazivaem znach None - mozem tipo ne obyazatelno davat` znach parametru
#pereopredelili metod(postavili znach po umolchaniu)
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, "age is:", self.age, "Happy is:", self.isHappy)

    def user_cat(self):
        self.name = input("Vvedite imya cota: ")
        self.age = int(input("Vvedite vosrast cota: "))
        if self.age <= 5:
            self.isHappy = True
        else:
            self.isHappy = False

cat1 = Cats("Barsik", 5, True)
cat1.set_data("Djoe", 6)
cat1.get_data()

