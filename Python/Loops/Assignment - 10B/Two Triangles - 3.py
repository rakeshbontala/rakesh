n = int(input())

for i in range (1,n+1):
    if i==1 or i==2:
        print( ("* "*i)+ ("  "*(2*n-2*i))+("* "*(i)))
    elif i==n:
        print("* "*(2*n))
    else:
        print(  ("* ")+ ("  "*(i-2))+"* "+ ("  "*(2*n-2*i))     +"* "+  ("  "*(i-2))+"* ")
        