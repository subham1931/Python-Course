#ask a user to input a number containing more than one digit 
#example -1234,33535
#Calculate 1+2+3+4

number = input("Enter an digit more tan one : ")
sum = 0
i =0
while i < len(number) :
    sum += int(number[i])
    i += 1
print(sum)