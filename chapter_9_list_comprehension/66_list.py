#generalywe use a list like 
li = []
for i in range(1,11):
    li.append(i**2)
print(li)

##in list comprehension
squre = [i**2 for i in range(1,11)]
print(squre)

negetive = [-i for i in range(1,11)]
print(negetive)

name = ['subham','anubhab','rohit']
print([i[0] for i in name])