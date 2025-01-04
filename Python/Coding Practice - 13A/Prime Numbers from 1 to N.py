n = int(input())

for i in range(2,n+1):
    fact = 0 
    
    for j in range(2,i):
        if (i%j)==0:
            fact=fact+1 
    if fact==0:
        print(i)