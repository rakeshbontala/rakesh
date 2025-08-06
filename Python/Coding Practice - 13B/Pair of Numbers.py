n = int(input())  #7 
 
 
numbers_of_pairs = 0 
 
 
for i in range(1,n):  #1,6-> 1,2,3,4,5,6 
    # print(i)
    
    if n>n-i and n-i>i:
        # print('i:'+str(i))
        # print('n-i:'+str(n-i))
        numbers_of_pairs=numbers_of_pairs+1 
print(numbers_of_pairs)
         