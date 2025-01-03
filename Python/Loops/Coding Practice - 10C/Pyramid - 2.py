m = int(input())

for i in range (m):
    spaces = '  '*(m-i-1)
    numbers= (str(i+1)+ ' ')*((2*i)+1)
    print(spaces+numbers+spaces)
    
    
    