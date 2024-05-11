# Tic-Tac-Toe Game in Python

## Description
This is a simple Tic-Tac-Toe game implemented in Python. The game allows two players to take turns marking the spaces in a 3x3 grid with their respective symbols, usually X and O. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/MITHUNTR7/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
2. **Install Dependencies** <br>
   This project does not depend on external libraries beyond Python's standard library.
3. **Run the Program** <br>
    Ensure you have Python installed on your system. This project is compatible with Python 3.7 and above.

## Usage
To play a game, run the following command from your terminal:
```bash
python tictactoe.py <player1_type> <player2_type>
```
Where:

player1_type and player2_type can be one of the following:
- human_player: For human players.
- random_ai: Picks a move randomly.
- minimax_ai: Uses the Minimax algorithm for decision making.
- finds_own_winning_move_ai: AI that tries to find and make a winning move.
- finds_all_winning_moves_ai: AI that prevents losing and tries to win.

Example:
```bash
python tictactoe.py human_player minimax_ai
```

## Features
- Multiple AI Players: Choose between different types of AI or play against a human.
- CLI Based: Simple and easy-to-use command line interface.
- Custom AI Implementations: Includes implementations of various AI strategies like the advanced Minimax algorithm.

## Contributing
Contributions are welcome! If you have suggestions for improvements or bug fixes, feel free to:

- Fork the project
- Create a new branch (git checkout -b feature/AmazingFeature)
- Make your changes
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request
 project, as well as detailing how to contribute effectively.  
