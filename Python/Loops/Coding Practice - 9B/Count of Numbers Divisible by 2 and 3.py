n = int(input())

count = 0 


for i in range (1,n+1):
    if (i%2)==0 and (i%3)==0:
        count=count+1 
print(count)
