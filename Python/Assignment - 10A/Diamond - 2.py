n = int(input())

for i in range(1,(n+1)):
    spaces = (n-i)*" "
    nums = (str(i)+" ")*i 
    print(spaces+nums+spaces)
for j in range(1,n):
    spaces=" "*j 
    nums = (str(n-j)+" ")*(n-j)
    print(spaces+nums)