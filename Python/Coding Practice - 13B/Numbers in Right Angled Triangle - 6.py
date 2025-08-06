a = int(input())


for i in range(1,a+1):
    rev=''
    for j in range(1,i+1):
        rev=rev+str(j)+' '
    for k in range(1,i):
        rev=rev+str(k)+' '
    print(rev)