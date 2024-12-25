N = int(input())

N_div_5 = (N%5)==0
N_div_7 = (N%7)==0
N_is_lessthan_7 = (N<7)

if (N_div_5 and N_div_7) or N_is_lessthan_7:
    print(N)
else:
    print(N%5)
    print(N%7)