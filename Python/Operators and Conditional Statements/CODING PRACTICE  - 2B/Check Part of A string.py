

A = input() #Repeat

B = input() #pea 

index = int(input())  #2
l=len(B)
check=A[index:]
#print(check)

check1=check[:l]
#print(check1)

if check1==B:
    print(True)
else:
    print(False)