#area of triangle using loop
class triangle:
    def __init__(self,number):
        self.number=number
    def display(self):
        for i in range(0,self.number):
            base=float(input("enter a base value :"))
            height=float(input("enter a height value :"))
            area=0.5*base*height
            print("the area of square",area)
if __name__=="__main__":
    number=int(input("enter a loop number :"))
    obj=triangle(number)
    obj.display()            
