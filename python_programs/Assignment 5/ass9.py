#program to find the roots of quadratic equation using while loop and oops
import cmath
class loop:
    def result(self):
        value=""
        while(value !="s"):
            print("*************************")
            acoeff=int(input("Enter the value for coefficient a"))
            bcoeff=int(input("Enter the value for coefficient b"))
            ccoeff=int(input("Enter the value for coefficient c"))
            dis = pow(bcoeff,2)-4*acoeff*ccoeff
            sqt=cmath.sqrt(dis)
            root1=(-bcoeff-sqt)/(2*acoeff)
            root2=(-bcoeff+sqt)/(2*acoeff)
            print("The roots are ",root1,root2)
            print("*************************")
            value=input("type s to stop,c to continue")

if __name__=='__main__':
    obj1=loop()
    obj1.result()