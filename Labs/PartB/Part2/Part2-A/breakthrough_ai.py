#!/usr/bin/env python3
import copy
import random

# ---------------------------
# PART 1 FUNCTIONS
# ---------------------------

def display_state(state):
    """Print a pictorial representation of the board state."""
    for row in state:
        print(''.join(row))
    print()  # extra newline for readability

def initial_state(rows, cols, piece_rows):
    """
    Create the starting board state.
    Top piece_rows are filled with 'X' (white) and bottom piece_rows with 'O' (black).
    Empty cells are represented by '.'.
    """
    state = [['.' for _ in range(cols)] for _ in range(rows)]
    # Fill top rows with white pieces ('X')
    for r in range(piece_rows):
        for c in range(cols):
            state[r][c] = 'X'
    # Fill bottom rows with black pieces ('O')
    for r in range(rows - piece_rows, rows):
        for c in range(cols):
            state[r][c] = 'O'
    return state

def opponent(player):
    """Return the opponent's symbol."""
    return 'O' if player == 'X' else 'X'

def get_possible_moves(state, player):
    """
    Generate all possible moves for the given player.
    Moves are represented as tuples: (start_row, start_col, end_row, end_col)
    
    In Breakthrough, a piece moves one step forward:
      - For 'X' (white), forward is increasing the row index.
      - For 'O' (black), forward is decreasing the row index.
    A piece may move straight forward into an empty cell or diagonally forward
    (left/right) into a cell that is empty or occupied by an opponent.
    """
    moves = []
    rows = len(state)
    cols = len(state[0])
    
    # Determine direction: white moves down (+1), black moves up (-1)
    dr = 1 if player == 'X' else -1
    
    for r in range(rows):
        for c in range(cols):
            if state[r][c] == player:
                # Straight move: must be empty.
                new_r = r + dr
                if 0 <= new_r < rows:
                    if state[new_r][c] == '.':
                        moves.append((r, c, new_r, c))
                # Diagonal left move.
                new_c = c - 1
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    # Allow move if destination is empty or occupied by opponent.
                    if state[new_r][new_c] == '.' or state[new_r][new_c] == opponent(player):
                        moves.append((r, c, new_r, new_c))
                # Diagonal right move.
                new_c = c + 1
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if state[new_r][new_c] == '.' or state[new_r][new_c] == opponent(player):
                        moves.append((r, c, new_r, new_c))
    return moves

def apply_move(state, move, player):
    """
    Return a new board state after applying the given move.
    The move is a tuple (r, c, r2, c2). This function makes a deep copy of the state,
    moves the piece from (r, c) to (r2, c2), and, if an opponent piece was present, it is captured.
    """
    new_state = copy.deepcopy(state)
    r, c, r2, c2 = move
    new_state[r2][c2] = player
    new_state[r][c] = '.'
    return new_state

def is_terminal(state):
    """
    Check whether the state is terminal (i.e. a win has occurred).
    A game-ending state is one where:
      - A white piece ('X') reaches the bottom row.
      - A black piece ('O') reaches the top row.
      - One player has no pieces remaining.
    Returns a tuple (terminal, winner). If not terminal, winner is None.
    """
    rows = len(state)
    cols = len(state[0])
    
    # Check if white has reached the bottom row.
    if any(cell == 'X' for cell in state[rows - 1]):
        return (True, 'X')
    # Check if black has reached the top row.
    if any(cell == 'O' for cell in state[0]):
        return (True, 'O')
    
    # Count remaining pieces for each player.
    count_X = sum(row.count('X') for row in state)
    count_O = sum(row.count('O') for row in state)
    
    if count_X == 0:
        return (True, 'O')
    if count_O == 0:
        return (True, 'X')
    
    # Not terminal.
    return (False, None)

# ---------------------------
# MINIMAX SEARCH FOR PART 2-A
# ---------------------------

