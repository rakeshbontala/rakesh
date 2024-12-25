d =int(input())

bonus = 30

first_20 = d*2 

second_40 = d*4 

third_60 = d*6 

if d<=20:
    print(first_20 + bonus)
elif 20<d<=60:
    print((2*20)+((d-20)*4)+bonus)
elif d>60:
    print( (2*20) + (4*40) + ((d-60)*6)+bonus  )
    
    
    
    
