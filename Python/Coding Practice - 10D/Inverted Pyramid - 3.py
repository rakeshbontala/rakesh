n = int(input())

for i in range(n):
    if i==0:
        print(("+ ")*n)
    else:
        spaces = " "*i
        starts = "* "*(n-i)
        print(spaces+starts+spaces)