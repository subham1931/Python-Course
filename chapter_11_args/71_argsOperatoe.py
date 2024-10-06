# *args operator

# def sum(n1,n2):
#     return n1 + n2
# print(sum(1,2))

##if i want more numbers to be added then we have to create more veriable to pass values
##we will use *arg operator which create an tuple where multiple values are stored cand can be used

def addtion(*args):
    total = 0
    for i in args:
        total += i
    return total

def addtion(*args):
    return sum(args)

print(addtion(1,2,3,4,5,6,7,8,9,10))