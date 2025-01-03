m=int(input())
n=int(input())

mul=1
for i in range(m,n+1):
    if i%2==1:
        mul=mul*i 
print(mul)