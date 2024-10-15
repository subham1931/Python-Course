##iterator , interable
l = [1,2,3,4,5] #---->iterable
for i in map(lambda i : i**2 ,l):#--->Iterator
     print(i)

# for i in l:
#     ##Here when the i called or the for loop start the i call th next() which hold the 1-thn 2 - thn 3 - 4 - 5 
#     print(i)


##Example
# here l is an iterable and the i was iterator
# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

###If we add one more next func then it will cause a problem stop iteration


##Geneartors are iterators
## generatyors are like list structure 

##in list the data re called oneby one and poped
#l = [1,2,3,4,5]
#l = [2,3,4,5]
#l = [3,4,5]
#l = [4,5]
#l = [5]


##We use generators sequense only for one time
#in generator it store the data in orther adress
##aand use like
# generator = (1)
# generator = (2)
# generator = (3)
# generator = (4)
# generator = (5)