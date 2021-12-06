from tabulate import tabulate
class marksheet:
    def __init__(self,marks):
        self.marks=marks
    def result(self):
        self.marks=list(self.marks())
        print("{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{}".format("id","name","Tamil","English","Maths","Science","Social","total"))
        c=1
        for i in self.marks:
            print("{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{}".format(c,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
            c=c+1
if __name__=="__main__":
    marks={1:(1234,"kishore",11,12,13,14,15,16),2:(2345,"ajith",65,67,45,68,89),3:(3456,"angu",34,56,76,67,56,77)}
    obj=marksheet(marks)
    obj.result()
