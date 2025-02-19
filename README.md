# Minesweeper Game (Text-Based)

This is a simple, text-based version of the classic Minesweeper game written in Python. The game is played in the terminal, and your goal is to uncover all the cells that don't contain mines, while avoiding the ones that do.

## Features:
- Text-based interface.
- Randomly placed mines on a grid.
- Clickable cells to reveal safe areas or trigger mines.
- Recursive opening of cells with no neighboring mines.
- Checks for a win when all non-mine cells are revealed.

## How to Play:
1. The game will display a grid of cells. Your task is to uncover the cells by entering the row and column coordinates.
2. If you uncover a cell with a mine, you lose the game.
3. If you uncover all non-mine cells, you win the game!  

### Example Game Flow:
Enter row (0-9): 3 Enter column (0-9): 4 Current board: ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 1 ■ ■ ■ ■ ■ ■ ■ ■ 2 ■ ■ ■ ■ ■ ■ ■ ■ 3 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■

## How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/minesweeper-game.git 
cd minesweeper-game

python3 minesweeper.py
License:
This project is licensed under the MIT License - see the LICENSE file for details.

Contributions:
Feel free to fork the repository and submit pull requests. If you have ideas for improvements or new features, let me know!

Technologies Used:
Python 3.x
