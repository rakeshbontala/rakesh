N = int(input())

is_divisible_by_10 = ((N%10)==0)

is_divisible_by_5 = ((N%5)==0)

if is_divisible_by_10:
    print("Divisible by 10")
else:
    if is_divisible_by_5:
        print("Divisible by 5")
    else:
        print("Not Divisible by 10 or 5")

