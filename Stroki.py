# word = "itproger"
#
# # print(word[3])
# # # Lubaya stroka - spisok
# #
# # print(len(word))
# #
# # print(word.count("pro"))
# #
# # print(word.upper()) #Orobrajenie v verhnem registre
# # print(word.lower())
# # print(word.isupper())
# # print(word.islower())
# # # True or False ferhni ili nizni registr
# # print(word.capitalize()) #Pervi simvol v verhni registr a ostal v nizn
# print(word.find("r")) #ishet mesto simvola, esli net simvola, vivodit -1

# word = "football, basketball, volleyball"
#
# # print(word.split(", "))
# #razbitie stroki po simvolu!!!!!!!!! Sozdaet spisok, udobno
# hobby = word.split(", ")
# print(hobby[1])

# word = "basketball, hokkey, volleyball, tennis, polo"
# hobbi = word.split(", ")
# # b = []
# # for i in hobbi:
# #     i = i.capitalize()
# #     print(i)
# #     b.extend(i.split(" "))
# # print(b)
# for i in range (len(hobbi)): #Mozno enumerate(hobbi)
#     hobbi[i] = hobbi[i].capitalize()
#
# result = ", ".join(hobbi) #join - obiedinaet list v stroku
# print(result)
#SREEEZII
# word = "Football"
# #print(word[4:-1])
# #vivodim kolichewstvo simvolov (startovi: do konechni(ne vkluch)/mozno nichego, i budet do konca)
# #mozno i minus stavit`
# print(word[1: -1: 2])
# #vivod budet ota, 2 - shag
lis = [6, 2, "strok", True, 5.2]
print(lis[2:-1])
print(lis[::-2])#esli - v konce, eshe i perevorachivaet