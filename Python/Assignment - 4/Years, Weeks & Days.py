days = int(input())

years = days//365
days = days%365 

weeks = days//7 
days = days%7 

days = days//1 


print(years)
print(weeks)
print(days)