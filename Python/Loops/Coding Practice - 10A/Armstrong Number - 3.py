a = input()
l = len(a)

sum=0

for i in a:
    sum=sum+(int(i)**l )
if sum==int(a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")