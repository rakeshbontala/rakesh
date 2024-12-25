s=input()
l=len(s)
last=s[l-1]
number=int(s[:l-1])

# print(last)
# print(number)
if last=='T':
    print(number*10)
elif last=='H':
    print(number*100)
elif last=='K':
    print(number*1000)