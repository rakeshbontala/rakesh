a=(input())
N=int(input())
l=int(len(a))
first_charcter = a[:N]
last_charcter = a[l-N:]
print(first_charcter!=last_charcter)