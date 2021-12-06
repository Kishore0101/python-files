#Biggest among five numbers 
class biggest:
    def __init__(self,First_number,Second_number,Third_number,Fourth_number,Fifth_number):
        self.First_number=First_number
        self.Second_number=Second_number
        self.Third_number=Third_number
        self.Fourth_number=Fourth_number
        self.Fifth_number=Fifth_number
    def display(self):
        if self.First_number>self.Second_number and self.First_number>self.Third_number and self.First_number>self.Fourth_number and self.First_number>self.Fifth_number:
            return print(self.First_number)
        elif self.Second_number>self.Third_number and self.Second_number>self.Fourth_number and self.Second_number>self.Fifth_number:
            return print(self.Second_number)
        elif self.Third_number>self.Fourth_number and self.Third_number>self.Fifth_number:
            return print(self.Third_number)
        elif self.Fourth_number>self.Fifth_number:
            return print(self.Fourth_number)
        else:
            return print(self.Fifth_number)
if __name__=="__main__":
    First_number=int(input("enter a First number : "))
    Second_number=int(input("enter a Second number : "))
    Third_number=int(input("enter a Third number : "))  
    Fourth_number=int(input("enter a Fourth number : "))
    Fifth_number=int(input("enter a Fifth number : "))
    obj=biggest(First_number,Second_number,Third_number,Fourth_number,Fifth_number)
    obj.display()
        
                   