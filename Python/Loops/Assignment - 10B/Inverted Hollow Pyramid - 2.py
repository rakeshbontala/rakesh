
n = int(input())

for i in range (n):
    if i==0 :
        space = "  "*(n-1)
        print(space+ ("1"+" "))
    else:
        hollow_spaces = " "*(2*i-1)
        print("  "*(n-i-1)+str(i+1)+hollow_spaces+str(i+1))

a=n-1 #2 

for i in range (1,n):
    if i==n-1:
        space = "  "*(n-1)
        print(space+ ("1"+" "))
    else:
        hollow_spaces = " "*(2*(n-i)-3)
        print("  "*(i)+str(a)+hollow_spaces+str(a))
        a=a-1
        
        
        