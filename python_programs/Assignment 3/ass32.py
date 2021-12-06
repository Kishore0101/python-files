#get three names and print alphabetic order                
class alphabet:
    def __init__(self,names):
        self.names=names
    def display(self):
        names=self.names.split(",")
        n=3
        i=0
        while i<n:
            j=i+1
            while j<n:
                if names[i][0]>names[j][0]:
                    temp1=names[i]
                    names[i]=names[j]
                    names[j]=temp1
                j=j+1
            i=i+1
        print("Names after sorting")
        for nam in names:
            print(names)
if __name__=='__main__':
    names=input("Enter four names as comma seperated")
    obj1=alphabet(names)
    obj1.display()        
