def findList(l):
    res = 0
    for i in li :
        if type(i) == list:
            res += 1
    return res


li =[1,2,3,[12,32],[12,32]]
print(findList(li))