# game game game
import random 
random_number = (random.randint(1, 10))
# user_guess = int(input('Enter your guess here:'))
# print(f"random number is {random_number}")
initial_guess = 0
while initial_guess < 3:
    user_guess = int(input('Enter your guess here:'))
    initial_guess += 1
    if user_guess == random_number:
        print(f'The value is matched in {initial_guess}  attempts')
        break
    elif user_guess < random_number:
        print("your choice is smaller  ")
    elif user_guess > random_number:
        print("your choice is greater  ")
    else:
        print("Enter Again")
else:
    print(f"Better try next time and the number is {random_number}")
 
