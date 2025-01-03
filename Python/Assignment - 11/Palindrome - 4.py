a = input()
a=a.replace(' ','')
a=a.replace("'",'')
b =a.lower()
c = a.upper()
reverse = a[::-1]

print(c==reverse.upper())