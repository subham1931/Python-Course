def defArg(dataType):
    def decFunc( func):
        def wrapper(*args,**kwargs) : 
            if all([type(i) == dataType for i in args]):
                return func(*args,**kwargs)
            print("Invalid argument")
        return wrapper
    return decFunc

@defArg(str)
def strJoin(*args):
    res = ''
    for i in args:
        res+=i
    return res

print(strJoin('subham ','nayak'))
    