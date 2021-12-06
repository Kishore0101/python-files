#roots of quadratic equation
import cmath
acoeff=float(input("enter a value of a :"))
bcoeff=float(input("enter a value of b :"))
ccoeff=float(input("enter a value of c :"))
dis=pow(bcoeff,2)-4*acoeff*ccoeff
sqt=cmath.sqrt(dis)
root1=(-bcoeff+sqt)/2*acoeff
root2=(-bcoeff+sqt)/2*acoeff
print("the annswer is ",root1,root2)

