print({i : i**2 for i in range(1,11)})

###counting a char in string
name = "subham nayak"
print({i : name.count(i) for i in name})

##check odd even
print({i : ('even' if i % 2 ==  0 else 'odd') for i in range(1,11)})