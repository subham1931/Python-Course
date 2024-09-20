#Function
# len()

def add(num):
    total = 0
    for i in num:
        total += int(i)
    return total


number = input("Enter a number for fing total : ")
print(add(number))