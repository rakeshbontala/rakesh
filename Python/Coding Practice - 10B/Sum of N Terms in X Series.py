x = int(input())

terms =int(input())
sum = 0

for i in range(1,terms+1):
    terms = str(x)*i 
    sum=sum+int(terms)
print(sum)
