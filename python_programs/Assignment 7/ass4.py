#program to find out the union from set of prime numbers and fibinocii series
class series:
    def __init__(self,length):
        self.length=length
    def primeno(self):
        self.prime_no=set()
        i=2
        while len(self.prime_no) <length:
            for j in range(2, i):
                    if (i%j) == 0:
                        break
                    else:
                        self.prime_no.add(i)
            i=i+1

        print("prime numbers",self.prime_no)
    def fibinocii(self):
        self.fibinocii_series=set()
        first,second=0,1
        for i in range(1,length):
            self.fibinocii_series.add(first)
            third=first+second
            first=second
            second=third
        print("fibinocii_series",self.fibinocii_series)
    def setunion(self):
        print("union",self.prime_no.union(self.fibinocii_series))
if __name__=='__main__':
    length=int(input("Enter the range "))
    obj1=series(length)
    obj1.primeno()
    obj1.fibinocii()
    obj1.setunion()