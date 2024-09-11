w = input()

first_2 = w[:2]

l = len(w)

last_2 = w[l-2:]

print(first_2+('*'*(l-4))+last_2)