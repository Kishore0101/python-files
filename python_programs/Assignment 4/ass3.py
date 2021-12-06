#area of square using loop
class square:
    def __init__(self,number):
        self.number=number
    def display(self):
        for i in range(0,self.number):
            length=int(input("enter a value :"))
            area=length*length
            print("the area of square",area)
if __name__=="__main__":
    number=int(input("enter a loop number :"))
    obj=square(number)
    obj.display()            
