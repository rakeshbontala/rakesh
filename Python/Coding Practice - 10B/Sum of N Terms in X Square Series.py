
m = int(input())

n = int(input())

sum =0 
for i in range (1,n+1):
    term = str(m)*i

    sum=sum+int(term)**2 

print(sum)