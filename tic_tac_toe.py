board = [" " for _ in range(9)]

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None

def tic_tac_toe():
    current_player = "X"

    print("================================")
    print("       TIC TAC TOE GAME")
    print("================================")
    print("Player 1: X")
    print("Player 2: O")
    print("Enter positions from 1 to 9.")

    while True:
        display_board()

        try:
            position = int(input(
                f"Player {current_player}, enter position (1-9): "
            ))

            if position < 1 or position > 9:
                print("Invalid position! Choose between 1 and 9.")
                continue

            if board[position - 1] != " ":
                print("Position already occupied! Try again.")
                continue

            board[position - 1] = current_player

        except ValueError:
            print("Please enter a valid number!")
            continue

        winner = check_winner()

        if winner:
            display_board()
            print(f"Congratulations! Player {winner} wins!")
            break

        if " " not in board:
            display_board()
            print("It's a Draw!")
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
