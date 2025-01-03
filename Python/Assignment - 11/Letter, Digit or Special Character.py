a = input()

if a.isdigit():
    print("Digit")
elif a.isupper():
    print("Uppercase Letter")
elif a.islower():
    print("Lowercase Letter")
else:
    print("Special Character")