def squreNumber(num):
    squreList = []
    for i in num:
        squreList.append(i**2)
        i += 1
    return squreList

# number = list(map(int,input("Enter numbers for squre : ").split(",")))
number = list(range(1,11))
print(squreNumber(number))