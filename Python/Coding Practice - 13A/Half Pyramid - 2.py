a = int(input())
start=1
for i in range (a):
    rev=''
 
    for j in range(0,i+1):
        rev=rev+str(int(start))+" "
        start=start+1 
    print(rev)
        