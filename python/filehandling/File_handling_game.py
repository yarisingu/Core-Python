import random

def play_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # Initialize variables
    score = 0
    high_score = read_high_score()
    
    print("Welcome to the High Score Game!")
    print("The current high score is:", high_score)
    print("Guess a number between 1 and 100.")
    
    while True:
        guess = int(input("Enter your guess: "))
        score += 1
        
        if guess == number:
            print("Congratulations! You guessed the number in", score, "attempts.")
            
            if score < high_score:
                print("You've achieved a new high score!")
                write_high_score(score)
            else:
                print("Try again to beat the high score.")
            
            break
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

def read_high_score():
    try:
        with open("C:\\Users\\yaris\\OneDrive\\Desktop\\deleteafteruse\\python\\files_create_with_python_code\\createdbypython.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = float('inf')
    
    return high_score

def write_high_score(score):
    with open("C:\\Users\\yaris\\OneDrive\\Desktop\\deleteafteruse\\python\\files_create_with_python_code\\createdbypython.txt", "w") as file:
        file.write(str(score))

# Start the game
play_game()
