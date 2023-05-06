import random

def game():
    # It a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Allow the player to make up to 5 guesses
    guesses_left = 5
    
    # Loop until the player runs out of guesses or guesses correctly
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print("You win!")
            return
        
        guesses_left -= 1
        
    print("You lose. The number was {secret_number}.")

game()
