#program to find the time taken travel a distance using while loop and oops
class loop:
    def result(self):
        value=""
        while(value !="s"):
            print("*************************")
            distance=float(input("Enter the distance in km"))
            speed=float(input("Enter the speed in km\hr"))
            time=distance/speed
            print("The time taken to travel in hours is",time)
            print("*************************")
            value=input("type s to stop,c to continue")


if __name__=='__main__':
    obj1=loop()
    obj1.result()