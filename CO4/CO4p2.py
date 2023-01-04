#create a bankaccount and members,acciunt number and type etc
class bankaccount:
    def __init__(self,acno,actype,name,balance=0):
        self.acno=acno
        self.actype=actype
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
    
x=input("Enter the name of account holder:")
y=int(input("Enter the account number:"))
z=input("Enter the account type:")
#b=int(inpu
obj=bankaccount(y,z,x)
print("Account Number:" ,obj.acno)
print("Account Name:" ,obj.name)
print("Account type:",obj.actype)
print("Account Balance:", obj.balance)

w=int(input("Enter the value to deposit:"))
obj.deposit(w)
print("Account Balance:", obj.balance)

u=int(input("Enter the value to withdraw:"))
obj.withdraw(u)
print("Account Balance:", obj.balance)


        
    
    
