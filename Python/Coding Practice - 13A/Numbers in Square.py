a = int(input())

for i in range(1,a+1):
    rev = ''
    for j in range(1,a+1):
        rev=rev+str(j)+" "
    print(rev)