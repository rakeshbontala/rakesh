# mark=input()
# med=input()

# if (int(mark[0:-1])>=75) or (med=="Y"):
#     print("Allowed to write exam")

# else:
#     print("Cannot write exam")
    

# print(type(mark[0:-1]))
# print(type(int(mark[0:-1])))

PERCENTAGE =input() 
MEDICAL = input()
l =len(PERCENTAGE)

value = int(PERCENTAGE[:l-1])

if value>=75 or MEDICAL=='Y':
    print("Allowed to write exam")
else:
    print("Cannot write exam")












