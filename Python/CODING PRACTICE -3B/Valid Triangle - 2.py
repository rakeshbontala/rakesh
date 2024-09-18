a = int(input())
b = int(input())
c = int(input())

if a+b+c==180:
    for i in range(1,4):
        print("*"*i)
else:
    print("Not a Valid Triangle")