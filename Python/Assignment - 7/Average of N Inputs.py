# Read the number of inputs 

first_number = int(input())

count = 1 
sum = 0

while count <= first_number:
    sum=sum+int(input())
    count=count+1 
print(sum/first_number)