def minimax(state, depth, current_player, maximizing_player, heuristic):
    """
    Recursively perform minimax search.
    
    - state: current board state.
    - depth: remaining depth of search.
    - current_player: whose turn it is.
    - maximizing_player: the player for whom we are computing the best move (fixed at the root).
    - heuristic: evaluation function that takes (state, maximizing_player) and returns a value.
    
    Returns a tuple (value, move) where move is the best move found (or None at a leaf).
    For terminal states, returns a very high (or low) value.
    """
    terminal, winner = is_terminal(state)
    if depth == 0 or terminal:
        if terminal:
            if winner == maximizing_player:
                return (10000, None)
            elif winner is None:
                return (0, None)
            else:
                return (-10000, None)
        else:
            return (heuristic(state, maximizing_player), None)
    
    moves = get_possible_moves(state, current_player)
    if not moves:
        # No legal moves; treat as a loss.
        if current_player == maximizing_player:
            return (-10000, None)
        else:
            return (10000, None)
    
    if current_player == maximizing_player:
        best_value = -float('inf')
        best_move = None
        for move in moves:
            new_state = apply_move(state, move, current_player)
            value, _ = minimax(new_state, depth - 1, opponent(current_player), maximizing_player, heuristic)
            if value > best_value:
                best_value = value
                best_move = move
        return (best_value, best_move)
    else:
        best_value = float('inf')
        best_move = None
        for move in moves:
            new_state = apply_move(state, move, current_player)
            value, _ = minimax(new_state, depth - 1, opponent(current_player), maximizing_player, heuristic)
            if value < best_value:
                best_value = value
                best_move = move
        return (best_value, best_move)

# ---------------------------
# UTILITY FUNCTION: Evasive
# ---------------------------

def heuristic_evasive(state, player):
    """
    Evasive heuristic:
    The value is the number of pieces the given player has plus a random value in [0,1)
    to break ties.
    """
    count = sum(row.count(player) for row in state)
    return count + random.random()

# ---------------------------
# PLAY GAME FUNCTION FOR PART 2-A
# ---------------------------

def play_game(heuristic_white, heuristic_black, board_state, depth=3):
    """
    Simulate a game between two AI players using minimax search.
    
    heuristic_white: function used by White ('X').
    heuristic_black: function used by Black ('O').
    board_state: initial board configuration.
    depth: search depth for minimax (e.g., 3 steps ahead).
    
    The function prints the board after each move and, at game end, shows the winner,
    the total number of moves, and a count of captures for each player.
    """
    state = board_state
    current_player = 'X'  # White starts
    move_count = 0
    captures = {'X': 0, 'O': 0}
    
    while True:
        terminal, winner = is_terminal(state)
        if terminal:
            print("Game Over!")
            print("Winner:", winner)
            print("Total moves:", move_count)
            print("Captures - White: {}, Black: {}".format(captures['X'], captures['O']))
            print("Final board state:")
            display_state(state)
            break

        print("Move {}: Player {}".format(move_count, current_player))
        display_state(state)
        
        # Choose the appropriate heuristic for the current player.
        if current_player == 'X':
            _, move = minimax(state, depth, current_player, current_player, heuristic_white)
        else:
            _, move = minimax(state, depth, current_player, current_player, heuristic_black)
        
        if move is None:
            print("No legal moves for player", current_player)
            break
        
        # Check if the move is a capture (i.e. destination contains opponent's piece)
        r, c, r2, c2 = move
        if state[r2][c2] != '.' and state[r2][c2] == opponent(current_player):
            captures[current_player] += 1
        
        # Apply the move to generate the new state.
        state = apply_move(state, move, current_player)
        move_count += 1
        # Switch turns.
        current_player = opponent(current_player)

# ---------------------------
# MAIN: Run a sample game
# ---------------------------

if __name__ == "__main__":
    # Set a seed for reproducibility if desired:
    random.seed(42)
    
    # Create an initial board: for example, a 5x5 board with 1 row of pieces for each side.
    board = initial_state(5, 5, 1)
    
    print("Initial board:")
    display_state(board)
    
    print("Starting game: Evasive (White) vs. Evasive (Black)")
    # Both players use the same Evasive heuristic.
    play_game(heuristic_evasive, heuristic_evasive, board, depth=3)