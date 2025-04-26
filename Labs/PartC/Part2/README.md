# Decision Tree Implementation for Lab C Part 2

This repository contains the Python implementation of a decision tree learning algorithm for CS365 Lab C.

## Files

- **main.py**  
  The main Python program that:
  - Reads a tab-delimited dataset where the first row contains attribute names and the last column is the classification attribute (`yes` or `no`).
  - Builds a decision tree using an entropy-based (ID3) algorithm.
  - Prints the decision tree in an indented, human-readable format.
  - Computes the training set accuracy.
  - Performs leave-one-out cross validation to report test accuracy.

- **Report.pdf**

  The attached PDF report provides a comprehensive summary of the decision tree analysis for LabC.

## Dataset Descriptions

This repository includes three sample datasets, each demonstrating a different decision-making scenario for testing the decision tree algorithm.

### pets.txt
- **size**: The physical size of the pet (e.g., tiny, small, medium, large, enormous).
- **color**: The color of the pet (e.g., white, brown, gray, yellow, orange).
- **earshape**: The shape of the pet’s ears (e.g., pointed, folded).
- **tail**: Indicates whether the pet has a tail (yes/no).
- **iscat**: The target attribute that classifies if the pet is a cat (yes/no).

This dataset is used to build a decision tree that classifies pets based on their physical attributes.

### tennis.txt
- **outlook**: The weather outlook (e.g., sunny, overcast, rain).
- **temperature**: The daily temperature condition (hot, mild, cool).
- **humidity**: The level of humidity (high, normal).
- **wind**: The wind condition (weak, strong).
- **playtennis**: The target classification indicating whether tennis is played (yes/no).

This classic dataset is often used to illustrate decision tree learning and helps in understanding how different weather conditions can be used to decide whether to play tennis.

### titanic2.txt
- **pclass**: The ticket class of the passenger (1st, 2nd, 3rd).
- **age**: The age group of the passenger (adult, child).
- **sex**: The gender of the passenger (male, female).
- **survived**: The target classification attribute indicating whether the passenger survived (yes/no).

This dataset, based on Titanic passenger information, demonstrates the application of decision trees in predicting outcomes such as survival.

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Open a terminal in the directory containing the files.
3. Run the program with a data file as a command-line argument. For example, to run the program on the tennis dataset:

   ```bash
   python3 main.py tennis.txt