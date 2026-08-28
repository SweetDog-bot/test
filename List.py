# # nums = [1,2,3,4,5,"Heelo",12.4,True, False, [1, 2,3]]
# #
# #
# # #VAZNO esli k spisku obrashaus, mogu s konca s -1 (nums[-1])
# # print(nums[-1][0])
#
# numbers = [5, 6, 7]
#
# numbers.append(100) #dobavlenie k spisku v konec
# numbers.append(200)
# numbers.insert(2, True) # dobavlenie na ukazannoe mesto
# numbers.extend([3, 4 ,5]) #dobavka spiska k spisku
# # b = [1, 2, 3]
# # numbers.extend(b) !!!!!MOZNO I TAK
# #True = 1, False = 0 pri avto sorte
# numbers.sort() #Sortirovka avto
# #numbers.reverse() #Perevorot s nachala v konec
# numbers.pop() #Udalenie po umolch poslednego {pop()}
# numbers.remove(7) #udalenie opredelennogo elementa
# #numbers.clear() # Uda;aet ves spisok
# #print(numbers.count(5)) #podshitivaet skolko takih elementov
# #print(len(numbers)) #dlina spiska
# print(numbers)

# nums = [1, 2, 3, 4, "50", True]
#
# for el in nums:
#     el *= 2
#     print(el)

n = int(input("Enter length: "))
user_list = []
i = 0
while i < n:
    string = "Enter element #" +str(i)+ ":"
    user_list.append(input(string))
    i += 1
print(user_list)

