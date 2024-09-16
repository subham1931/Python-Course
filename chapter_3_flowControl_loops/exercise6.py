import random

winning_num = random.randint(1, 100)  # Generate a random winning number
count = 0
over = False

while not over:
    user_number = int(input("Enter your lucky number between 1-100: "))  # Get user's guess
    
    if user_number == winning_num:
        print("You win!")
        over = True  # End the game if the guess is correct
    elif user_number > winning_num:
        print("Too high")
        count += 1
    elif user_number < winning_num:
        print("Too low")
        count += 1

print(f"It took you {count} attempts.")
