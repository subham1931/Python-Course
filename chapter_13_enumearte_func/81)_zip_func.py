##zip function
##return object which have tuples

# std = ['subham','rohit','situ']
std = ['subham','rohit']
roll = [27,24,8]

res = list(zip(std,roll))
print(dict(res))
print(list(zip(std,roll)))

#unpacking list
l1,l2 = list(zip(*res))
print(l1)
print(l2)

