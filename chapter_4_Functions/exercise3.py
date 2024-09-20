def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

n1,n2,n3 = input("Emer 2 number for finding greatest").split(',')
print(f"Greatest between {n1},{n2},{n3} is {greatest(int(n1),int(n2),int(n3))}")