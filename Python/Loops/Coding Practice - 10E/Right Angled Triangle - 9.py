n = int(input())

for i in range(n):
    dots = '. '
    zeros = '0 '
    
    if i==0 or i==1:
        print(dots*(i+1))
    elif i==n-1:
        print(dots*n)
    else:
        print(dots+"0 "*(i-1)+dots)
        
    