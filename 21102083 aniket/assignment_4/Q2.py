year=int(input("enter year"))
y=year
if y%4==0:
    if(y%100!=0):
        print("leap year")
        
    else:
        if(y%400==0):
            print("leap year")
else:
    print("year")