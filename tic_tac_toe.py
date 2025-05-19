import random 

# Function to print the game board with numbers for available spots
def print_board(board):
    # Show position numbers for empty spots; keep X/O for occupied ones
    display = [board[i] if board[i] != ' ' else str(i+1) for i in range(9)]

    # Display the board in a 3x3 grid format
    print()
    print(f" {display[0]} | {display[1]} | {display[2]} ")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]} ")
    print()

# Function to check if a given player has won
def check_winner(board, player):
    # All winning combinations (rows, columns, diagonals)
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    # Check if any winning combination is fully owned by the player
    return any(all(board[i] == player for i in combo) for combo in wins)

# Function to check for a tie (board is full and no winner)
def is_tie(board):
    return ' ' not in board

# Function to handle the player's move
def player_move(board):
    while True:
        try:
            # Ask for input and convert it to board index (0–8)
            move = int(input("Choose a position (1-9): ")) - 1
            # If the spot is empty, place the player's mark
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Spot taken. Try again.")
        except (ValueError, IndexError):
            # Handle invalid input: not a number or out of range
            print("Invalid input. Choose a number between 1 and 9.")

# Function for AI's move using simple strategy
def ai_move(board):
    # 1. Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner(board, 'O'):
                return  # Make winning move
            board[i] = ' '  # Undo if not a winner

    # 2. Try to block player's winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner(board, 'X'):
                board[i] = 'O'  # Block the player
                return
            board[i] = ' '  # Undo move

    # 3. Take center if available
    if board[4] == ' ':
        board[4] = 'O'
        return

    # 4. Pick a random available corner or side
    choice = random.choice([i for i in range(9) if board[i] == ' '])
    board[choice] = 'O'

# Function to manage one round of the game
def play_game():
    # Initialize an empty board
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.\n")
    print_board(board)

    while True:
        # Player's turn
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!\n")
            break
        if is_tie(board):
            print("It's a tie!\n")
            break

        # AI's turn
        print("AI's turn...")
        ai_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!\n")
            break
        if is_tie(board):
            print("It's a tie!\n")
            break

# Main function to allow repeated play
def main():
    while True:
        play_game()  # Play a round
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# Entry point: start the game
if __name__ == "__main__":
    main()
