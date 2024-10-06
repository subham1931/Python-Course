def toPower(n,*args):
    if not args:
        return 'Please provide the args'
    else:
        return [i**n for i in args]
li = [1,2,3,4,5,6,7,8,9]
print(toPower(2,*li))