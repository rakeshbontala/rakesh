

rows=int(input())

columns=int(input())

for i in range(0,rows):
    if (i%2)==0:
        print("+ "*columns)
    else:
        print("- "*columns)