num1,num2 = map(int,input().split())
for i in str((num1*num2))[::-2]:
    print(i,end="")