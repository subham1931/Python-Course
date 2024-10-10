##all() return true if a list have all value true or return false

n1 = [2,4,6,8,9]
res = lambda n1:[i%2==0 for i in n1]
print(all(res(n1)))


##create an func when it will summ all the param having int value 

def sumInt(*args):
    if all([(type(args) == int or type(args) == float) for args in args]):
        res = 0
        for i in args:
            res+=i
        return res
    else:
        return 'Wrong input'
print(sumInt(1,2,3,4,5))