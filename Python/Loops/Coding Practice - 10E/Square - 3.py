a = int(input())


for i in range(0,a):
    if (i==0) or (i==a-1):
        print("* "*a)
        
    else :
        star = "* "
        term_number="0 "*(a-2)
        print(star+term_number+star)
        