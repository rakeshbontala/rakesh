n=int(input())
for g in range(1,n+1):
    if g==1:
        print("1")
    elif g==n:
        space="  "*(n-2)
        print(str(g)+" "+space+str(g))
    else:
        space="  "*(g-2)
        print(str(g)+" "+space+str(g))
a=n-1
for g in range(2,n+1):
    if g==n:
        print("1")
    else:
        space="  "*(n-g-1)
        print(str(a)+" "+space+str(a))
        a=a-1
        