x=int(input("enter the numbers:"))
r=range(1,x+1,1)
fact=1
if x<0:
    print("invalid input")
elif x==0:
    print("factorial of 0 is 0")
else:
    for i in r:
        fact=fact*i
        print( "factorial of",x,"is",fact)
