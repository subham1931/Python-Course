##we can create an generator using yield keyword

def createGen(n):
    for i in range(1,n + 1):
        yield(i)

# for i in createGen(10):
#     print(i)

res  = createGen(10)
print([i for i in res])

## Here how it works
##In List it create the memore for whole sequence
#memory[list] = [..........]

#but in generators it does not create the full memery sequecse
#memory(generator) = (1)
#memory(generator) = (2)
#memory(generator) = (3)
#memory(generator) = (4)
#memory(generator) = (5)
#memory(generator) = (6)
#memory(generator) = (7)
#memory(generator) = (8)
#memory(generator) = (9)
#memory(generator) = (10)