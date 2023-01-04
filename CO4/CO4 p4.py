class time:
    def __init__(self):
        self.__hour=int(input("Enter the time in hour :"))
        self.__minute=int(input("Enter the time in minute :"))
        self.__second=int(input("Enter the time in second :"))
        
    def __add__(self,ob2):
        hours=self.__hour + ob2.__hour
        minutes=self.__minute+ob2.__minute
        seconds=self.__second+ob2.__second
        
        
        if seconds>=60:
            seconds-=60
            minutes+=1
        if minutes>=60:
            minutes-=60
            hours+=1
        print("Sum of hours",hours)
        print("Sum of minutes",minutes)
        print("Sum of seconds",seconds)
            
            
#         return time(hour,minute,second)
   
print("Enter the time of first object:")
ob1=time()  
print("Enter the time of second object:")
ob2=time()
ob1.__add__(ob2)
    