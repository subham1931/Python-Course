def print_user():
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    mov = input("Enter favourite movies : ").split(',')
    song = input("Enter favourite songs : ").split(',')
    user= {
        'name':name,
        'age' : age,
        'mov' : mov,
        'song' : song
    }

    for i,j in user.items():
        print(f'{i}:{j}')

print_user()  