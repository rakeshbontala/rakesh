n=int(input()) #10

k=int(input()) #5
 
sum = 0
 
for i in range(1,k+1):
    sum=sum+i 
sum=sum+n-1 
for j in range(1,k+1):
    rev = ''
    for k in range(j):
        rev=rev+str(sum)+" "
        sum=sum-1
    print(rev)