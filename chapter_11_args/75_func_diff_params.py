#parameter
#*args
#default params
#**kwargs

def func(name,*args,clg='vssut',**kwargs):
    print(name)
    print(*args)
    print(clg)
    for i,j in kwargs.items():
        print(f"{i} : {j}")

func('subham','nayak',24,roll=2206151027,sec='A')
