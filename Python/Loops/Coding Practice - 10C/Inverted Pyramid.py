a = int(input())

for i in range(a):
    spaces = ' '*i 
    stars = "*"*(2*(a-i)-1)
    print(spaces+stars+spaces)