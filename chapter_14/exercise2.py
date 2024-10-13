from functools import wraps
import time

def print_data(func):
    @wraps(func)
    def wrapperFunc(*args, **kwargs):
        t1 = time.time()  # Start timing
        print(f'You are calling {func.__name__} function')
        print(func.__doc__)
        result = func(*args, **kwargs)  # Call the original function
        t2 = time.time()  # End timing
        print(f'Execution time: {t2 - t1:.6f} seconds')
        return result
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