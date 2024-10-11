def myMap(func,l):
    res = []
    for i in l:
        res.append(func(i))
    return res

l = list(range(1,11))
# l = [1,2,3,4,5]
print(myMap(lambda a : a**3,l))