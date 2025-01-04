a = int(input())

# rev=''
# for i in range(1,a+1):
#     rev=rev+str(i)+" "

# for i in range (a):
#     print(rev[:len(rev)-2*i-1])

for i in range(a):
    row=''
    number = a-i 
    for j in range(1,number+1):
        row=row+str(j)+" "
    print(row)