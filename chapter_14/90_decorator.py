##Decorators - Used for enhance the functionality of a function
## @use for decorators

def decorator(any_function):
    def resFunc():
        print("Functions was enhanced")
        any_function()
    return resFunc

@decorator
def fun1():
    print("This is function one")


@decorator
def fun2():
    print("This is function two")

# fun1()
fun2()

# var = decorator(fun1)
# var()