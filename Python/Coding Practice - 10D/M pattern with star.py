n = int(input())

# for i in range(1,n+1):
#     stars = "* "*i
#     spaces = "  "*((2*n)-(2*i))  # 12-2 = 10 12-4 =8
#     print(stars+spaces+stars)
    
for i in range(1,n+1):
    stars = '* '*i
    spaces=4*(n-i)
    # print(spaces)
    print(stars+' '*spaces+stars)

    
    