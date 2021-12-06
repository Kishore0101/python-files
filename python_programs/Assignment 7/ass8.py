
#program to find the area of triangle  using user defined function with oops
import math
class triangle:
    def area(self):
        area=0.5*base*height
        print("The area of triangle is",area)
if __name__=='__main__':
    base=int(input("Enter the base of the triangle"))
    height=int(input("Enter the height of the triangle"))
    obj=triangle(base,height)
    obj.area()