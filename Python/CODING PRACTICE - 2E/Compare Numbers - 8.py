a=str(int(input()))
fd=int(a[0])
sd=int(a[1])
td=int(a[2])

if ( ((fd==1) or (sd==1) or (td==1))  and (fd+sd+td<12) and (td==5)):
    print(True)
else:
    print(False)