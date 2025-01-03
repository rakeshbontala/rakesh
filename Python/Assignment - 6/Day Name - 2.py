day=input()
date=int(input())

if day=="Sunday":
    day=0
elif day=="Monday":
    day=1
elif day=="Tuesday":
    day=2
elif day=="Wednesday":
    day=3
elif day=="Thursday":
    day=4
elif day=="Friday":
    day=5
elif day=="Saturday":
    day=6

total_days=day + (date) -1



day=(total_days%7)
print(day)

if day==0:
    print("Sunday")
elif day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
    


