a = input()  #Subway
b = input()  #Sub

l=len(b)
c=0

for i in range(l):
    if a[i]==b[i]:
        c=c+1

print(c*"*"+a[c:])
#