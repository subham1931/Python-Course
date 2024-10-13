def decoratorFunc(anyFunc):
    def resFunc(*args,**kwargs):
        print("Optimized function")
        return anyFunc(*args,**kwargs)
    return resFunc

@decoratorFunc
def add(a,b):
    return a+b

print(add(4,5))