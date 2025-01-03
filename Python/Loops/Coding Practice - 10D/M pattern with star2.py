n = int(input())
for i in range(1,n+1):
    spaces = ' '*(n-i)
    starts = '* '*i 
    print(2*(spaces+starts+spaces))