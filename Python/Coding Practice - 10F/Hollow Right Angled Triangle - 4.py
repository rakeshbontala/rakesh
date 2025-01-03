a = int(input())


for i in range (1,a+1):
    if i==1:
        print("# "*a)
    elif i==a:
        print("+ ")
    else:
        plus = "+ "
        hollow_spaces = " "*((2*(a-i))-2)
        
        print(plus+hollow_spaces+plus)
        