import random

# Display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
        return True
    return False

# Check if the board is full (tie)
def is_tie(board):
    return all(cell != " " for row in board for cell in row)

# Get player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Get computer's move
def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = "O"

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and the computer is 'O'.")
    print("Enter a number (1-9) to place your move:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        display_board(board)
        player_move(board)
        if check_winner(board, "X"):
            display_board(board)
            print("Congratulations! You win!")
            break
        if is_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        computer_move(board)
        if check_winner(board, "O"):
            display_board(board)
            print("Computer wins! Better luck next time.")
            break
        if is_tie(board):
            display_board(board)
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
