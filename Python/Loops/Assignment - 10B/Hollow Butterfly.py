n = int(input())

for i in range (1,n+1):
    if i==1 or i==2:
        print(  ("* "*i)+("  "*(2*n-2*i))+("* "*i) )

    else:
        print(("* ") + ("  "*(i-2)) + "* " + ("  "*(2*n-2*i))+"* "+("  "*(i-2))+"* ")

for i in range (n):
    if i==n-1:
        print("* "+"  "*(2*n-2)+"* ")
    else:   
        print( "* "+"  "*(n-i-2)+"* "+"  "*(2*i)+"* "+"  "*(n-i-2)+"* ")