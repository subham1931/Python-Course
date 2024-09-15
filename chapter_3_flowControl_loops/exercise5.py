#ask user name as input
#print each charctaer count in the name 

name = input("Enter you name : ")
name = name.lower()
i = 0
temp = ""
while i < len(name):
    if name[i] not in temp:
        print(f"{name[i]} = {name.count(name[i])}")
        temp += name[i]
    i += 1 