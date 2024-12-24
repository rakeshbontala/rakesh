a = (input())

f = int(a[0])
s = int(a[1])

check_both_divisible_or_not = ( (int(a)%f) == 0) and ( (int(a)%s) == 0)

if check_both_divisible_or_not ==True:
    print(int(a)*2)
else:
    print(int(a))