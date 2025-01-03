a = input()


number = ""

for i in a:
    if i.isdigit():
        number=number+str(i)+""


if number.isdigit():
    print("Valid Password")
else:
    print("Invalid Password")