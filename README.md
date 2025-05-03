# CS365 Folder Overview

Welcome to the `CS365` folder! This repository contains all the work and assignments for the CS365 course, organized into three main parts under the `Labs` directory and additional exercises under the `Activities` directory. Below, you'll find an explanation of the folder structure and a summary of what was done in each part of the labs and activities.

---

## Folder Structure

Here is the inner architecture of the `CS365` folder:

```
CS365/
├── InClassActivities/                 
│   ├── DicisionTree/           
│   │   ├── dicision_tree.py
│   │   ├── data.csv
│   │   ├── DicisionTree.png
│   │   └── README.md
│   ├── kNN/                    
│   │    ├── kNN.py
│   │    ├── knn_before_after.png
│   │    ├── drug200.csv
│   │    └── README.md
│   └── slides/
│        ├── 1.2.pdf
│        ├── 8.1.pdf 
│        ├── 8.2.pdf
│        └── 8.3.pdf
│
├── Projects/                       
│   ├── inputs/
│   ├── main.py
│   ├── mnist_model.h5
│   └── ProjectPlan.pdf
│
└── RA/
          
```

---

## Activities Overview

### **DicisionTree: Breast Cancer Diagnosis using Decision Tree**
This activity implements a Decision Tree classifier to diagnose breast cancer based on cell nuclei features.

- **What I Did:**
  1. Preprocessed the dataset by removing unnecessary columns and encoding the target.
  2. Trained a `DecisionTreeClassifier` (entropy, max depth 4) on 80% of the data.
  3. Evaluated the model (test accuracy: 95.61%).
  4. Visualized the tree and interpreted key features.
  5. Provided a human-readable decision path for medical validation.

- **How to Run:**
  ```bash
  python3 dicision_tree.py
  ```

---

### **kNN: Breast Cancer Diagnosis using k-Nearest Neighbors**
This activity implements a k-Nearest Neighbors (kNN) classifier for the same diagnosis task.

- **What I Did:**
  1. Preprocessed the dataset (removed unnecessary columns, encoded target).
  2. Standardized features using `StandardScaler` for optimal kNN performance.
  3. Trained a `KNeighborsClassifier` (k=5) on 80% of the data.
  4. Evaluated the model (e.g., test accuracy: 70~80%).
  5. Explored the effect of different `k` values and discussed the importance of feature scaling.

- **How to Run:**
  ```bash
  python3 kNN.py
  ```

---

## Labs Overview

### **Lab A: Search and Pathfinding Algorithms**
- **Part 1:** Implemented DFS for simple mazes.
- **Part 2:** Added BFS, GBFS, and A*; compared their performance.
- **Part 3:** Enhanced algorithms for multiple prizes and optimized efficiency.

### **Lab B: Adversarial Search (Breakthrough Game)**
- **Part 1:** Built a basic game engine and random move generator.
- **Part 2-A:** Developed Minimax with alpha-beta pruning.
- **Part 2-B:** Enhanced AI with heuristics and tested against random moves.

### **Lab C: Decision Tree Learning**
- **Part 1:** Implemented a recursive decision tree learner and tested on small datasets.
- **Part 2:** Added cross-validation and optimized for larger datasets.

---

## How to Use This Repository

1. **Navigate to the Activities or Labs Folder:**  
   Each activity or lab is organized into its respective folder. Inside each part, you'll find Python scripts, datasets, and documentation.

2. **Run the Code:**  
   Follow the instructions in the `README.md` files inside each activity or lab part to run the code.

3. **Explore the Projects Folder:**  
   The `Projects/` folder contains additional course projects that build on the concepts learned in the labs and activities.

---

Feel free to explore and modify the code as needed. If you're new to the folder, start by reading the `README.md` files in each activity or lab part for detailed instructions.
