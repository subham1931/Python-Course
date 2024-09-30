user_info = {
    "name" : "subham",
    'age' : 24,
    'games':['GTA','RDR'], 
    'anime' : ['jujutsu kaisen','Demon Slayer','Naruto']
}

more_info = {'song': ['song1','song2','song3']}

user_info.update(more_info)
print(user_info.items())