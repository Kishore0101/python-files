# area of circle using loop 
import math
class circle:
    def __init__(self,number):
        self.number=number
    def display(self):
        for i in range(0,self.number):
            radius=int(input("enter a value :"))
            area=math.pi*pow(radius,2)
            print("the area of square",area)
if __name__=="__main__":
    number=int(input("enter a loop number :"))
    obj=circle(number)
    obj.display()            
