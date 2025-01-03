m = int(input())

n = int(input())
power=2
sum=0
for i in range (1,n+1):

    sum=sum+(m)**power
    power=power+2 
print(sum)
    
    