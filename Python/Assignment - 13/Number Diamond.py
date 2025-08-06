a = int(input())


rev=''
for i in range(1,a):
    left_space=' '*(a-i)
    rev=rev+str(i)+" "
    print(left_space+rev)

for i in range (a):
    rev=''
    left_space=' '*i
    for j in range(a-i):
        rev=rev+str(j+1)+" "
    print(left_space+rev)
        
