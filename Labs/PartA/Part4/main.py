import heapq

def read_maze(file_path):
    with open(file_path, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
    
    start, goals = None, []
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'P':
                start = (i, j)
            elif cell == '.':
                goals.append((i, j))
    
    return maze, start, goals

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(current, remaining_goals):
    if not remaining_goals:
        return 0
    return min(manhattan_distance(current, goal) for goal in remaining_goals)

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def mark_path(maze, full_path, prize_order):
    for index, (i, j) in enumerate(full_path):
        if (i, j) in prize_order:
            maze[i][j] = str(prize_order[(i, j)])
        else:
            maze[i][j] = '#'
    return '\n'.join(''.join(row) for row in maze)

def multi_astar(file_path):
    maze, start, prizes = read_maze(file_path)
    prize_order = {}
    path_cost, nodes_expanded = 0, 0
    full_path = []
    
    current_pos = start
    remaining_goals = set(prizes)
    
    while remaining_goals:
        queue = [(0, 0, current_pos)]
        came_from = {current_pos: None}
        cost_so_far = {current_pos: 0}
        target = min(remaining_goals, key=lambda g: manhattan_distance(current_pos, g))
        
        while queue:
            _, cost, current = heapq.heappop(queue)
            nodes_expanded += 1
            if current == target:
                path = reconstruct_path(came_from, current_pos, target)
                path_cost += len(path)
                full_path.extend(path)
                current_pos = target
                remaining_goals.remove(target)
                prize_order[target] = len(prize_order)
                break
            
            for d in [(0,1), (1,0), (0,-1), (-1,0)]:
                neighbor = (current[0] + d[0], current[1] + d[1])
                if maze[neighbor[0]][neighbor[1]] in (' ', '.') and (neighbor not in cost_so_far or cost + 1 < cost_so_far[neighbor]):
                    cost_so_far[neighbor] = cost + 1
                    priority = cost_so_far[neighbor] + heuristic(neighbor, remaining_goals)
                    heapq.heappush(queue, (priority, cost_so_far[neighbor], neighbor))
                    came_from[neighbor] = current
    
    return mark_path(maze, full_path, prize_order), path_cost, nodes_expanded

if __name__ == "__main__":
    for maze_file in ["multiprize-micro.txt", "multiprize-tiny.txt", "multiprize-small.txt"]:
        solution, path_cost, nodes_expanded = multi_astar(maze_file)
        print(f"\nA* Solution for {maze_file}:")
        print(solution)
        print(f"Path Cost: {path_cost}, Nodes Expanded: {nodes_expanded}\n")
