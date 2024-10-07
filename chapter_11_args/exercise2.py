def exercise(*name,**kwargs):
    if  kwargs.get('revStr') == False:
        return [i.title() for i in name]
    elif kwargs.get('revStr') == True:
        return [i[::-1].title() for i in name]

name = ['subham','anubhab','rohit']
# print(exercise(*name,revStr = False))
print(exercise(*name,revStr = True))