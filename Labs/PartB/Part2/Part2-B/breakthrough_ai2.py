import random
import copy
import math

#############################
# Game Setup and State Representation
#############################

def initial_state(rows, cols, piece_rows):
    """
    Returns the starting board state.
    Top 'piece_rows' rows are filled with black pieces ('X') and
    bottom 'piece_rows' rows are filled with white pieces ('O').
    Empty squares are marked with '.'.
    """
    state = [['.' for _ in range(cols)] for _ in range(rows)]
    # Place black pieces on top
    for r in range(piece_rows):
        for c in range(cols):
            state[r][c] = 'X'
    # Place white pieces on bottom
    for r in range(rows - piece_rows, rows):
        for c in range(cols):
            state[r][c] = 'O'
    return state

def display_state(state):
    """
    Displays the board state in a simple text format.
    """
    for row in state:
        print("".join(row))
    print()

def terminal_test(state):
    """
    Checks if the state is terminal.
    Terminal conditions:
      - A white piece ('O') reaches the top row (row 0) → White wins.
      - A black piece ('X') reaches the bottom row → Black wins.
      - One player loses all pieces.
    Returns a tuple: (True/False, winning_player or None)
    """
    rows = len(state)
    cols = len(state[0])
    # Check if white reached top row.
    for c in range(cols):
        if state[0][c] == 'O':
            return True, 'O'
    # Check if black reached bottom row.
    for c in range(cols):
        if state[rows-1][c] == 'X':
            return True, 'X'
    # Check if a player has no pieces left.
    white_exists = any('O' in row for row in state)
    black_exists = any('X' in row for row in state)
    if not white_exists:
        return True, 'X'
    if not black_exists:
        return True, 'O'
    return False, None

def get_opponent(player):
    """
    Returns the opponent piece given a player ('O' or 'X').
    """
    return 'O' if player == 'X' else 'X'

def move_generator(player, state):
    """
    Generates all legal moves for the given player.
    A move is a tuple: (player, (src_row, src_col), (dest_row, dest_col))
    
    Movement rules (adapted for Breakthrough):
      - A piece can move forward vertically if the square is empty.
      - It can also move diagonally forward (left or right) if the square is either empty
        or occupied by an opponent (which counts as a capture).
      - For white ('O'), "forward" is one row up (r - 1).
      - For black ('X'), "forward" is one row down (r + 1).
    """
    moves = []
    rows = len(state)
    cols = len(state[0])
    dr = -1 if player == 'O' else 1  # white moves up; black moves down
    for r in range(rows):
        for c in range(cols):
            if state[r][c] == player:
                new_r = r + dr
                if 0 <= new_r < rows:
                    # Forward move (vertical)
                    if state[new_r][c] == '.':
                        moves.append((player, (r, c), (new_r, c)))
                    # Diagonal moves (left and right)
                    for dc in [-1, 1]:
                        new_c = c + dc
                        if 0 <= new_c < cols:
                            # Diagonal allowed if target is empty or contains opponent
                            if state[new_r][new_c] == '.' or state[new_r][new_c] == get_opponent(player):
                                moves.append((player, (r, c), (new_r, new_c)))
    return moves

def transition(state, action):
    """
    Returns a new state by applying the given action.
    The action is not applied in-place.
    """
    new_state = copy.deepcopy(state)
    player, (src_r, src_c), (dest_r, dest_c) = action
    new_state[src_r][src_c] = '.'
    new_state[dest_r][dest_c] = player
    return new_state

#############################
# Utility (Heuristic) Functions
#############################

def evasive_heuristic(state, player):
    """
    Evasive: number_of_own_pieces_remaining + random()
    """
    count = sum(row.count(player) for row in state)
    return count + random.random()

def conqueror_heuristic(state, player):
    """
    Conqueror: (0 - number_of_opponent_pieces_remaining) + random()
    """
    opponent = get_opponent(player)
    opp_count = sum(row.count(opponent) for row in state)
    return -opp_count + random.random()

