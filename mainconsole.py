import math

# Display board
def print_board(board):
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("--+---+--")


# Check winner
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Check if moves are left
def moves_left(board):
    return any(" " in row for row in board)

# Minimax AI logic
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # AI wins
        return 1
    elif winner == "X":  # Human wins
        return -1
    elif not moves_left(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

# Find best AI move
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe — You (X) vs AI (O)")
    print_board(board)

    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("Invalid move! Try again.")
                continue
        except:
            print("Please enter a number from 1 to 9.")
            continue

        board[row][col] = "X"

        if check_winner(board):
            print_board(board)
            print("🎉 You win!")
            break
        if not moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"

        print_board(board)
        if check_winner(board):
            print("💻 AI wins!")
            break
        if not moves_left(board):
            print("It's a draw!")
            break

# Run game
tic_tac_toe()