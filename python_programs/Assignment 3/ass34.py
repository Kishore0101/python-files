#gives number odd or even
class check:
    def __init__(self,number):
        self.number=number
    def display(self):
        if self.number%2==0:
            print("given number is even")
        else:
            print("given number is odd")  
if __name__=="__main__":
    number=int(input("enter the any number :"))
    obj=check(number)   
    obj.display()               

    