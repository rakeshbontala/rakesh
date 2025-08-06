a  = int(input())

sum = 0

for i in range(1,a+1):
    sum=sum+int(i)

for j in range(a):
    left_spaces = ' '*(2*j)
    rev=''
    for k in range (a-j):
        rev=rev+str(sum)+' '
        sum=sum-1 
    print(left_spaces+rev)
