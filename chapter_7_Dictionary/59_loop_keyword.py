user_info = {
    "name" : "subham",
    'age' : 24,
    'games':['GTA','RDR'], 
    'anime' : ['jujutsu kaisen','Demon Slayer','Naruto']
}

##Check key is present or not
# if 'games' in user_info:
#     print('present')
# else:
#     print('Not present')

##Check string value present or not
# if 'subham' in user_info.values():
#     print('present')
# else:
#     print('Not present')

##check list value present or not
# if ['GTA','RDR'] in user_info.values():
#     print('present')
# else:
#     print('Not present')

##Printting all keys in dict
# for i in user_info:
#     print(i)

##Printing al values in a dict
# for i in user_info.values():
#     print(i)


##Values method()
##Print dict values inside a list
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

##keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

##items method
##it resturn a list having tubple objects
user_info_item = user_info.items()
print(user_info_item)

##tuple unpacking
for i,j in user_info.items():
    print(i,j)