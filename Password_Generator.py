import random
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_@#$&$!{]}[+-*/?<>()"
length = int(input("Enter thr length of your password:"))
password=""
for a in range(length):
    password+=random.choice(chars)
print("The program has created:",password)
