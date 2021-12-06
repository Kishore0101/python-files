# get foue names and print alphabetic order
class alphabetic:
    def __init__(self,names):
        self.names=names
    def display(self):
        names=self.names.split(",")
        n=4
        i=0
        while i<n:
            j=i+1
            while j<n:
                if names[i][0]>names[j][0]:
                    temp=names[i]
                    names[i]=names[j]
                    names[j]=temp
                j=j+1
            i=i+1
            print("print after sorting")
            for nam in names:
                print(nam)
if __name__=="__main__":
    names=input("enter a four names :")
    obj=alphabetic(names)
    obj.display()                        


