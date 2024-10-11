##First class func

def squre(*args):
    return [n**2 for n in args]

func = squre
print(func(1,2,3,4,5))