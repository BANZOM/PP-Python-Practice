n = int(input("Enter no. of rows: "))

for i in range(n):
    print(" "*(n-i-1),end="")
    s=""
    for j in range(i+1):
        print(chr(65+j),end="")
        if j!=i:
            s+=chr(65+j)
    print(s[::-1],end="\n")