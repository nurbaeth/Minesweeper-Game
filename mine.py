import random

# Board dimensions
width = 10
height = 10
num_mines = 10

# Create the board
def create_board():
    board = [[' ' for _ in range(width)] for _ in range(height)]
    mines = random.sample(range(width * height), num_mines)  # Place mines

    for mine in mines:
        row = mine // width
        col = mine % width
        board[row][col] = '*'

    return board

# Print the board
def print_board(board, reveal=False):
    for row in board:
        for cell in row:
            if cell == ' ' and not reveal:
                print('■', end=' ')
            else:
                print(cell, end=' ')
        print()

# Count neighboring mines
def count_neighbors(board, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < height and 0 <= c < width and board[r][c] == '*':
            count += 1
    return count

# Open a cell
def open_cell(board, revealed, row, col):
    if revealed[row][col] or board[row][col] == '*':
        return
    
    # Count mines around the cell
    neighbors = count_neighbors(board, row, col)
    revealed[row][col] = True
    if neighbors == 0:
        # Recursively open neighboring cells if no mines
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < height and 0 <= c < width and not revealed[r][c]:
                open_cell(board, revealed, r, c)

# Main game loop
def play_game():
    board = create_board()
    revealed = [[False for _ in range(width)] for _ in range(height)]
    
    while True:
        print_board(board, reveal=False)
        row = int(input(f'Enter row (0-{height-1}): '))
        col = int(input(f'Enter column (0-{width-1}): '))

        if board[row][col] == '*':
            print("Game Over! You hit a mine!")
            break

        open_cell(board, revealed, row, col)

        # Check for win
        if all(revealed[row][col] or board[row][col] == '*' for row in range(height) for col in range(width)):
            print("Congratulations, you won!")
            break

        print_board(board, reveal=True)

# Start the game
if __name__ == "__main__":
    play_game()
