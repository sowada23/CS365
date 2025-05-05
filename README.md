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

## InclassActivities Overview

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


### **Slides Overview**

The `InClassActivities/slides` folder contains various slide decks from course lectures. Each slide file covers key concepts and takeaways from the lectures. Below is a brief summary for each:

- **1.2.pdf**
  - **Summary:**  
    Introduces the fundamentals of search algorithms and pathfinding concepts.
  - **Key Takeaways:**  
    - Understanding basic search methods (e.g., DFS and BFS).
    - Importance of algorithm efficiency and complexity analysis.

- **8.1.pdf**
  - **Summary:**  
    Focuses on adversarial search and game AI concepts, laying the groundwork for the Breakthrough game project.
  - **Key Takeaways:**  
    - Overview of minimax algorithms and the need for pruning strategies such as alpha-beta pruning.
    - Basic principles of designing game engines and evaluating AI performance.

- **8.2.pdf**
  - **Summary:**  
    Delves deeper into AI enhancements, including heuristic functions and advanced search optimizations.
  - **Key Takeaways:**  
    - The impact of heuristics on improving AI decision-making.
    - Comparisons between basic and enhanced adversarial search strategies.

- **8.3.pdf**
  - **Summary:**  
    Covers advanced topics in decision tree learning and model evaluation techniques.
  - **Key Takeaways:**  
    - How decision trees work and methods for controlling overfitting.
    - Evaluation metrics and the trade-offs between model complexity and interpretability.

---


## Projects

### Handwritten Digit Recognition: CNN on MNIST
This project builds a Convolutional Neural Network (CNN) to classify handwritten digits (0–9) using the MNIST dataset.

**What I Did:**
1. **Data Preprocessing:**
   - Loaded the MNIST dataset via `tensorflow.keras.datasets.mnist`.
   - Normalized pixel values to the range [0, 1] and reshaped images to `(28, 28, 1)`.
   - One-hot encoded the labels for training.
2. **Model Architecture:**
   - Built two convolutional blocks (`Conv2D → MaxPooling2D → BatchNormalization → LeakyReLU`).
   - Flattened and added two dense layers, ending in a 10-unit `softmax` for digit classes.
3. **Training & Evaluation:**
   - Compiled with the Adam optimizer and sparse categorical cross-entropy loss.
   - Trained for 20 epochs with an 80/20 train/validation split, recording loss and accuracy.
   - Evaluated on the held-out test set.
4. **Visualization:**
   - Plotted training vs. validation accuracy and loss over epochs:
     ![Accuracy Plot](accuracy_plot.png)
     ![Loss Plot](loss_plot.png)
   - Observed smooth convergence in the loss curves and high (>98%) validation accuracy by epoch 20.

**Key Takeaways:**
- Gained hands-on experience designing and tuning a CNN for image classification.
- Saw firsthand how monitoring training/validation curves helps detect overfitting and guides hyperparameter adjustments.
- Reinforced best practices in data normalization, model checkpointing, and result visualization.

**How to Run:**
```bash
python main.py
```

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
