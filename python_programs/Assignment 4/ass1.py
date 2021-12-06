#print address using for loop
class loop:
    def __init__(self,number):
        self.number=number
    def display(self):
        for i in range(0,self.number):
            address=input("enter the address")
            print("address")
if __name__=="__main__":
    number=int(input("enter a number"))
    obj=loop(number)
    obj.display()


