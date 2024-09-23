#pass list into a function
num = [1,2,3,4,5,6,7,8,9]
def negative(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative(num))