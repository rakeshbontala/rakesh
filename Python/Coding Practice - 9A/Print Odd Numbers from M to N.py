a = int(input())

b = int(input())

result = ''
for i in range(a,b+1):
    if i%2 ==1:
        result=result+str(i)+" "
print(result)