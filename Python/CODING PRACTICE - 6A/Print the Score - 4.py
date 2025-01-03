d = int(input())

bonus = 50

if 0<d<=40:
    print(d*2 +(bonus))
    
elif 41<=d<=60:
    print( (40*2) + ((d-40)*4) +bonus )
    
elif 61<=d<=120:
    print( (40*2) + (20*4)+ ((d-60)*6) + bonus)
    
    
elif d>121:
    print((40*2) + (20*4)+ ((60)*6) + ((d-120)*8)+bonus)
    
    

    