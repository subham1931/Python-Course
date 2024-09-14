sen = "She is beautiful and She is  good dancer"
print(sen.replace("is","was"))
#we can replace number of replaces
# print(sen.replace("is","was",1))

#stntax string.find("char",index of stat searching)
# print(sen.find("is"))

isPos1 = sen.find("is")
isPos2 = sen.find("is",isPos1+1)
print(isPos2,isPos1)