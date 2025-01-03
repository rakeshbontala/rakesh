a=int(input())
b=int(input())

summ = ((a+b)<10)
diff = ((a-b)<10)
bett = ((a>=5 and a<30))

print(summ or diff or bett)