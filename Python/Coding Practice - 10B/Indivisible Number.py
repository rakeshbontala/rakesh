a = int(input())
count = 0
for i in range(2,10):
    if (a%i) == 0:
        count =count+1 
if count>1:
    print("Divisible Number")
else:
    print("Indivisible Number")
