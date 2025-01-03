n = int(input())

for i in range (0,n):
    if i==0:
        print("* "*n)
    elif i==n-1:
        print("* ")
    else:
        print("* "+"  "*(n-i-2)+"* ")