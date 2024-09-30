##Define a function that takes a number(n)
#retun a dict containing cube of number  from 1 to n

##example
#cube_finser(3)
##{1:1,2:8,3:27}

def cube_finer(num):
    cube = {}
    for i in range(1,num+1):
        cube[i] = i**3
    return cube
print(cube_finer(3))