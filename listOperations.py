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

#inserting elements at a particular index and shift rest
x = l[0:2]
l.insert(0,0) # (index,element)
print(l)
l.insert(1,x)
print(l)


#sorting of lists
l= [55,6,55,55,444454,54,655,879,6654,86455,55,48687,686,4487,6548,65587,57,946525,46,85,40,5.55,464,5]
l.sort()
print(l)


#pop of list: deleting element from list
l.pop(1)            # .pop(index_to_pop)
print(l)
removed = l.pop(2)  #storing of Removed element
print(l)
print("Removed element is: ",removed)


#counting of same elements in a given list
count= l.count(55)
print(f"55 is counted by {count} times.")

#lenght of list
print("the lenght of list is: ",len(l))