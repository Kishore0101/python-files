#smallest among three numbers
def greater(First_number,Second_number,Third_number):
    if First_number<Second_number and First_number<Third_number:
        return First_number
    elif Second_number<Third_number:
        return Second_number
    else:
        return Third_number

if __name__=="__main__":
    First_number=int(input("enter a First number : "))
    Second_number=int(input("enter a Second number : "))
    Third_number=int(input("enter a Third number : "))
    Fourth_number=greater(First_number,Second_number,Third_number)
    print(Fourth_number)
