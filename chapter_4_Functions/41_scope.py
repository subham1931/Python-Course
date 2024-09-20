x = 5# global variable

def localFun():
    global x #calling the global x
    x = 7 #local variable
    return x

print(localFun())
print(x)
    