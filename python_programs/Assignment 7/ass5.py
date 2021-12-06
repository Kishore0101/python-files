#program to print the sin,cos,tan,asin,acos,atan,degrees value  of radian using oops
import math
class conversion:
    def __init__(self):
        self.radian=float(input("Enter the value of  radian"))
    def display(self):
        print("sin=",math.sin(self.radian))
        print("cos=",math.cos(self.radian))
        print("tan=",math.tan(self.radian))
        print("asin=",math.asin(self.radian))
        print("acos=",math.acos(self.radian))
        print("atan=",math.atan(self.radian))
        print("degrees",math.degrees(self.radian))
if __name__=='__main__':
    obj=conversion()
    obj.display()