def aggressor_heuristic(state, player):
    """
    Aggressor (custom utility):
      - Rewards having more pieces than the opponent.
      - Rewards advancing pieces toward the opponent's side.
      For white ('O'), advancement = (rows - 1 - current_row).
      For black ('X'), advancement = (current_row).
      Final score = 10*(own_count - opponent_count) + sum(advancement) + random()
    """
    rows = len(state)
    opponent = get_opponent(player)
    own_count = 0
    opp_count = 0
    adv_sum = 0
    for r in range(rows):
        for c in range(len(state[0])):
            if state[r][c] == player:
                own_count += 1
                if player == 'O':
                    adv_sum += (rows - 1 - r)
                else:
                    adv_sum += r
            elif state[r][c] == opponent:
                opp_count += 1
    return 10 * (own_count - opp_count) + adv_sum + random.random()

def defender_heuristic(state, player):
    """
    Defender (custom utility):
      - Rewards maintaining a high piece count and
        strongly penalizes opponent pieces and their advancement.
      - For the opponent, advancement is calculated as:
          if opponent is 'O': (rows - 1 - r)
          if opponent is 'X': (r)
      Final score = 15*(own_count) - 15*(opponent_count) - (sum of opponent advancements) + random()
    """
    rows = len(state)
    opponent = get_opponent(player)
    own_count = 0
    opp_count = 0
    opp_adv_sum = 0
    for r in range(rows):
        for c in range(len(state[0])):
            if state[r][c] == player:
                own_count += 1
            elif state[r][c] == opponent:
                opp_count += 1
                if opponent == 'O':
                    opp_adv_sum += (rows - 1 - r)
                else:
                    opp_adv_sum += r
    return 15 * own_count - 15 * opp_count - opp_adv_sum + random.random()

#############################
# Minimax Search (Depth-Limited)
#############################

def minimax(state, depth, is_maximizing, player, heuristic):
    """
    A depth-limited minimax search that uses the given heuristic function.
    The search is performed from the perspective of 'player' (whose heuristic is used).
    When it is the opponent's turn, the algorithm assumes that opponent will try to minimize
    the current player's heuristic value.
    """
    terminal, _ = terminal_test(state)
    if terminal or depth == 0:
        return heuristic(state, player)
    if is_maximizing:
        max_eval = -math.inf
        for move in move_generator(player, state):
            new_state = transition(state, move)
            eval = minimax(new_state, depth - 1, False, player, heuristic)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        opponent = get_opponent(player)
        min_eval = math.inf
        for move in move_generator(opponent, state):
            new_state = transition(state, move)
            eval = minimax(new_state, depth - 1, True, player, heuristic)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(state, player, depth, heuristic):
    """
    Determines the best move for the player using minimax search.
    Returns the action (move) with the best evaluated value.
    """
    best_val = -math.inf
    best_action = None
    for move in move_generator(player, state):
        new_state = transition(state, move)
        value = minimax(new_state, depth - 1, False, player, heuristic)
        if value > best_val:
            best_val = value
            best_action = move
    return best_action

#############################
# Game Play Function
#############################

def play_game(heuristic_white, heuristic_black, board_state, depth=3, display=True):
    """
    Simulates a game where white ('O') and black ('X') take turns.
    Each uses its own heuristic function:
      - heuristic_white for white
      - heuristic_black for black
    The function returns a dictionary with:
      - 'winner': the winning player
      - 'moves': total number of moves taken
      - 'captures': dictionary counting captures by each player
      - 'final_state': the final board configuration
    """
    state = board_state
    move_count = 0
    capture_count = {'O': 0, 'X': 0}
    # White ('O') moves first.
    current_player = 'O'
    
    while True:
        terminal, winner = terminal_test(state)
        if terminal:
            if display:
                print("Game Over!")
                display_state(state)
            return {'winner': winner, 'moves': move_count, 'captures': capture_count, 'final_state': state}
        if display:
            print(f"Move {move_count}: Player {current_player}'s turn")
            display_state(state)
        # Select heuristic for current player.
        heuristic = heuristic_white if current_player == 'O' else heuristic_black
        move = best_move(state, current_player, depth, heuristic)
        if move is None:
            # No legal moves; opponent wins.
            winner = get_opponent(current_player)
            if display:
                print(f"No legal moves for player {current_player}. {winner} wins!")
            return {'winner': winner, 'moves': move_count, 'captures': capture_count, 'final_state': state}
        # Check if move is a capture.
        dest_r, dest_c = move[2]
        if state[dest_r][dest_c] == get_opponent(current_player):
            capture_count[current_player] += 1
        state = transition(state, move)
        move_count += 1
        current_player = get_opponent(current_player)

