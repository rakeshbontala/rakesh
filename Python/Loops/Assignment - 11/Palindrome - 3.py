a = input()
a=a.lower()
rev=''
for i in a:
    if i.islower():
        rev = i +rev

if a==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")