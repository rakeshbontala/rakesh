a = int(input())
b = int(input())

a_square  = a**2 
b_square  = b**2 

sum_both = a_square+b_square 

if sum_both>= 60:
    print("Greater than or Equal to 60")
else:
    if sum_both<60:
        print("Less than 60")