def calPower(x):
    def power(n):
        return n ** x
    return power

cube = calPower(3)
print(cube(3))

squre = calPower(2)
print(squre(4))