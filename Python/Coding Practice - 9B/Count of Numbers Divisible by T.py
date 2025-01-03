N = int(input())

T = int(input())

count = 0

for i in range(1,N+1):
    if i%T == 0:
        count+=1 
print(count)
        