n=int(input())


for i in range(n):
    if i==0:
        print("* "*n)
    elif i==n-1:
        spaces = ' '*(n-1)
        stars='* '
        print(spaces+stars+spaces)
    else:
        spaces=" "*i 
        star="* "
        hollow= "  "*(n-i-2)
        print(spaces+star+hollow+star+spaces)