##Filter odd and even number form a list

def filterList(l):
    resetList = [[],[]]
    for i in l:
        if i % 2 == 0:
            resetList[1].append(i)
        else:
            resetList[0].append(i)
    return resetList

number = list(map(int,input("Enter numbers for squre : ").split(",")))
print(filterList(number))