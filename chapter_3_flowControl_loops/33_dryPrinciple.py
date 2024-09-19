# Dont't REPEAT YOURSELF = DRY

import random

winning_num = random.randint(1, 100)  # Generate a random winning number
count = 0
over = False
user_number = int(input("Enter your lucky number between 1-100: "))  # Get user's guess

while not over:
    
    if user_number == winning_num:
        print("You win!")
        over = True  # End the game if the guess is correct
    else:
        if user_number > winning_num:
            print("Too high")
        else :
            print("Too low")
        user_number = int(input("Guess again : "))
        count += 1

print(f"It took you {count} attempts.")
