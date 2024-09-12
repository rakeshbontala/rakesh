a=int(input())
b=int(input())

is_positive=(a>0 and b>0)

is_less_than_70 =(a<70) and (b<70)

if is_less_than_70 or is_positive :
    print(True)
else:
    print(False)

# both a and b are positive or both values are greater than 70 then true otherwise false
