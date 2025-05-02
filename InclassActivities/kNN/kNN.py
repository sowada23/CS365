from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

# Load the CSV data
csv_path = "./drug200.csv"
df = pd.read_csv(csv_path)

# Encode categorical columns
label_encoders = {}
for col in ['Sex', 'BP', 'Cholesterol', 'Drug']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Split into features and labels
X = df.drop(columns=['Drug'])
y = df['Drug']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the kNN classifier
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)

# Predict and calculate accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Select a test instance
test_sample = X_test.iloc[[0]]

# 🔍 Find nearest neighbors
neighbors_idx = clf.kneighbors(test_sample, return_distance=False)
neighbor_labels = y_train.iloc[neighbors_idx[0]]

# Decode neighbor labels
decoded_neighbors = label_encoders['Drug'].inverse_transform(neighbor_labels)

# 🧠 Majority vote
most_common = Counter(decoded_neighbors).most_common(1)[0][0]

print("✅ 5 Nearest Neighbors:", decoded_neighbors)
print(f"📌 Predicted drug based on majority vote: {most_common}")

# Plot Before/After classification
x1_feature = 'Age'
x2_feature = 'Na_to_K'
class_labels = y.unique()
colors = ['blue', 'deeppink', 'green', 'orange', 'purple']

plt.figure(figsize=(14, 6))

# Before training
plt.subplot(1, 2, 1)
for i, label in enumerate(class_labels):
    group = X_train[y_train == label]
    plt.scatter(group[x1_feature], group[x2_feature], color=colors[i],
                s=90, marker='D', label=label_encoders['Drug'].inverse_transform([label])[0], alpha=0.8)
plt.scatter(test_sample[x1_feature], test_sample[x2_feature],
            color='yellow', edgecolor='black', s=200, marker='s', label='query datapoint')
plt.xlabel("$x_1$"); plt.ylabel("$x_2$")
plt.title("Before training")
plt.legend()
plt.grid(True)

# After training
plt.subplot(1, 2, 2)
for i, label in enumerate(class_labels):
    group = X_train[y_train == label]
    plt.scatter(group[x1_feature], group[x2_feature], color=colors[i],
                s=90, marker='D', label=label_encoders['Drug'].inverse_transform([label])[0], alpha=0.8)
plt.scatter(test_sample[x1_feature], test_sample[x2_feature],
            color='black', edgecolor='cyan', s=200, marker='s', label='query datapoint')
plt.text(test_sample[x1_feature].values[0] + 1,
         test_sample[x2_feature].values[0],
         f"assigned to\n{most_common}",
         fontsize=10, bbox=dict(facecolor='white', edgecolor='black'))
plt.xlabel("$x_1$"); plt.ylabel("$x_2$")
plt.title("After training")
plt.legend()
plt.grid(True)

# Save the image
plt.tight_layout()
plt.savefig("knn_before_after.png")
plt.show()