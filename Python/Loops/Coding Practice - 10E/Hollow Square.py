


m = int(input())


for i in range (m):
    if i==0 or i==m-1:
        print("* "*m) 
    else:
        print("* "+"  "*(m-2)+"* ")