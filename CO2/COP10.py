#Generate all factors of a number. 
n=int(input("Enter a number :"))
print(" factors of ",n," are:")

for i in range(1,n+1):
    
#     for j in range(0,n):
        
        if n % i==0:
            print(i)