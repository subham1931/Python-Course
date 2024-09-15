#ask user for a natural number (n)
#print total sum of 1 to n

number = int(input("Enter a nanutal number : "))

total = 0

while number >= 1:
    total += number
    number -= 1

print(total)