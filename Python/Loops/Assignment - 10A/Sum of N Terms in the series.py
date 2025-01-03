m = int(input())

n = int(input())

power = 1 
sum=0

for i in range(1,n+1):
    term = (m)**power
    check = ((i%2) == 0)
    if check:
        term=-((m)**power)
    sum=sum+term
    power=power+2
print(sum)
    
    
    