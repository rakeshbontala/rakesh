# 1 to 200

n = int(input())

for each_char in range (1,n+1):
    sum = 0
    each_char = str(each_char)
    length = len(each_char)
    for i in each_char:
        sum = sum + int(i)**length
   
    if sum == int(each_char):    
        print(each_char)
    