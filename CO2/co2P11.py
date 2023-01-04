l=int(input("Enter length of the rectangle:"))
b=int(input("Enter breadth of the rectangle:"))
h=int(input("Enter height of the triangle:"))
ar=lambda x,y:x*y
asq=lambda x:x*x
at=lambda x,y:0.5*x*y
print("area of rectangle:",ar(l,b))
print("area of square:",asq(l))
print("area of triangle:",at(b,h))