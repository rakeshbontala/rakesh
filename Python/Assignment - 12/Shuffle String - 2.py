s1 = input()
s2 = input()

first = s1[0]

ls1 = len(s1)
ls2 = len(s2)

for i in range(1,ls1):
    if (i%2)==1:
        first= first+s2[i]
    else:
        first=first+s1[i]
print(first)
        