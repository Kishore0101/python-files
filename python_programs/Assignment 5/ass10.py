#program to find the slope of line using while loop and oops
class loop:
    def result(self):
        value=""
        while(value !="s"):
            print("*************************")
            x1=float(input("Enter the the coordinate x1"))
            y1=float(input("Enter the the coordinate y1"))
            x2=float(input("Enter the the coordinate x2"))
            y2=float(input("Enter the the coordinate y2"))
            slope=(y2-y1)/(x2-x1)
            print("The slope of the given line is ",slope)
            print("*************************")
            value=input("type s to stop,c to continue")
if __name__=='__main__':
    obj1=loop()
    obj1.result()