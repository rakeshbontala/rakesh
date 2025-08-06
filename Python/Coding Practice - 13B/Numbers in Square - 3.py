a = int(input())

start = 1 

for i in range (a):
    rev=''
    for j in range(a):
        rev=rev+str(start)+" "
        start=start+1 
    print(rev)

