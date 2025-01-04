String = input()

length_of_String = len(String)

shuffled_string = ''

for i in String:
    index = int(input())
    shuffled_string=String[index]
    print(shuffled_string)