#############################
# Example Matches (Part 2-B)
#############################

if __name__ == '__main__':

    import random
import copy
import math

#############################
# Game Setup and State Representation
#############################

def initial_state(rows, cols, piece_rows):
    """
    Returns the starting board state.
    Top 'piece_rows' rows are filled with black pieces ('X') and
    bottom 'piece_rows' rows are filled with white pieces ('O').
    Empty squares are marked with '.'.
    """
    state = [['.' for _ in range(cols)] for _ in range(rows)]
    # Place black pieces on top
    for r in range(piece_rows):
        for c in range(cols):
            state[r][c] = 'X'
    # Place white pieces on bottom
    for r in range(rows - piece_rows, rows):
        for c in range(cols):
            state[r][c] = 'O'
    return state

def display_state(state):
    """
    Displays the board state in a simple text format.
    """
    for row in state:
        print("".join(row))
    print()

def terminal_test(state):
    """
    Checks if the state is terminal.
    Terminal conditions:
      - A white piece ('O') reaches the top row (row 0) → White wins.
      - A black piece ('X') reaches the bottom row → Black wins.
      - One player loses all pieces.
    Returns a tuple: (True/False, winning_player or None)
    """
    rows = len(state)
    cols = len(state[0])
    # Check if white reached top row.
    for c in range(cols):
        if state[0][c] == 'O':
            return True, 'O'
    # Check if black reached bottom row.
    for c in range(cols):
        if state[rows-1][c] == 'X':
            return True, 'X'
    # Check if a player has no pieces left.
    white_exists = any('O' in row for row in state)
    black_exists = any('X' in row for row in state)
    if not white_exists:
        return True, 'X'
    if not black_exists:
        return True, 'O'
    return False, None

def get_opponent(player):
    """
    Returns the opponent piece given a player ('O' or 'X').
    """
    return 'O' if player == 'X' else 'X'

def move_generator(player, state):
    """
    Generates all legal moves for the given player.
    A move is a tuple: (player, (src_row, src_col), (dest_row, dest_col))
    
    Movement rules (adapted for Breakthrough):
      - A piece can move forward vertically if the square is empty.
      - It can also move diagonally forward (left or right) if the square is either empty
        or occupied by an opponent (which counts as a capture).
      - For white ('O'), "forward" is one row up (r - 1).
      - For black ('X'), "forward" is one row down (r + 1).
    """
    moves = []
    rows = len(state)
    cols = len(state[0])
    dr = -1 if player == 'O' else 1  # white moves up; black moves down
    for r in range(rows):
        for c in range(cols):
            if state[r][c] == player:
                new_r = r + dr
                if 0 <= new_r < rows:
                    # Forward move (vertical)
                    if state[new_r][c] == '.':
                        moves.append((player, (r, c), (new_r, c)))
                    # Diagonal moves (left and right)
                    for dc in [-1, 1]:
                        new_c = c + dc
                        if 0 <= new_c < cols:
                            # Diagonal allowed if target is empty or contains opponent
                            if state[new_r][new_c] == '.' or state[new_r][new_c] == get_opponent(player):
                                moves.append((player, (r, c), (new_r, new_c)))
    return moves

def transition(state, action):
    """
    Returns a new state by applying the given action.
    The action is not applied in-place.
    """
    new_state = copy.deepcopy(state)
    player, (src_r, src_c), (dest_r, dest_c) = action
    new_state[src_r][src_c] = '.'
    new_state[dest_r][dest_c] = player
    return new_state

#############################
# Utility (Heuristic) Functions
#############################

