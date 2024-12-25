a = int(input())
b = int(input())

remainder_a_b = a%b 
remainder_b_a = b%a 

if remainder_a_b>remainder_b_a:
    print(remainder_b_a)
    
    
else:
    print(remainder_a_b)