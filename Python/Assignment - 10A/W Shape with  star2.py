n = int(input())

print("* "*(2*n-1))

for i in range (1,n):
    spaces = ' '*(i)
    stars = '* '*(n-i)
    hollow_spaces = " "*((2*i)-1-1)
    print(spaces+stars+hollow_spaces+stars+spaces)

