

start=int(input())

end=int(input())

for i in range(start,end+1):
    sum=0
    for j in range(2,i):
        if (i%j==0):
            sum=sum+1 
    if sum==0:
        print(i)