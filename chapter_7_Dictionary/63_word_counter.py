def counter(name):
    count = {}
    for i in name:
        count[i] = name.count(i)
    return count

word = input("Ener a word for count character : ")
print(counter(word))
