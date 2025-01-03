a = int(input())

for i in range (a):
    if i==0:
        spaces=' '*(a-i-1)
        stars = "* "
        print(spaces+stars+spaces)
    elif i==a-1:
        print("* "*a)
    else:
        spaces=" "*((2*i)-1-1)
        star="* "
        print(" "*(a-i-1)+star+spaces+star+" "*(a-i-1))
        