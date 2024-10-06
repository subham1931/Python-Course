def multi(num,*args):
    mul = 1
    for i in args:
        mul *= i
    return mul,num

print(multi(2,2,3))

##if we use normal params then we have to use it before the args it will took values from the passed arguments
##if we use the normal params after the *args then it will no use