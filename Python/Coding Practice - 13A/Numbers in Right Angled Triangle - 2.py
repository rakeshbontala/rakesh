n = int(input())

for i in range (1,n+1):
    row=''
    left_spaces = (n-i)*"  "
    for j in range(i):
        row=str(j+1)+" "+row
    # print(row)
    print(left_spaces+row)