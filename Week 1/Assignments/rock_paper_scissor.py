# if both players choose the same option then the game is tie
# otherwise the rules will be applied

# rock > scissor
# scissor > paper
# paper > rock




# assignment
import random
player = input("Enter the name: ")
player_score = 0
attempts = 1
mylist = ['Rock', 'Paper','Scissors']
# computer = random.choice(mylist)
# print(computer)
while attempts < 4:

    computer = random.choice(mylist)
    print(computer)

    hand = input("Enter Your Choice: ")
    attempts += 1
    if hand == computer:
        print("it's a tie")
        # break
    elif(computer == 'Rock' and hand == 'Paper'):
        
        player_score +=1
        print(f"{player} won the match { player_score}")

    elif(computer == 'Rock' and hand == 'Scissors'):
        print("Computer won the match")

    elif (computer == 'Scissors' and hand == 'Rock'):
        player_score +=1
        print(f"{player} won the match { player_score}")


    elif (computer == 'Scissors' and hand == 'Paper'):
        print('computer won the match')
        
    elif (computer == 'Paper' and hand == 'Scissors'):
        player_score +=1
        print(f"{player} won the match { player_score}")


    elif (computer == 'Paper' and hand == 'Rock'):
        print("computer won the match")
else:
    print("Limit Reached")
print(f'{player} won the match of total { player_score}')