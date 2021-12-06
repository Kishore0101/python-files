#get 2 names and print alphabetical order
class albhabet:
    def __init__(self):
        self.First_name=input("enter the first name : ")
        self.Second_name=input("enter the second name : ")
    def display(self):
        if self.First_name[0]<self.Second_name[0]:

            return print(self.First_name,self.Second_name)
        else:
            return print(self.Second_name,self.First_name)
if __name__=="__main__":
    obj=albhabet()
    obj.display()            
