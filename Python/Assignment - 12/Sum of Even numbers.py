a = int(input())

sum= 0 

for i in range(2,a+1):
    if (i%2)==0:
        sum=sum+i 
print(f'{sum}')