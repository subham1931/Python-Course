####fromkeys
##list
d1 = dict.fromkeys(['name','age','roll'],'unknown')

##tuple
d2= dict.fromkeys(('name','age','roll'),'unknown')

##string
d3 = dict.fromkeys('abc','unknown')

##range
d4 = dict.fromkeys(range(1,4),'unknown')
# print(d1)
# print(d2)
# print(d3)
# print(d4)



##get method
user_info = {
    "name" : "subham",
    'age' : 24,
    'games':['GTA','RDR'], 
    'anime' : ['jujutsu kaisen','Demon Slayer','Naruto']
}

##if there was no key found then it will return none
# print(user_info.get('name'))
###we can overwrite the none with our custom output
print(user_info.get('names','not found'))

##clear method
# user_info.clear()
# print(user_info)


##copy method
# data = user_info.copy()
# print(data)