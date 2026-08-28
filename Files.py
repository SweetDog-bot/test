# #NE ZABIYVAT OTKRIVAT I OBYAZATELNI ZAKRIVAT
#
# data = input("Vvedite tekst")
#
# file = open("/Users/sasha/PycharmProjects/WelcomeScreen/data/text.txt", "a")
# #mozno ukazat papku(tyt data, i v ney sozd file
# #vtoroi parametr - sposob otkr, dlya chten, zapisi i td
#
# file.write(data + "\n")
#
# file.close() #zakr file

# file = open("/Users/sasha/PycharmProjects/WelcomeScreen/data/text.txt", "r")
#
# # print(file.read(5)) #mozno ukazat skolko vivod simvolov v skobk
#
# for line in file:
#     print(line, end="")
# # po strokam
# file.close()

### WITH as dlya files
# try:
#     file = open("text1.txt", "r")
#     file.read()
# except FileNotFoundError:
#     print("File ne naiden")
# finally:
#     file.close()
# ## Ne rabotaet, prichina - peremennoi net, file ne sushestv proga lomaetsa, file ne zakr,krchp
try:
    with open("text1.txt", "r", encoding = "utf-8") as file: #encoding - kodirovka
        print(file.read())
except FileNotFoundError:
    print("File not found")