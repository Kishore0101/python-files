#store in months using list
def display(months):
    for i in months:
        print("***********************")
        print(i)


if __name__=="__main__":
    months=["jan","feb","mar","apr","may","jun","july","aug","sep","oct","nov","dec"]
    result=display(months)
    print(result)