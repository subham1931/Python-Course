#loops on tuple 
tup = ("subham","nayak",27)
for i in tup :
    print(i)

#tuple with one elemnt
#if there is one elemnet in the the tuple without  comma then it is not a tuple 
words = ('e')
word = ('a',)
print(type(words))
print(type(word))

#tuple without parhantheses
#we can use the tuple without parenthesis
bike = 'bajaj','yamaha','hero'
print(type(bike))

#tuple unpacking
students = ('subham','rohit','bikash','rahul')
#we can only use string for unpacking
a,b,c,d = (students)
print(b)

##list inside tuple
#we can't do the data manupulation with tuple but we can do it in the list inside tuple
std = ("subam","nayak",[27,79.95])
print(std[2].pop())

#tuple functions
##min,max,sum
num = (1,2,3,4,5)
print(min(num))
print(max(num))
print(sum(num))