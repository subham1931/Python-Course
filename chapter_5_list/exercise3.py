def strRev(l):
    rev = []
    for i in l:
        rev.append(i[::-1])
    return rev

name = input("Enter names for reverse: ").split(",")
print(strRev(name))