a = int(input())

if a>=4 and a<12:
    print("Good Morning")
else:
    if a>=12 and a<16:
        print("Good Afternoon")
    else:
        if a>=16 and a<20:
            print("Good Evening")
        else:
            if a>=20 or a<4:
                print("Good Night")