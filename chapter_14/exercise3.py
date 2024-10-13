def decFunc( func):
    def wrapper(*args,**kwargs) : 
        if all([type(i) == int for i in args]):
            return func(*args,**kwargs)
        print("Invalid argument")
    return wrapper

@decFunc
def func(*args):
    total = 0
    for i in args:
        total += i
    return total

print(func(1,2,3,4,5))
print(func(1,2,3,4,5,'subham'))
    