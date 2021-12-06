#volume of cube using while loop
class volume:
    def result(self):
        value=""
        while(value!="s"):
            side=float(input("enter a value"))
            volume=pow(side,3)
            print("the volume of cube",volume)
            value=input("s means stop c means continue : ")
if __name__=="__main__":
    obj=volume()
    obj.result()
