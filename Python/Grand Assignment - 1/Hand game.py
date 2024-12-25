abhinav =input()
anjali = input()

if abhinav == 'Paper' and anjali == 'Rock':
    print("Abhinav Wins")
elif abhinav == 'Rock' and anjali == 'Paper':
    print("Anjali Wins")
elif abhinav == 'Scissors' and anjali == 'Paper':
    print("Abhinav Wins")

elif abhinav == 'Paper' and anjali == 'Scissors':
    print("Anjali Wins")

elif abhinav == 'Rock' and anjali == 'Scissors':
    print("Abhinav Wins")

elif abhinav == 'Scissors' and anjali == 'Rock':
    print("Anjali Wins")
elif abhinav==anjali:
    print("Tie")
