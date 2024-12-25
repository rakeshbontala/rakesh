rupees = int(input())

first_100s = rupees//100

rupees =rupees%100 

second_50s = rupees//50 

rupees=rupees%50 

third_10s = rupees//10 

rupees = rupees%10

ones = rupees//1 

print("100:"+str(first_100s))
print("50:"+str(second_50s))
print("10:"+str(third_10s))
print("1:"+str(ones))