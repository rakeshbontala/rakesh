

n = int(input())
 
for i in range(n):
    spaces = '  '*(n-i-1)
    stars = '* '* ((2*i)+1)
    print(spaces+stars+spaces)
     
     