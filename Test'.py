# def filter_even(numbers):
#     for num in numbers:
#         if num % 2 != 0:
#             numbers.remove(num)
#     print(numbers)
#
# numbers = [1, 2,3,4 ,5,6,7,8]
# filter_even(numbers)
#
# grades = {
#     "Alice" : 85,
#     "Bob" : 92,
#     "Charlie" : 78,
#     "Diana": 95
#
# }
#
# for i in grades:
#     if grades[i] > 80:
#         print(i, ": ", grades[i])
#
# class BankAccount:
#     owner = None
#     balance = 0
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Neverni vvod")
#
#     def withdraw(self, amount):
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("Neverni vvod")
#
#
#
#     def get_balance(self):
#         print(self.owner, self.balance)
#
# acc = BankAccount("John", 100)
# acc.deposit(50)
# acc.withdraw(30)
# acc.get_balance()
#
# import time
#
# def timer(func):
#     def wrapper():
#         func()
#         print("Функция выполнилась за ", time.process_time(), "секунд")
#     return wrapper
#
# @timer
# def sleep_example():
#     time.sleep(1)
#
# sleep_example()
#
# def safe_read_file(filename):
#     try:
#         with open(filename, "r") as file:
#             print(file.read())
#     except FileNotFoundError:
#         print("Файл не найден")
#     else:
#         print("Ошибка чтения файла")

def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))
print(func(3, []))
print(func(4))