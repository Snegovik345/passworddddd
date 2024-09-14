import random
print("Привет, здесь ты можешь записать свой пароль")
count = int(input("Из скольки знаков будет пароль?"))
count_znakov =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
for i in range(count):
    password += random.choice(count_znakov)



print(password)
