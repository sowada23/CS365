# Breakthrough Game - Part 1

## Overview
This project implements Part 1 of the **Breakthrough Board Game AI** as required in CS365 Lab B. The implementation includes a board representation, functions to display the board, generate legal moves, apply transitions, and check for terminal states.

## Features Implemented
- **Board Representation**: A 2D list represents the game board.
- **Display State (`display_state`)**: Prints a text-based representation of the board.
- **Initial State (`initial_state`)**: Creates the starting configuration based on given dimensions.
- **Transition Function (`transition`)**: Moves a piece and returns the new board state.
- **Terminal Test (`is_terminal`)**: Checks if a player has won the game.
- **Move Generator (`generate_moves`)**: Lists all legal moves for a given player.

## Installation & Usage
### Prerequisites
- Python 3.x installed

### Running the Code
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd PartB
   cd Part1
   ```
2. Run the game script:
   ```bash
   python3 main.py
   ```

### Example Output
When running the script, the initial board state will be displayed, followed by possible moves for the `O` (White) player.

```
XXXXXXXX
XXXXXXXX
........
........
........
........
OOOOOOOO
OOOOOOOO

Possible moves for O: [((6, 0), (5, 0)), ((6, 1), (5, 1)), ...]
```

## Code Structure
- `main.py` - Main implementation of the game.
- `README.md` - This documentation file.

## Future Work
This implementation is **Part 1** of Lab B. Future work includes implementing AI strategies using Minimax search in **Part 2**.

## Authors
- Sora Owada
- CS365 Spring 2025

## License
This project is for educational purposes as part of CS365 coursework.

