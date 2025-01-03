# a  = input()

# l=len(a)

# first = a[0]

# last = a[l-1]

# if first==last:
#     print(True)
# else:
#     print(False)

a = input()

rev = ''

for j in a:
    rev=j+rev
print(rev==a)