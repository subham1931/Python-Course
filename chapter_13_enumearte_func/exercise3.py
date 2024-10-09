def averageFiner(*args):
    tup = []
    for i in zip(*args):
        tup.append(sum(i)//len(i))
    return tup

res = lambda *args : [sum(i)//len(i) for i in zip(*args)]

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
print(averageFiner(l1,l2))
print(res(l1,l2))