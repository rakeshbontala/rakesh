n = int(input())
first_number = int(input())

for i in range (n-1):
    numbers = int(input())
    if first_number> numbers:
        first_number = first_number
    else:
        first_number=numbers
    # print('first_number:- '+str(first_number))
print(first_number)
        
    