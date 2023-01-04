from Graphics.rectangle import*
from Graphics.circle import*
from Graphics.threeDgraphics.cuboid import*
from Graphics.threeDgraphics.sphere import*

l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of Rectangle= ",RectArea(l,b))
print("Perimeter of rectangle= ",RectPerimeter(l,b))

r=int(input("Enter the radius of a circle:"))
print("Area of circle= ",CircleArea(r))
print("perimeter of circle= ",CirclePeri(r))

l1=int(input("Enter the length of cuboid:"))
b1=int(input("Enter the breadth of cuboid:"))
h1=int(input("Enter the height of cuboid:"))
print("Area of cuboid:",CuboidArea(l1,b1,h1))
print("Perimeter of cuboid:",CuboidPeri(l1,b1,h1))

r=int(input("Enter the radius of sphere:"))
print("Area of sphere= ",SpArea(r))
print("perimeter of sphere= ",SpPerimeter(r))

