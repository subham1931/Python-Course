def func(n):
    # for i in range(1,n+1):
    #    if i %2 == 0 :
    #        yield(i)
    yield from (i  for i in range(1,n+1) if i % 2 == 0)

res = func(11)
print([i for i in res])