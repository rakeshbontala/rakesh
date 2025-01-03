

d = int(input())
bonus = 100
if 0<=d<=50:
    print( (d*3) +bonus) 
elif 51<=d<=100:
    print( (50*3) + ( (d-50)*5) +bonus ) 

elif 101<=d<=200:
    print(  (50*3) + (50*5) + ( (d-100)*6) +bonus) 
else:
    print((50*3) + (50*5) + ( (100)*6) + ((d-200)*10)+ bonus) 
    