
X = int(input())
N = int(input())

sum = 0

power = 0

for i in range (1,N+1):
    power=power+2 
    term = (X)**power
    if (i%2)==0:
        term = - ((X)**power)
        
    sum=sum+term
print(sum)