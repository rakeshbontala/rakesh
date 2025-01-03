m = int(input())
n = int(input())
pat =''

for i in range (m,n+1):
    if i%9 ==0:
        pat=pat+str(i)+' '
if len(pat)>1:
    print(pat)
else:
    print("No Numbers found")