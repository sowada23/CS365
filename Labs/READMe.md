# CS365 Labs Summary

This repository contains my solutions and work for CS365 Labs A, B, and C at Earlham College.
Each lab focuses on a different major concept in Artificial Intelligence and Search algorithms.

## Lab A: Search and Pathfinding

**Goal**: Develop search algorithms to navigate a maze and collect prizes.

### Part 1: State Representation, Transition Model, Goal Test
- Implemented a `MazeState` class to represent the environment, including agent position and remaining prizes.
- Created a transition model for moving North, South, East, and West, ensuring moves are valid (no walls, no out-of-bounds).
- Implemented a goal test to determine if all prizes have been collected.

### Part 2: Depth-First Search (DFS)
- Implemented a `single_dfs` function to search for a path to the prize using DFS.
- Displayed the solution path with `#`, showed path cost and nodes expanded.

### Part 3: BFS, Greedy Best-First Search, and A* Search
- Implemented `single_bfs`, `single_gbfs`, and `single_astar` functions.
- Used Manhattan distance heuristic for Greedy Best-First and A* search.
- Reported path cost, nodes expanded, and visualized the final paths.

### Part 4: Multi-Prize A* Search
- Extended the state and heuristic to work with multiple prizes.
- Implemented `multi_astar`, labeling the order prizes were collected (0,1,2,...).
- Designed an admissible heuristic based on cumulative Manhattan distances.

---

## Lab B: Adversarial Games (Breakthrough Game)

**Goal**: Develop an AI player for the Breakthrough board game using adversarial search.

### Part 1: Environment Setup
- Designed a board state representation as a 2D array.
- Implemented:
  - `display_state` to print the board
  - `initial_state` to set up the starting board
  - `transition_function` to move pieces according to game rules
  - `is_terminal` to check if the game is over
  - `move_generator` to list all valid moves for a player

### Part 2: Minimax Search

#### Part 2-A: Evasive Strategy
- Implemented a minimax AI with an "Evasive" heuristic (favoring survival).
- Two AI agents using Evasive heuristic played against each other.
- Tracked the number of moves, pieces captured, and board states.

#### Part 2-B: Conqueror vs Evasive + Custom Heuristics
- Added a "Conqueror" heuristic (favoring capturing enemy pieces).
- Developed two custom heuristics that consistently defeated both Evasive and Conqueror agents.
- Ran experiments on various board sizes and recorded outcomes.

---

## Lab C: Decision Trees

**Goal**: Build a Decision Tree learner and perform evaluation using cross-validation.

### Part 1: Design Plan
- Drafted a detailed design document for how the Decision Tree Learning would be implemented.
- Explained information gain calculation, tree node structure, and pruning rules.

### Part 2: Decision Tree Implementation
- Built a `decisiontree.py` script that:
  - Reads tab-delimited datasets.
  - Builds a decision tree using the ID3 algorithm based on entropy.
  - Outputs the tree in an indented readable text format.

- Handled edge cases during leave-one-out cross-validation (e.g., missing values).
- Measured and reported training accuracy and cross-validation accuracy.
- Generated trees for three datasets: `tennis.txt`, `titanic2.txt`, and `pets.txt`.

---

# How to Run Each Lab

## Lab A:
```bash
python3 main.py  # (or individually call single_dfs, single_bfs, single_gbfs, single_astar, multi_astar functions)
```

## Lab B:
```bash
python3 breakthrough.py  # Main file to run AI vs AI matches
```

## Lab C:
```bash
python3 decisiontree.py tennis.txt
python3 decisiontree.py titanic2.txt
python3 decisiontree.py pets.txt
```

---

# Notes
- Please see each lab's subfolder for the specific README examples, code files, and generated reports.
- All experiments, final trees, and match results are included in the PDF reports.

---

# Contact
For any questions regarding this repository or the labs, please reach out to the author through the Earlham College GitLab platform.
