a=int(input())
thousand=(a//1000)
a=(a%1000)
five=(a//500)
a=(a%500)
hund=(a//100)
a=(a%100)
fif=(a//50)
a=(a%50)
twe=(a//20)
a=(a%20)
fiv=(a//5)
a=(a%5)
one=(a//1)
a=(a%1)
print("1000:"+str(thousand))
print("500:"+str(five))
print("100:"+str(hund))
print("50:"+str(fif))
print("20:"+str(twe))
print("5:"+str(fiv))
print("1:"+str(one))


