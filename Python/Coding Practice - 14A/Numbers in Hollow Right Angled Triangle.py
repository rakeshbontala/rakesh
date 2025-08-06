#read the input value 

n = int (input())

for i in range (1,n+1):
    if (i>2) and (i<n):
        hollow_spaces = " "*(2*i-4)
        print("1 "+hollow_spaces+str(i))
    else:
        numbers=''
        for j in range(i):
            numbers=numbers+str(j+1)+" "
        print(numbers)
            
            