def evasive_heuristic(state, player):
    """
    Evasive: number_of_own_pieces_remaining + random()
    """
    count = sum(row.count(player) for row in state)
    return count + random.random()

def conqueror_heuristic(state, player):
    """
    Conqueror: (0 - number_of_opponent_pieces_remaining) + random()
    """
    opponent = get_opponent(player)
    opp_count = sum(row.count(opponent) for row in state)
    return -opp_count + random.random()

def aggressor_heuristic(state, player):
    """
    Aggressor (custom utility):
      - Rewards having more pieces than the opponent.
      - Rewards advancing pieces toward the opponent's side.
      For white ('O'), advancement = (rows - 1 - current_row).
      For black ('X'), advancement = (current_row).
      Final score = 10*(own_count - opponent_count) + sum(advancement) + random()
    """
    rows = len(state)
    opponent = get_opponent(player)
    own_count = 0
    opp_count = 0
    adv_sum = 0
    for r in range(rows):
        for c in range(len(state[0])):
            if state[r][c] == player:
                own_count += 1
                if player == 'O':
                    adv_sum += (rows - 1 - r)
                else:
                    adv_sum += r
            elif state[r][c] == opponent:
                opp_count += 1
    return 10 * (own_count - opp_count) + adv_sum + random.random()

def defender_heuristic(state, player):
    """
    Defender (custom utility):
      - Rewards maintaining a high piece count and
        strongly penalizes opponent pieces and their advancement.
      - For the opponent, advancement is calculated as:
          if opponent is 'O': (rows - 1 - r)
          if opponent is 'X': (r)
      Final score = 15*(own_count) - 15*(opponent_count) - (sum of opponent advancements) + random()
    """
    rows = len(state)
    opponent = get_opponent(player)
    own_count = 0
    opp_count = 0
    opp_adv_sum = 0
    for r in range(rows):
        for c in range(len(state[0])):
            if state[r][c] == player:
                own_count += 1
            elif state[r][c] == opponent:
                opp_count += 1
                if opponent == 'O':
                    opp_adv_sum += (rows - 1 - r)
                else:
                    opp_adv_sum += r
    return 15 * own_count - 15 * opp_count - opp_adv_sum + random.random()

#############################
# Minimax Search (Depth-Limited)
#############################

def minimax(state, depth, is_maximizing, player, heuristic):
    """
    A depth-limited minimax search that uses the given heuristic function.
    The search is performed from the perspective of 'player' (whose heuristic is used).
    When it is the opponent's turn, the algorithm assumes that opponent will try to minimize
    the current player's heuristic value.
    """
    terminal, _ = terminal_test(state)
    if terminal or depth == 0:
        return heuristic(state, player)
    if is_maximizing:
        max_eval = -math.inf
        for move in move_generator(player, state):
            new_state = transition(state, move)
            eval = minimax(new_state, depth - 1, False, player, heuristic)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        opponent = get_opponent(player)
        min_eval = math.inf
        for move in move_generator(opponent, state):
            new_state = transition(state, move)
            eval = minimax(new_state, depth - 1, True, player, heuristic)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(state, player, depth, heuristic):
    """
    Determines the best move for the player using minimax search.
    Returns the action (move) with the best evaluated value.
    """
    best_val = -math.inf
    best_action = None
    for move in move_generator(player, state):
        new_state = transition(state, move)
        value = minimax(new_state, depth - 1, False, player, heuristic)
        if value > best_val:
            best_val = value
            best_action = move
    return best_action

#############################
# Game Play Function
#############################

