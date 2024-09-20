def user(f,l):
    print(f"Full name is {f.title()}  {l.title()}")

def display():
    fName = input("Enter your first name : ")
    lName = input("Enter your last name : ")
    user(fName,lName)
    
display()