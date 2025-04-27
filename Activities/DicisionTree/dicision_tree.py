from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV data
csv_path = "./data.csv"
df = pd.read_csv(csv_path)

# Display the first few rows of the dataset to understand its structure
df.head()

# Drop unnecessary columns
df_clean = df.drop(columns=['id', 'Unnamed: 32'])

# Encode target label: M -> 1, B -> 0
df_clean['diagnosis'] = df_clean['diagnosis'].map({'M': 1, 'B': 0})

# Split into features and labels
X = df_clean.drop(columns=['diagnosis'])
y = df_clean['diagnosis']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the decision tree
clf = DecisionTreeClassifier(random_state=42, max_depth=4)
clf.fit(X_train, y_train)

# Predict and calculate accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Plot the decision tree
plt.figure(figsize=(20, 10))
plot_tree(clf, feature_names=X.columns, class_names=["Benign", "Malignant"], filled=True)
plt.title("Decision Tree")
plt.show()

# Print tree as text and accuracy
tree_text = export_text(clf, feature_names=list(X.columns))

tree_text, accuracy