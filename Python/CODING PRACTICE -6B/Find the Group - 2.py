n = int(input())

check = (n%6) # (3%6)
# print(check)

if (check==1) or (check==7) or (check ==13) or (check==19) or (check==25):
    print("Group 1")
elif (check==2) or (check==8) or (check ==14) or (check==20) or (check==26):
    print("Group 2")
elif (check==3) or (check==9) or (check ==15) or (check==21) or (check==27):  # (3%6)
    print("Group 3")
elif (check==4) or (check==10) or (check ==16) or (check==22) or (check==28):
    print("Group 4")
elif (check==5) or (check==11) or (check ==17) or (check==23) or (check==29):
    print("Group 5")
elif (check==6) or (check==12) or (check ==18) or (check==24) or (check==30) or (check==0):
    print("Group 6")