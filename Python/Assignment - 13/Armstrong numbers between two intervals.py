m = int(input())
n = int(input())

rev=''
for i in range(m,n+1):
    c=0
    i=str(i)
    l=len(i)
    for j in i:
        c=c+(int(j)**l)
    if c==int(i):
        
        rev=rev+str(i)+" "

if len(rev)>1:
    print(rev)
else:
    print("-1")