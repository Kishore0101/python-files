#program to find the simple interest using while loop and oops
class loop:
    def result(self):
        value=""
        while(value !="s"):
            print("*************************")
            principle=float(input("Enter the principle amount"))
            rate=float(input("Enter the rate of interest"))
            number=float(input("Enter the number of days"))
            SI=principle*rate*number/100
            print("The simple interest is",SI)
            print("*************************")
            value=input("type s to stop,c to continue")

if __name__=='__main__':
    obj1=loop()
    obj1.result()