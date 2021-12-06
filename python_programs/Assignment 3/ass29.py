#biggest among four number
def greater(First_number,Second_number,Third_number,Fourth_number):
    if First_number>Second_number and First_number>Third_number and First_number>Fourth_number:
        return First_number
    elif Second_number>Third_number and Second_number>Fourth_number:
        return Second_number
    elif Third_number>Fourth_number:
        return Third_number
    else:
        return print("Biggest Number is :",Fourth_number) 
if __name__=="__main__":
    First_number=int(input("enter a first number :")) 
    Second_number=int(input("enter a Second number :")) 
    Third_number=int(input("enter a Third number :"))
    Fourth_number=int(input("enter a fourth number :"))
    Answer=greater(First_number,Second_number,Third_number,Fourth_number)
    print(Answer)            

           