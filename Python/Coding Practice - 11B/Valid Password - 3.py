# a  = input()
# digit=""
# upper=""
# lower=''
# for i in a:
#     if i.isupper():
#         upper=upper+str(i)+''

# for j in a:
#     if j.islower():
#         lower=lower+str(j)+""

# for k in a:
#     if k.isdigit():
#         digit=digit+str(k)+''


# if len(upper)>=1 and len(lower)>=1 and len(digit)>=1 :
#     print("Valid Password")
# else:
#     print('Invalid Password')


a = input() 

contains_digit = False

for i in a:
    if i.isdigit():
        contains_digit=True


# print(a)
# print(a.lower())
# print(a.upper())
all_letters_lower = (a.lower()==a)
all_letters_upper = (a.upper()==a)

# print(all_letters_lower)
# print(all_letters_upper)

check = not (all_letters_upper) and not (all_letters_lower)

if (check and contains_digit):
    print("Valid Password")
else:
    print("Invalid Password")






















