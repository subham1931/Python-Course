num  = input("Enter a number having more tgan one digit : ")

sum = 0

for i in range(len(num)):
    sum += int(num[i])
print(sum)