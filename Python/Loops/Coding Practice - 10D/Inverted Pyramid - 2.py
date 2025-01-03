a = int(input())


for i in range(a):
    spaces = ' '*i 
    stars = "* "*(a-i)
    print(spaces+stars+spaces)