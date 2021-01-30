import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

length = input("Password length: ")
length = int(length)

number = input("Numbers of passwords: ")
number = int(number)

for p in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)
