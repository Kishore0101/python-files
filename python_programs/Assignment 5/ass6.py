#program to find the compound interest using while loop and oops
class loop:
    def result(self):
        value=""
        while(value !="s"):
            print("*************************")
            principle=float(input("Enter the principle amount"))
            rate=float(input("Enter the rate of interest"))
            number=float(input("Enter the compounds per year"))
            time=float(input("Enter the number of year"))
            compound_interest=principle*pow((1+rate/number),number*time)
            print("The compound interest is",compound_interest)
            print("*************************")
            value=input("type s to stop,c to continue")

if __name__=='__main__':
    obj1=loop()
    obj1.result()