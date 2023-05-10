def start_game():
    # Introduce the game
    print("Welcome to the text-based adventure game!")
    print("You wake up in a dark room. You can't see anything.")
    print("What do you do?")
    
    # Present the first set of choices
    print("1. Try to find a light switch")
    print("2. Yell for help")
    print("3. Wait for someone to find you")
    
    # Get the user's choice
    choice = input("Enter your choice (1-3): ")
    
    # Process the user's choice
    if choice == "1":
        # User chooses to find a light switch
        print("You feel your way along the wall and eventually find a light switch.")
        print("You turn it on and see that you're in a small room with a door.")
        print("What do you do?")
        
        # Present the next set of choices
        print("1. Try to open the door")
        print("2. Look for a key")
        
        # Get the user's choice
        choice = input("Enter your choice (1-2): ")
        
        # Process the user's choice
        if choice == "1":
            # User chooses to try to open the door
            print("The door is locked. You need to find a key.")
            start_game()  # Restart the game
        elif choice == "2":
            # User chooses to look for a key
            print("You search the room and find a key under the bed.")
            print("You use the key to unlock the door and escape.")
            print("Congratulations! You win!")
    elif choice == "2":
        # User chooses to yell for help
        print("You yell for help, but no one hears you.")
        start_game()  # Restart the game
    elif choice == "3":
        # User chooses to wait for someone to find them
        print("You wait for hours, but no one comes.")
        start_game()  # Restart the game
    else:
        # User enters an invalid choice
        print("Invalid choice. Please enter 1, 2, or 3.")
        start_game()  # Restart the game
        
# Start the game
start_game()
