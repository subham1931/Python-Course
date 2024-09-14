#ask user's name and age
#if user name starts wiht ('a' or 'A') and age is above than 10
#print You can woth movies
#else print sorry youn can"t watch movie

name,age = input("Enter name and age (,)").split(',')

if (name[0] == 'a' or name[0] == 'A') and int(age) >= 18 :
    print("You can watch movie")
else:
    print("you can t eatch the movie")