from functools import wraps

def print_data(func):
    @wraps(func)
    def wrapperFunc(*args,**kwargs):
        print(f'You are calling {func.__name__} function')
        print(func.__doc__)
        return func( *args,**kwargs)
    return wrapperFunc

@print_data
def add(a,b):
    '''This function takes 2 number as input and return by adding them'''
    return a+b


@print_data
def add(a,b):
    '''This function takes 2 number as input and return by adding them'''
    return a+b

print(add(2,3))