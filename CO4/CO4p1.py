class rectangle:
    def __init__ (self,length,breadth):
        self.length=length
        self.breadth=breadth

    def getperimeter(self):
        return 2 *(self.length+self.breadth)
    def getarea(self):
        return self.length*self.breadth

    def compare(self,obj2):
    
        try:
            if obj1.getarea()==obj2.getarea():
               print("Area of both rectangles are equal")
                
            elif obj1.getarea()>obj2.getarea():
                print("Area of first rectangle is greater than second rectangle")
            elif obj1.getarea()<obj2.getarea():
                print("Area of second rectangle is greater than the first")
        except:
                print("an error has occured")
l1=int(input("Enter the length of first rectangle"))
b1=int(input("Enter the breadth of first rectangle"))
b2=int(input("Enter the breadth of second rectangle"))
l2=int(input("Enter the length of second rectangle"))
obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
print("Peimeter of first rectangle is",obj1.getperimeter())
print("Peimeter of second rectangle is",obj2.getperimeter())
print("Area of first rectangle is ",obj1.getarea())
print("Area of second rectangle is ",obj2.getarea())
obj1.compare(obj2)
                