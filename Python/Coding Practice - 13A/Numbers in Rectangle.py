M = int(input())
N = int(input())

for i in range (M):
    rev = ''
    a=7
    for j in range(N):
        rev=rev+str(a+j)+" "
    print(rev)

    