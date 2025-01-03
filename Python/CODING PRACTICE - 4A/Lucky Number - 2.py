a = (input())
f = int(a[0])
s = int(a[1])
a = int(a)
is_divisible_by_9   = (a%9==0)


if is_divisible_by_9 or (f==9 or s==9):
    print("Lucky Number")
else:
    print("Unlucky Number")