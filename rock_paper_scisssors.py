import random

user_wins = 0
computer_wins = 0
ties = 0

while True:
    # Get user's choice
    while True:
        user_choice = input("Enter your choice ('r' for rock, 'p' for paper, 's' for scissors): ").lower()
        if user_choice in ["r", "p", "s"]:
            break
        else:
            print("Invalid choice. Please enter 'r', 'p, or 's'")
            
    if user_choice == "r":
        user_choice = "rock"
    elif user_choice == "p":
        user_choice = "paper"
    elif user_choice == "s":
        user_choice = "scissors"

        
    # Generate computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        winner = "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        winner = "user"
    else:
        winner = "computer"

    # Display results
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if winner == "user":
        print("You win!")
        user_wins += 1
    elif winner == "computer":
        print("Computer wins!")
        computer_wins += 1
    else:
        print("It's a tie!")
        ties += 1

    print(f"Current Score: User-{user_wins}, Computer-{computer_wins}, Ties-{ties}")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break

print("Final Score:")
print(f"User: {user_wins}")
print(f"Computer: {computer_wins}")
print(f"Ties: {ties}")
print("Thanks for playing!")