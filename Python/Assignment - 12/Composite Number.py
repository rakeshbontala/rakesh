a = int(input())

fact = 0 

for i in range(1,a+1):
    if (a%i)==0:
        fact=fact+1 
# print(fact)

# if fact>2:
#     print(True)
# else:
#     print(False)

print(fact>2)