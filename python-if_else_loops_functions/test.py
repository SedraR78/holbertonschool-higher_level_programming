#!/usr/bin/python3

def print_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0  # Track number of moves

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            # Check input is in valid range
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid position. Please enter numbers between 0 and 2.")
                continue

            # Check if cell is empty
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Make move
            board[row][col] = player
            moves += 1

            # Check winner
            if check_winner(board):
                print_board(board)
                print(f"🎉 Player {player} wins!")
                break

            # Check draw
            if moves == 9:
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid coordinates. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
    