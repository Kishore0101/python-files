#volume of cylinder using while loop
import math
class volume:
    def result(self):
        value=""
        while(value!="s"):
            radius=float(input("enter a radius value :"))
            height=float(input("enter a height value"))
            volume=math.pi*pow(radius,2)*height
            print("volume of cylinder is ",volume)
            value=input("s means stop c means continue")
if __name__=="__main__":
    obj=volume()
    obj.result()            

