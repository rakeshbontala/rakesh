


m = int(input())

for i in range(m):
    if i==0 or i==1:
        print("* "*(i+1))
    elif i==m-1:
        print("* "*m)
    else:
        spaces ="  "*(i-1)
        print("* "+spaces+"* ")