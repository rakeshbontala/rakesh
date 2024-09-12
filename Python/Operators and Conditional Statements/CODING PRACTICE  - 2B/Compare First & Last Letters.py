a = input()
first_letter = a[0]
l=len(a)

last_letter=a[l-1:]
print(first_letter)
print(last_letter)

if first_letter==last_letter:
    print(False)
else:
    print(True)