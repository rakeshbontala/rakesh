a=str(int(input()))

f=int(a[0])
s=int(a[1])
t=int(a[2])

if (t>7 and s>7 and f>7) or ( (s*f<=30) and (s*t<=30) and (t*f<=30)):
    print(True)
else:
    print(False)