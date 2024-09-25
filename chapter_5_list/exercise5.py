def common(l1,l2):
    commonList = []
    for i in l1:
        if i in l2:
            commonList.append(i)
        else:
            continue
    return commonList

l1 = [1,2,3,4,5]
l2 = [2,4,8,9,6]
print(common(l1,l2))