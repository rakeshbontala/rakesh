x = int(input())
N = int(input())

mul = 1 
count = 1 

while count <= N :
    x = x+1
    mul = mul*x 
    count=count+1 
print(mul)