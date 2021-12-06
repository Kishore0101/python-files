#volume of cone using while loop
import math
class loop:
    def result(self):
        value=""
        while(value !="s"):
            print("*************************")
            radius=float(input("Enter the radius of cone"))
            height=float(input("Enter the height of cone"))
            volume=math.pi*pow(radius,2)*height/3
            print("The volume of cone is",volume)
            print("*************************")
            value=input("Type s to stop,c to continue")

if __name__=='__main__':
    obj1=loop()
    obj1.result()