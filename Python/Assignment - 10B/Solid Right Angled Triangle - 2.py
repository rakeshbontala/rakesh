# n=int(input())
# for i in range (n):
#     print('  '*(n-i-1),end='')
#     print('* '*(i+1),end='')
#     print()
    

n=int(input())

for i in range(1,n+1):
    if i==1: #logic 1
        print("  "*(n-1)+"*")
    elif i==n:
        print("* "*n)
    else:
        left_space="  "*(n-i)
        hollow_space="* "*(i-1)
        print(left_space+hollow_space+"*")