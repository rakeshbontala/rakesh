start = int(input())

end = int(input())
c=0
for i in range(start,end+1):
    for j in range (2,i):
        if (i%j)==0:
            print(i)
            break