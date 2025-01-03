# Read the input string 
a = input()
# Intialize the input string 

first = a[0]

l = len(a)

for i in range(1,l):
    i=a[i]
    if i == i.upper():
        first = first+"-"+i.lower()
    else:
        first=first+i 
        
print(first)