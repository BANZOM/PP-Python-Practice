def assertCheck(a):
    print("Input number is: {}".format(a))
    assert isinstance(a,int) and a>0, "This should be a positive integer"
    
    
a = int(input("Enter a num: "))
assertCheck(a)