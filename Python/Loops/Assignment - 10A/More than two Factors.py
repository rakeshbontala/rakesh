a = int(input())

c=0
for i in range (1,a+1):
    if (a%i)==0:
        c=c+1
if c>2:
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")