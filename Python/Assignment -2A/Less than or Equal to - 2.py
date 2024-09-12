a = int(input()) #5
b = int(input()) #3

if a>b and b<a:
    print('A <= B is False')
    print('B <= A is True')
else:
    if a<b and b>a:
        print('A <= B is True')
        print('B <= A is False')
    else:
        if a==b and b==a:
             print('A <= B is True')
             print('B <= A is True')
            
        


