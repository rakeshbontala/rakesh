a = int(input())

for i in range (1,a+1):
    spaces = ' '*(a-i)
    numbers= ((str(i))+" ")*i 
    print(spaces+numbers+spaces)