##method 1
# def revList(l):
#     l.reverse()
#     return l

##method 2
# def revList(l):
#     return l[::-1]

#method 3
def revList(l):
    rev = []
    i =0
    while l:
        rev.append(l.pop())
        i += 1
    return rev



number = list(map(int,input("Enter numbers for squre : ").split(",")))
#[1,2,3,4,5]
print(revList(number))
