

n = int(input())

for i in range (1,n+1):
    starts= '* '*i 
    spaces = 2*(n-i)*"  "
    print(starts+spaces+starts)

for i in range (1,n):
    starts= '* '*(n-i) 
    spaces = (2*i) *"  "
    print(starts+spaces+starts)