unit = int(input())

bill = 0

if unit <= 50:
    bill = 2*unit
elif unit <= 150:
    bill = (2*50) + (3*(unit-50))
elif unit <= 250:
    bill = (2*50) + (3*100) + (5*(unit-150))
elif unit > 251:
    bill = (2*50) + (3*100) + (5*100) +(8*(unit-250))

subcharge = bill*(0.2)

print(bill+subcharge)