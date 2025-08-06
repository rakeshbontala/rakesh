m_rows = int(input())
n_columns = int(input())


for i in range (1,m_rows+1):
    start='7 '
    next_number = 8 
    if i==1 or i==m_rows:
        for j in range(2,n_columns+1):
            start=start+str(next_number)+" "
            next_number=next_number+1 
        print(start)
    else:
        hollow_spaces="  "*(n_columns-2)
        print(start+hollow_spaces +str(7+n_columns-1)+" ")
    
        
