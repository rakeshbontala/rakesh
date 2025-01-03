n = int(input())

for i in range (n):
    spaces = '  '*(n-i-1)
    plues = "+ "*i
    print(spaces+plues+"# ")
for j in range (1,n):
    spaces = '  '*j
    plues = '+ '*(n-j-1)
    print(spaces+plues+"# ")