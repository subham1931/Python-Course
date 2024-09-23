cars = ['Rolls-Royce Phantom','Bentley Continental GT','Lamborghini Aventador','Aston Martin DB11','Ferrari SF90 Stradale']

#pop method
#it will delete last element
cars.pop()
print(cars)

# #delete with index
cars.pop(1)
print(cars)

#delete operator
del cars[1]
print(cars)

#remove method
cars.remove('Lamborghini Aventador')
print(cars)