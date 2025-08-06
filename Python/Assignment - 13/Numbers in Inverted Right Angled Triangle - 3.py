s = int(input())

n = int(input())

k = 0


for i in range (1,n+1):
    k=k+i 
r=k+s-1
for j in range (n):
    rev=''
    for k in range (n-j):
        rev=rev+str(r)+' '
        r=r-1
    print(rev)