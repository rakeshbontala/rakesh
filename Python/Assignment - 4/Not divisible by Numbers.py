n=int(input())

div_2=((  (n)  %  2  )  !=0  )

div_3=((  (n)  %  3  )  !=0  )

div_5=((  (n)  %  5  )  !=0  )

div_7=((  (n)  %  7  )  !=0  )

if div_2 and div_3 and div_5 and div_7:
    print("True")
else:
    print("False")


