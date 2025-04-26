x# CS365 Folder Overview

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
