##pirnt element by there position
##without using enumerate func
name = ['subham','anubhab','rohit']
pos = 0
for i in name:
    print(f'{pos} -> {i}')
    pos += 1

##using enumerate func 
for i,j in enumerate(name):
    print(f"{i} : {j}")
