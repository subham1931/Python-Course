###set is an unorder collection of unique items
# s = {1,2,1}
# #output {1,2}
# print(s)

##we can store int,float,str,tuple in a set
# s = {1,2.3,'subham',(1,2)}
# print(s)

# l = [1,2,3,4,5,6,7,8,9,1,2,3]
# print(l)
# #remove the duplicate
# print(list(set(l)))

se = {1,2}

##adding new data
se.add('adding new data')
print(se)

##remove a data it will remove data using remove method taking parameter as a the value
# se.remove(1)
# print(se)

##discard data itr will disard data using the discard() taking the value as parameter
# se.discard(1)
# print(se)

###copy()
seCopy = se.copy()
print(seCopy)