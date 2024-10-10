# res = lambda l : [len(i) for i in l]



# names = ['subham','anubhab','rohit']
# print(max(res(names)))
# print(max(names,key= res))
# print(max(names,key= lambda names : len(names)))


###find max score 

#data
# std = [
#     {'name':'subham','roll' : 27,'score' : 88},
#     {'name':'anubhab','roll' : 28,'score' : 78},
#     {'name':'rohit','roll' : 29,'score' : 70}
# ]

# print(max(std,key = lambda i : i.get('score') ))
# print(max(std,key = lambda i : i.get('score') )['name'])
# print(max(std,key = lambda i : i.get('score') ).get('roll'))


std2= {
    'subham' : {'score':90,'roll' : 34},
    'anubhab' : {'score':92,'roll' : 35},
    'rohit' : {'score':93,'roll' : 36},
}

print(max(std2,key = lambda i : std2[i]['score']))