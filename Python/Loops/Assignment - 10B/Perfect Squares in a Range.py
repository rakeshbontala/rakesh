a = int(input())

b = int(input())
c=0
for i in range (1,b+1):
    d = i*i 
    if d>=a and d<=b:
        if ((d)**0.5)==i:
            # print(i)
            c=c+1
    
print(c)