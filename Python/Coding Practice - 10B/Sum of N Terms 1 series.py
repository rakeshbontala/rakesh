

a = int(input())

term_number = '1'

sum_of_terms = 0 

for i in range (1,a+1):
    terms = term_number*i 
    sum_of_terms=sum_of_terms+int(terms)
print(sum_of_terms)