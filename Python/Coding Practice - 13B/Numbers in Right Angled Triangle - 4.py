start = int(input())
rows = int(input())

for i in range(1,rows+1):
    rev=''
    for j in range(2*i):
        rev=rev+str(start)+" "
        start=start+1 
    print(rev)