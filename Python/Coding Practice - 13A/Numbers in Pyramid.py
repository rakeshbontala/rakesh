s = int(input())

c = int(input())

for i in range (1,c+1):
    left_spaces = " "*(c-i)
    each_row = ''
    for j in range(s,s+i):
        each_row=each_row+str(j)+" "
    # print(each_row)
    print(left_spaces+each_row)