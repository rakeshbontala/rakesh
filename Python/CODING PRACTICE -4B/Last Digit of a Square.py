a = input()

l=len(a)

last_digit = int((a[l-1]))
square_of_n = str((int(a)*int(a)))
square_of_n_length = len((square_of_n))
last_square_n_a = square_of_n[square_of_n_length-1]



if str(last_digit) == str(last_square_n_a):
    print('Equal')
else:
    print("Not Equal")
