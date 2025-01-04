rows = int(input())
 
columns = int(input())
 
start =1
for i in range(rows):
    row=''
    for j in range(1,columns+1):
        row=row+str(int(start))+" "
        start=start+1
    print(row)
         