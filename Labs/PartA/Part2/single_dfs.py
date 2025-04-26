import sys

class Maze:
    def __init__(self, file_path):
        self.grid = []
        self.start = None
        self.prize = None
        self.load_maze(file_path)
    
    def load_maze(self, file_path):
        with open(file_path, 'r') as f:
            for y, line in enumerate(f.readlines()):
                row = list(line.strip())
                for x, char in enumerate(row):
                    if char == 'P':
                        self.start = (x, y)
                    elif char == '.':
                        self.prize = (x, y)
                self.grid.append(row)
    
    def is_valid_move(self, x, y):
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]) and self.grid[y][x] != '%'
    
    def solve_dfs(self):
        stack = [(self.start, [self.start])]
        visited = set()
        nodes_expanded = 0
        
        while stack:
            (x, y), path = stack.pop()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))
            nodes_expanded += 1
            
            if (x, y) == self.prize:
                self.mark_solution_path(path)
                return path, len(path) - 1, nodes_expanded
            
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_x, new_y = x + dx, y + dy
                if self.is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                    stack.append(((new_x, new_y), path + [(new_x, new_y)]))
        
        return None, -1, nodes_expanded
    
    def mark_solution_path(self, path):
        for x, y in path:
            if self.grid[y][x] not in ('P', '.'):  # Keep start and prize unchanged
                self.grid[y][x] = '#'
    
    def print_maze(self):
        for row in self.grid:
            print(''.join(row))


def single_dfs(file_path):
    maze = Maze(file_path)
    path, cost, nodes_expanded = maze.solve_dfs()
    
    print("Solution:")
    maze.print_maze()
    print(f"Path Cost: {cost}")
    print(f"Nodes Expanded: {nodes_expanded}")
    
    return cost, nodes_expanded

if __name__ == "__main__":
 
    single_dfs('1prize-open.txt')
    single_dfs('1prize-medium.txt')
    single_dfs('1prize-large.txt')
