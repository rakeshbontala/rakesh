a = int(input())

rows = int(input())
start=0
for i in range(1,rows+1):
    start=start+int(i)
b=start+a-1
# print(b)
for i in range(1,rows+1):
    rev=''
    for j in range(i):
        rev=rev+str(b)+" "
        b=b-1 
    print(rev)