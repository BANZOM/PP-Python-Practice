x = int(input())
y = int(input())
z = int(input())
n = int(input())


lst = []

#possible permutations 
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            lst.append([i,j,k])
reqLst = []
#required permutations 
for [x,y,z] in lst:
    if x+y+z != n :
        reqLst.append([x,y,z])
    
print(reqLst)

'''
List comprehensions are an elegant way where lists can be built without having to use different for loops to append values one by one.

print [[x,y,z] for x in xrange(a + 1) for y in xrange(b + 1) for z in xrange(c + 1) if x + y + z != n]
'''