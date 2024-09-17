m=int(input()) #60

p=int(input()) #60

c=int(input()) #40


cond1 =(m>=60) and (p>=50) and (c>=45) and (m+p+c>=180)

cond2=(c+p>=110)  or (m+p>=120)

print(cond1 or cond2)