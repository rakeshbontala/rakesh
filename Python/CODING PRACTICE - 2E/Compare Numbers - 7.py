a=str(int(input()))

fsd=a[:2]=='19'
tfd=int(a[2:])

if fsd and (tfd>30 and tfd<60):
    print(True)
else:
    print(False)
