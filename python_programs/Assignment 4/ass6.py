#program to find the perimeter of rectangle using for loop and oops
class loop:
    def __init__(self,number):
        self.number=number
    def result(self):
        for i in range(0,self.number):
            print("--------------------------------------")
            length=int(input("Enter the length"))
            breadth=int(input("Enter the breadth"))
            perimeter=2*(length+breadth)
            print("The perimeter of the rectangle is",perimeter)
            print("--------------------------------------")



if __name__=='__main__':
    number=int(input("Enter the range"))
    obj1=loop(number)
    obj1.result()