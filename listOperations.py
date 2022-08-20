'''

LISTS: advanced of array

'''

#initializing list
l = [1,2,3,4,5,6]
print(l)

print("First element of list: ", l[0])

#slicing of list
x = l[0:2]
print(x)
print(l[0:2])
print(l[0:4])
print(l[4:6])

#adding elements in list
l.append(7)
l.append([7,8])
print(l)
l.append(x)
print(l)
print(l[6:8])