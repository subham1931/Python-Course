user = 'subham'
user2 = "test"
password = "Subham@pass"

name,passw = input("Enter you name and password (using ,)").split(',')

if (name == user or name == user2) and passw == password:
    print("Login sucessfuly")
else:
    print("Login faild")