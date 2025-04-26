# Breakthrough AI

## Overview
This project implements an AI agent to play the Breakthrough board game using a minimax search algorithm with various heuristic functions.

## Requirements
- Python 3.x
- No external libraries required

## Game Rules
Breakthrough is a two-player game where players move pieces forward, aiming to reach the opponent’s last row or eliminate all opponent pieces.

## Features
- **Board Representation**: The game state is stored in a 2D list.
- **Move Generation**: Legal moves include forward and diagonal captures.
- **Minimax AI**: Implements depth-limited minimax with heuristic evaluations.
- **Heuristics**:
  - `evasive_heuristic`: Maximizes survival.
  - `conqueror_heuristic`: Maximizes opponent elimination.
  - `aggressor_heuristic`: Encourages piece count advantage and board control.
  - `defender_heuristic`: Penalizes opponent advancement while maintaining own pieces.

## Usage
Run the script to see AI matches:
```bash
python breakthrough_ai2.py
```

## Example Output
```
Starting game: White (Evasive) vs Black (Conqueror)
Move 0: Player O's turn
XXXXXXXX
XXXXXXXX
........
........
........
........
OOOOOOOO
OOOOOOOO
...
Game Over!
Final State:
XXXXXXXX
XXXXXXXX
........
........
........
........
OOOOOOOO
OOOOOOOO
Winner: Black (X)
Total Moves: 24
```

## License
This project is for educational purposes.

