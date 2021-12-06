#program to find number of hours,minutes,seconds in the given days
ndays=int(input("enter the number of days"))
nhours=24*ndays
nmin=60*nhours
nsec=60*nmin
print("No of hours=",nhours)
print("No of minitues=",nmin)
print("No of seconds=",nsec)