a = int(input())


sum=0

for i in range(1,a):
    if (a%i)==0:
        sum=sum+i 

# print(a)
# print(sum)
if a==sum:
    print("Perfect Number")
else:
    print("Not a Perfect Number")