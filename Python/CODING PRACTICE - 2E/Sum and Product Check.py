a=(int(input()))
b=(int(input()))

summ=(a+b)
summ_l=len(str(summ))
prod=(a*b)
prod_l=len(str(prod))
# print(summ_l)
# print(prod_l)
if (summ_l>3 or prod_l>3) or summ>=100 or prod>=100:
    print(False)
else:
    print(True)

