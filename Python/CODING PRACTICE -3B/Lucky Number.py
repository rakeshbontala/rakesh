a=int(input())
b=int(input())

if (a==6 or b==6) or (a+b==6) or (a-b==6) or (b-a==6):
    print('Lucky')
else:
    print("Not Lucky")