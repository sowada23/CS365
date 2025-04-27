
# Breast Cancer Diagnosis using Decision Tree

This project implements a Decision Tree classifier to diagnose breast cancer based on cell nuclei features extracted from digitized images of a breast mass. The dataset used is based on the [Wisconsin Breast Cancer Diagnostic Dataset].

---

## Dataset Overview

- **Filename:** `data.csv`
- **Target Column:** `diagnosis`  
  - `M` = Malignant  
  - `B` = Benign
- **Number of Features:** 30 numeric features such as:
  - `radius_mean`, `texture_mean`, `area_mean`, `concavity_mean`, etc.
- **Total Records:** 569 samples

---

## Model Implementation

The classifier used in this project is a **Decision Tree Classifier** from `scikit-learn`. Here's a summary of the pipeline:

1. **Data Preprocessing:**
   - Removed unnecessary columns: `id` and `Unnamed: 32`
   - Encoded diagnosis: `'M' → 1`, `'B' → 0`

2. **Splitting the Dataset:**
   - 80% for training
   - 20% for testing

3. **Training the Classifier:**
   ```python
   from sklearn.tree import DecisionTreeClassifier
   clf = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=1)
   clf.fit(X_train, y_train)
   ```

4. **Evaluation:**
   - Used accuracy as metric
   - **Test Accuracy: `95.61%`**

---

## Decision Tree Structure

A simplified version of the resulting tree:
```
|--- perimeter_worst <= 105.15
|   |--- concave points_worst <= 0.14
|   |   |--- area_se <= 48.98
|   |   |   |--- class: 0 (Benign)
|   |   |--- area_se >  48.98
|   |   |   |--- smoothness_worst <= 0.11
|   |   |   |   |--- class: 0
|   |   |   |--- smoothness_worst >  0.11
|   |   |   |   |--- class: 1
|   |--- concave points_worst >  0.14
|   |   |--- texture_worst <= 25.94
|   |   |   |--- class: 0
|   |   |--- texture_worst >  25.94
|   |   |   |--- concavity_mean <= 0.10
|   |   |   |   |--- class: 0
|   |   |   |--- concavity_mean >  0.10
|   |   |   |   |--- class: 1
|--- perimeter_worst >  105.15
|   |--- concave points_worst <= 0.15
|   |   |--- texture_worst <= 19.91
|   |   |   |--- class: 0
|   |   |--- texture_worst >  19.91
|   |   |   |--- radius_worst <= 16.80
|   |   |   |   |--- class: 0
|   |   |   |--- radius_worst >  16.80
|   |   |   |   |--- class: 1
|   |--- concave points_worst >  0.15
|   |   |--- texture_mean <= 15.35
|   |   |   |--- texture_mean <= 15.14
|   |   |   |   |--- class: 1
|   |   |   |--- texture_mean >  15.14
|   |   |   |   |--- class: 0
|   |   |--- texture_mean >  15.35
|   |   |   |--- class: 1
```

---

## Insights from the Tree

- **Key Splitting Feature:** `perimeter_worst` and `concave points_worst` — these are highly effective in differentiating malignant from benign.
- **Deeper Nodes:** Features like `area_se`, `texture_worst`, and `concavity_mean` help refine predictions.
- **Interpretability:** Tree-based models provide human-readable decision paths, useful for medical diagnosis validation.

---

## Tree Visualization

![Decision Tree](DicisionTree.png)

---

## How to Run
```bash
python3 dicision_tree.py
```

## Conclusion

This Decision Tree model achieves high classification accuracy and produces an interpretable structure that can be understood by medical professionals. The project demonstrates the effectiveness of classic tree-based models for medical diagnosis tasks.

