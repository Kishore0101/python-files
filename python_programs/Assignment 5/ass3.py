#volume of sphere using while loop
import math
class volume:
    def result(self):
        value=""
        while(value!="s"):
            radius=float(input("enter the radius value"))
            volume=1.33*math.pi*pow(radius,3)
            print("volume of sphere is :",volume)
            value=input("stop means s and c means continue")
if __name__=="__main__":
    obj=volume()
    obj.result()    