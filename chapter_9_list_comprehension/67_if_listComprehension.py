##if conditon in list comprehension

evenNum = [i for i in range(1,21) if i % 2 == 0]
print(f'Even numbers are : {evenNum}')

oddNumber = [i for i in range(1,21) if i % 2 != 0]
print(f"odd numbers are : {oddNumber}")