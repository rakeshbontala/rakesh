a = int(input())

sum=0

for i in range(1,a+1):
    if (a%i)==0:
        sum=sum+i 
print(sum)