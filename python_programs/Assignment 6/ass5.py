#print marksheet using list
class marksheet:

    def __init__(self,marks):
        self.marks=marks
    def result(self):
        print("             GOVERNMENT STATE BOARD CERTIFICATION               ")
        print("****************************************************************")  
        print("roll no:{:<25}name:{}".format(self.marks[0],self.marks[1]))
        print("\n")
        print("{:<25}{}".format("subject","subject obtained"))
        print("{:<28}{}".format("tamil",self.marks[2]))
        print("{:<28}{}".format("english",marks[3]))
        print("{:<28}{}".format("maths",marks[4]))
        print("{:<28}{}".format("science",marks[5]))
        print("{:<28}{}".format("social",marks[6]))
        c=0
        for i in marks[2:7]:
            if i>35:
                c=c+1
        if c==5:
            print("total marks:{:<15}result:{}".format(sum(marks[2:7]),"PASS"))
        else:
            print("total marks:{:<15}result{}".format(sum(marks[2:7]),"PASS"))            
        


if __name__=="__main__":
    marks=["1622026","kishore kumar",93,76,98,100,97,"01/11/1998"]
    obj=marksheet(marks)
    obj.result()
