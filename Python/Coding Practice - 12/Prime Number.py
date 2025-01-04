a = int(input())

factors = 0

for i in range(2,a):
    if (a%i)==0:
        factors+=1 
if factors==0:
    print("Prime Number")
else:
    print("Not a Prime Number")