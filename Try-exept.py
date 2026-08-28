#ISKLUCHENMIYA
#
# try: #tipo pitaemsya sdelat` programmu
#     x = int(input("Vvedite chislo: "))
#     x += 5
#     print(x)
# except ValueError: #otslezivaem oshibku
#     print("Nyzno imenno chislo")
# #Byzno, chtobi programma ne fatal error, a tak kak nam udobno

# x = 0
# while x == 0:
#     try:
#         x = int(input("Vvedite chislo: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print("Nyzno chislo syka")
#         x = 0

# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print("delenie na 0")
###MOZNO PISAT LUBUU OSHIBKU VOZMOZNUU!!!!!!!!!!
##Mozno pisat` ih podryad na raznie oshibki

try:
    x = int(input("Vvedite chislo: "))
    x = 5 / x
    print(x)
except ZeroDivisionError:
    print("Delenie na 0")
except ValueError:
    print("Nyzno chislo")
else:
    print("else") # ESLI ne srabotali except
finally: ##Ne vazno vipolnilos` try or except, vse ravno srabotaet
    print("Finaly")
##Mozno pri rabote s failami sto proc ego zakrivat`