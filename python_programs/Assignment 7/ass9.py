#program to print the address with try except using oops 
class Address:
    def __init__(self):
      self.addr=input("Enter the Address")
    def display(self):
        try:
          print("##################")
          print("----"+self.addr+"-----")
          print("#################")
        except NameError:
            print("The variable is not declared")
        finally:
            print("The try except is executed")
if __name__=='__main__':
    obj1=Address()
    obj1.display()
    