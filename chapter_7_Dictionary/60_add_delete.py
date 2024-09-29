user_info = {
    "name" : "subham",
    'age' : 24,
    'games':['GTA','RDR'], 
    'anime' : ['jujutsu kaisen','Demon Slayer','Naruto']
}

##add data to dictionary
user_info['songs'] = ['song1','song2']

##pop data from the dictionary
print(user_info.pop('age'))
for i,j in user_info.items():
    print(i,j)