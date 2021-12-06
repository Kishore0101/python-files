#find biggest two numbers
def greater(First_number,Second_number):
    if First_number>Second_number:
        return First_number
    else:
        return Second_number
if __name__=="__main__":
    First_number=int(input("enter a first number :")) 
    Second_number=int(input("enter a Second number :")) 
    Third_number=greater(First_number,Second_number)
    print(Third_number)            


