#program to print fibinoci series
first_num,second_num=0,1
number=int(input("enter the end value : "))
for i in range(0,number):
    print(first_num)
    third_num=first_num+second_num
    first_num=second_num
    second_num=third_num

