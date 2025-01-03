


a = int(input())

b = int(input())

sum = 0
power=1

for i in range(1,b+1):
    power = power*1 
    
    sum=sum+(a)**power
    power=power+2 
print(sum)