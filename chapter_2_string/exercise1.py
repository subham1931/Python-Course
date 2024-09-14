#Ask user to input2 number and you have to print average of 3 numbers using string formatiing

num1,num2,num3 = map(int,input("Enter 3 numbers (input coma seperated)").split(","))
average = (num1 + num2 + num3) / 3;

print(f"Average of three {num1},{num2},{num3} is : " + str(average))
print(f"Average of three {num1},{num2},{num3} is : " + str((int(num1) + int(num2) + int(num3)) / 3))