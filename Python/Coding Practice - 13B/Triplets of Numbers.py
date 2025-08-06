n = int(input())

sum = 0

for i in range(1,n): #1,9
    for j in range (i+1,n): #2,9
        if n>(n-i-j) and (n-i-j)>j>i:
            sum=sum+1 
print(sum)