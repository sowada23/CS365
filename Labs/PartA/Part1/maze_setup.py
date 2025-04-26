class State:
    def __init__(self, position, collected_prizes=None):
        self.position = position
        self.collected_prizes = collected_prizes or set()
    
    def __eq__(self, other):
        return self.position == other.position and self.collected_prizes == other.collected_prizes
    
    def __hash__(self):
        return hash((self.position, frozenset(self.collected_prizes)))

class Maze:
    def __init__(self, file_path):
        self.grid = []
        self.start = None
        self.prizes = set()
        self.load_maze(file_path)
    
    def load_maze(self, file_path):
        with open(file_path, 'r') as f:
            for y, line in enumerate(f.readlines()):
                row = list(line.strip())
                for x, char in enumerate(row):
                    if char == 'P':
                        self.start = (x, y)
                    elif char == '.':
                        self.prizes.add((x, y))
                self.grid.append(row)
    
    def is_valid_move(self, x, y):
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]) and self.grid[y][x] != '%'
    
    def move_agent(self, state, action):
        moves = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        dx, dy = moves[action]
        new_x, new_y = state.position[0] + dx, state.position[1] + dy
        
        if self.is_valid_move(new_x, new_y):
            new_collected = set(state.collected_prizes)
            if (new_x, new_y) in self.prizes:
                new_collected.add((new_x, new_y))
            return State((new_x, new_y), new_collected)
        
        return state  # Return the same state if the move is invalid
    
    def goal_test(self, state):
        return state.collected_prizes == self.prizes
    
    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.grid])

# Example usage
if __name__ == "__main__":
    maze = Maze("1prize-open.txt")
    initial_state = State(maze.start)
    print("Maze:")
    print(maze)
    print("Start position:", maze.start)
    print("Prizes:", maze.prizes)
    print("Goal Reached?", maze.goal_test(initial_state))
    
    # Example move test
    new_state = maze.move_agent(initial_state, 'S')  # Move South
    print("New Position after moving South:", new_state.position)
    print("Goal Reached?", maze.goal_test(new_state))