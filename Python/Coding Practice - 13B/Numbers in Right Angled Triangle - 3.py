start = int(input())

columns = int(input())

for i in range(1,columns+1):
    rev=''
    for j in range (i):
        rev=rev+str(start)+" "
        start=start+1 
    print(rev)
    
    
