salary = int(input())
years_service = int(input())
bonus=0
if years_service>5:
    bonus=5*(salary)*(1/100)
    print(bonus)
else:
    print("No Bonus")
