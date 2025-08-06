n = int(input())


for i in range (n):
    left_space=" "*(i)
    rev=''
    for j in range (n-i):
        rev=rev+str(j+1)+" "
    print(left_space+rev)