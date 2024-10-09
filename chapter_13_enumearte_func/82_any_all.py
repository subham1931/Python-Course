##all() return true if a list have all value true or return false

n1 = [2,4,6,8,9]
res = lambda n1:[i%2==0 for i in n1]
print(all(res(n1)))