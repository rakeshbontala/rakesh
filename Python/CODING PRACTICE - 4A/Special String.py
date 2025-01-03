a = input()

first_3_chars = a[:3]

last_chars = int(a[3:])

if (first_3_chars=='NXT') and ( ((last_chars%2)==0) or ((last_chars%7)==0)):
    print("Special String")
else:
    print("Not a Special String")


