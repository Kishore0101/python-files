#program using 5 builtin function with oops
class built:
    def __init__(self):
        self.string=input("Enter a string")
        self.lst=[23,45,25,89,76,87,98]
    def display(self):
        print("length of string is",len(self.string))
        print("the type of the word is",type(self.string))
        print("whether the string has any uppercase",self.string.upper())
        print("whether the string has any lowercase",self.string.lower())
        print("the greatest number in the list is",max(self.lst))
        print("the lowest number in the list is",min(self.lst))
if __name__=='__main__':
    obj=built()
    obj.display()