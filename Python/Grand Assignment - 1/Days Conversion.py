a=int(input())
years=a//(365)


a=(a%(365))

weeks=(a//7)

a=(a%7)

days=(a//1)

a=(a%1)

print(str(years)+" years "+str(weeks)+" weeks "+str(days)+" days")