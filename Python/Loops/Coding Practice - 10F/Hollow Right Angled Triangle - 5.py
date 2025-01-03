n = int(input())

for i in range (0,n):
    if i==0:
        print("  "*(n-1)+"* ")
    elif i==n-1:
        print("* "*n)
    else:
        print("  "*(n-i-1)+"* "+" "*(2*i-2)+"* ")