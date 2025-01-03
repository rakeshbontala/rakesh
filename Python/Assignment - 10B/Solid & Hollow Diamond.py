n=int(input())

for i in range(1,n):
    left_spaces=" "*(n-i)
    pattern=""
    for j in range(1,i+1):
        pattern=pattern+str("*")+" "
    print(left_spaces+pattern)
for j in range(1,n+1):
    i=n-(j-1)
    left_spaces=" "*(n-i)
    if i>2 and i<n:
        hollow_spaces="  "*(i-2)
        stars="* "+hollow_spaces+"*"
        print(left_spaces+stars)
    else:
        stars="* "*i 
        print(left_spaces+stars)
    
    