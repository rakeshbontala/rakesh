rows = int(input())

columns = int(input())


start = rows*columns 


for i in range (rows):
    rev=''
    for j in range (columns):
        rev=rev+str(start)+" "
        start=start-1 
    print(rev)