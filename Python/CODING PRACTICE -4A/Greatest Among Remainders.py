# Read 

n = int(input())
 
divisible_4 = (n%4)
divisible_5 = (n%5) 

if divisible_5 > divisible_4:
    print(divisible_5)
else:
    print(divisible_4)
