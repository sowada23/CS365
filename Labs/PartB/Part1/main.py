class Breakthrough:
    def __init__(self, rows=8, cols=8, start_rows=2):
        self.rows = rows
        self.cols = cols
        self.start_rows = start_rows
        self.board = self.initial_state(rows, cols, start_rows)
    
    def initial_state(self, rows, cols, start_rows):
        """Creates the initial board configuration."""
        board = [['.' for _ in range(cols)] for _ in range(rows)]
        for r in range(start_rows):
            board[r] = ['X'] * cols  # Top player (black)
            board[rows - 1 - r] = ['O'] * cols  # Bottom player (white)
        return board
    
    def display_state(self):
        """Displays the current board state."""
        for row in self.board:
            print(''.join(row))
        print()
    
    def is_terminal(self):
        """Checks if the game is in a terminal state (win condition)."""
        for c in range(self.cols):
            if self.board[0][c] == 'O':  # White wins
                return True, 'O'
            if self.board[self.rows - 1][c] == 'X':  # Black wins
                return True, 'X'
        
        white_pieces = any('O' in row for row in self.board)
        black_pieces = any('X' in row for row in self.board)
        
        if not white_pieces:
            return True, 'X'  # Black wins if no white pieces remain
        if not black_pieces:
            return True, 'O'  # White wins if no black pieces remain
        
        return False, None  # Game is still ongoing
    
    def generate_moves(self, player):
        """Generates all possible moves for a given player."""
        moves = []
        direction = -1 if player == 'O' else 1  # White moves up (-1), Black moves down (+1)
        player_piece = 'O' if player == 'O' else 'X'
        
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == player_piece:
                    possible_moves = []
                    
                    # Forward move
                    if 0 <= r + direction < self.rows and self.board[r + direction][c] == '.':
                        possible_moves.append((r + direction, c))
                    
                    # Diagonal left capture
                    if 0 <= r + direction < self.rows and 0 <= c - 1 and self.board[r + direction][c - 1] != player_piece and self.board[r + direction][c - 1] != '.':
                        possible_moves.append((r + direction, c - 1))
                    
                    # Diagonal right capture
                    if 0 <= r + direction < self.rows and c + 1 < self.cols and self.board[r + direction][c + 1] != player_piece and self.board[r + direction][c + 1] != '.':
                        possible_moves.append((r + direction, c + 1))
                    
                    for move in possible_moves:
                        moves.append(((r, c), move))
        
        return moves
    
    def transition(self, move):
        """Applies a move and returns a new board state."""
        (start_r, start_c), (end_r, end_c) = move
        new_board = [row[:] for row in self.board]  # Deep copy
        new_board[end_r][end_c] = new_board[start_r][start_c]
        new_board[start_r][start_c] = '.'
        return new_board


# Example usage
game = Breakthrough()
game.display_state()
moves = game.generate_moves('O')
print("Possible moves for O:", moves)

if moves:
    new_board = game.transition(moves[0])
    game.board = new_board  # Apply the move
    game.display_state()
