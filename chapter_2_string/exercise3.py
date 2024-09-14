name,char = input("Enter your name and a latter  for find its count (input will be seperated with comma) : ").split(',')

print(f"Length of {name} is {len(name)}")

print(f"{char} in {name} : {name.lower().count(char.lower())}")