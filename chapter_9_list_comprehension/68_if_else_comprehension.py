# even_list = []
# odd_list=[]

# for i in range(1,11):
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)

# print(f'Even numbers : {even_list}')
# print(f'odd numbers : {odd_list}')


print(f'Even numbers {[str(i) + ' even' if (i % 2 == 0) else str(i) + ' odd' for i in range(1,11)]}')