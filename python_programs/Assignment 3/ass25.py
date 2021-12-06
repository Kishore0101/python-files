#find smallest number
def greater(First_number,Second_number):
     if First_number<Second_number:
        return First_number
            #print("The smallest of two numbers is",a)
     else:
            #print("The smallest of two numbers is",b)
        return Second_number
if __name__ == "__main__":
    First_number=int(input("Enter a First number :"))
    Second_number=int(input("Enter a First number :"))
    Third_number=greater(First_number,Second_number)
    print(Third_number)