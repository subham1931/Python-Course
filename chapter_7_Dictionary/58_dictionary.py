##BEcause of the limitation of list ,list are not enough to represent real data 
user_li = ['Subham','24',['GTA','RDR'],['jujutsu kaisen','Demon Slayer','Naruto']]
###this is a list having user data but this is not the proper method of declaration

##To overcome this problem we use dictionary which is an unordered collection of data in key : value pair
user_dict = {'name' : 'subham' , 'age' : 24, 'games':['GTA','RDR'], 'anime' : ['jujutsu kaisen','Demon Slayer','Naruto']}
# print(user_dict)

user1 = dict(name='Subham',age=24)
# print(user1)

##acess value using key
# print(user_dict['name'])
# print(user1['name'])

##We can store numbers ,strings,lis,dictionary inside a dictionary
user_info = {
    "name" : "",
    'age' : 24,
    'games':['GTA','RDR'], 
    'anime' : ['jujutsu kaisen','Demon Slayer','Naruto']

}

print(user_info['games'])