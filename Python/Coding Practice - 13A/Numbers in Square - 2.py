n = int(input())  #3 

for i in range (n): #0 1 2
    rev = '' 
    for j in range (n):
        rev=rev+(str(n-j))+' '
    print(rev)
    