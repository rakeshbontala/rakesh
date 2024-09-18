a=int(input())
b=int(input())
c=int(input())

a_big = (a>b) and (a>c)
b_big = (b>a) and (b>c)
c_big = (c>b) and (c>a)

if a_big:
    print(a)
else:
    if b_big:
        print(b)
    else:
        print(c)