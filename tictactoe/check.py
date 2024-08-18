def underline(text):
    return f"\033[4m{text}\033[0m"

# print(underline("This text will be underlined"))

def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} ")
        if i < 2:
            print("-----------")

# Initialize an empty board
board = [" " for _ in range(9)]

# Example usage
print_board(board)