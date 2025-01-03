

a = int(input())

first = int(input())

for i in range(a-1):
    n=int(input())
    if first<n:
        first=first
    else:
        first = n
print(first)