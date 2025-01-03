# print(input().swapcase())

a = input()
pat =''
for i in a:
    if i.isupper():
        pat=pat+i.lower()
    else:
        pat=pat+i.upper()
print(pat)