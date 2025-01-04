m = int(input())
n = int(input())
prime=''
for i in range (m,n+1):
    if i>1:
        fact=0
    else:
        fact=1
    
    for j in range(2,i):
        if (i%j)==0:
            fact=fact+1 
    if fact==0:
        prime=prime+str(i)+' '
if len(prime)==0:
    prime=("No Prime Numbers Found")
else:
    prime=prime
print(prime)
    