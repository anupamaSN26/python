def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter a:"))
b=int(input("Enter b:"))
GCD=gcd(a,b)
print("GCD is ", GCD)

#. Count the occurrences of each word in a line of text. 


#The split() method splits a string into a list.
w=(input("Enter the text:").split())
a={i:w.count(i) for i in w}
print(a)