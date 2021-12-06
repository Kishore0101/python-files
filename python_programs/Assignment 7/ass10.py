#program to find area of rectangle with try except using oops
class rectangle:
    def area(self,length,breadth):
        try:
            area=length*breadth
            print( "The area of rectangle is",area)
        except NameError:
            print("variable is not declared")
        finally:
            print("Try except is executed")
if __name__=='__main__':
    obj1=rectangle()
    length=int(input("Enter the length"))
    breadth=int(input("Enter the breadth"))
    obj1.area(length, breadth)