#program to find the perimeter of triangle using for loop and oops
class loop:
    def __init__(self,number):
        self.number=number
    def result(self):
        for i in range(0,self.number):
            print("--------------------------------------")
            length=int(input("Enter the length"))
            height=int(input("Enter the height"))
            base=int(input("Enter the base"))
            perimeter=length+height+base
            print("The perimeter of triangle is",perimeter)
            print("--------------------------------------")
if __name__=='__main__':
    number=int(input("Enter the range"))
    obj1=loop(number)
    obj1.result()