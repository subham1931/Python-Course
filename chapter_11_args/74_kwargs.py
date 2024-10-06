##kwargs take the value as an dict
##we use kwargs when we have ky:value argument
##for kwargs we have to use **operator


def func(**kwargs):
    {print(f"{i}: {j}") for i, j in kwargs.items()}

##normal passing argument
func(fname = 'subham',lname='nayak')

# passing argument as dictionary unpacking
di = {'firstname':'Subham','lastname':'Nayak','age':23}
func(**di)