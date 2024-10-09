##filter return with tuple
##filter(condition,operation) -----> syntax
def addtion(n):
    return n**2

nums = [1,2,3,4,5]
res = tuple(filter(addtion,nums))
even = tuple(filter(lambda a : a % 2 == 0 ,res))
print(res,even)
