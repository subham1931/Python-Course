name,age = input("Eter yout name and age (,)").split(',')

if 1 < int(age) <=3:
    print(f"{name.title()} your ticket  is free")
elif 4 < int(age) <= 10:
    print(f"{name.title()} your ticket price is 150")
elif 11 < int(age) <= 60:
    print(f"{name.title()} your ticket price is 250")
else:
    print(f"{name.title()} your ticket price is 200")
    