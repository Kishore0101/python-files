#calculate compound interest
principal=float(input("enter a amount value :"))
rate_interest=float(input("enter a interest value :"))
time=float(input("enter a time period :"))
compound=float(input("enter a compound value : "))
compound_interest=principal*pow((1+rate_interest/time),compound*time)
print("compound of interest value is :",compound_interest)