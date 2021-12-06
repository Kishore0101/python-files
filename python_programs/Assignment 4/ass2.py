#area of rectangle using loop
class rectangle:
    def __init__(self,number):
        self.number=number
    def display(self):
        for i in range(0,self.number):
            base=int(input("enter a value :"))
            height=int(input("enter a value :"))
            area=base*height
            print("the area of rectangle",area)
if __name__=="__main__":
    number=int(input("enter a loop number :"))
    obj=rectangle(number)
    obj.display()
