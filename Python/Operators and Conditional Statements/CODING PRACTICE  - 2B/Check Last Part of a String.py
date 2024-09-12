a=input()
b=input()
l1=len(a)
l2=len(b)
di=l1-l2
chec1k=a[di:]

if chec1k==b:
    print(True)
else:
    print(False)
    