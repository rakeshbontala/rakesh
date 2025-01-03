n = int(input())

for i in range(1,n+1):  # 1 2 3
    if i == 1:
        print((str(n)+" ")*n)
    else:
        spaces = "  "*(i-1)
        numbers = (str(n+1-i)+" ")*((n+1-i))
        print(spaces+numbers)