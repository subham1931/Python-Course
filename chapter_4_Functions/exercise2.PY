def greater(num1,num2):
    if num1 > num2 :
        return num1
    return num2

num1,num2 = input("Enter 2 number for checking which one is greater : ").split(',')
print(greater(int(num1),int(num2)))

