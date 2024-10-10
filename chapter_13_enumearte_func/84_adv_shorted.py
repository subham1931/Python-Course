# names = ['subham','anubhab','rohit']
# names.sort()
# print(names)

# ##we dont have sort method for tuple and sets 
# ##so we can use the sorted method which return a list with sorted items
# names2 = ('subham','anubhab','rohit')
# print(sorted(names2))
# names3 = {'subham','anubhab','rohit'}
# print(sorted(names3))


##create an func for guessing the score
std = [
    {'name':'subham','roll' : 27,'score' : 88},
    {'name':'anubhab','roll' : 28,'score' : 78},
    {'name':'rohit','roll' : 29,'score' : 70}
]

print(sorted(std,key= lambda i : i['score'],reverse=True))

###only getting the names
print([s['name'] for s in sorted(std,key= lambda i : i['score'],reverse=True)]) 