# README - Depth-first Search (DFS) Maze Solver

## 1. Overview
This program implements **Depth-first Search (DFS)** to solve a maze traversal problem. The agent starts at `P` (starting position) and navigates to collect a single prize (`.`) while avoiding walls (`%`). The algorithm explores the maze systematically and finds a valid path to the prize.

## 2. Files Included
- `main.py`: Updated versin of maze.py and contains the `Maze` class for parsing and handling the maze structure.
- `main.py`: Implements the **DFS algorithm** to find the path to the prize.
- `README.md`: This file, providing instructions on how to run the program.
- `report.pdf`: Contains analysis, implementation details, and results from running the program on the given mazes.

## 3. How to Run the Program
### **Prerequisites**
Ensure you have **Python 3.x** installed on your system.

### **Running DFS on a maze file**
Use the following command in your terminal or command prompt:
```bash
python main.py path/to/your_maze.txt
```
#### **Example:**
```bash
python main.py 1prize-open.txt
```
This will execute the DFS algorithm and display the solution.

## 4. Expected Output
When the program runs successfully, it prints:
1. **The solution maze** (where `#` marks the path taken by the agent).
2. **Path cost** (number of steps from `P` to `.`).
3. **Number of nodes expanded** during the search.

### **Example Output:**
```
Solution Maze:
%%%%%%%%%%
%P  #   .%
%  ##  %%%
%     #  %
%%%%%%%%%%

Path cost: 7
Nodes expanded: 12
```

## 5. Implementation Details
- Uses **Depth-first Search (DFS)** with a **stack** (LIFO) approach.
- Keeps track of **visited nodes** to prevent infinite loops.
- Displays **optimal path with `#`** in the maze.
- **Counts the number of expanded nodes** to measure performance.
- Uses **North, South, East, and West** movements only (no diagonal movement).
- Reads and parses the maze dynamically from the provided text file.

## 6. Notes & Considerations
- Works only for **single-prize mazes** (Part 2 requirement).
- If no valid path exists, the program will print `"No solution found"`.
- The algorithm stops execution once the **first prize is reached**, as per Part 2 requirements.
- The program assumes a correctly formatted maze file; unexpected formats may lead to errors.

## 7. Results for Given Mazes
The program was tested on the three provided **1prize** mazes. Detailed results, including performance evaluation, are included in `Part1DesginXs.pdf`.

## 8. Troubleshooting
### **Issue: Maze file not found**
- Ensure that the file path provided in the command exists.
- Use an absolute path if necessary.

### **Issue: Incorrect output or unexpected behavior**
- Verify the maze file format (`P` for start, `.` for prize, `%` for walls, and spaces for open paths).
- Check that the maze is structured properly with consistent row lengths.

### **Issue: No solution found**
- The maze might have an **inaccessible prize** due to walls.
- Try using a different test maze to ensure DFS is functioning correctly.

---
### **Author: [Your Name]**
CS365 - Part 2: Search and Pathfinding
Spring 2025


