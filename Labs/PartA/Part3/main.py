import heapq
from collections import deque

def read_maze(file_path):
    with open(file_path, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
    
    start, goal = None, None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'P':
                start = (i, j)
            elif cell == '.':
                goal = (i, j)
    
    return maze, start, goal

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def mark_path(maze, path):
    for i, j in path:
        maze[i][j] = '#'
    return '\n'.join(''.join(row) for row in maze)

def single_bfs(file_path):
    maze, start, goal = read_maze(file_path)
    queue = deque([start])
    came_from = {start: None}
    nodes_expanded = 0
    
    while queue:
        current = queue.popleft()
        nodes_expanded += 1
        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return mark_path(maze, path), len(path), nodes_expanded
        
        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if maze[neighbor[0]][neighbor[1]] in (' ', '.') and neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current
    return None

def single_gbfs(file_path):
    maze, start, goal = read_maze(file_path)
    queue = [(manhattan_distance(start, goal), start)]
    came_from = {start: None}
    nodes_expanded = 0
    
    while queue:
        _, current = heapq.heappop(queue)
        nodes_expanded += 1
        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return mark_path(maze, path), len(path), nodes_expanded
        
        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if maze[neighbor[0]][neighbor[1]] in (' ', '.') and neighbor not in came_from:
                heapq.heappush(queue, (manhattan_distance(neighbor, goal), neighbor))
                came_from[neighbor] = current
    return None

def single_astar(file_path):
    maze, start, goal = read_maze(file_path)
    queue = [(0 + manhattan_distance(start, goal), 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0
    
    while queue:
        _, cost, current = heapq.heappop(queue)
        nodes_expanded += 1
        if current == goal:
            path = reconstruct_path(came_from, start, goal)
            return mark_path(maze, path), len(path), nodes_expanded
        
        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + d[0], current[1] + d[1])
            new_cost = cost + 1
            if maze[neighbor[0]][neighbor[1]] in (' ', '.') and (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(queue, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    return None

if __name__ == "__main__":
    for algo, func in [('BFS', single_bfs), ('GBFS', single_gbfs), ('A*', single_astar)]:
        for maze_file in ["1prize-open.txt", "1prize-medium.txt", "1prize-large.txt"]:
            solution, path_cost, nodes_expanded = func(maze_file)
            print(f"\n{algo} Solution for {maze_file}:")
            print(solution)
            print(f"Path Cost: {path_cost}, Nodes Expanded: {nodes_expanded}\n")
