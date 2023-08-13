from functools import reduce


n = list(filter(lambda x: (x)>10, range(5,20)))
# print(n)

n = reduce(lambda x,y: x+y, range(1,5))
print(n)