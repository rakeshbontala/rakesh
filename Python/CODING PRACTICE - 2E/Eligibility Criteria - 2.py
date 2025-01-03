m=int(input())
p=int(input())
c=int(input())

if ( ((m+p >=100) or (c+p >=100) or (m+c >=100) ) and (m+p+c >=180)):
    print(True)
else:
    print(False)
    