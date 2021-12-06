
class marksheet:
    def __init__(self,marks):
            self.marks=marks
    def result(self):
        print("*********************************************")
        print("            Marksheet of KG                  ")
        print("*********************************************")
        print("\n")
        print("Reg.no:{}".format(self.marks["Reg no"]))
        print("\n")
        print("---------marks secured-----------------")
        print("Language 1: {}".format(self.marks["lang 1"]))
        print("Language 2: {}".format(self.marks["lang 2"]))
        print("English: {}".format(self.marks["Eng"]))
        print("Science: {}".format(self.marks["Sci"]))
        print("Social Science: {}".format(self.marks["Soc"]))
        print("--------------RESULT--------------")
        marks=[self.marks["lang 1"],self.marks["lang 2"],self.marks["Eng"],self.marks["Sci"],self.marks["Soc"]]
        total=sum(marks)
        print("TOTAL :",total)
        Avg=total/len(marks)
        print("Avearage :",Avg)
        print("Result : PASS")
    


        
if __name__=="__main__":
    marks={"Reg no":83849,"lang 1":87,"lang 2":76,"Eng":45,"Sci":87,"Soc":98}
    obj=marksheet(marks)
    obj.result()
