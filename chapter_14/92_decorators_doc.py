from functools import wraps
def decoratorFunc(anyFunc):
    @wraps(anyFunc)
    def resFunc(*args,**kwargs):
        '''This is res function'''
        print(add.__doc__)
        print("Optimized function")
        return anyFunc(*args,**kwargs)
    return resFunc

@decoratorFunc
def add(a,b):
    '''This is add function'''
    return a+b

# print(add.__doc__)
print(add(4,5))