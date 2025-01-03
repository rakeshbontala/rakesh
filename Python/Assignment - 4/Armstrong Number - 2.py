a = input()
l=len(a)
summ = 0

for i in a:
    summ=summ+(int(i)**l)

if summ==int(a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")