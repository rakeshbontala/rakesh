m = int(input())
p = int(input())
c = int(input())

print  ( ( (m>=35) and (p>=35) and (c>=35) ) and ( (m+p>=30) or (p+c>=30) or (m+c>=30) ))