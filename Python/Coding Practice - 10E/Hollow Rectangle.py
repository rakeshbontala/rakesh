

m = int(input())
 
 
n = int(input())
 
 
for i in range (m):
    if i==0 or i==m-1:
        print("* "*n)
    else:
        print("* "+("  "*(n-2))+"* "  )
        