a = int(input())
for i in range (0,a):
    rev=''
    for j in range(a-i,0,-1):
        rev=rev+str(j)
    print(rev)
    
# n = int(input())
# for row_num in range(n):
#     row_output = ""
#     seq_num = n-row_num
#     while seq_num > 0:
#         row_output = row_output + str(seq_num)
#         seq_num = seq_num - 1
#     print(row_output)