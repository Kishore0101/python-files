#program to find the perimeter of circle using for loop and oops
import math
class loop:
    def __init__(self,number):
        self.number=number
    def result(self):
        for i in range(0,self.number):
            print("--------------------------------------")
            radius=float(input("Enter the radius of circle"))
            area=math.pi*radius*2
            print("The perimeter of circle is",area)
            print("--------------------------------------")
            
if __name__=='__main__':
    number=int(input("Enter the range"))
    obj1=loop(number)
    obj1.result()