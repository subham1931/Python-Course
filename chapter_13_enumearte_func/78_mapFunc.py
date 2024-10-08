numb = [1,2,3,4,5]
def squre(n):
    return n**2

####using for loop
res = []
for i in numb:
    res.append(squre(i))
print(res)

##using list comprehension
print([i**2 for i in numb])

# using map
print(list(map(squre,numb)))


# using map and lambda
print(list(map(lambda a:a**2,numb)))

# map(function,data)