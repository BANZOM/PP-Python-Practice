def func1(arg1,*args):
    print(arg1,args)

func1(1,2,3,4,5)

def func2(arg1,**kwargs):
    print(arg1,kwargs)

func2(1,a=2,b=3,c=4,d=5)