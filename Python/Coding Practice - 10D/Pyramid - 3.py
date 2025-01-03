a = int(input())

for i in range (1,a+1):
    stars = '* '*(i)
    print(stars)
for j in range(a-1,0,-1):
    print("* "*j)