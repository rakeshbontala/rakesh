
n=(input())


f=int(n[0])
s=int(n[1])
n=int(n)
cond=(((f+s)==7) or ((f==7) or (s==7)) or ((n%7)==0))

if cond:
    print("Special Number")
else:
    print("Normal Number")