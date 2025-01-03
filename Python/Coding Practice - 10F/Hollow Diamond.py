n  = int(input())

for i in range (n):
    if i==0:
        spaces = " "*(n-1)
        print(spaces+"* "+spaces)
    else:
        spaces=" "*(n-i-1)
        hollow="  "*(i-1)
        print(spaces+"* "+hollow+"* "+spaces)
        
for i in range (1,n-1):
        spaces=" "*i
        hollow="  "*(n-i-2)
        print(spaces+"* "+hollow+"* "+spaces)
        
for i in range (1):
        spaces=" "*(n-1)
        print(spaces+"* "+spaces)