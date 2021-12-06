#print number of hours minutes seconds using while loop
class days:
    def __init__(self,ndays):
        self.ndays=ndays
    def result(self):
            nhours=self.ndays*24
            nminutes=nhours*60
            nseconds=nminutes*60
            print("hours :",nhours)
            print("minutes :",nminutes)
            print("seconds :",nseconds)
if __name__=="__main__":
    value=""
    while(value!="s"):
        ndays=int(input("enter the days :"))
        obj=days(ndays)
        obj.result()
        value=input("s means stop c means continue :")        
