n = int(input())
for i in range(n,0,-1):
    spaces='  '*(n-i)
    stars = '* '*i
    print(spaces+stars)