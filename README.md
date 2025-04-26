<<<<<<< HEAD
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


=======
# CS365 Folder Overview

Welcome to the `CS365` folder! This repository contains all the work and assignments for the CS365 course, organized into three main parts under the `Labs` directory. Below, you'll find an explanation of the folder structure and a summary of what was done in each part of the labs.

---

## Folder Structure

Here is the inner architecture of the `CS365` folder:

```
CS365/
├── Activities/          # Additional exercises and activities
├── Labs/                # Main lab assignments
│   ├── PartA/           # Lab A: Search and Pathfinding Algorithms
│   │   ├── Part1/       # Part 1 of Lab A
│   │   ├── Part2/       # Part 2 of Lab A
│   │   └── Part3/       # Part 3 of Lab A
│   ├── PartB/           # Lab B: Adversarial Search (Breakthrough Game)
│   │   ├── Part1/       # Part 1 of Lab B
│   │   ├── Part2/       # Part 2 of Lab B
│   │   └── Part3/       # Part 3 of Lab B
│   └── PartC/           # Lab C: Decision Tree Learning
│       ├── Part1/       # Part 1 of Lab C
│       ├── Part2/       # Part 2 of Lab C
│       └── Part3/       # Part 3 of Lab C
├── Projects/            # Course projects
└── test.txt             # Placeholder or test file
```

---

## Labs Overview

### **Lab A: Search and Pathfinding Algorithms**
This lab focuses on implementing and comparing different search algorithms to solve mazes.

- **Part 1**: 
  - Implemented Depth-First Search (DFS) to solve simple mazes.
  - Tested the algorithm on small maze files like `1prize-open.txt`.
- **Part 2**: 
  - Extended the implementation to include Breadth-First Search (BFS), Greedy Best-First Search (GBFS), and A* Search.
  - Compared the performance of these algorithms on medium and large mazes.
- **Part 3**: 
  - Added functionality to handle mazes with multiple prizes.
  - Optimized the search algorithms for efficiency.

### **Lab B: Adversarial Search (Breakthrough Game)**
This lab involves implementing adversarial search techniques for a two-player board game called Breakthrough.

- **Part 1**: 
  - Created a basic game engine for Breakthrough.
  - Implemented a random move generator for testing.
- **Part 2**: 
  - Developed a Minimax algorithm with alpha-beta pruning to play the game intelligently.
  - Tested the algorithm against the random move generator.
- **Part 3**: 
  - Enhanced the AI with heuristics to improve decision-making.
  - Conducted experiments to evaluate the performance of the AI.

### **Lab C: Decision Tree Learning**
This lab focuses on building a decision tree learner for classification tasks.

- **Part 1**: 
  - Implemented a basic decision tree learner using a recursive algorithm.
  - Tested the learner on small datasets.
- **Part 2**: 
  - Added cross-validation to evaluate the performance of the decision tree.
  - Optimized the tree-building process to handle larger datasets.
- **Part 3**: 
  - Extended the implementation to include pruning techniques.
  - Compared the performance of pruned and unpruned trees.

---

## How to Use This Repository

1. **Navigate to the Labs Folder**: 
   - Each lab is organized into its respective folder under `Labs/`.
   - Inside each part, you'll find Python scripts, maze files, and documentation.

2. **Run the Code**:
   - Follow the instructions in the `README.md` files inside each lab part to run the code.
   - Example: To run the DFS maze solver, navigate to `Labs/PartA/Part1/` and execute the script.

3. **Explore the Projects Folder**:
   - The `Projects/` folder contains additional course projects that build on the concepts learned in the labs.

---

Feel free to explore and modify the code as needed. If you're new to the folder, start by reading the `README.md` files in each lab part for detailed instructions.

Happy coding!
>>>>>>> e4dd7b5 (Updated README file)
