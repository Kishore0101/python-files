#print prime number and fibonacci series using set
#program to print the set of prime numbers and fibbinocci series
class series:
    def __init__(self,length):
        self.length=length
    def primeno(self):
        num=15
        find_no=2
        prime=set()
        while num != len(prime):    
            for i in range(1,find_no):
                if find_no%i==0 and find_no!=i and i!=1:
                    break
                else:
                    if i== find_no-1:
                        print(find_no)
                        prime.add(find_no)

    find_no+=1
    def fibinocii(self):
        fibinocii_series=set()
        first,second=0,1
        for i in range(1,length):
            fibinocii_series.add(first)
            third=first+second
            first=second
            second=third
        print("fibinocii_series",fibinocii_series)
if __name__=='__main__':
    length=int(input("Enter the range "))
    obj1=series(length)
    obj1.primeno()
    obj1.fibinocii()