m=int(input())
p=int(input())
c=int(input())

if (( (m>=70) and (p>=60) and (c>=60) ) or (m+p+c>=180)):
    print(True)
else:
    print(False)
    