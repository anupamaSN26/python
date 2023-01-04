class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
   
    def get_area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.get_area() < other.get_area()
a=int(input("enter the length: "))
b=int(input("enter the width: "))
c=int(input("enter the lenth of 2nd rect: "))
d=int(input("enter the width of 2nd rect: "))
rectangle1=Rectangle(a,b)
rectangle2=Rectangle(c,d)
if rectangle1 < rectangle2:
    print("obj 1 has a smaller area than obj 2")
else:
    print("obj 1 has a larger  area to obj 2")

    