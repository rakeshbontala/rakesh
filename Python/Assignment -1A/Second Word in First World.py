#Midterm
#mid
#op:2

a = input()
b = input()

l1 = len(a)
l2 = len(b)
c=0
for i in range(l1-1):
    for j in range(l2-1):
        if a[:i]==b[:j]:
            c=c+1
print(c)