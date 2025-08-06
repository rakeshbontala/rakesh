n = int(input())

for i in range(1,n+1):
    rev=''
    for j in range(1,n+1):
        if i==1 or i==n:
            rev=rev+str(j)+" "
        else:
            if j==1 or j==n:
                rev=rev+str(j)+" "
            else:
                rev=rev+'  '
    print(rev)
    