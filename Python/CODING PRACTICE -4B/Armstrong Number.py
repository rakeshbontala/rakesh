
a = input()
l=len(a)
number = 0
for i in a:
    number=number+(int(i)**l)

if str(number)==a:
    print(True)
else:
    print(False)

    