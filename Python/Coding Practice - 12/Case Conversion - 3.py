a = input()

length = len(a)

first = a[0].lower()

for i in range(1,length):
    upper=a[i].upper()
    if a[i]==upper:
        first=first+"-"+a[i].lower()
    else:
        first=first+a[i]

print(first)

