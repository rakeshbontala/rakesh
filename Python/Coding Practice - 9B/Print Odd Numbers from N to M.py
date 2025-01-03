m = int(input())

n = int(input())
pat = ''
for i in range (n,m-1,-1):
    if i%2==1:
        pat=pat+str(i)+" "
print(pat)
