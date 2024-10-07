###Define a func that takes 2 arguments
###list containing strings
###string that we want to find 
###this func will return the index fof the string 
###if the string not present on the list then it will return -1

def findName(name,*args):
    for i,j in enumerate(args):
        if j == name:
            return i
    return -1   

names = ['subham','anubhab','rohit']

nameToFind = input("Enter a name to find : ")
print(findName(nameToFind, *names))