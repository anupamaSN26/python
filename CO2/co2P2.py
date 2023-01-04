n=int(input("Enter the limit:"))
first=0
second=1
third=first+second
print(first)
while third<n:
    print(third)
    third=first+second
    first=second
    second=third