def isPalindrome(name):
    return name == name[::-1]

name = input("Enter your name : ").lower()
print(isPalindrome(name))
# revname = name[::-1]

# if name == revname :
#     print(f"{name} is Palindrome")
# print(f"{name} is Not a palindrome")

