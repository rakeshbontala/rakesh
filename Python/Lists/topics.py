list_a = [1,2,3]
list_b = [1,2,3]

print(id(list_a))  #objects are different
print(id(list_b))


list_a = [1,2,3]
list_b = list_a

print(id(list_a))   #same object used to another variable 
print(id(list_b))


list_a = [1,2,3,5]
list_b = list_a 
list_a[3]=4 

print(list_a)
print(list_b)
print(id(list_a))  #same id
print(id(list_b))


list_a = [1,2]
list_b = list_a
list_a = [6,7]

print(list_a)
print(list_b)
print(id(list_a))
print(id(list_b))  #different id's


list_a = [1,2]
list_b = list_a
list_a = list_a+[6,7]

print(list_a)
print(list_b)

print(id(list_a))  #different id's
print(id(list_b))



list_a = [1,2]
list_b = list_a

list_a += [6,7]

print(list_a)
print(list_b)

print(id(list_a))  #same id's  (compound operator)
print(id(list_b))


list_a = [1,2]
list_b = [3,list_a]
list_a[1] = 4

print(list_a)
print(list_b)


a=2
list_a = [1,a]
print(list_a)
a=3
print(list_a)