def play_game(heuristic_white, heuristic_black, board_state, depth=3, display=True):
    """
    Simulates a game where white ('O') and black ('X') take turns.
    Each uses its own heuristic function:
      - heuristic_white for white
      - heuristic_black for black
    The function returns a dictionary with:
      - 'winner': the winning player
      - 'moves': total number of moves taken
      - 'captures': dictionary counting captures by each player
      - 'final_state': the final board configuration
    """
    state = board_state
    move_count = 0
    capture_count = {'O': 0, 'X': 0}
    # White ('O') moves first.
    current_player = 'O'
    
    while True:
        terminal, winner = terminal_test(state)
        if terminal:
            if display:
                print("Game Over!")
                display_state(state)
            return {'winner': winner, 'moves': move_count, 'captures': capture_count, 'final_state': state}
        if display:
            print(f"Move {move_count}: Player {current_player}'s turn")
            display_state(state)
        # Select heuristic for current player.
        heuristic = heuristic_white if current_player == 'O' else heuristic_black
        move = best_move(state, current_player, depth, heuristic)
        if move is None:
            # No legal moves; opponent wins.
            winner = get_opponent(current_player)
            if display:
                print(f"No legal moves for player {current_player}. {winner} wins!")
            return {'winner': winner, 'moves': move_count, 'captures': capture_count, 'final_state': state}
        # Check if move is a capture.
        dest_r, dest_c = move[2]
        if state[dest_r][dest_c] == get_opponent(current_player):
            capture_count[current_player] += 1
        state = transition(state, move)
        move_count += 1
        current_player = get_opponent(current_player)

#############################
# Example Matches (Part 2-B)
#############################

if __name__ == '__main__':

    # Define Board Sizes to Test
    board_sizes = [(8, 8, 2), (6, 6, 2), (10, 10, 3)]  # (rows, cols, piece_rows)
    num_trials = 10  # Number of times to run each matchup

    # Data Storage
    results = {}

    # AI Matchups to Compare
    ai_matchups = [
        ("Evasive vs Conqueror", evasive_heuristic, conqueror_heuristic),
        ("Aggressor vs Defender", aggressor_heuristic, defender_heuristic),
    ]

    # Run experiments for each board size
    for rows, cols, piece_rows in board_sizes:
        results[(rows, cols, piece_rows)] = {}

        for match_name, ai1, ai2 in ai_matchups:
            win_counts = {"AI1 Wins": 0, "AI2 Wins": 0, "Total Moves": [], "Captured Pieces": [], "Final Board States": []}

            for _ in range(num_trials):
                board = initial_state(rows, cols, piece_rows)

                # Run the game and get results
                result = play_game(ai1, ai2, board, depth=3)
                print("DEBUG: Game Result:", result)  # Debugging to ensure correct format

                # Ensure result is a dictionary and extract values correctly
                if isinstance(result, dict):
                    winner = result.get('winner', None)
                    total_moves = result.get('moves', 0)
                    captured_pieces = sum(result.get('captures', {}).values())  # Sum captured pieces
                    final_board = result.get('final_state', [])

                    # Store Results
                    win_counts["Total Moves"].append(total_moves)
                    win_counts["Captured Pieces"].append(captured_pieces)
                    win_counts["Final Board States"].append(copy.deepcopy(final_board))

                    if winner == "X":  # Assuming 'X' is AI1
                        win_counts["AI1 Wins"] += 1
                    elif winner == "O":  # Assuming 'O' is AI2
                        win_counts["AI2 Wins"] += 1
                else:
                    print("ERROR: Unexpected result format:", result)
                    continue  # Skip this iteration if format is incorrect

            # Store aggregated results
            results[(rows, cols, piece_rows)][match_name] = {
                "AI1 Wins": win_counts["AI1 Wins"],
                "AI2 Wins": win_counts["AI2 Wins"],
                "Avg Moves": sum(win_counts["Total Moves"]) / num_trials if win_counts["Total Moves"] else 0,
                "Avg Captured Pieces": sum(win_counts["Captured Pieces"]) / num_trials if win_counts["Captured Pieces"] else 0,
                "Final Boards": win_counts["Final Board States"]
            }

    # Print results for analysis
    for board_size, match_data in results.items():
        print(f"\n🔹 Board Size: {board_size}")
        for match, data in match_data.items():
            print(f"\nMatch: {match}")
            print(f"  ✅ AI1 Wins: {data['AI1 Wins']} / {num_trials}")
            print(f"  ✅ AI2 Wins: {data['AI2 Wins']} / {num_trials}")
            print(f"  📊 Avg Moves Before Victory: {data['Avg Moves']:.2f}")
            print(f"  📉 Avg Captured Pieces: {data['Avg Captured Pieces']:.2f}")