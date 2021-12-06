#program to find the distance between points
import math
x1=float(input("Enter the the coordinate x1"))
y1=float(input("Enter the the coordinate y1"))
x2=float(input("Enter the the coordinate x2"))
y2=float(input("Enter the the coordinate y2"))
y=pow((y2-y1),2)
x=pow((x2-x1),2)
dist=math.sqrt((y+x))
print("The distance between the points is",dist)