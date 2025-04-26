# CS365 Lab A - Part 1: State Representation & Transition Model

## Overview
This project implements the foundational components for solving the **maze search problem**:
- **State Representation**: Defines how the agent and prizes are stored.
- **Transition Model**: Defines possible movements in the maze.
- **Goal Test**: Determines if the agent has collected all prizes.

The agent (`P`) moves through the maze to collect **prizes (`.`)** while avoiding **walls (`%`)**.

## Provided Maze Format
- `P` = Agent's **starting position**.
- `%` = **Wall (impassable tile)**.
- `.` = **Prize (goal state)**.
- `Space` = **Open tile (walkable path)**.

### **Example Maze**
```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                     %P            %
%                     %             %
%                     %             %
%                     %             %
%                     %             %
%                     %%%%%%        %
%                          %        %
%                          %        %
%                          %        %
%                          %        %
%                          %        %
%        %%%%%%%%%%%%               %
%        %                          %
%        %                          %
%        %                          %
%        %                          %
%        %                          %
%        .%                         %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

## How to Run the Code
### **Prerequisites**
- Install **Python 3** on your system.

### **Run the State Model**
To execute the **state representation and transition model**, run:
```bash
python3 main.py
```
This will:
1. Load the maze.
2. Display **possible movements** for the agent.
3. Check if the goal condition is met.

## Implemented Functions
### **`State(position, collected_prizes)`**
- Represents the **agent’s position** and **prizes collected**.
- Uses a **set** to track collected prizes.

### **`get_successors(state, maze)`**
- Returns **valid moves** for the agent.
- Ensures movement is **only within open spaces**.

### **`goal_test(state, all_prizes)`**
- Returns **True** if all prizes have been collected.

## Example Output
```
Start position: (23, 1)
Prizes: {(9, 18)}
Goal Reached? False
New Position after moving South: (23, 2)
Goal Reached? False
```

## Notes
- The **state representation** is designed to be simple and extendable.
- The **transition model** prevents movement into walls (`%`).
- The **goal test** ensures multi-prize scenarios are supported.

## Contributors
- Your Name
- Lab Partner (if applicable)

---
Run `python3 main.py` to test the state model! 🚀