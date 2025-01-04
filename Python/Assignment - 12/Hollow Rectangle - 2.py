a = int(input())


b = int(input())

for i in range (a+2):
    if i==0 or i==a+1:
        print("+"+("-"*b)+"+")
    else:
        print("|"+(" "*b)+"|")