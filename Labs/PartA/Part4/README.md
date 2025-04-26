# Multi-Prize A* Search for Maze Solving

## Overview
This project implements **A* Search (A*)** to solve multi-prize maze problems. The agent must pass over **ALL prizes** before reaching the goal. The algorithm efficiently determines the optimal path using a heuristic that selects the nearest prize first.

## How to Run
To execute the multi-prize A* search, run the following command:

```bash
python main.py
```

The script will solve four maze files and print the results.

## Output
The script will output:
- The solved maze with `#` marking the path and numbers representing the order in which prizes were collected.
- The **path cost** (number of steps taken from start to goal).
- The **number of nodes expanded** during the search.

## Example Output
### A* Solution for `multiprize-tiny.txt`:
```
%%%%%%%%%%
%6##%#7  %
%#%5%#%% %
%#%###8%9%
%#4%P%###%
%1##0  10#%
%#%%%% %#%
%2#3   %11%
%%%%%%%%%%
```
**Path Cost: 47, Nodes Expanded: 92**

### A* Solution for `multiprize-small.txt`:
```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  ####P #####6%###   14##13###%
%  #%%%%%#%%%%%%#%# % %#%%  #%
%  #%0 % ####%  #%# % %##%  12%
%1#### %  ###5###%7   % #%%%%%
%%%%%#%%%%#%%% #%%%%%%%#####11%
%2###############8    %#%%%  %
%%#%%%%%%%%#%%%%%%%%%%%#%    %
%##     %  #########   #% %%%%
%##     %%%%%#    %9####     %
%3% %%%    % #%   %% %%#%%%%%%
%          % 4%        #####10%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```
**Path Cost: 181, Nodes Expanded: 498**

### A* Solution for `multiprize-micro.txt`:
```
%%%%%%%%%%
%6  % %2#%
%#% 0#1%#%
%# %P%###%
%5#4####3%
%%%%%%%%%%
```
**Path Cost: 23, Nodes Expanded: 43**

## Heuristic Explanation
The heuristic function estimates the cost of reaching all remaining prizes by selecting the **nearest prize first** and repeating until all are collected. This approach ensures an **admissible heuristic**, meaning A* search finds an optimal path.

## Conclusion
A* Search successfully finds the optimal path through the multi-prize maze. The results demonstrate the efficiency of using an admissible heuristic to solve complex search problems. The solution accounts for all required movement constraints while optimizing for minimal path cost and node expansion.

