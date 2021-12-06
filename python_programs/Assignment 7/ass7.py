
#program to find the area of circle using user defined function with oops
import math
class circle:
    def area(self):
        radius=21
        area=math.pi*pow(radius,2)
        print("The area of circle is",area)
if __name__=='__main__':
    obj=circle()
    obj.area()