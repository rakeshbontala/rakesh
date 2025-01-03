n = int(input())  #over all numbers


count = 0 #count satisfy
for i in range (1,n+1):
    if (i%6)==0 and (i%8)==0:
        count=count+1 
print(count)