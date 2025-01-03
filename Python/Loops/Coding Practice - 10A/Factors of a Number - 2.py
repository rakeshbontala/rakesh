a = int(input())

pat =""

for i in range (1,a+1):
    if (a%i)==0:
        pat=pat+str(i)+" "
print(pat)